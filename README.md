# README for the TAC 2014 Computational Linguistics Shared Task Corpus

## (scisumm-corpus @ https://github.com/WING-NUS/scisumm-corpus)

August 27, 2014

This is the open repository for the Scientific Document Summarization Corpus and Annotations contributed to the public by the Web IR / NLP Group at @ the National University of Singapore (WING-NUS).

Please read further for details on the TAC 2014 Computational Linguistics Shared Task.

Please see ./docs/corpusconstruction.txt for details. 

### Overview

The Computational Linguistics Shared Task is under the Biomedical Summarization Track of the Text Analysis Conference. It follows the basic  structure and guidelines of the Biomedical Summarization Track and adapts them for annotating and creating a corpus of training topics from computational linguistics research papers.  The task is defined as follows:

Given: A topic consisting of a Reference Paper (RP) and upto 10 Citing Papers (CPs) that all contain citations to the RP. In each CP, the text spans (i.e., citances) have been identified that pertain to a particular citation to the RP.

* Task 1a: For each citance, identify the spans of text (cited text spans) in the RP that most accurately reflect the citance. These are of the granularity  of a sentence fragment, a full sentence, or several consecutive sentences (no more than 5).
* Task 1b: For each cited text span, identify what facet of the paper it belongs to, from a predefined set of facets.

For more information about the project, please refer to the details hosted at 
http://www.nist.gov/tac/2014/BiomedSumm/

This package contains an initial (partial) release of training topics
to aid in the development of computational linguistics summarization systems.

### Contents

    ./README.md
 
This file.

    ./docs/corpusconstruction.txt
 
A readme detailing the rules and steps followed to create the document
corpus by randomly sampling 10 documents from the ACL Anthology corpus
and selecting their citing papers.
  
    ./docs/annotation_naming_convention.txt

Describes the naming convention followed to identify annotation files 
for each training topic in ./data/???-????_TRAIN/Annotation/

    ./docs/annotation_rules.txt
  
Rules followed to resolve difficult cases in annotation. It can serve as a synopsis of the larger annotation guidelines. For the detailed annotation guidelines, please refer to the details hosted at http://www.nist.gov/tac/2014/BiomedSumm/

    ./docs/sources/*.csv

References for each of the papers for each of the topics, one file
per topic.

    ./data/???-????_TRAIN
  
Directories containing the Documents, Summaries, and Annotations for
each topic, one directory per Topic ID.

    ./data/???-????_TRAIN/Documents_PDF/

This directory contains the 10 source documents for the topic (1 RP
and upto 10 CPs), one file per paper, in the original pdf format.

    ./data/???-????_TRAIN/Documents_TXT/

This directory contains the 10 source documents for the topic in UTF-8 text format, where each file corresponds to the similarly named pdf file above.  All annotations and offsets for the topic are with respect to the text files in this directory.  Most text files
were created from the pdf file using Adobe Acrobat. The remaining were
converted using the GATE 8.0 open source software. 
However, there were OCR errors in reading several of the files, and the
annotators often had to manually edit the converted txt files.
Research groups using are free to use alternative parsing tools on the pdfs provided, if they are found to perform better.

    ./data/???-????_TRAIN/Annotation/

This directory contains the annotation files for the topic, from 3 different annotators.  The annotation files are named with the following convention: <TopicID>.<AnnotatorID>.ann.txt The naming convention is explained in ./docs/annotation\_naming\_convention.txt.

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

README first created by Kokil Jaidka on Aug 27, 2014.  For revision information, check source code control logs.
