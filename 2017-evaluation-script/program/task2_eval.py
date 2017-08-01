import sys
import os

def main(input_file, output_file, model_type):
    with open(input_file, "r") as f:
        raw_content = f.readlines()
    average_r = 0
    average_p = 0
    average_f = 0

    scores = {}

    for line in raw_content:
        if line.startswith("system"):
            fields = line.split()
            print(fields)
            if fields[2].startswith("Average_P"):
                average_p = float(fields[3])
            elif fields[2].startswith("Average_R"):
                average_r = float(fields[3])
            elif fields[2].startswith("Average_F"):
                average_f = float(fields[3])
            else:
                file_name = fields[3].split(".")[0]
                model_cnt = int(fields[4].split(":")[1])
                peer_cnt = int(fields[5].split(":")[1])
                hit = int(fields[6].split(":")[1])
                try:
                    r = hit / float(model_cnt)
                except ZeroDivisionError as e: 
                    r = 0
                try:
                    p = hit / float(peer_cnt)
                except ZeroDivisionError as e: 
                    p = 0
                try:
                    f = 2 * p * r / float(p + r)
                except ZeroDivisionError as e: 
                    f = 0
                scores[file_name] = {}
                scores[file_name]['p'] = p
                scores[file_name]['r'] = r
                scores[file_name]['f'] = f

    with open(output_file, "a") as f:
        for file in scores:
            f.write(file + "_" + model_type + "_task2_precision: " + str(scores[file]['p']) + "\n")
            f.write(file + "_" + model_type + "_task2_recall: " + str(scores[file]['r']) + "\n")
            f.write(file + "_" + model_type + "_task2_f1: " + str(scores[file]['f']) + "\n")
        f.write(model_type + "_task2_precision_avg: " + str(average_p) + "\n")
        f.write(model_type + "_task2_recall_avg: " + str(average_r) + "\n")
        f.write(model_type + "_task2_f1_avg: " + str(average_f) + "\n")

if __name__ == "__main__":
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    model_type = sys.argv[3]
    unformat_result_file = os.path.join(output_dir, "task2_raw")
    score_file = os.path.join(output_dir, "scores.txt")
    if not os.path.exists(unformat_result_file):
        print("raw file does not exist")
        with open(score_file, "a") as f:
            for file in os.listdir(os.path.join(input_dir, "ref", "Task2")):
                file = file.split(".")[0]
                model_type = file.split(".")[1]
                f.write(file + "_" + model_type + "_task2_precision: 0.0\n")
                f.write(file + "_" + model_type + "_task2_recall: 0.0\n")
                f.write(file + "_" + model_type + "_task2_f1: 0.0\n")
            f.write(model_type + "_task2_precision_avg: 0.0\n")
            f.write(model_type + "_task2_recall_avg: 0.0\n")
            f.write(model_type + "_task2_f1_avg: 0.0\n")
    else:
        print("else part task 2")
        print("eval: " + model_type)
        main(unformat_result_file, score_file, model_type)
