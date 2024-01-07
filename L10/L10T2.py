######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Sami Anttalainen
# Päivämäärä: 14.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L10T2.py
import sys

def lueTiedosto(Nimi, Autot):
    Lista = []
    try:
        Tiedosto = open(Nimi, "r", encoding="UTF-8")
        Tiedosto.readline()
        Rivi = Tiedosto.readline()
        while len(Rivi) > 0:
            Lista.append(Rivi)
            Rivi = Tiedosto.readline()
        Tiedosto.close()

    except Exception:
        print("Tiedoston '" + Nimi + "' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    Autolista = [0, 0, 0, 0, 0, 0, 0]
    for Rivi in Lista:
        Sarakkeet = Rivi.split(";")
        Vuosi = Sarakkeet[1][0:4]
        Index = int(Sarakkeet[1][3:4])
        Autolista[Index] += 1
        Autot[Vuosi] = 0
    
    for i in range(7):
        Autot["201" + str(i)] = Autolista[i]
    Autolista.clear()
    Lista.clear()
    return Autot

def tulostaTiedosto(Sanakirja):
    Summa = 0
    Lajiteltu = sorted(Sanakirja, reverse=True)
    print("Autot lajiteltuna vuosiluvun mukaan laskevaan järjestykseen.")
    print("Vuosi: Autoja")
    for Vuosi in Lajiteltu:
        print("{0}: {1:d}".format(Vuosi, Sanakirja[Vuosi]))
    for Vuosi in Lajiteltu:
        Summa += Sanakirja[Vuosi]
    print("Yhteensä {0} autoa.".format(Summa))
    return None

def paaohjelma():
    Luettava = input("Anna luettavan tiedoston nimi: ")
    Autokirja = {}
    Autokirja = lueTiedosto(Luettava, Autokirja)
    tulostaTiedosto(Autokirja)
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
######################################################################
# eof
