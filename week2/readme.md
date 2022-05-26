Objective
---
Calculate the type/token ratio for the 2016 and 2017 state of the union speeches.
For tokenization, use Stanford's tokenizer, NLTK, or Spacy You must send the result along with a description of your processing (scripts, tools, ...)

Pour ce devoir, nous utilisons l'un des tokenizers pour calculer le ratio type/token pour les deux
discours prononcés par Obama et Trump dans les années 2016 et 2017. Le type est un forme unique
d’un mot et token il s’agit des mots graphiques. J'ai utilisé le tokenizer spacy et écrit une fonction
Python pour saisir les tokens et les types afin de calculer le ratio TTR. Grâce à ces résultats, nous
pouvons dire quel discours présente la plus grande variété de vocabulaire, ce qui est indiqué par un
nombre élevé de TTR.

Les résultats donnés:
----
TTR results for State of Union 2016 are: 7866 1808 22.984998728705822
TTR results for State of Union 2017 are: 6560 1656 25.24390243902439

Analyse des résultats
---
Les résultats montrent que le discours de 2017 fait par Trump présente une plus grande variété
d'utilisation du vocabulaire par rapport à celui d'Obama. Apparemment, les deux textes diffèrent
l'un de l'autre en termes de type de discours si l'on regarde de plus près la politique américaine.
Dans un discours sur l'état de l'Union, le président revient généralement sur l'année écoulée et sur
l'état de la nation, et profite également de l'occasion pour mettre en avant le programme législatif
de son administration. Comme il s'agissait du premier discours de Trump, on dit qu'il s'agit d'un
discours plutôt que d'un SOTU. Comme leurs réflexions sont différentes, il est possible de voir la
petite différence dans le ratio.
