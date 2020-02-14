# README 

# (scisumm-corpus @ https://github.com/WING-NUS/scisumm-corpus)

This package contains a release of training and test topics to aid in 
the development of computational linguistics summarization systems.

The CL-SciSumm Shared Task is run off the CL-SciSumm corpus and is composed of  
three sub-tasks in automatic research paper summarization on a new corpus 
of research papers. A training corpus of forty topics has been released. A 
test corpus of ten topics is held-out as a blind test-set. The topics comprise of ACL 
Computational Linguistics and Natural Language Processing research papers, and their 
citing papers and three output summaries each. The three output summaries comprise: 
the traditional authors' summary of the paper (the abstract), the community summary 
(the collection of citation sentences ‘citances’) and a human summary written 
by a trained annotator. Within the corpus, each citance is also mapped to its 
referenced text in the reference paper and tagged with the information facet 
it represents.

The manually annotated training set of 40 articles and citing papers 
is readily available for download and can be used by participants.
This data can be found in /data/Training-Set-2019/Task1/From-Training-Set-2018
and /data/Training-Set-2019/Task2/From-Training-Set-2018

**NEW Changes for CL-SciSumm 2020**

<To be Announced -- Stay Tuned>

**Updates for Cl-SciSumm 2019**

Further, this year we have introduced 1000 document 
sets that were automatically annotated to be used as training data. This 
training data was generated following Nomoto,2018. 
This data can be found in **/data/Training-Set-2019/Task1/From-ScisummNet-2019**. 
Note that the auto-annotated data is available only for *Task 1a*. No discourse facet is provided 
for the classification task: Task1b. We recommend you to use the auto-anootated data
only for training 'reference span selection' models for Task 1a and use the 
manually annotated training data from 40 document sets for Task1b.

Further, for Task 2 one thousand summaries that were released as part of 
the <a href="https://cs.stanford.edu/~myasu/projects/scisumm_net/">SciSummNet</a> (Yasunaga et al., 2019) have been included as human summaries to 
train on. This data can be found in **/data/Training-Set-2019/Task2/From-ScisummNet-2019**

The **test set** of 20 articles is available in **/data/Test-Set-2018**.
This is a blind test set, that is, the ground truth is withheld.
The system outputs from the test set should be submitted to the task organizers, 
for the collation of the final results to be presented at the workshop.

For more details, see the Contents Section at the bottom of this Readme. 
To know how this corpus was constructed, please see ./docs/corpusconstruction.txt

Results of the CL-SciSumm-20 will be released in the SDP workshop collocated 
with <a href="https://2020.emnlp.org/">EMNLP</a> 2020, Punta Cana, Dominican Republic. 
<a href="https://ornlcda.github.io/SDProc/">Go to task website</a>.<br> 

Last editions proceedings - CL-SciSumm '19 @ SIGIR '19 can be found in BIRNDL 
Proceedings: http://ceur-ws.org/Vol-2414/ under the header 'System Papers'

If you use the data and publish please let us know and cite our CL-SciSumm 2019 task overview paper:<br>
@inproceedings{,<br>
title={Overview and Results: CL-SciSumm Shared Task 2019},<br>
author={Chandrasekaran, Muthu Kumar and Yasunaga, Michihiro and Radev, Dragomir and Freitag, Dayne and Kan, Min-Yen},<br>
booktitle={In Proceedings of Joint Workshop on Bibliometric-enhanced Information Retrieval and NLP for Digital Libraries (BIRNDL 2019)},<br>
year={2019}<br>
}<br>

## README for The 6th Computational Linguistics Scientific Document Summarization Shared Task Corpus (CL-SciSumm 2020)

February 15, 2020

Please read further for details on the Computational Linguistics Shared Task run as part of 
Scholarly Document Processing 2020 workshop collocated with EMNLP 2020 @ Punta Cana, Dominican Republic, Nov 11/12 - official website hosted at: https://ornlcda.github.io/SDProc/

### Overview

You are invited to participate in the CL-SciSumm Shared Task at SDP@EMNLP 2020. The shared task will be on automatic 
paper summarization in the Computational Linguistics (CL) domain. The output summaries will be of two types: 
faceted summaries of the traditional self-summary (the abstract) and the community summary (the collection of 
citation sentences ‘citances’). We also propose to group the citances by the facets of the text that they refer to.

This task follows up on the successful previous editions at SIGIR 2019, 2018, 2017, JCDL 2016 and the Pilot Task conducted as 
a part of the BiomedSumm Track at the Text Analysis Conference 2014 (TAC 2014).

The task is defined as follows:

Given: A topic consisting of a Reference Paper (RP) and <del>upto 10</del> Citing Papers (CPs) that all contain citations to the RP. In each CP, the text spans (i.e., citances) have been identified that pertain to a particular citation to the RP.

* Task 1a: For each citance, identify the spans of text (cited text spans) in the RP that most accurately reflect the citance. These are of the granularity  of a sentence fragment, a full sentence, or several consecutive sentences (no more than 5).
* Task 1b: For each cited text span, identify what facet of the paper it belongs to, from a predefined set of facets.
* Task 2 (optional bonus task): Finally, generate a structured summary of the RP from the cited text spans of the RP. The length of the summary should not exceed 250 words.

Evaluation: Task 1 will be scored by overlap of text spans measured by number of sentences in the system output vs gold standard. Task 2 will be scored using the ROUGE family of metrics between i) the system output and the gold standard summary fromt the reference spans ii) the system output and the asbtract of the reference paper. Again, Task 2 is optional.

## Contents

This is the open repository for the Scientific Document Summarization Corpus and Annotations contributed to the public by the Web IR / NLP Group at @ the National University of Singapore (WING-NUS) 
with generous support from Microsoft Research Asia.

    ./README.md
 
This file.

    ./FAQ2018
	
Frequently asked questions on the 2018 shared task including updates to the corpus, 
annotation format from the previous edition.

    ./README2014.md
    ./README2016.md
    ./README2017.md
    ./README2018.md
    ./README2019.md
 
README files for the previous editionS of the shared task hosted at 
BIRNDL@SIGIR 2018, BIRNDL@SIGIR 2017, BIRNDL@JCDL 2016 and TAC2014.

    ./docs/corpusconstruction.txt
 
A readme detailing the rules and steps followed to create the document
corpus by randomly sampling documents from the ACL Anthology corpus
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

    ./data/Training-Set-2019/Task?/From-Training-Set-2018/???-????
    ./data/Training-Set-2019/Task?/From-ScisummNet-2019/???-????
  
Directories containing the Documents, Summaries, and Annotations for
each topic, one directory per Topic ID.

    ./data/Training-Set-2019/Task1/From-Training-Set-2018/???-????/Documents_PDF/

This directory contains the 10 source documents for the topic (1 RP
and upto 10 CPs), one file per paper, in the original pdf format.

    ./data/Training-Set-2019/Task1/From-Training-Set-2018/???-????/Reference_XML/
    ./data/Training-Set-2019/Task1/From-ScisummNet-2019/???-????/Reference_XML/

This directory contains the source document for the RP of the topic in XML format in 
UTF-8 character encoding. The file corresponds to the similarly named pdf file in 
Documents_PDF/. All annotations and offsets for the topic are with respect to the xml 
files in this directory. All the files were created from the pdf file using Adobe Acrobat.  
Note that there were OCR errors in reading several of the files, and the annotators often 
had to manually edit the converted txt files. Research groups using are free to use alternative 
parsing tools on the pdfs provided, if they are found to perform better.

    ./data/Training-Set-2019/Task1/From-Training-Set-2018/???-????/CITANCE_XML/
	
This directory contains the source document for the CPs of the topic in xml format in 
UTF-8 character encoding. Each file corresponds to the similarly named pdf file above.  

    ./data/Training-Set-2019/Task1/From-Training-Set-2018/???-????/Annotation/
    ./data/Training-Set-2019/Task1/From-ScisummNet-2019/???-????/Annotation/
    
This directory contains the annotation files for the topic, from 3 different annotators.  
Please DO NOT use older annotations; only use <TopicID>.annv3.txt for the 2016 Shared Task.

    ./data/Training-Set-2019/Task2/From-Training-Set-2018/???-????/summary/
    ./data/Training-Set-2019/Task2/From-ScisummNet-2019/???-????/summary/
    
The summary task (Task 2) is an optional, "bonus" task which participants may want to attempt.
This directory contains the two kinds of summaries - i. the abstract, and ii.human written summaries
of the reference paper.

## Annotation

Given a reference paper (RP) and 10 or  more citing papers (CPs), annotators from the University of 
Hyderbad were instructed to find citations to the RP in the CPs. Annotators followed instructions in 
SciSumm-annotation-guidelines.pdf to mark the Citation Text,
Citation Marker, Reference Text, and Discourse Facet for each citation of the RP found in the CP.  

## Organisers' Contacts

For further information about this data release, contact the following members of the BRNDL 2017 workshop organising committee:

* <a href="https://www.linkedin.com/in/muthukumarc">Muthu Kumar Chandrasekaran</a> (Advanced Computer Scientist, Artificial Intelligence Center, SRI International) cmkumar087@gmail.com
* <a href="https://www.sri.com/about/people/dayne-freitag">Dayne Freitag</a> (Technical Director, Artificial Intelligence Center, SRI International)

LongSumm
*
*
*

LaySumm
*
* 

--------------------------------------------------------------------------

This README was updated from README2018 by Muthu Kumar Chandrasekaran in Feb, 2020. For revision information, check source code control logs.
