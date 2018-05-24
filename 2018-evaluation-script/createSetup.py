import sys
import os
import shutil

run_dir = sys.argv[1]
gold_dir = sys.argv[2]
output_dir = sys.argv[3]
program_dir = sys.argv[4]

for subdir in os.listdir(run_dir):
    if os.path.isdir(os.path.join(run_dir, subdir)):
        os.makedirs(os.path.join(output_dir, subdir))
        os.mkdir(os.path.join(output_dir, subdir, "input"))
        shutil.copytree(os.path.join(run_dir, subdir), os.path.join(output_dir, subdir, "input", "res"))
        shutil.copytree(gold_dir, os.path.join(output_dir, subdir, "input", "ref"))
        os.mkdir(os.path.join(output_dir, subdir, "output"))
        shutil.copytree(program_dir, os.path.join(output_dir, subdir, "program"))

