import spacy
import fr_core_news_md
nlp = fr_core_news_md.load()

def get_pos(fichier):

    file=open(fichier, "r", encoding="utf-8")
    document=nlp(file.read())
    for tok in document:
        print(tok.text, tok.pos_)

fichier = "sequoia.txt"
get_pos(fichier)

def get_pos_tagged(fichier):
    with open(fichier,"r",encoding='utf-8')as fic:
         texte=fic.read()
    liste = texte.split('\n')
    return(liste)

fichier2 = "sequoia_pos.txt"
manuel = "sequoia_pos_manuel.txt"
nom_fic = "sequoia_eval.txt"
elem_pos=get_pos_tagged(fichier2)
elem_manuel=get_pos_tagged(manuel)


f_positifs=[]
v_positifs=[]
f_negatifs=[]
a_trouver=len(elem_manuel)


for element in elem_pos:
    if element in elem_manuel:
        v_positifs.append(element)
        elem_manuel.remove(element)
    else:
        f_positifs.append(element)
    
rappel=len(v_positifs)/a_trouver
precision=len(v_positifs)/len(elem_pos)
f_mesure=2*(precision*rappel)/(precision+rappel)



with open(nom_fic,"x",encoding='utf-8')as file:
    file.write("resultats: " + nom_fic + '\n\n')
    file.write("nombre d'éléments totale: " + str(a_trouver) + '\n')
    file.write("nombre de vrais positifs: " + str(len(v_positifs))+'\n')
    file.write("nombre de faux positifs: " + str(len(f_positifs))+'\n\n')
    file.write("rappel: " + str(rappel)+'\n')
    file.write("precision: " + str(precision)+'\n')
    file.write("f_mesure: " + str(f_mesure)+ '\n')
    file.write("----------------------------------------------------------------------------------------\n")
    file.write("liste des vrais positifs: \n")
    v_positifs.sort()
    for element in v_positifs:
        file.write(element + '\n')
    file.write("----------------------------------------------------------------------------------------\n")
    file.write("liste des faux positifs: \n")
    f_positifs.sort()
    for element in f_positifs:
        file.write(element + '\n')
    file.write("----------------------------------------------------------------------------------------\n")
    file.write("liste des pos non retrouvées:" + str(len(elem_manuel))+ " \n")
    elem_manuel.sort()
    for element in elem_manuel:
        file.write(element + '\n')
              




