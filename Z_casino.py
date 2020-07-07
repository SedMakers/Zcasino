from random import randrange # import la fonction randrange qui est dans le module random
from math import ceil # import la fonction ceil qui est dans le module math
import os
print("Bonjour et Bienvenue a la roulette du Zcasino !")
argent = input("Avec combien d'argent souhaitais vous jouer ?")
argent = int(argent)
while argent > 0:
    rand = -1
    while rand < 0 or rand > 49:
        rand = input("Sur quel numero souhaitez vous miser ? (entre 0 et 49)")
        try:
            rand = int(rand)
        except ValueError:
            print("Vous n'avez pas saisi de nombre")
            rand = -1
            continue
        if rand < 0:
            print("Ce nombre est négatif")
        if rand > 49:
            print("Ce nombre est superieur a 49")
    mise = 0
    while mise <= 0 or mise > argent:
        mise = input("Combien souhaitez vous miser ?")
        try:
            mise = int(mise)
        except ValueError:
            print("Vous n'avez pas saisi de mise")
            mise =- 1
            continue
        if mise <= 0:
            print("La mise saisie est négatif ou nulle")
        if mise > argent:
            print("Vous ne pouvez pas miser autant, vous n'avez que", argent)

    numero_gagnant = randrange(50)
    print("La boule est tombé sur le numero :", numero_gagnant)

    if numero_gagnant == rand:
        print("Vous etes tombé sur le bon numero")
        print("Vous avez gagné ", mise * 3)
        argent += mise * 3
    else:
        print("Vous etes tombé sur le mauvais numero...")
        print("Vous avez perdu", mise)
        argent -= mise

    print("Il vous reste", argent)


os.system("pause")