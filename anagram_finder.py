mon_dict = input("entrer l'emplacement du fichier : ")
if len(mon_dict) == 0:
    mon_dict = './dico-fr.txt' # Juste pour cet exercice
else:
    pass
mot_pour_chercher_anagramme = input("entrer le mot pour chercher l'anagramme : ")
__mot_pour_chercher_anagramme__ = list(mot_pour_chercher_anagramme.lower())
__mot_pour_chercher_anagramme__.sort()

def chercheur_anagramme():
    with open(mon_dict,'r') as dictionnaire:
        mots = dictionnaire.readlines()
    print("Tout les anagrammes du mot",mot_pour_chercher_anagramme,"sont :")
    for mot in mots:
        mot = mot.strip("\n")
        __mot__ = list(mot.lower())
        __mot__.sort()
        if __mot_pour_chercher_anagramme__ == __mot__ :
            if mot == mot_pour_chercher_anagramme.lower():
                pass
            else:
                print(mot)
        else:
            pass
chercheur_anagramme()
