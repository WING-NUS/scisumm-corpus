# README for the 1st Computational Linguistics Lay Summary Challenge Shared Task Corpus (CL-LaySumm 2020)

This package contains a release of training and test topics to aid in 
the development of computational linguistics summarization systems.

# CL-LaySumm @ EMNLP 2020

February 21, 2020

CL-LaySumm Shared Task is part of Scholarly Document Processing 2020 workshop collocated with EMNLP 2020 @ Punta Cana, Dominican Republic, Nov 11/12 - official website hosted at: https://ornlcda.github.io/SDProc/


### Introduction

The CL-LaySumm Shared Task is to automatically produce Lay Summaries of technical (scientific research article) texts.  A Lay Summary is defined as a textual summary intended for a non-technical audience.  It is typically produced either by the authors or by a journalist or commentator.  Examples are provided in the training data.  The corpus will cover three distinct domains: epilepsy, archeology, and materials engineering. 

In more detail, a lay summary explains, succinctly and without using technical jargon, what the overall scope, goal and potential impact of a scientific paper is.  It is typically about 70 - 100 words in length.  The task is to generate summaries that are representative of the content, comprehensible, and interesting to a lay audience. 

The intrinsic evaluation will be done by ROUGE, using ROUGE-1, -2, and Skipgram metrics. In addition, a randomly selected subset of the summaries will undergo human evaluation by science journalists and communicators for comprehensiveness, legibility, and interest.

All nominated entries will be invited to publish a paper in Open Access (Author-Payment Charges will be waived) in a selected Elsevier publication. Authors will be asked to provide an automatically generated lay summary of their paper, together with their contribution.

## Lay Summary Task

The task is defined as follows:
- Given: A full-text paper, its Abstract, and a Lay Summary of a given paper
- Task: For each paper, generate a Lay Summary of the specified length
- Evaluation: The Lay Summary Task will be scored by using several ROUGE metrics to compare the system output and the gold standard Lay Summary.

As a follow-up to the intrinsic evaluation, we will crowdsource a number of automatically generated lay summaries to a panel of judges and a lay audience. Details of the crowdsourcing evaluation will be announced with the sharing of the final test corpus on July 1st.

## Corpus Access

To obtain access to full the LaySumm (training and test) corpus, please send an email to a.dewaard@elsevier.com. You will be emailed and asked to sign acontract that grants you research access to the full corpus of approximately 600 full-text articles, abstracts and lay summaries. A training corpus consisting of approximately 2/3 of the corpus will be made available directly; the full corpus will be available on the Test Set Release date, July 1, 2020.

A sample file of 2 records consisting of full-text, abstract, and lay summary records can be downloaded here. Each folder consists of 1 file containing the full text, abstract and lay summary.

For any questions on the contracts or the corpus, please contact a.dewaard@elsevier.com.

## Organisers' Contacts

For further information about this data release, contact the following members of the SDP 2020 workshop organising committee:

LaySumm
* Anita de Waard (Elsevier, VT), a.dewaard@elsevier.com
* Eduard Hovy (LTI, CMU), hovy@cmu.edu

--------------------------------------------------------------------------

This README was created by LaySumm Organier, Anita De Waard in February, 2020 
