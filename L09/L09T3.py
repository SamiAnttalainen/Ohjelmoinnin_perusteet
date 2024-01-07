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
# Tehtävä L09T3.py
import sys

def lueTiedosto(Nimi, Lista):
    try:
        Tiedosto = open(Nimi, "r", encoding="UTF-8")
        Rivi = Tiedosto.readline()[:-1]
        Edellinen = None
        while len(Rivi) > 0:        
            if Rivi != Edellinen:
                Lista.append(Rivi)
                Edellinen = Rivi
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
    Autolista = []
    for Alkio in Lista:
        Autolista.append(Alkio)
    print("Tiedostossa oli " + str(len(Autolista)) + " eri automerkkiä.")
    return Autolista

def kirjoitaTiedosto(Nimi, Lista):
    for Alkio in Lista:
        print(Alkio)
    try:
        Tiedosto = open(Nimi, "w", encoding="UTF-8")
        for Merkki in Lista:
            Tiedosto.write(Merkki + "\n")
        Tiedosto.close()
    except Exception:
        print("Tiedoston '" + Nimi + "' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    return None

def paaohjelma():
    Lista = []
    Automerkit = []
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
