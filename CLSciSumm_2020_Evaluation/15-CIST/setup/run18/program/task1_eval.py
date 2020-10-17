import os
import sys
import json, csv

from bs4 import BeautifulSoup
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
        print("original cit marker offset is " + line_data["Citation Marker Offset"])
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
        print("new cit marker offset is " + line_data["Citation Marker Offset"])
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
        line = str(BeautifulSoup(line, "xml"))
        # line = line.replace("<\s>", "</s>")
        # print("Line is:")
        # print(line)
        root = ET.fromstring(line)
        ref_text_dict = dictify(root)
        # print(ref_text_dict)
        ref_text_dict_clean = {}
        cnt = 0
        for item in ref_text_dict["root"]["S"]:
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

def parse_csv(file):
    print("parsing: " + str(file))
    parse_data = {}

    csv_obj = csv.reader(open(file,"r",encoding='latin1'))
    items_list = None
    for i, row in enumerate(csv_obj):
        if i==0: # first line
            items_list = row # Citance Number,Reference Article, ...
            continue
        line_data = {}
        if len(row) != len(items_list):
            print("Error: # of items mismatch")
            print(items_list)
            print(row)
            continue
        for key, value in zip(items_list, row):
            # print kvpair
            line_data[key] = value
        if line_data["Reference Text"] == "NA":
            continue
        # print items_list
        print(line_data["Reference Text"])

        line_data["Reference Article"] = line_data["Reference Article"].replace(".xml", "")
        line_data["Citing Article"] = line_data["Citing Article"].replace(".xml", "")
        print("original cit marker offset is " + line_data["Citation Marker Offset"])
        # if line_data["Citation Marker Offset"].startswith("["):
        #     line_data["Citation Marker Offset"] = line_data["Citation Marker Offset"][1:]
        # if line_data["Citation Marker Offset"].endswith("]"):
        #     line_data["Citation Marker Offset"] = line_data["Citation Marker Offset"][:-1]
        # if line_data["Citation Marker Offset"].startswith("\'"):
        #     line_data["Citation Marker Offset"] = line_data["Citation Marker Offset"][1:]
        # if line_data["Citation Marker Offset"].endswith("\'"):
        #     line_data["Citation Marker Offset"] = line_data["Citation Marker Offset"][:-1]
        # if line_data["Citation Offset"].startswith("["):
        #     line_data["Citation Offset"] = line_data["Citation Offset"][1:]
        # if line_data["Citation Offset"].endswith("]"):
        #     line_data["Citation Offset"] = line_data["Citation Offset"][:-1]
        line_data["Citation Marker Offset"] = '0'
        line_data["Citation Offset"] = '0'

        print("new cit marker offset is " + line_data["Citation Marker Offset"])
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
        line = line.replace("&amp;", "&")
        line = line.replace("&", "&amp;")
        line = str(BeautifulSoup(line, "xml"))
        # line = line.replace("<\s>", "</s>")
        # print("Line is:")
        # print(line)
        root = ET.fromstring(line)
        ref_text_dict = dictify(root)
        # print(ref_text_dict)
        ref_text_dict_clean = {}
        cnt = 0
        # if "S" not in ref_text_dict["root"]:
        #     # print "Key Error at", file
        #     continue
        try:
            for item in ref_text_dict["root"]["S"]:
                cnt += 1
                ref_text_dict_clean[item.get("sid", cnt)] = item["_text"]
            parse_data[line_data["Reference Article"]][line_data["Citing Article"]][line_data["Citation Marker Offset"]]["Reference Text"] = ref_text_dict_clean
            # print "ref_text_dict_clean", ref_text_dict_clean
            parse_data[line_data["Reference Article"]][line_data["Citing Article"]][line_data["Citation Marker Offset"]]["Reference Offset"] = parsed_ref_offset
        except:
            print("Error in Reference Offset")
            continue
        try:
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
                    parsed_discourse_facet_tmp = [x.strip().lower().replace(" ", "_") for x in ref_discourse_facet.split(",")]
                    parsed_discourse_facet = []
                    for ref in parsed_discourse_facet_tmp:
                        if ref.startswith("\'") or ref.startswith("\""):
                            ref = ref[1:]
                        if ref.endswith("\'") or ref.endswith("\""):
                            ref = ref[:-1]
                        parsed_discourse_facet.append(ref)
            print("parsed_discourse_facet", parsed_discourse_facet)
            parse_data[line_data["Reference Article"]][line_data["Citing Article"]][line_data["Citation Marker Offset"]]["Discourse Facet"] = parsed_discourse_facet
        except:
            print("Error in Discourse Facet")
            continue

    # print(json.dumps(parse_data, sort_keys=True, indent=4))
    # print("###################################################################################################################")
    return parse_data


def calculate(gold_data, submit_data):
    # print(json.dumps(gold_data, indent=4, sort_keys=True))
    # print(json.dumps(submit_data, indent=4, sort_keys=True))
    [TP_ref, FN_ref, FP_ref, TP_facet, FN_facet, FP_facet] = [0, 0, 0, 0, 0, 0]
    for ref_article in gold_data:
        for cit_article in gold_data[ref_article]:
            for cit_marker_offset in gold_data[ref_article][cit_article]:
                old_TP_ref = TP_ref
                try:
                    for ref_offset in gold_data[ref_article][cit_article][cit_marker_offset]["Reference Offset"]:
                        try:
                            ref_offset_list = submit_data[ref_article][cit_article][cit_marker_offset]["Reference Offset"]
                            if ref_offset in ref_offset_list:
                                TP_ref += 1
                                gold_data[ref_article][cit_article][cit_marker_offset]["comparable"] = True
                            else:
                                FN_ref += 1
                        except KeyError as e:
                            print("IGNORE THIS: key error 1")
                            FN_ref += 1
                except: continue

    for ref_article in submit_data:
        for cit_article in submit_data[ref_article]:
            for cit_marker_offset in submit_data[ref_article][cit_article]:
                try:
                    for ref_offset in submit_data[ref_article][cit_article][cit_marker_offset]["Reference Offset"]:
                        try:
                            ref_offset_list = gold_data[ref_article][cit_article][cit_marker_offset]["Reference Offset"]
                            if ref_offset not in ref_offset_list:
                                FP_ref += 1
                        except KeyError as e:
                            print("IGNORE THIS: key error 2")
                            FP_ref += 1
                except: continue
    [precision_ref, recall_ref, f_ref] = [0.0, 0.0, 0.0]
    try:
        precision_ref = TP_ref / float(TP_ref + FP_ref)
    except ZeroDivisionError as e:
        precision_ref = 0
    try:
        recall_ref = TP_ref / float(TP_ref + FN_ref)
    except ZeroDivisionError as e:
        recall_ref = 0
    try:
        f_ref = 2.0 * precision_ref * recall_ref / float(precision_ref + recall_ref)
    except ZeroDivisionError as e:
        f_ref = 0

    for ref_article in gold_data:
        for cit_article in gold_data[ref_article]:
            for cit_marker_offset in gold_data[ref_article][cit_article]:
                try:
                    for facet in gold_data[ref_article][cit_article][cit_marker_offset]["Discourse Facet"]:
                        if gold_data[ref_article][cit_article][cit_marker_offset]["comparable"]:
                            print("\n\n")
                            print(ref_article)
                            print(cit_article)
                            print(cit_marker_offset)
                            print(facet)
                            print(submit_data[ref_article][cit_article][cit_marker_offset]["Discourse Facet"])
                            try:
                                if facet in submit_data[ref_article][cit_article][cit_marker_offset]["Discourse Facet"]:
                                    TP_facet += 1
                                else:
                                    FN_facet += 1
                            except KeyError as e:
                                print("IGNORE THIS: Key error 4")
                                FN_facet += 1
                        else:
                            FN_facet += 1
                except: continue

    for ref_article in submit_data:
        for cit_article in submit_data[ref_article]:
            for cit_marker_offset in submit_data[ref_article][cit_article]:
                try:
                    for facet in submit_data[ref_article][cit_article][cit_marker_offset]["Discourse Facet"]:
                        try:
                            if gold_data[ref_article][cit_article][cit_marker_offset]["comparable"]:
                                if facet not in gold_data[ref_article][cit_article][cit_marker_offset]["Discourse Facet"]:
                                    FP_facet += 1
                        except KeyError as e:
                            print("IGNORE THIS: Key error 5")
                            FP_facet += 1
                except: continue

    [precision_facet, recall_facet, f_facet] = [0.0, 0.0, 0.0]
    try:
        precision_facet = TP_facet / float(TP_facet + FP_facet)
    except ZeroDivisionError as e:
        precision_facet = 0
    try:
        recall_facet = TP_facet / float(TP_facet + FN_facet)
    except ZeroDivisionError as e:
        recall_facet = 0
    try:
        f_facet = 2.0 * precision_facet * recall_facet / float(precision_facet + recall_facet)
    except ZeroDivisionError as e:
        f_facet = 0

    return (precision_ref, recall_ref, f_ref, precision_facet, recall_facet, f_facet, TP_ref, FP_ref, FN_ref, TP_facet, FP_facet, FN_facet)

def evaluate(gold_file, submit_file, score_file):
    # print(gold_file)
    # print(submit_file)
    gold_data = parse_csv(gold_file)
    submit_data = parse_csv(submit_file)
    (p_ref, r_ref, f_ref, p_facet, r_facet, f_facet, TP_ref, FP_ref, FN_ref, TP_facet, FP_facet, FN_facet) = calculate(gold_data, submit_data)
    with open(score_file, "a") as f:
        f.write(os.path.basename(gold_file) + "_task1a_precision: " + str(p_ref) + "\n")
        f.write(os.path.basename(gold_file) + "_task1a_recall: " + str(r_ref) + "\n")
        f.write(os.path.basename(gold_file) + "_task1a_f1: " + str(f_ref) + "\n")
        f.write(os.path.basename(gold_file) + "_task1b_precision: " + str(p_facet) + "\n")
        f.write(os.path.basename(gold_file) + "_task1b_recall: " + str(r_facet) + "\n")
        f.write(os.path.basename(gold_file) + "_task1b_f1: " + str(f_facet) + "\n")
    return (p_ref, r_ref, f_ref, p_facet, r_facet, f_facet, TP_ref, FP_ref, FN_ref, TP_facet, FP_facet, FN_facet)

def main(input_dir, output_dir):
    print(input_dir, output_dir)
    if not os.path.exists(input_dir):
        print("%s not a valid director" % input_dir)
    if not os.path.exists(output_dir):
        print("%s not a valid director" % output_dir)

    truth_dir = os.path.join(input_dir, "ref", "Task1")
    if not os.path.exists(truth_dir):
        print("%s not a valid director" % truth_dir)
    submit_dir = os.path.join(input_dir, "res", "Task1")
    if not os.path.exists(submit_dir):
        print("%s not a valid director" % submit_dir)

    score_file = os.path.join(output_dir, "scores.txt")
    if os.path.exists(score_file):
        os.remove(score_file)

    P_ref_list = []
    P_facet_list = []
    R_ref_list = []
    R_facet_list = []
    F_ref_list = []
    F_facet_list = []

    TP_ref_list = []
    FP_ref_list = []
    FN_ref_list = []
    TP_facet_list = []
    FP_facet_list = []
    FN_facet_list = []

    for gold_file in os.listdir(truth_dir):
        if gold_file.startswith('.'):
            continue
        paper_id = gold_file.split('_')[0]
        submit_file = os.path.join(submit_dir, paper_id +".annv3.csv")
        if not os.path.exists(submit_file):
            continue
        (p_ref, r_ref, f_ref, p_facet, r_facet, f_facet, TP_ref, FP_ref, FN_ref, TP_facet, FP_facet, FN_facet) = evaluate(os.path.join(truth_dir, gold_file), submit_file, score_file)
        P_ref_list.append(p_ref)
        P_facet_list.append(p_facet)
        R_ref_list.append(r_ref)
        R_facet_list.append(r_facet)
        F_ref_list.append(f_ref)
        F_facet_list.append(f_facet)

        TP_ref_list.append(TP_ref)
        FP_ref_list.append(FP_ref)
        FN_ref_list.append(FN_ref)
        TP_facet_list.append(TP_facet)
        FP_facet_list.append(FP_facet)
        FN_facet_list.append(FN_facet)

    TP_ref_sum = sum(TP_ref_list)
    FP_ref_sum = sum(FP_ref_list)
    FN_ref_sum = sum(FN_ref_list)
    TP_facet_sum = sum(TP_facet_list)
    FP_facet_sum = sum(FP_facet_list)
    FN_facet_sum = sum(FN_facet_list)

    try:
        precision_ref_micro = TP_ref_sum / float(TP_ref_sum + FP_ref_sum)
    except ZeroDivisionError as e:
        precision_ref_micro = 0
    try:
        recall_ref_micro = TP_ref_sum / float(TP_ref_sum + FN_ref_sum)
    except ZeroDivisionError as e:
        recall_ref_micro = 0
    try:
        f_ref_micro = 2.0 * precision_ref_micro * recall_ref_micro / float(precision_ref_micro + recall_ref_micro)
    except ZeroDivisionError as e:
        f_ref_micro = 0
    try:
        precision_ref_macro = sum(P_ref_list) / len(P_ref_list)
    except ZeroDivisionError as e:
        precision_ref_macro = 0
    try:
        recall_ref_macro = sum(R_ref_list) / len(R_ref_list)
    except ZeroDivisionError as e:
        recall_ref_macro = 0
    try:
        f_ref_macro = 2.0 * precision_ref_macro * recall_ref_macro / float(precision_ref_macro + recall_ref_macro)
    except ZeroDivisionError as e:
        f_ref_macro = 0

    try:
        # precision_facet_micro = TP_ref_sum / float(TP_ref_sum + FP_ref_sum)
        precision_facet_micro = TP_facet_sum / float(TP_facet_sum + FP_facet_sum)
    except ZeroDivisionError as e:
        precision_facet_micro = 0
    try:
        # recall_facet_micro = TP_ref_sum / float(TP_ref_sum + FN_ref_sum)
        recall_facet_micro = TP_facet_sum / float(TP_facet_sum + FN_facet_sum)
    except ZeroDivisionError as e:
        recall_facet_micro = 0
    try:
        # f_facet_micro = 2.0 * precision_ref_micro * recall_ref_micro / float(precision_ref_micro + recall_ref_micro)
        f_facet_micro = 2.0 * precision_facet_micro * recall_facet_micro / float(precision_facet_micro + recall_facet_micro)
    except ZeroDivisionError as e:
        f_facet_micro = 0
    try:
        precision_facet_macro = sum(P_facet_list) / len(P_facet_list)
    except ZeroDivisionError as e:
        precision_facet_macro = 0
    try:
        recall_facet_macro = sum(R_facet_list) / len(R_facet_list)
    except ZeroDivisionError as e:
        recall_facet_macro = 0
    try:
        f_facet_macro = 2.0 * precision_facet_macro * recall_facet_macro / float(precision_facet_macro + recall_facet_macro)
    except ZeroDivisionError as e:
        f_facet_macro = 0

    with open(score_file, "a") as f:
        f.write("task1a_precision_micro_avg: " + str(precision_ref_micro) + "\n")
        f.write("task1a_precision_macro_avg: " + str(precision_ref_macro) + "\n")
        f.write("task1a_recall_micro_avg: " + str(recall_ref_micro) + "\n")
        f.write("task1a_recall_macro_avg: " + str(recall_ref_macro) + "\n")
        f.write("task1a_f1_micro_avg: " + str(f_ref_micro) + "\n")
        f.write("task1a_f1_macro_avg: " + str(f_ref_macro) + "\n")
        f.write("task1b_precision_micro_avg: " + str(precision_facet_micro) + "\n")
        f.write("task1b_precision_macro_avg: " + str(precision_facet_macro) + "\n")
        f.write("task1b_recall_micro_avg: " + str(recall_facet_micro) + "\n")
        f.write("task1b_recall_macro_avg: " + str(recall_facet_macro) + "\n")
        f.write("task1b_f1_micro_avg: " + str(f_facet_micro) + "\n")
        f.write("task1b_f1_macro_avg: " + str(f_facet_macro) + "\n")

if __name__ == "__main__":
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    main(input_dir, output_dir)
