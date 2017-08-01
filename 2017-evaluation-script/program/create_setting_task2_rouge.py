import sys
import os

input_dir = sys.argv[1]
if input_dir.endswith("/"):
    input_dir = input_dir[0:-1]
output_dir = sys.argv[2]
model_type = sys.argv[3]
print("creating setting: " + model_type)

settings_string = """<ROUGE_EVAL version="1.5.5">
    <EVAL ID="C98-1097">
        <PEER-ROOT>
            {input_dir}/res/Task2
        </PEER-ROOT>
        
        <MODEL-ROOT>
            {input_dir}/ref/Task2
        </MODEL-ROOT>
        
        <INPUT-FORMAT TYPE="SPL"></INPUT-FORMAT>
        
        <PEERS>
            <P ID="system">C98-1097.system.txt</P>
        </PEERS>
        
        <MODELS>
            <M ID="abstract">C98-1097.{model_type}.summary.txt</M>
        </MODELS>
    </EVAL>
    <EVAL ID="D09-1023">
        <PEER-ROOT>
            {input_dir}/res/Task2
        </PEER-ROOT>
        
        <MODEL-ROOT>
            {input_dir}/ref/Task2
        </MODEL-ROOT>
        
        <INPUT-FORMAT TYPE="SPL"></INPUT-FORMAT>
        
        <PEERS>
            <P ID="system">D09-1023.system.txt</P>
        </PEERS>
        
        <MODELS>
            <M ID="abstract">D09-1023.{model_type}.summary.txt</M>
        </MODELS>
    </EVAL>
    <EVAL ID="D10-1058">
        <PEER-ROOT>
            {input_dir}/res/Task2
        </PEER-ROOT>
        
        <MODEL-ROOT>
            {input_dir}/ref/Task2
        </MODEL-ROOT>
        
        <INPUT-FORMAT TYPE="SPL"></INPUT-FORMAT>
        
        <PEERS>
            <P ID="system">D10-1058.system.txt</P>
        </PEERS>
        
        <MODELS>
            <M ID="abstract">D10-1058.{model_type}.summary.txt</M>
        </MODELS>
    </EVAL>
    <EVAL ID="N09-1001">
        <PEER-ROOT>
            {input_dir}/res/Task2
        </PEER-ROOT>
        
        <MODEL-ROOT>
            {input_dir}/ref/Task2
        </MODEL-ROOT>
        
        <INPUT-FORMAT TYPE="SPL"></INPUT-FORMAT>
        
        <PEERS>
            <P ID="system">N09-1001.system.txt</P>
        </PEERS>
        
        <MODELS>
            <M ID="abstract">N09-1001.{model_type}.summary.txt</M>
        </MODELS>
    </EVAL>
    <EVAL ID="N09-1025">
        <PEER-ROOT>
            {input_dir}/res/Task2
        </PEER-ROOT>
        
        <MODEL-ROOT>
            {input_dir}/ref/Task2
        </MODEL-ROOT>
        
        <INPUT-FORMAT TYPE="SPL"></INPUT-FORMAT>
        
        <PEERS>
            <P ID="system">N09-1025.system.txt</P>
        </PEERS>
        
        <MODELS>
            <M ID="abstract">N09-1025.{model_type}.summary.txt</M>
        </MODELS>
    </EVAL>
    <EVAL ID="P00-1025">
        <PEER-ROOT>
            {input_dir}/res/Task2
        </PEER-ROOT>
        
        <MODEL-ROOT>
            {input_dir}/ref/Task2
        </MODEL-ROOT>
        
        <INPUT-FORMAT TYPE="SPL"></INPUT-FORMAT>
        
        <PEERS>
            <P ID="system">P00-1025.system.txt</P>
        </PEERS>
        
        <MODELS>
            <M ID="abstract">P00-1025.{model_type}.summary.txt</M>
        </MODELS>
    </EVAL>
    <EVAL ID="P07-1040">
        <PEER-ROOT>
            {input_dir}/res/Task2
        </PEER-ROOT>
        
        <MODEL-ROOT>
            {input_dir}/ref/Task2
        </MODEL-ROOT>
        
        <INPUT-FORMAT TYPE="SPL"></INPUT-FORMAT>
        
        <PEERS>
            <P ID="system">P07-1040.system.txt</P>
        </PEERS>
        
        <MODELS>
            <M ID="abstract">P07-1040.{model_type}.summary.txt</M>
        </MODELS>
    </EVAL>
    <EVAL ID="W06-3909">
        <PEER-ROOT>
            {input_dir}/res/Task2
        </PEER-ROOT>
        
        <MODEL-ROOT>
            {input_dir}/ref/Task2
        </MODEL-ROOT>
        
        <INPUT-FORMAT TYPE="SPL"></INPUT-FORMAT>
        
        <PEERS>
            <P ID="system">W06-3909.system.txt</P>
        </PEERS>
        
        <MODELS>
            <M ID="abstract">W06-3909.{model_type}.summary.txt</M>
        </MODELS>
    </EVAL>
    <EVAL ID="W09-0621">
        <PEER-ROOT>
            {input_dir}/res/Task2
        </PEER-ROOT>
        
        <MODEL-ROOT>
            {input_dir}/ref/Task2
        </MODEL-ROOT>
        
        <INPUT-FORMAT TYPE="SPL"></INPUT-FORMAT>
        
        <PEERS>
            <P ID="system">W09-0621.system.txt</P>
        </PEERS>
        
        <MODELS>
            <M ID="abstract">W09-0621.{model_type}.summary.txt</M>
        </MODELS>
    </EVAL>
    <EVAL ID="W11-0815">
        <PEER-ROOT>
            {input_dir}/res/Task2
        </PEER-ROOT>
        
        <MODEL-ROOT>
            {input_dir}/ref/Task2
        </MODEL-ROOT>
        
        <INPUT-FORMAT TYPE="SPL"></INPUT-FORMAT>
        
        <PEERS>
            <P ID="system">W11-0815.system.txt</P>
        </PEERS>
        
        <MODELS>
            <M ID="abstract">W11-0815.{model_type}.summary.txt</M>
        </MODELS>
    </EVAL>
</ROUGE_EVAL>
"""

result_settings = settings_string.format(**locals())

with open(os.path.join(output_dir, "task2_settings.xml"), "w") as f:
    f.write(result_settings)
