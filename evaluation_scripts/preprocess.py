# -*- coding: utf-8 -*-
"""
Created on Thu May 26 15:00:50 2016

@author: rustagi
"""

folder_read="C:\\Users\\rustagi\\Desktop\\Work_home\\summaries\\"
folder_write="C:\\Users\\rustagi\\Desktop\\rouge\\Rouge_Java\\Summaries_ROGUE\\"

#filenames_1_reference=folder_read+"C02-1025.abstract.txt"
#filenames_1_reference_write=folder_write+"reference\\"+"C02-1025_abstract.txt"
#
#file_open_read=open(filenames_1_reference,"r")
#file_open_write=open(filenames_1_reference_write,"a")
#
#for line in file_open_read.readlines() :
#    line=line.split(">")[1].split("<")[0]+"\n"
#    file_open_write.write(line)
##    
#file_open_read.close()   
#file_open_write.close()

#filenames_1_reference=folder_read+"C02-1025.community.txt"
#filenames_1_reference_write=folder_write+"reference\\"+"C02-1025_community.txt"
#
#file_open_read=open(filenames_1_reference,"r")
#file_open_write=open(filenames_1_reference_write,"a")
#
#for line in file_open_read.readlines() :
#    line=line.split(">")[1].split("<")[0]+"\n"
#    file_open_write.write(line)
#     
#file_open_read.close()   
#file_open_write.close()

#filenames_1_reference=folder_read+"C02-1025.human.txt"
#filenames_1_reference_write=folder_write+"system\\"+"C02-1025_human1.txt"
#
#file_open_read=open(filenames_1_reference,"r")
#file_open_write=open(filenames_1_reference_write,"a")
#
#for line in file_open_read.readlines() :
#    lines=line.split(".")
#    for line_split in lines:
#        if line_split.replace(" ","")!="" :
#            file_open_write.write(line_split+".\n")
# 
#file_open_read.close()   
#file_open_write.close()



import os
#for file in os.listdir(folder_read):
#    if file.endswith(".txt"):
#        filenames_1_reference=folder_read+file
#        file_open_read=open(filenames_1_reference,"r")
#        if "human" in file:
#            filenames_1_reference_write=folder_write+"system\\"+file.split(".")[0]+"_human1.txt"
#            file_open_write=open(filenames_1_reference_write,"a")
#            
#            for line in file_open_read.readlines() :
#                lines=line.split(".")
#                for line_split in lines:
#                    if line_split.replace(" ","")!="" :
#                        file_open_write.write(line_split+".\n")
#        else :
#            filenames_1_reference_write=folder_write+"reference\\"+file.split(".")[0]+"_"+file.split(".")[1]+".txt"
#            file_open_write=open(filenames_1_reference_write,"a")
#            
#            for line in file_open_read.readlines() :
#                line=line.split(">")[1].split("<")[0]+"\n"
#                file_open_write.write(line)
#        file_open_read.close()   
#        file_open_write.close()
            
#            

#folder_read="C:\\Users\\rustagi\\Desktop\\rouge\\Rouge_Java\\Summaries_Gold_Community\\reference_1\\"
#folder_write="C:\\Users\\rustagi\\Desktop\\rouge\\Rouge_Java\\Summaries_Gold_Community\\reference\\"
#for file in os.listdir(folder_read):
#    print file
#    filenames_1_reference=folder_read+file
#    file_open_read=open(filenames_1_reference,"r")
#    filenames_1_reference_write=folder_write+file
#    file_open_write=open(filenames_1_reference_write,"w")
#    for line in file_open_read.readlines() :
#            if line!="\n":
#                #print line
#                line=line.split(">")[1].split("<")[0]+"\n"
#                file_open_write.write(line)
#    file_open_write.close()
##    
#folder_read="C:\\Users\\rustagi\\Desktop\\rouge\\Rouge_Java\\Summaries_Gold_Human\\reference_1\\"
#folder_write="C:\\Users\\rustagi\\Desktop\\rouge\\Rouge_Java\\Summaries_Gold_Human\\reference\\"
#for file in os.listdir(folder_read):
#    print file
#    filenames_1_reference=folder_read+file
#    file_open_read=open(filenames_1_reference,"r")
#    filenames_1_reference_write=folder_write+file
#    file_open_write=open(filenames_1_reference_write,"w")
#    for line in file_open_read.readlines() :
#        lines=line.split(".")
#        for line_split in lines:
#            if line_split.replace(" ","")!="" :
#                file_open_write.write(line_split+".\n")
#    file_open_write.close()
    
    
count=0
folder_read="C:\\Users\\rustagi\\Desktop\\Work_home\\new_system\\"
folder_write="C:\\Users\\rustagi\\Desktop\\rouge\\Rouge_Java\\Summaries_Gold_Human\\system\\"
for systems in os.listdir(folder_read):
    if systems != "Gold":
        for runs in os.listdir(folder_read+systems):
             run_path=folder_read+systems+"\\"+runs+"\\"
             for tasks in os.listdir(run_path):
                 if tasks=="Task2" :
                    for files in os.listdir(run_path+tasks+"\\"):
                        filenames_1_reference=run_path+tasks+"\\"+files
                        file_open_read=open(filenames_1_reference,"r")
                        file_split=files.split(".")[0]
                        file_write=file_split+"_"+systems+"$"+runs+".txt"
                        filenames_1_reference_write=folder_write+file_write
                        file_open_write=open(filenames_1_reference_write,"w")
                        if systems=="System15":
                            for line in file_open_read.readlines() :
                                lines=line.split(".")
                                for line_split in lines:
                                    if line_split.replace(" ","")!="" :
                                        file_open_write.write(line_split+".\n")
                        else :
                            for line in file_open_read.readlines() :
                                file_open_write.write(line)
                        file_open_write.close()
                            

