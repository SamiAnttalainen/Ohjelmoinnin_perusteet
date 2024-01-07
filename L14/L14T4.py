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
# Tehtävä L14T4.py

import random
import sys

def arvoLuvut(Maara, Alaraja, Ylaraja, Lista):
    Lkm = 0
    while Lkm < Maara:
        Luku = random.randint(Alaraja, Ylaraja)
        if Luku not in Lista:
            Lista.append(Luku)
            Lkm = Lkm + 1
    return Lista

def kirjoitaTiedosto(Nimi, Lista, Maara, Alaraja, Ylaraja):
    try:
        Tiedosto = open(Nimi, "w", encoding="UTF-8")
        Tiedosto.write("Arvottu {0:d} lukua väliltä {1:d}-{2:d}:\n".format(Maara, Alaraja, Ylaraja))
        for Luku in Lista:
            Tiedosto.write("{0:d}\n".format(Luku))
        Tiedosto.close()
    except Exception:
        print("Tiedoston'" + Nimi + "' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    return None

def paaohjelma():
    random.seed(1)
    Lista = []
    print("Tämä ohjelma arpoo haluamasi määrän kokonaislukuja halutulta väliltä")
    print("ja kirjoittaa ne tekstitiedostoon.")
    Kirjoitettava = input("Anna tehtävän tiedoston nimi: ")
    Asetukset = input("Anna lukujen määrä, alaraja ja yläraja, esim. 7 1 37: ")
    Tiedot = Asetukset.split(" ")
    Maara = int(Tiedot[0])
    Alaraja = int(Tiedot[1])
    Ylaraja = int(Tiedot[2])
    Lista = arvoLuvut(Maara, Alaraja, Ylaraja, Lista)
    kirjoitaTiedosto(Kirjoitettava, Lista, Maara, Alaraja, Ylaraja)
    print("Tiedosto '" + Kirjoitettava + "' luotu, kiitos ohjelman käytöstä.")
    Lista.clear()
    return None
paaohjelma()

######################################################################
# eof
