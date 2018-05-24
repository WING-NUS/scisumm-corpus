import sys
import os
import shutil

working_dir = sys.argv[1]
working_dir_list = [run for run in os.listdir(working_dir) if not run.startswith(".")]
for run in working_dir_list:
    print("\n\n")
    print(run)
    task1_run_dir = os.path.join(working_dir, run, "input", "res", "Task1")
    print(task1_run_dir)
    if os.path.exists(task1_run_dir):
        print(task1_run_dir)
        task1_run_dir_list = [x for x in os.listdir(task1_run_dir) if not x.startswith(".")]
        print(task1_run_dir_list)
        if len(task1_run_dir_list) == 0:
            shutil.rmtree(task1_run_dir)
        for task1_file in task1_run_dir_list:
            print(task1_file)
            if os.path.isfile(os.path.join(task1_run_dir, task1_file)) and not task1_file.startswith("."):
                doc_name = task1_file.split(".", 1)[0]
                new_doc_name = doc_name + ".annv3.txt"
                print(os.path.join(task1_run_dir, new_doc_name))
                os.rename(os.path.join(task1_run_dir, task1_file), os.path.join(task1_run_dir, new_doc_name))
    else:
        print("does not exist")

    task2_run_dir = os.path.join(working_dir, run, "input", "res", "Task2")
    if os.path.exists(task2_run_dir):
        print(task2_run_dir)
        task2_run_dir_list = [x for x in os.listdir(task2_run_dir) if not x.startswith(".")]
        if len(task2_run_dir_list) == 0:
            shutil.rmtree(task2_run_dir)        
        for task2_file in task2_run_dir_list:
            if os.path.isfile(os.path.join(task2_run_dir, task2_file)) and not task2_file.startswith("."):
                doc_name = task2_file.split(".", 1)[0]
                new_doc_name = doc_name + ".system.txt"
                print(os.path.join(task2_run_dir, new_doc_name))
                os.rename(os.path.join(task2_run_dir, task2_file), os.path.join(task2_run_dir, new_doc_name))