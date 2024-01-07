######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Sami Anttalainen
# Päivämäärä: 7.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L09T1.py

import sys

def lueTiedosto(Nimi, Lista):
    try:
        Tiedosto = open(Nimi, "r", encoding="UTF-8")
        Rivi = Tiedosto.readline()
        Lkm = 0
        while len(Rivi) > 0:
            Lista.append(Rivi)
            Lkm = Lkm + 1
            Rivi = Tiedosto.readline()
        Tiedosto.close()
    except Exception:
        print("Tiedoston '" + Nimi + "' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    print("Tiedoston '" + Nimi + "' lukeminen onnistui, " + str(Lkm) + " riviä.")
    return Lista

def kirjoitaTiedosto(Nimi, Lista):
    try:
        Tiedosto = open(Nimi, "w", encoding="UTF-8")
        for Alkio in Lista:
            Tiedosto.write(Alkio)
        Tiedosto.close()
    except Exception:
        print("Tiedoston '" + Nimi + "' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    print("Tiedoston '" + Nimi + "' kirjoittaminen onnistui.")
    return None

def paaohjelma():
    Rivilista = []
    Luettava = input("Anna luettavan tiedoston nimi: ")
    Rivilista = lueTiedosto(Luettava, Rivilista)
    Kirjoitettava = input("Anna kirjoitettavan tiedoston nimi: ")
    kirjoitaTiedosto(Kirjoitettava, Rivilista)
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()

######################################################################
# eof
