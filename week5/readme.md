Objectives
---
Using the Spacy library, you will identify the characters mentioned in Le ventre de Paris.
For each character who appears at least three times, you will indicate the verbs of which they are the subject.

Results Sequoia
---
total number of items: 90
number of true positives: 87
number of false positives: 4
recall: 0.9666666666666667
precision: 0.9560439560439561
f_measure: 0.9613259668508287

Results Bashung
---
number of total elements: 59
number of true positives: 55
number of false positives: 5
recall: 0.9322033898305084
precision: 0.9166666666666666
f_measure: 0.9243697478991596

Results Orfeo
---
total number of elements: 149
number of true positives: 137
number of false positives: 13
recall: 0.9194630872483222
precision: 0.913333333333333333
f_measure: 0.9163879598662208

false positives in orfeo
---
ah CCONJ
ben ADV
is VERB
uh ADV
uh X
eh VERB
j~ PROPN
j~ PROPN
yeah ADJ
yeah NOUN

After labelling the texts with
Spacy, I corrected them. There were some
problems that are very visible. 

1) First of all, Spacy does not label
correctly, but instead marks them as adverbs
rather as adverbs, cconj or can't mark them, which is
cannot mark them, which is represented by X.

2)In the text Orfeo, tilde was
used to show that the speech was
intermittent. The tagger recognized "j~"
as a proper noun while in the presence of
"je~", it was correctly recognized.

3)The auxiliary verbs were
recognized but not as AUX but
VERBS.

In general, the accuracy is good, but the
French poses some problems when labelling.
labelling.

Comment on my script
---
It is necessary to remove the evaluation text
to restart the script.
To do the manual tagging, I first launched the script on the texts and put them in
the script on the texts and put them in separate
separate files. If it is necessary to run
the script to tag them again, the easiest way is to
simplest way is to redirect them to the command line first
command line first, then run the script
to get the evaluation file.
