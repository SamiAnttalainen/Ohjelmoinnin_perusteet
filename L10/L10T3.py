######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Sami Anttalainen
# Päivämäärä: 15.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L10T3.py
import numpy

def paaohjelma():
    print("Tämä ohjelma testaa numpy-matriisin käyttöä.")
    MatriisiA = numpy.zeros((4,4), dtype=int)
    RiviIndex = 0
    for Rivi in range(4):
        RiviIndex += 1
        for Sarake in range(4):
            MatriisiA[Rivi, Sarake] = (RiviIndex) * (Sarake+1)
    print("Matriisi tulostettuna numpy-muotoilulla:")
    print(MatriisiA)
    print()
    print("Matriisi tulostettuna alkiot puolipisteillä eroteltuna:")
    RiviIndex = 0
    for Rivi in range(4):
        RiviIndex += 1
        for Sarake in range(4):
            MatriisiA[Rivi, Sarake] = (RiviIndex) * (Sarake+1)
            if 0 <= Sarake < 3:
                print(MatriisiA[Rivi, Sarake], end=";")
            elif Sarake == 3:
                print(MatriisiA[Rivi, Sarake], end=";\n")
    print()
    print("Kiitos ohjelman käytöstä.")
    MatriisiA = numpy.delete(MatriisiA, numpy.s_[:], None)
    return None
paaohjelma()


######################################################################
# eof
