import sys
import os
import json
import subprocess

from BeautifulSoup import BeautifulSoup
import xml.etree.ElementTree as ET
from copy import copy

def dictify(r,root=True):
    if root:
        return {r.tag : dictify(r, False)}
    d=copy(r.attrib)
    if r.text:
        d["_text"]=r.text
    for x in r.findall("./*"):
        if x.tag not in d:
            d[x.tag]=[]
        d[x.tag].append(dictify(x,False))
    return d

def parse(file):
    print("parsing: " + str(file))
    parse_data = {}
    with open(file, "r") as f:
        data = f.read().strip().split("\n")
    for line in data:
        line = line.strip()
        if len(line) == 0:
            continue
        if line[-1] == "|":
            line = line[0:-1]
        # print("Old line: " + line)
        line = line.replace("a | s, ", "a PIPE s, ")
        # print("New line: " + line)
        items = line.split(" | ")
        line_data = {}
        for kvpair in items:
            if len(kvpair) == 0:
                continue
            # print kvpair
            key = kvpair.strip().split(":", 1)[0].strip()
            value = kvpair.strip().split(":", 1)[1].strip()
            # print key + ":" + value
            line_data[key] = value
        if "Discourse Facet" not in line_data:
            line_data["Discourse Facet"] = "None"

        line_data["Reference Article"] = line_data["Reference Article"].replace(".xml", "")
        line_data["Citing Article"] = line_data["Citing Article"].replace(".xml", "")
        if line_data["Citation Marker Offset"].startswith("["):
            line_data["Citation Marker Offset"] = line_data["Citation Marker Offset"][1:]
        if line_data["Citation Marker Offset"].endswith("]"):
            line_data["Citation Marker Offset"] = line_data["Citation Marker Offset"][:-1]
        if line_data["Citation Marker Offset"].startswith("\'"):
            line_data["Citation Marker Offset"] = line_data["Citation Marker Offset"][1:]
        if line_data["Citation Marker Offset"].endswith("\'"):
            line_data["Citation Marker Offset"] = line_data["Citation Marker Offset"][:-1]
        if line_data["Citation Offset"].startswith("["):
            line_data["Citation Offset"] = line_data["Citation Offset"][1:]
        if line_data["Citation Offset"].endswith("]"):
            line_data["Citation Offset"] = line_data["Citation Offset"][:-1]

        if line_data["Reference Article"] not in parse_data:
            parse_data[line_data["Reference Article"]] = {}
        if line_data["Citing Article"] not in parse_data[line_data["Reference Article"]]:
            parse_data[line_data["Reference Article"]][line_data["Citing Article"]] = {}
        if line_data["Citation Marker Offset"] not in parse_data[line_data["Reference Article"]][line_data["Citing Article"]]:
            parse_data[line_data["Reference Article"]][line_data["Citing Article"]][line_data["Citation Marker Offset"]] = {"original": line_data, "comparable": False}
        ref_offset = line_data["Reference Offset"]
        if ref_offset.startswith("["):
            ref_offset = ref_offset[1:]
        if ref_offset.endswith("]"):
            ref_offset = ref_offset[:-1]
        parsed_ref_offset_tmp = [x.strip() for x in ref_offset.split(",")]
        print("\n\n")
        print(parsed_ref_offset_tmp)
        parsed_ref_offset = []
        for ref in parsed_ref_offset_tmp:
            print(ref)
            if ref.startswith("\'") or ref.startswith("\""):
                ref = ref[1:]
            if ref.endswith("\'") or ref.endswith("\""):
                ref = ref[:-1]
            parsed_ref_offset.append(ref)
        print(parsed_ref_offset)
        # print("<root>" + line_data["Reference Text"] + "</root>")
        line = "<root>" + line_data["Reference Text"] + "</root>"
        # print("Line is:")
        # print(line)
        line = line.replace("&", "&amp;")
        line = str(BeautifulSoup(line))
        # line = line.replace("<\s>", "</s>")
        # print("Line is:")
        # print(line)
        root = ET.fromstring(line)
        ref_text_dict = dictify(root)
        # print(ref_text_dict)
        ref_text_dict_clean = {}
        cnt = 0
        for item in ref_text_dict["root"]["s"]:
            cnt += 1
            ref_text_dict_clean[item.get("sid", cnt)] = item["_text"]
        parse_data[line_data["Reference Article"]][line_data["Citing Article"]][line_data["Citation Marker Offset"]]["Reference Text"] = ref_text_dict_clean
        parse_data[line_data["Reference Article"]][line_data["Citing Article"]][line_data["Citation Marker Offset"]]["Reference Offset"] = parsed_ref_offset
        ref_discourse_facet = line_data["Discourse Facet"]
        parsed_discourse_facet = []
        if len(ref_discourse_facet) > 0:
            if ref_discourse_facet[0] == "[":
                parsed_discourse_facet_tmp = [x.strip().lower().replace(" ", "_") for x in ref_discourse_facet[1:-1].split(",")]
                parsed_discourse_facet = []
                for ref in parsed_discourse_facet_tmp:
                    if ref.startswith("\'") or ref.startswith("\""):
                        ref = ref[1:]
                    if ref.endswith("\'") or ref.endswith("\""):
                        ref = ref[:-1]
                    parsed_discourse_facet.append(ref)
            else:
                ref = ref_discourse_facet.lower().replace(" ", "_")
                if ref.startswith("\'") or ref.startswith("\""):
                    ref = ref[1:]
                if ref.endswith("\'") or ref.endswith("\""):
                    ref = ref[:-1]
                parsed_discourse_facet.append(ref)
        parse_data[line_data["Reference Article"]][line_data["Citing Article"]][line_data["Citation Marker Offset"]]["Discourse Facet"] = parsed_discourse_facet

    # print(json.dumps(parse_data, sort_keys=True, indent=4))
    # print("###################################################################################################################")
    return parse_data

def do_rouge(temp_dir, gold_file, submit_file):
    settings_string = """<ROUGE_EVAL version="1.5.5">
        <EVAL ID="test">
            <PEER-ROOT>
                {temp_dir}
            </PEER-ROOT>
            
            <MODEL-ROOT>
                {temp_dir}
            </MODEL-ROOT>
            
            <INPUT-FORMAT TYPE="SPL"></INPUT-FORMAT>
            
            <PEERS>
                <P ID="system">{gold_file}</P>
            </PEERS>
            
            <MODELS>
                <M ID="abstract">{submit_file}</M>
            </MODELS>
        </EVAL>
    </ROUGE_EVAL>
    """
    settings_string = settings_string.format(**locals())
    with open(os.path.join(temp_dir, "settings"), "w") as f:
        f.write(settings_string)

    p = subprocess.Popen(['/bin/bash', '-c', os.path.join(temp_dir, "rouge", "ROUGE-1.5.5.pl") + " -e " + os.path.join(temp_dir, "rouge", "data") + " -f A -a -x -s -d -t 1 -m -2 -4 " + os.path.join(temp_dir, "settings") + " > " + os.path.join(temp_dir, "raw_output")])
    p.wait()

    with open(os.path.join(temp_dir, "raw_output"), "r") as f:
        raw_content = f.readlines()

    [p, r, f] = [0, 0, 0]

    for line in raw_content:
        if line.startswith("system"):
            fields = line.split()
            print(fields)
            if fields[2].startswith("Average_P"):
                p = float(fields[3])
            elif fields[2].startswith("Average_R"):
                r = float(fields[3])
            elif fields[2].startswith("Average_F"):
                f = float(fields[3])

    return (p, r, f)

def evaluate(gold_file, submit_file, temp_dir):
    print(gold_file)
    print(submit_file)
    print("\n\n\n\n")
    gold_data = parse(gold_file)
    submit_data = parse(submit_file)

    precision_list = []
    recall_list = []
    f1_list = []

    for ref_article in gold_data:
        for cit_article in gold_data[ref_article]:
            for cit_marker_offset in gold_data[ref_article][cit_article]:
                gold_ref_text = gold_data[ref_article][cit_article][cit_marker_offset]["Reference Text"]
                try:
                    submit_ref_text = submit_data[ref_article][cit_article][cit_marker_offset]["Reference Text"]
                except KeyError as e:
                    # print("Data not found in submit file")
                    # precision_list.append(0)
                    # recall_list.append(0)
                    # f1_list.append(0)
                    # continue
                    submit_ref_text = {}

                with open(os.path.join(temp_dir, "gold"), "w") as f:
                    print(gold_ref_text.values())
                    s = "\n".join(gold_ref_text.values())
                    f.write(s.encode("utf-8"))
                with open(os.path.join(temp_dir, "submit"), "w") as f:
                    print(submit_ref_text.values())
                    s = "\n".join(submit_ref_text.values())
                    f.write(s.encode("utf-8"))

                (p, r, f) = do_rouge(temp_dir, "gold", "submit")
                precision_list.append(p)
                recall_list.append(r)
                f1_list.append(f)

    avg_p = sum(precision_list) / float(len(precision_list))
    avg_r = sum(recall_list) / float(len(recall_list))
    avg_f = sum(f1_list) / float(len(f1_list))
    return (avg_p, avg_r, avg_f)

def main(input_dir, temp_dir, output_dir):
    p_list = []
    r_list = []
    f_list = []
    for gold_file in os.listdir(os.path.join(input_dir, "ref", "Task1")):
        submit_file = os.path.join(input_dir, "res", "Task1", gold_file)
        if gold_file.startswith("."):
            continue
        if not os.path.exists(submit_file):
            continue
        (p, r, f1) = evaluate(os.path.join(input_dir, "ref", "Task1", gold_file), submit_file, temp_dir)
        # p = 0
        # r = 0
        # f1 = 0
        p_list.append(p)
        r_list.append(r)
        f_list.append(f1)
        with open(os.path.join(output_dir, "scores.txt"), "a") as f:
            f.write(gold_file + "_task1a_precision_rouge: " + str(p) + "\n")
            f.write(gold_file + "_task1a_recall_rouge: " + str(r) + "\n")
            f.write(gold_file + "_task1a_f1_rouge: " + str(f1) + "\n")
    avg_p = sum(p_list) / float(len(p_list))
    avg_r = sum(r_list) / float(len(r_list))
    avg_f = sum(f_list) / float(len(f_list))
    with open(os.path.join(output_dir, "scores.txt"), "a") as f:
        f.write("task1a_rouge_precision_avg: " + str(avg_p) + "\n")
        f.write("task1a_rouge_recall_avg: " + str(avg_r) + "\n")
        f.write("task1a_rouge_f1_avg: " + str(avg_f) + "\n")

if __name__ == "__main__":
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    temp_dir = sys.argv[3]
    main(input_dir, temp_dir, output_dir)
