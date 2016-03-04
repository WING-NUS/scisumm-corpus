# README for the The 2nd Computational Linguistics Scientific Document Summarization Shared Task Corpus (CL-SciSumm 2016)

## (scisumm-corpus @ https://github.com/WING-NUS/scisumm-corpus)

February 29, 2016

This is the open repository for the Scientific Document Summarization Corpus and Annotations contributed to the public by the Web IR / NLP Group at @ the National University of Singapore (WING-NUS) 
with generous support from Microsoft Research Asia.

Please read further for details on the Computational Linguistics Shared Task run as part of BIRNDL 2016 workshop collocated with JCDL 2016.

To participate in the 2016 shared task, please register your team details at: https://easychair.org/conferences/?conf=birndl2016

Please see ./docs/corpusconstruction.txt for details. 

### Overview

You are invited to participate in the CL-SciSumm Shared Task at BIRNDL 2016. The shared task will be on automatic paper summarization in the Computational Linguistics (CL) domain. The output summaries will be of two types: faceted summaries of the traditional self-summary (the abstract) and the community summary (the collection of citation sentences ‘citances’). We also propose to group the citances by the facets of the text that they refer to.

This task follows up on the successful CL Pilot Task conducted as a part of the BiomedSumm Track at the Text Analysis Conference 2014 (TAC 2014).
It follows the basic  structure and guidelines of the Biomedical Summarization Track and adapts them for annotating and 
creating a corpus of training topics from computational linguistics research papers.  
The task is defined as follows:

Given: A topic consisting of a Reference Paper (RP) and upto 10 Citing Papers (CPs) that all contain citations to the RP. In each CP, the text spans (i.e., citances) have been identified that pertain to a particular citation to the RP.

* Task 1a: For each citance, identify the spans of text (cited text spans) in the RP that most accurately reflect the citance. These are of the granularity  of a sentence fragment, a full sentence, or several consecutive sentences (no more than 5).
* Task 1b: For each cited text span, identify what facet of the paper it belongs to, from a predefined set of facets.

For more information about the project, please refer to the details hosted at 
http://wing.comp.nus.edu.sg/cl-scisumm2016/

BIRNDL Workshop home page: http://wing.comp.nus.edu.sg/cl-scisumm2016

This package contains an release of training topics to aid in the development of 
computational linguistics summarization systems.

### Contents

    ./README.md
 
This file.

    ./FAQ2016
	
Frequently asked questions on the 2016 shared task including updates to the corpus, 
annotation format from the previous edition.

    ./README2014.md
 
README file for the previous edition of the shared task hosted at TAC2014.

    ./docs/corpusconstruction.txt
 
A readme detailing the rules and steps followed to create the document
corpus by randomly sampling 10 documents from the ACL Anthology corpus
and selecting their citing papers.
  
    ./docs/annotation_naming_convention.txt

Describes the naming convention followed to identify annotation files 
for each training topic in ./data/???-????_TRAIN/Annotation/

    ./docs/annotation_rules.txt
  
Rules followed to resolve difficult cases in annotation. It can serve as a 
synopsis of the larger annotation guidelines. For the detailed annotation guidelines, 
please refer to the details hosted at http://www.nist.gov/tac/2014/BiomedSumm/

    ./docs/sources/*.csv

References for each of the papers for each of the topics, one file
per topic.

    ./data/???-????_TRAIN
  
Directories containing the Documents, Summaries, and Annotations for
each topic, one directory per Topic ID.

    ./data/???-????_TRAIN/Documents_PDF/

This directory contains the 10 source documents for the topic (1 RP
and upto 10 CPs), one file per paper, in the original pdf format.

    ./data/???-????_TRAIN/Reference_XML/

This directory contains the source document for the RP of the topic in xml format in 
UTF-8 character encoding. The file corresponds to the similarly named pdf file in 
Documents_PDF/. All annotations and offsets for the topic are with respect to the xml 
files in this directory. All the files were created from the pdf file using Adobe Acrobat.  
Note that there were OCR errors in reading several of the files, and the annotators often 
had to manually edit the converted txt files. Research groups using are free to use alternative 
parsing tools on the pdfs provided, if they are found to perform better.

    ./data/???-????_TRAIN/CITANCE_XML/
	
This directory contains the source document for the CPs of the topic in xml format in 
UTF-8 character encoding. Each file corresponds to the similarly named pdf file above.  

    ./data/???-????_TRAIN/Annotation/

This directory contains the annotation files for the topic, from 3 different annotators.  
The annotation files are named with the following convention: <TopicID>.<AnnotatorID>.ann3.txt 
The naming convention is explained in ./docs/annotation\_naming\_convention.txt.
Please DO NOT use older annotations from <TopicID>.<AnnotatorID>.ann.txt and 
<TopicID>.<AnnotatorID>.ann2.txt for the 2016 Shared Task.

### Annotation

Given a reference paper (RP) and upto 10 citing papers (CPs), annotators from 
National University of Singapore and Nanyang Technological University
were instructed to find citations to the RP in the 10 CPs. Annotators followed instructions
in SciSumm-annotation-guidelines.pdf to mark the Citation Text,
Citation Marker, Reference Text, and Discourse Facet for each citation
of the RP found in the CP.  

### Contact Information

For further information about this data release, contact the following
members of the BiomedSumm Organizing Committee:

* Kokil Jaidka (Nanyang Technological University) <koki0001@e.ntu.edu.sg>
* Min-Yen Kan (Dept. of Computer Science, School of Computing, National University of Singapore) <kanmy@comp.nus.edu.sg>
* Muthu Kumar Chandrasekaran (Dept. of Computer Science, School of Computing, National University of Singapore) <muthu.chandra@comp.nus.edu.sg>
* Ankur Khanna (Web,IR/NLP group, National University of Singapore) <khanna89ankur@gmail.com>
  
--------------------------------------------------------------------------

This README was updated from README2014 by Muthu Kumar Chandrasekaran in Feb, 2016.  For revision information, check source code control logs.
