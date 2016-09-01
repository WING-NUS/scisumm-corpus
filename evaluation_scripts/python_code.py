# -*- coding: utf-8 -*-
"""
Created on Fri May 06 14:43:15 2016

@author: rustagi
"""
import ast
import os
import csv

csvfile=open('results_task1_last.csv', 'wb') 
fieldnames = ['System_Name','Filename','Precision_Task_1a','Recall_Task_1a','F1_Score_Task_1a','Precision_Task_1b','Recall_Task_1b','F1_Score_Task_1b']
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
writer.writeheader()


def calculate_values(list_gold,list_comp) :
    set_gold=set(list_gold)
    set_comp=set(list_comp)
    #print set_gold
    #print set_comp
    TP=len(set_gold.intersection(set_comp))
    FP=len(set_comp.difference(set_gold))
    FN=len(set_gold.difference(set_comp))
    return [TP,FP,FN]
    
def calculate_metric(TP,FP,FN) :
    recall="NA"
    precision="NA"
    sum_precision_deno=TP+FP
    if sum_precision_deno!=0 :
        precision=TP/float(sum_precision_deno)
    sum_recall_deno=TP+FN
    if sum_recall_deno!=0 :
        recall=TP/float(sum_recall_deno)
    return (precision,recall)
    
def make_dict(filename,dict_main) :
    gold_file=open(filename,"r")
    filename=filename.split(".")[0].split("\\")[-1]
    dict_main[filename]={}
    for lines in gold_file.readlines():
        if lines !="\n":
            #print lines
            split_line=lines[:-1].split(" | ")
            for index in [2,3] :
                item_split=split_line[index].split(":")
                item_name=item_split[0].strip()
                item_value=item_split[1].strip()
                if index==2:
                    if item_value not in dict_main[filename]:
                        dict_main[filename][item_value]={}
                    index_item_value_2=item_value
                else :
                    dict_main[filename][index_item_value_2][item_value]={}
                    index_item_value_3=item_value
            for index in range(len(split_line)) :
              if split_line[index]!="":
                item_split=split_line[index].split(":")
                #print item_split
                item_name=item_split[0].strip()
                item_value=item_split[1].strip()
                if index==3 or index==5 or index==7 :
                    if "-" in item_value :
                       item_value= ast.literal_eval("['"+item_value+"']") 
                    else :
                        item_value= ast.literal_eval(item_value)
                if index==9 :
                    if "[" in item_value :
                        item_value= ast.literal_eval(item_value)
                    else :
                        item_value=[item_value]
                dict_main[filename][index_item_value_2][index_item_value_3][item_name]=item_value
    return dict_main


result_file="results.txt"
folder_read="C:\\Users\\rustagi\\Desktop\\Work_home\\new_system\\"

dict_gold={}
gold_file_path=folder_read+"Gold\\Default\\Task1\\"
for file_2 in os.listdir(gold_file_path) :
    print file_2
    gold_filename=file_2.split(".")[0]
    dict_gold=make_dict(gold_file_path+gold_filename+".annv3.txt",dict_gold)


for systems in os.listdir(folder_read):
    if systems!="Gold" and systems!="System3" :
        for runs in os.listdir(folder_read+systems):
            system_name= systems+"->"+runs
            print system_name
          
            dict_comp={}
            comp_file_path=folder_read+systems+"\\"+runs+"\\Task1\\"
            for file_2 in os.listdir(comp_file_path) :
                print file_2
                comp_filename=file_2.split(".")[0]
                dict_comp=make_dict(comp_file_path+comp_filename+".annv3.txt",dict_comp)
            for files in dict_gold :
             
                main_file_values=dict_gold[files]
                comp_file_values=dict_comp[files]
                [TP_discourse_facet,FP_discourse_facet,FN_discourse_facet]=[0,0,0]
                #[TP_citation_marker,FP_citation_marker,FN_citation_marker]=[0,0,0]
                #[TP_citation_offset,FP_citation_offset,FN_citation_offset]=[0,0,0]
                [TP_reference_offset,FP_reference_offset,FN_reference_offset]=[0,0,0]
                
                
                for gold_values in main_file_values :
                    if gold_values in comp_file_values :
                        for gold_values_2 in main_file_values[gold_values] :
                            if gold_values_2 in comp_file_values[gold_values] :
                                    gold_value=main_file_values[gold_values][gold_values_2]
                                    comp_value=comp_file_values[gold_values][gold_values_2]
                                    old_value=TP_reference_offset        
                                    [TP_reference_offset,FP_reference_offset,FN_reference_offset]=[x+y for x,y in zip([TP_reference_offset,FP_reference_offset,FN_reference_offset], calculate_values(gold_value["Reference Offset"],comp_value["Reference Offset"]))]
                                    if (TP_reference_offset-old_value)>=1:
                                        [TP_discourse_facet,FP_discourse_facet,FN_discourse_facet]=[x+y for x,y in zip([TP_discourse_facet,FP_discourse_facet,FN_discourse_facet], calculate_values(gold_value["Discourse Facet"],comp_value["Discourse Facet"]))]
                                    else :
                                        [TP_discourse_facet,FP_discourse_facet,FN_discourse_facet]=[x+y for x,y in zip([TP_discourse_facet,FP_discourse_facet,FN_discourse_facet], calculate_values(gold_value["Discourse Facet"],[]))]
                   
                            else :
                                    gold_value=main_file_values[gold_values][gold_values_2]
                                    [TP_reference_offset,FP_reference_offset,FN_reference_offset]=[x+y for x,y in zip([TP_reference_offset,FP_reference_offset,FN_reference_offset], calculate_values(gold_value["Reference Offset"],[]))]
                                    [TP_discourse_facet,FP_discourse_facet,FN_discourse_facet]=[x+y for x,y in zip([TP_discourse_facet,FP_discourse_facet,FN_discourse_facet], calculate_values(gold_value["Discourse Facet"],[]))]
                                    print "2"   
                    else :
                        for gold_values_2 in main_file_values[gold_values] :
                            gold_value=main_file_values[gold_values][gold_values_2]
                            [TP_reference_offset,FP_reference_offset,FN_reference_offset]=[x+y for x,y in zip([TP_reference_offset,FP_reference_offset,FN_reference_offset], calculate_values(gold_value["Reference Offset"],[]))]
                            [TP_discourse_facet,FP_discourse_facet,FN_discourse_facet]=[x+y for x,y in zip([TP_discourse_facet,FP_discourse_facet,FN_discourse_facet], calculate_values(gold_value["Discourse Facet"],[]))]
                            print "4"
                            
                for comp_values in comp_file_values:
                    if comp_values in main_file_values :
                        for comp_values_2 in comp_file_values[comp_values] :
                            if comp_values_2 not in main_file_values[comp_values] :
                                comp_value=comp_file_values[comp_values][comp_values_2]
                                [TP_reference_offset,FP_reference_offset,FN_reference_offset]=[x+y for x,y in zip([TP_reference_offset,FP_reference_offset,FN_reference_offset], calculate_values([],comp_value["Reference Offset"]))]
                                [TP_discourse_facet,FP_discourse_facet,FN_discourse_facet]=[x+y for x,y in zip([TP_discourse_facet,FP_discourse_facet,FN_discourse_facet], calculate_values([],comp_value["Discourse Facet"]))]
                                print "1"
                                        
                    else :
                        for comp_values_2 in comp_file_values[comp_values] :
                            comp_value=comp_file_values[comp_values][comp_values_2]
                            [TP_reference_offset,FP_reference_offset,FN_reference_offset]=[x+y for x,y in zip([TP_reference_offset,FP_reference_offset,FN_reference_offset], calculate_values([],comp_value["Reference Offset"]))]
                            [TP_discourse_facet,FP_discourse_facet,FN_discourse_facet]=[x+y for x,y in zip([TP_discourse_facet,FP_discourse_facet,FN_discourse_facet], calculate_values([],comp_value["Discourse Facet"]))]
                            print "3"
                                    
                (precision_discourse_facet,recall_discourse_facet)=calculate_metric(TP_discourse_facet,FP_discourse_facet,FN_discourse_facet)
                if precision_discourse_facet!="NA" and recall_discourse_facet!="NA" :
                    if precision_discourse_facet+recall_discourse_facet!=0 :
                        f1_score_discourse_facet=2*precision_discourse_facet*recall_discourse_facet/float(precision_discourse_facet+recall_discourse_facet)
                    else :
                        f1_score_discourse_facet="NA"
                else :
                    f1_score_discourse_facet="NA"
                    #(precision_citation_marker,recall_citation_marker)=calculate_metric(TP_citation_marker,FP_citation_marker,FN_citation_marker)
                    #(precision_citation_offset,recall_citation_offset)=calculate_metric(TP_citation_offset,FP_citation_offset,FN_citation_offset)
                (precision_reference_offset,recall_reference_offset)=calculate_metric(TP_reference_offset,FP_reference_offset,FN_reference_offset)
                if precision_reference_offset!="NA" and recall_reference_offset!="NA" :
                    if precision_reference_offset+recall_reference_offset!=0 :
                        f1_score_reference_offset=2*precision_reference_offset*recall_reference_offset/float(precision_reference_offset+recall_reference_offset)
                    else :
                        f1_score_reference_offset="NA"
                else :
                    f1_score_reference_offset="NA"
               # writer.writerow({'System_Name': systems, 'Method': runs, 'Filename' :files,'Precision_Task_1a': precision_reference_offset,'Recall_Task_1a': recall_reference_offset,'F1_Score_Task_1a': f1_score_reference_offset,'Precision_Task_1b': precision_discourse_facet,'Recall_Task_1b': recall_discourse_facet,'F1_Score_Task_1b': f1_score_discourse_facet})
                writer.writerow({'System_Name': systems+"$"+runs, 'Filename' :files,'Precision_Task_1a': precision_reference_offset,'Recall_Task_1a': recall_reference_offset,'F1_Score_Task_1a': f1_score_reference_offset,'Precision_Task_1b': precision_discourse_facet,'Recall_Task_1b': recall_discourse_facet,'F1_Score_Task_1b': f1_score_discourse_facet})
    
csvfile.close()
"""    
gold_filename="C00-2123"   
comp_filename="C00-2123_ref_2"



dict_comp=make_dict(comp_filename+".annv3.txt",dict_comp)
main_file_values=dict_gold[gold_filename]
comp_file_values=dict_comp[comp_filename]

"""
                