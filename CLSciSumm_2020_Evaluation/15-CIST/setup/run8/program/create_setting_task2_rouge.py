import sys
import os

input_dir = sys.argv[1]
if input_dir.endswith("/"):
    input_dir = input_dir[0:-1]
output_dir = sys.argv[2]
model_type = sys.argv[3]
print("creating setting: " + model_type)

# paper_ids = ["A00-2018", "A00-2030", "A97-1014", "D09-1092", "D10-1044", "E03-1005", "J01-2004", "P04-1036", "P05-1013", "P08-1028", "P08-1043", "P08-1102","P11-1060", "P11-1061", "P87-1015", "W06-2932", "W06-3114", "W11-2123", "W99-0613", "W99-0623"]

paper_ids = []
for fname in os.listdir(input_dir +"/res/Task2"):
    fname_paper = fname.split('.')[0]
    paper_ids.append(fname_paper)

settings_string = """<ROUGE_EVAL version="1.5.5">"""
for paper_id in paper_ids:
    one_setting = """<EVAL ID="%s">
        <PEER-ROOT>
            {input_dir}/res/Task2
        </PEER-ROOT>

        <MODEL-ROOT>
            {input_dir}/ref/Task2
        </MODEL-ROOT>

        <INPUT-FORMAT TYPE="SPL"></INPUT-FORMAT>

        <PEERS>
            <P ID="system">%s.system.txt</P>
        </PEERS>""" % (paper_id, paper_id)

    model_setting = """<MODELS>"""
    for ref_fname in os.listdir(input_dir +"/ref/Task2"):
        ref_fname_paper = ref_fname.split('.')[0].split('_')[0]
        ref_fname_summtype = ref_fname.split('.')[1]
        if (ref_fname_paper == paper_id) and (ref_fname_summtype == model_type): # this is the right summary
            model_setting += """<M ID="%s">%s</M>""" % (model_type, ref_fname)
    model_setting += """</MODELS>"""

    one_setting += model_setting
    one_setting += """</EVAL>"""

    settings_string += one_setting

settings_string += """</ROUGE_EVAL>"""

# settings_string = """<ROUGE_EVAL version="1.5.5">
#     <EVAL ID="C98-1097">
#         <PEER-ROOT>
#             {input_dir}/res/Task2
#         </PEER-ROOT>
#
#         <MODEL-ROOT>
#             {input_dir}/ref/Task2
#         </MODEL-ROOT>
#
#         <INPUT-FORMAT TYPE="SPL"></INPUT-FORMAT>
#
#         <PEERS>
#             <P ID="system">C98-1097.system.txt</P>
#         </PEERS>
#
#         <MODELS>
#             <M ID="abstract">C98-1097.{model_type}.summary.txt</M>
#         </MODELS>
#     </EVAL>
#     <EVAL ID="D09-1023">
#         <PEER-ROOT>
#             {input_dir}/res/Task2
#         </PEER-ROOT>
#
#         <MODEL-ROOT>
#             {input_dir}/ref/Task2
#         </MODEL-ROOT>
#
#         <INPUT-FORMAT TYPE="SPL"></INPUT-FORMAT>
#
#         <PEERS>
#             <P ID="system">D09-1023.system.txt</P>
#         </PEERS>
#
#         <MODELS>
#             <M ID="abstract">D09-1023.{model_type}.summary.txt</M>
#         </MODELS>
#     </EVAL>
#     <EVAL ID="D10-1058">
#         <PEER-ROOT>
#             {input_dir}/res/Task2
#         </PEER-ROOT>
#
#         <MODEL-ROOT>
#             {input_dir}/ref/Task2
#         </MODEL-ROOT>
#
#         <INPUT-FORMAT TYPE="SPL"></INPUT-FORMAT>
#
#         <PEERS>
#             <P ID="system">D10-1058.system.txt</P>
#         </PEERS>
#
#         <MODELS>
#             <M ID="abstract">D10-1058.{model_type}.summary.txt</M>
#         </MODELS>
#     </EVAL>
#     <EVAL ID="N09-1001">
#         <PEER-ROOT>
#             {input_dir}/res/Task2
#         </PEER-ROOT>
#
#         <MODEL-ROOT>
#             {input_dir}/ref/Task2
#         </MODEL-ROOT>
#
#         <INPUT-FORMAT TYPE="SPL"></INPUT-FORMAT>
#
#         <PEERS>
#             <P ID="system">N09-1001.system.txt</P>
#         </PEERS>
#
#         <MODELS>
#             <M ID="abstract">N09-1001.{model_type}.summary.txt</M>
#         </MODELS>
#     </EVAL>
#     <EVAL ID="N09-1025">
#         <PEER-ROOT>
#             {input_dir}/res/Task2
#         </PEER-ROOT>
#
#         <MODEL-ROOT>
#             {input_dir}/ref/Task2
#         </MODEL-ROOT>
#
#         <INPUT-FORMAT TYPE="SPL"></INPUT-FORMAT>
#
#         <PEERS>
#             <P ID="system">N09-1025.system.txt</P>
#         </PEERS>
#
#         <MODELS>
#             <M ID="abstract">N09-1025.{model_type}.summary.txt</M>
#         </MODELS>
#     </EVAL>
#     <EVAL ID="P00-1025">
#         <PEER-ROOT>
#             {input_dir}/res/Task2
#         </PEER-ROOT>
#
#         <MODEL-ROOT>
#             {input_dir}/ref/Task2
#         </MODEL-ROOT>
#
#         <INPUT-FORMAT TYPE="SPL"></INPUT-FORMAT>
#
#         <PEERS>
#             <P ID="system">P00-1025.system.txt</P>
#         </PEERS>
#
#         <MODELS>
#             <M ID="abstract">P00-1025.{model_type}.summary.txt</M>
#         </MODELS>
#     </EVAL>
#     <EVAL ID="P07-1040">
#         <PEER-ROOT>
#             {input_dir}/res/Task2
#         </PEER-ROOT>
#
#         <MODEL-ROOT>
#             {input_dir}/ref/Task2
#         </MODEL-ROOT>
#
#         <INPUT-FORMAT TYPE="SPL"></INPUT-FORMAT>
#
#         <PEERS>
#             <P ID="system">P07-1040.system.txt</P>
#         </PEERS>
#
#         <MODELS>
#             <M ID="abstract">P07-1040.{model_type}.summary.txt</M>
#         </MODELS>
#     </EVAL>
#     <EVAL ID="W06-3909">
#         <PEER-ROOT>
#             {input_dir}/res/Task2
#         </PEER-ROOT>
#
#         <MODEL-ROOT>
#             {input_dir}/ref/Task2
#         </MODEL-ROOT>
#
#         <INPUT-FORMAT TYPE="SPL"></INPUT-FORMAT>
#
#         <PEERS>
#             <P ID="system">W06-3909.system.txt</P>
#         </PEERS>
#
#         <MODELS>
#             <M ID="abstract">W06-3909.{model_type}.summary.txt</M>
#         </MODELS>
#     </EVAL>
#     <EVAL ID="W09-0621">
#         <PEER-ROOT>
#             {input_dir}/res/Task2
#         </PEER-ROOT>
#
#         <MODEL-ROOT>
#             {input_dir}/ref/Task2
#         </MODEL-ROOT>
#
#         <INPUT-FORMAT TYPE="SPL"></INPUT-FORMAT>
#
#         <PEERS>
#             <P ID="system">W09-0621.system.txt</P>
#         </PEERS>
#
#         <MODELS>
#             <M ID="abstract">W09-0621.{model_type}.summary.txt</M>
#         </MODELS>
#     </EVAL>
#     <EVAL ID="W11-0815">
#         <PEER-ROOT>
#             {input_dir}/res/Task2
#         </PEER-ROOT>
#
#         <MODEL-ROOT>
#             {input_dir}/ref/Task2
#         </MODEL-ROOT>
#
#         <INPUT-FORMAT TYPE="SPL"></INPUT-FORMAT>
#
#         <PEERS>
#             <P ID="system">W11-0815.system.txt</P>
#         </PEERS>
#
#         <MODELS>
#             <M ID="abstract">W11-0815.{model_type}.summary.txt</M>
#         </MODELS>
#     </EVAL>
# </ROUGE_EVAL>"""

result_settings = settings_string.format(**locals())

with open(os.path.join(output_dir, "task2_settings.xml"), "w") as f:
    f.write(result_settings)
