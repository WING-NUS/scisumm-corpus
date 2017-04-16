# README 

# (scisumm-corpus @ https://github.com/WING-NUS/scisumm-corpus)

This package contains a release of training and test topics to aid in the development of computational linguistics summarization systems.

The CL-SciSumm Shared Task is run off the CL-SciSumm corpus, and comprises three sub-tasks in automatic research paper summarization on a new corpus of research papers. A training corpus of twenty topics and a test corpus of ten topics were released. The topics comprised of ACL Computational Linguistics research papers, and their citing papers and three output summaries each. The three output summaries comprise: the traditional self-summary of the paper (the abstract), the community summary (the collection of citation sentences ‘citances’) and a human summary written by a trained annotator. Within the corpus, each citance is also mapped to its referenced text in the reference paper and tagged with the information facet it represents. We plan to further enrich this dataset with the AAN metafeatures and other meta-descriptors developed by researchers at DERI, National University of Ireland.

For more details, see the Contents Section at the bottom of this Readme. To know how this corpus was constructed, please see ./docs/corpusconstruction.txt

The CL-SciSumm 2017 task is open for registration! It will be collocated with <a href="http://sigir.org/sigir2017/">ACM SIGIR</a> 2017, Tokyo, Japan. 
<a href="http://wing.comp.nus.edu.sg/cl-scisumm2017">Go to task website</a>.<br> 
Register your team now via <a href ="https://easychair.org/conferences/?conf=birndl2017">easychair</a>

If you use the data and publish please let us know and cite our CL-SciSumm 2016 task overview paper:<br>
@inproceedings{jaidka2016overview,<br>
title={Overview of the CL-SciSumm 2016 Shared Task},<br>
author={Jaidka, Kokil and Chandrasekaran, Muthu Kumar and Rustagi, Sajal and Kan, Min-Yen},<br>
booktitle={In Proceedings of Joint Workshop on Bibliometric-enhanced Information Retrieval and NLP for Digital Libraries (BIRNDL 2016)},<br>
year={2016}<br>
}<br>


## README for The 3rd Computational Linguistics Scientific Document Summarization Shared Task Corpus (CL-SciSumm 2017)

April 16, 2017

Please read further for details on the Computational Linguistics Shared Task run as part of BIRNDL 2017 workshop collocated with SIGIR 2017 - official website hosted at: http://wing.comp.nus.edu.sg/cl-scisumm2017

To participate in the 2017 shared task, please register your team details at: https://easychair.org/conferences/?conf=birndl2017 ><br>

### Overview

You are invited to participate in the CL-SciSumm Shared Task at BIRNDL 2017. The shared task will be on automatic paper summarization in the Computational Linguistics (CL) domain. The output summaries will be of two types: faceted summaries of the traditional self-summary (the abstract) and the community summary (the collection of citation sentences ‘citances’). We also propose to group the citances by the facets of the text that they refer to.

This task follows up on the successful CL Pilot Task conducted as a part of the BiomedSumm Track at the Text Analysis Conference 2014 (TAC 2014).
It follows the basic  structure and guidelines of the Biomedical Summarization Track and adapts them for annotating and 
creating a corpus of training topics from computational linguistics research papers.  
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

    ./FAQ2016
	
Frequently asked questions on the 2016 shared task including updates to the corpus, 
annotation format from the previous edition.

    ./README2014.md
    ./README2016.md
 
README file for the previous editionS of the shared task hosted at TAC2014 and BIRNDL@JCDL 2016.

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
Please DO NOT use older annotations; only use <TopicID>.annv3.txt for the 2016 Shared Task.

    ./data/???-????_TRAIN/summary/
The summary task (Task 2) is an optional, "bonus" task which participants may want to attempt.
This directory contains the two kinds of summaries - i. the abstract, and ii.the reference spans 
(not citances but the information they referenced in the source paper). Both are extractive summaries. 
For the developemnt sets we will release in April, we will include a third type of summary - hand-written a
nnotator summaries. These would be abstractive.

## Annotation

Given a reference paper (RP) and 10 or  more citing papers (CPs), annotators from the University of Hyderbad were instructed to find citations to the RP in the CPs. Annotators followed instructions in SciSumm-annotation-guidelines.pdf to mark the Citation Text,
Citation Marker, Reference Text, and Discourse Facet for each citation of the RP found in the CP.  

## Contact Information

For further information about this data release, contact the following members of the BRNDL 2017 workshop organising committee:

* <a href="https://kokiljaidka.wordpress.com/">Kokil Jaidka</a> (University of Pennsylvania) kokil.j@gmail.com
* <a href="http://www.comp.nus.edu.sg/~kanmy/index.html">Min-Yen Kan</a> (Dept. of Computer Science, School of Computing, National University of Singapore) kanmy@comp.nus.edu.sg
* <a href="http://www.comp.nus.edu.sg/~a0092669/">Muthu Kumar Chandrasekaran</a> (Dept. of Computer Science, School of Computing, National University of Singapore) muthu.chandra@comp.nus.edu.sg

--------------------------------------------------------------------------

This README was updated from README2016 by Muthu Kumar Chandrasekaran in April, 2017. For revision information, check source code control logs.
