######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Sami Anttalainen
# Päivämäärä: 21.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L11T4.py

# (c) LUT 20221120 L11T4.py un
# Tämä esimerkki on tarkoitettu omatoimisen oppimisen tueksi ohjelmoinnin 
# opiskeluun. Muu käyttö kielletty.
###########################################################################
# Ohjelma, joka etsii sopivia numeroita

import time
import sys

class TULOKSET:
    Suurempi = None
    Pienempi = None

def hakufunktio(Nimi, Luvut):
    #####################################################
    # Lisää tarvittava koodi tämän kommentin alapuolelle.
    Rivit = []
    try:
        Tiedosto = open(Nimi, "r", encoding="UTF-8")
        Rivi = Tiedosto.readline()[:-1]
        while len(Rivi) > 0:
            Rivit.append(Rivi)
            Rivi = Tiedosto.readline()[:-1]
        Tiedosto.close()
    except Exception:
        print("Tiedoston '" + Nimi + "' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)

    Pienin = 50
    Suurin = 50
    for Luku in Rivit:
        if int(Luku) < Pienin:
            Pienin = int(Luku)
        elif int(Luku) > Suurin:
            Suurin = int(Luku)
        Jako = Suurin / Pienin
        if Jako > 3:
            Luvut.Pienempi = Pienin
            Luvut.Suurempi = Suurin
            break

    # Lisää tarvittava koodi tämän kommentin yläpuolelle.
    #####################################################
    return Luvut

def paaohjelma():
    Nimi = input("Anna luettavan tiedoston nimi: ")
    Tulokset = TULOKSET()
    Kello1 = time.perf_counter()
    Tulokset = hakufunktio(Nimi, Tulokset)
    Kello2 = time.perf_counter()
    Aika = Kello2 - Kello1
    if ((Tulokset.Suurempi == None) and (Tulokset.Pienempi == None)):
        print("Hakualgoritmi ei löytänyt sopivaa lukuparia.")
    elif (Aika > 2):
        print("Hakualgoritmi ei ollut tarpeeksi nopea.")
    else:
        print("Hakualgoritmi oli riittävän nopea!")
        print("Se löysi sopivan parin:", Tulokset.Pienempi, "ja", Tulokset.Suurempi)
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()

######################################################################
# eof
