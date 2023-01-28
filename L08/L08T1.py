######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Sami Anttalainen
# Opiskelijanumero: 001067291
# Päivämäärä: 31.10.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L08T1.py

import math
import random

def valikko():
    print("Mitä haluat tehdä?")
    print("1) Laske absoluuttinen arvo")
    print("2) Laske kertoma")
    print("3) Laske potenssi")
    print("4) Laske neliöjuuri")
    print("5) Arvo satunnaisluku")
    print("0) Lopeta")
    Valinta = int(input("Anna valintasi: "))
    return Valinta

def paaohjelma():
    random.seed(1)

    Valinta = valikko()

    while Valinta != 0:

        if Valinta == 1:
            Luku1 = float(input("Minkä luvun absoluuttinen arvo selvitetään: "))
            Aluku = round(math.fabs(Luku1), 1)
            print("Luvun absoluuttinen arvo on " + str(Aluku))

        elif Valinta == 2:
            Luku2 = int(input("Minkä luvun kertoma lasketaan: "))
            Kluku = math.factorial(Luku2)
            print("Luvun kertoma on " + str(Kluku))

        elif Valinta == 3:
            Luku3 = int(input("Mikä luku korotetaan potenssiin: "))
            Luku4 = int(input("Mitä eksponenttia käytetään: "))
            Pluku = round(math.pow(Luku3, Luku4), 0)
            print("Luku korotettuna eksponenttiin on " + str(Pluku))

        elif Valinta == 4:
            Luku5 = int(input("Mikä luvun neliöjuuri lasketaan: "))
            Nluku = round(math.sqrt(Luku5), 0)
            print("Luvun neliöjuuri on " + str(Nluku))

        elif Valinta == 5:
            print("Arvotaan satunnaisluku, anna rajat kokonaislukuina.")
            Alaraja = int(input("Anna minimi (otetaan mukaan): "))
            Ylaraja = int(input("Anna maksimi (otetaan mukaan): ")) + 1
            Sluku = random.randint(Alaraja, Ylaraja)
            print("Arvottiin satunnaisluku " + str(Sluku))
        
        else:
            print("Tuntematon valinta, yritä uudestaan.")
        print()
        Valinta = valikko()
    print("Lopetetaan")
    print()
    print("Kiitos ohjelman käytöstä.")
    return None
        
paaohjelma()
# eof