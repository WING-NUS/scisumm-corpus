import sys
import os
import json, csv
import subprocess

from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
from copy import copy
from task1_eval import parse, parse_csv

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
    print("\n\n\n\n")
    print(gold_file)
    print(submit_file)

    gold_data = parse_csv(gold_file)
    submit_data = parse_csv(submit_file)

    precision_list = []
    recall_list = []
    f1_list = []

    for ref_article in gold_data:
        for cit_article in gold_data[ref_article]:
            for cit_marker_offset in gold_data[ref_article][cit_article]:
                try:
                    if "Reference Text" not in gold_data[ref_article][cit_article][cit_marker_offset]:
                        print("no Reference Text in gold", ref_article)
                    gold_ref_text = gold_data[ref_article][cit_article][cit_marker_offset]["Reference Text"]
                    if "Reference Text" not in submit_data[ref_article][cit_article][cit_marker_offset]:
                        print("no Reference Text in submit", ref_article)
                    # try:
                    submit_ref_text = submit_data[ref_article][cit_article][cit_marker_offset]["Reference Text"]
                    # except KeyError as e:
                    #     print("Data not found in submit file")
                    #     # precision_list.append(0)
                    #     # recall_list.append(0)
                    #     # f1_list.append(0)
                    #     # continue
                    #     submit_ref_text = {}
                except:
                    # print "No reference text for", ref_article
                    continue

                with open(os.path.join(temp_dir, "gold"), "w",encoding="utf-8") as f:
                    print(gold_ref_text.values())
                    s = "\n".join(gold_ref_text.values())
                    # f.write(s.encode("utf-8"))
                    f.write(s)
                with open(os.path.join(temp_dir, "submit"), "w",encoding="utf-8") as f:
                    print(submit_ref_text.values())
                    s = "\n".join(submit_ref_text.values())
                    # f.write(s.encode("utf-8"))
                    f.write(s)

                (p, r, f) = do_rouge(temp_dir, "gold", "submit")
                precision_list.append(p)
                recall_list.append(r)
                f1_list.append(f)

    if len(precision_list) == 0:
        print("Length 0", gold_file)
    avg_p = sum(precision_list) / (float(len(precision_list)) + 10e-8)
    avg_r = sum(recall_list) / (float(len(recall_list)) + 10e-8)
    avg_f = sum(f1_list) / (float(len(f1_list)) + 10e-8)
    return (avg_p, avg_r, avg_f)

def main(input_dir, temp_dir, output_dir):
    p_list = []
    r_list = []
    f_list = []
    for gold_file in os.listdir(os.path.join(input_dir, "ref", "Task1")):
        paper_id = gold_file.split('_')[0]
        submit_file = os.path.join(input_dir, "res", "Task1", paper_id +".annv3.csv")
        if gold_file.startswith("."):
            continue
        if not os.path.exists(submit_file):
            continue
        (p, r, f1) = evaluate(os.path.join(input_dir, "ref", "Task1", gold_file), submit_file, temp_dir)
        print(p,r,f1)
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
