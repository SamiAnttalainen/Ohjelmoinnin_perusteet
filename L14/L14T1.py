######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Sami Anttalainen
# Päivämäärä: 14.12.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L14T1.py

import math

def laskeKustannukset(Kilometrit, Kulutus, Hinta, Ika, Vakuutus, Bonus, Vero):
    Ajettu = 200000
    Kesto = 6
    Vuosi = 1
    Alennus = (100 - Bonus) / 100
    KokoSumma = 0

    while Vuosi < Kesto:
        Ajettu = Ajettu + Kilometrit
        Summa = Kilometrit / 100 * Kulutus * Hinta + Vakuutus * Alennus + Vero + 200 * math.sqrt(Ika)
        print("{0:d}. vuosi: {1:.0f}".format(Vuosi, Summa))
        KokoSumma = KokoSumma + Summa
        #Bonus = Bonus + 10
        #Alennus = (100 - Bonus) / 100
        Ika = Ika + 1
        Vuosi = Vuosi + 1
    print("Viiden vuoden aikana autoon käytettiin rahaa {0:.0f} euroa.".format(KokoSumma))
    return None



def paaohjelma():
    Kilometrit = int(input("Anna vuotuiset kilometrit: "))
    Kulutus = float(input("Anna moottorin polttoaineen kulutus (l/100km): "))
    Hinta = float(input("Anna polttoaineen hinta (€/l): "))
    Ika = int(input("Anna auton ikä vuosissa: "))
    Vakuutus = int(input("Anna vakuutusten määrä (euroissa): "))
    Bonus = int(input("Anna bonusprosentti kokonaislukuna: "))
    Vero = float(input("Anna verojen määrä: "))
    laskeKustannukset(Kilometrit, Kulutus, Hinta, Ika, Vakuutus, Bonus, Vero)
    print("Kiitos ohjelman käytöstä.")
    return None
paaohjelma()
######################################################################
# eof
