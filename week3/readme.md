Objectives
---

1) With Grew-match, find in the corpus UD_French-Sequoia@2.5 :
        all subject, verb, object triplets
        sentences with inverted subjects


- tous les triplets sujet, verbe, objet

pattern { GOV-[nsubj|csubj]-> DEP; GOV[upos="VERB"]; GOV-[iobj|obj|obl:arg|obl:mod]->DEP1}


- les phrases avec sujets inversés 

pattern { GOV [upos="VERB"]; GOV-[nsubj]-> DEP; GOV <<  DEP

2) With the help of the Spacy module, extract the triplets (subject, verb, object) of the following sentences and comment on any errors or missing elements. (in the script)

    "Children don't like asparagus very much."
    "The French are asking for less taxes."
    "Acacia trees make a clear, flowing, amber honey."
    "The team is blaming the refereeing."
    "Swarms of billions of insects, from the Arabian Peninsula, are descending on the Horn of Africa and devouring crops, jeopardizing the region's food security.

