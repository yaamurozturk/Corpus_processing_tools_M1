import spacy #import spacy
nlp = spacy.load("en_core_web_sm") #downloading the english package
def file(name): #function that opens files in reading mode
with open(name, "r", encoding="UTF-8") as f:
return f.read()

def calculation(text): #function that calculates TTR
doc = nlp(text)
types = set()
#set() put each token in a set
for token in doc:
types.add(token.text.lower())

#turn the text to lowercase to eliminate repetitions, now we have a
vocabulary!
ratio = (len(types)/len(doc))*100 #calculation of TTR as V/N*100
return len(doc), len(types), ratio
#choosing the necessary texts and defining them
text2016 = file("2016L.txt")
text2017 = file("2017L.txt")
tokens_2016, types_2016, calculation_2016 = calculation(text2016)
tokens_2017, types_2017, calculation_2017 = calculation(text2017)
#printing out the results
print("TTR results for State of Union 2016 are: ", tokens_2016,
types_2016, calculation_2016)
print("TTR results for State of Union 2017 are: ", tokens_2017,
types_2017, calculation_2017)
