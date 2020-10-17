import os
import sys

def process(input_file, output_file):
    output_text = ""
    if input_file.endswith("abstract.summary.txt") or input_file.endswith("community.summary.txt") or input_file.endswith("combined.summary.txt") or input_file.endswith("human.summary.txt"):
        input_text = []
        with open(input_file, "r") as f:
            input_text = f.readlines()
        for i in range(len(input_text)):
            inp = input_text[i].strip()
            if len(inp) == 0:
                continue
            if inp.startswith("<S sid ="):
                out = inp.split(">", 1)[1]
                out = out.split("</S>", 1)[0]
            else:
                out = inp
            output_text += out + " "
    else:
        with open(input_file, "r") as f:
            output_text = f.read()

    with open(output_file, "w") as f:
        f.write(output_text)

def main(input_dir, output_dir):
    if not os.path.exists(input_dir):
        print("%s not a valid directory" % input_dir)
    if not os.path.exists(output_dir):
        print("%s not a valid directory" % output_dir)
    
    for file in os.listdir(input_dir):
        process(os.path.join(input_dir, file), os.path.join(output_dir, file))

if __name__ == "__main__":
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    main(input_dir, output_dir)