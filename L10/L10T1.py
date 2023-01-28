######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Sami Anttalainen
# Opiskelijanumero: 001067291
# Päivämäärä: 14.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L10T1.py

import sys

def lueTiedosto(Nimi, Lista):
    try:
        Tiedosto = open(Nimi, "r", encoding="UTF-8")
        Rivi = Tiedosto.readline()[:-1]
        while len(Rivi) > 0:        
            Lista.append(Rivi)
            Rivi = Tiedosto.readline()[:-1]
        Tiedosto.close()
    except Exception:
        print("Tiedoston '" + Nimi + "' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    if len(Lista) == 0:
            print("Tiedosto oli tyhjä, yhtään automerkkiä ei tunnistettu.")
            print("Kiitos ohjelman käytöstä.")
            sys.exit(0)
    return Lista
    
def analysoiTiedosto(Lista):
    Lkm = 0
    Autolista = {}
    Edellinen = Lista[0]
    for Alkio in Lista:
        Seuraava = Alkio
        if Seuraava == Edellinen:
            Lkm += 1
        else:
            Autolista[Edellinen] = Lkm
            Lkm = 1
            Edellinen = Seuraava
    Autolista[Seuraava] = Lkm
    Pituus = len(Autolista)
    print("Tunnistettiin " + str(Pituus) + " automerkkiä ja " + str(len(Lista)) + " autoa:")
    return Autolista

def kirjoitaTiedosto(Nimi, Autolista):
    Lajiteltu = sorted(Autolista)
    Pituus = len(Lajiteltu)
    Summa = 0
    for Merkki in Lajiteltu:
        if Autolista[Merkki] == 1:
            print("{0}: {1:d} auto".format(Merkki, Autolista[Merkki]))
            Summa += Autolista[Merkki]
        else:
            print("{0}: {1:d} autoa".format(Merkki, Autolista[Merkki]))
            Summa += Autolista[Merkki]
    try:
        Tiedosto = open(Nimi, "w", encoding="UTF-8")
        Tiedosto.write("Tunnistettiin " + str(Pituus) + " automerkkiä ja " + str(Summa) + " autoa:\n")
        for Merkki in Lajiteltu:
            if Autolista[Merkki] == 1:
                Tiedosto.write("{0}: {1:d} auto\n".format(Merkki, Autolista[Merkki]))
            else:
                Tiedosto.write("{0}: {1:d} autoa\n".format(Merkki, Autolista[Merkki]))
        Tiedosto.close()
    except Exception:
        print("Tiedoston '" + Nimi + "' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    return None

def paaohjelma():
    Lista = []
    Automerkit = {}
    Luettava = input("Anna luettavan tiedoston nimi: ")
    Kirjoitettava = input("Anna kirjoitettavan tiedoston nimi: ")
    Lista = lueTiedosto(Luettava, Lista)
    Automerkit = analysoiTiedosto(Lista)
    kirjoitaTiedosto(Kirjoitettava, Automerkit)
    Lista.clear()
    Automerkit.clear()
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()

######################################################################
# eof