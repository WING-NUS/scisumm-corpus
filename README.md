# README 

Shield: [![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by] except for the following files which are closed source under strict copyright laws enforced by Elsevier labs. We hold no accountability for these:
* https://github.com/WING-NUS/scisumm-corpus/blob/master/README_Laysumm.md
* and files under the directory: https://github.com/WING-NUS/scisumm-corpus/tree/master/data/LAYSUMM_SAMPLE

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
# (scisumm-corpus @ https://github.com/WING-NUS/scisumm-corpus)

This package contains a release of training and test topics to aid in 
the development of computational linguistics summarization systems.

# CL-SciSumm

The CL-SciSumm Shared Task is run off the CL-SciSumm corpus and is composed of  
three sub-tasks in automatic research paper summarization on a new corpus 
of research papers. A training corpus with summaries for one thousand forty topics 
and forty topics for citance to reference span id (or provenance identification) tasks 
has been released. A test corpus of twenty topics is held-out as a blind test-set. 
The topics comprise of ACL Computational Linguistics and Natural Language Processing 
research papers, and their citing papers and three output summaries each. The three 
output summaries comprise: 
the traditional authors' summary of the paper (the abstract), the community summary 
(the collection of citation sentences ‘citances’) and a human summary written 
by a trained annotator. Within the corpus, each citance is also mapped to its 
referenced text in the reference paper and tagged with the information facet 
it represents.

The manually annotated training set of 40 articles (Tasks 1a and b) and citing papers, 
human written summaries (1040 documents) for them and a further 1000 document corpus (ScisummNet), 
an auto-annotated noisy dataset with several thousands of article-citing paper papers (to aid in '
training deep learning models) are readily available for download and can be used by participants.
This data can be found in /data/Training-Set-2019/Task1/From-Training-Set-2018
and /data/Training-Set-2019/Task2/From-Training-Set-2018

The last edition of CL-SciSumm was CL-SciSumm 2020. The gold test data used for 2020, 2019, 2018 
are now available in public in this repo. You are welcome to use it for your evaluations and 
paper submissions to any conference / journal or your theses.

In 2020, we did not add any new training data.

In 2019 we had introduced 1000 document 
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


Last editions proceedings: 
- CL-SciSumm '20 @ EMNLP '20 can be found in EMNLP 2020 Proceedings on ACL Anthology. System papers are indexed in the overview paper: https://www.aclweb.org/anthology/2020.sdp-1.1/
- CL-SciSumm '19 @ SIGIR '19 can be found in BIRNDL 
Proceedings: http://ceur-ws.org/Vol-2414/ under the header 'System Papers'

If you use the data and publish please let us know and cite our CL-SciSumm 2019 task overview paper:<br>
```
@inproceedings{,<br>
title={Overview and Results: CL-SciSumm Shared Task 2019},<br>
author={Chandrasekaran, Muthu Kumar and Yasunaga, Michihiro and Radev, Dragomir and Freitag, Dayne and Kan, Min-Yen},<br>
booktitle={In Proceedings of Joint Workshop on Bibliometric-enhanced Information Retrieval and NLP for Digital Libraries (BIRNDL 2019)},<br>
year={2019}<br>
}<br>
```


### Overview

CL-SciSumm ran as a shared task at EMNLP 2020, SIGIR 2019, 2018, 2017, JCDL 2016 and the Pilot Task conducted as 
a part of the BiomedSumm Track at the Text Analysis Conference 2014 (TAC 2014).

The task is on automatic paper summarization in the Computational Linguistics (CL) domain. The output summaries are of 
two types: faceted summaries of the traditional self-summary (the abstract) and the community summary (the collection of 
citation sentences ‘citances’). We also group the citances by the facets of the text that they refer to.

The task is defined as follows:

Given: A topic consisting of a Reference Paper (RP) and <del>upto 10</del> Citing Papers (CPs) that all contain citations to the RP. In each CP, the text spans (i.e., citances) have been identified that pertain to a particular citation to the RP.

* Task 1a: For each citance, identify the spans of text (cited text spans) in the RP that most accurately reflect the citance. These are of the granularity  of a sentence fragment, a full sentence, or several consecutive sentences (no more than 5).
* Task 1b: For each cited text span, identify what facet of the paper it belongs to, from a predefined set of facets.
* Task 2 (optional bonus task): Finally, generate a structured summary of the RP from the cited text spans of the RP. The length of the summary should not exceed 250 words.

Evaluation: Task 1 is scored by overlap of text spans measured by number of sentences in the system output vs gold standard. Task 2 is scored using the ROUGE family of metrics between i) the system output and the gold standard summary fromt the reference spans ii) the system output and the asbtract of the reference paper.

## Contents

This is the open repository for the Scientific Document Summarization Corpus and Annotations contributed to the public
by the Web IR / NLP Group at @ the National University of Singapore (WING-NUS) with generous support from Microsoft Research Asia.

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
    ./README2020.md
 
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

Please open github issues for further information or to report a bug or a fix for the corpus.

Contacts for maintainers of the corpus:

* <a href="https://www.linkedin.com/in/muthukumarc">Muthu Kumar Chandrasekaran</a> (Amazon, Seattle) cmkumar087@gmail.com
* <a href="https://www.comp.nus.edu.sg/~kanmy/">Min-Yen Kan</a> National University of Singapore, kanmy@comp.nus.edu.sg


We provide links for Laysumm here and are not associated with it:

**README for Lay Summarization Task (LaySumm 2020)**

Task Description and a *sample* dataset can be found at: <a href="https://github.com/WING-NUS/scisumm-corpus/blob/master/README_Laysumm.md">here</a> in this Github repo.

LaySumm
* <a href="https://libraryconnect.elsevier.com/contributors/anita-de-waard">Anita de Waard</a>(Elsevier, VT), a.dewaard@elsevier.com
* <a href="https://www.cs.cmu.edu/~hovy/">Eduard Hovy</a>, (LTI, CMU), hovy@cmu.edu

--------------------------------------------------------------------------

This README was updated from README2020 by Muthu Kumar Chandrasekaran in 2021. For revision information, check source code control logs.
