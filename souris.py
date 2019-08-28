# Le but de ce code est de calculer l'evolution d'une population souris
# en se basant sur les elements suivant:
# - Population 0: Un couple de souris adulte
# - temps de gestation de 3 semaines
# - rapport M/F = 50%
# - les souris ne meurent pas
# - un souriceau met 6 semaine à devenir adulte, 
#   un couple de souriceau de même génération aura donc besoin de 9 semaines
#   au total avant de donner naissance à une nouvelle portée
# - chaque portée contient 8 souriceaux

import sys
import math

Adultes = [] 
Bebes = []

# semaine 0 - index 0
Adultes.append(2)
Bebes.append(0)

# Adultes = [2] & Bebes = [2]

# semaine 3 - index 1
Adultes.append(2)
Bebes.append(8)

# Adultes = [2, 2] & Bebes = [0, 8]

# semaine 6 - index 2 
Adultes.append(2)
Bebes.append(Bebes[1] + 8)

# Adultes = [2, 2, 2] & Bebes = [0, 8, 16]

SourisTotal = 0
i = 0

# a partir de semaine 9: 
# les enfants nes a la semaine 3 deviennent adultes mais ont encore besoin 
# de 3 semaines supplémentaires avant de pouvoir se reproduire
while(SourisTotal < 550):
    Anm1 = Adultes[-1]
    Bnm2 = Bebes[-2]
    Bnm1 = Bebes[-1]
    Adultes.append(Anm1 + Bnm2)
    Bebes.append(Bnm1 - Bnm2 + Anm1 * 0.5 * 8)
    SourisTotal = Adultes[-1] + Bebes[-1]
    print("semaine : ", i*3 + 9, ", Adultes: ", Adultes[-1], ", Bebes: ", Bebes[-1],  "-> nb souris : ", SourisTotal)
    i+=1

# output:
# semaine :  9    -> nb souris :  26.0
# semaine :  12   -> nb souris :  66.0
# semaine :  15   -> nb souris :  170.0  <===
# semaine :  18   -> nb souris :  338.0  <===
# semaine :  21   -> nb souris :  666.0
