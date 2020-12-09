# FONCTIONS

#1
#Une fonction qui choisit au hasard un mot parmis 10 mots.
def motAuHasard (tableauMots):
    i = random.randint(0,9)
    motATrouver = tableauMots[i]
    return motATrouver

#2
# Une fonction qui cherche une lettre dans un mot et renvoie sa position.
def chercheDansMot(mot, lettreCherchee):
    for i in range(len(mot)):
        if lettreCherchee == mot[i]:
            position = i
    return position

#3
# Une fonction qui compte le nombre de fois qu'une lettre donnée apparaît dans un mot.
def nombreFoisDansMot(mot, lettreCherchee):
    apparition = 0
    for i in range(len(mot)):
        if lettreCherchee == mot[i]:
            apparition = apparition+1
    return apparition

#4
# Une fonction qui prend le mot deviné.
def devineMot():
    guess = "guess"
    while len(guess) != 6:
        guess = input("Proposez un mot de 6 lettres : ")
        if len(guess) > 6:
            print("Votre mot fait plus de 6 lettres.")
        if len(guess) < 6:
            print("Votre mot fait moins de 6 lettres.")
    return guess

#5
# Une fonction qui check si 2 lettres sont pareilles

def checkSiPareil(a, b):
    if a == b:
        return True
    return False


#6
# Une fonction qui affiche une ligne dde Motus

def affLigne(motATrouver, guess):
    for i in range(len(guess)):
        print (Back.BLACK + "|", end=" ")
        if checkSiPareil(motATrouver[i], guess[i]):
            print(Fore.WHITE + Back.RED + guess[i], end=" ")
        else:
            print(Back.BLACK + guess[i], end=" ")
    print (Back.BLACK + "|")
    return

#MAIN PROGRAMME
import random
from colorama import init 
init()
from colorama import Fore, Back, Style

tableauMots = ["puzzle", "action", "nymphe", "wapiti", "alcool", "aqueux", "bambou", "cactus", "chacal", "exquis"]
motATrouver = motAuHasard (tableauMots)
tour = 0
gagne = False

print("Bienvenue dans ce Motus! Un mot de 6 lettres à été choisit au hasard parmis une liste, à vous de le deviner !")
while tour <= 8 and gagne = False:
    print("il vous reste", 8 - tour," essaies")
    tour += 1
    guess = devineMot()
    affLigne(motATrouver, guess)