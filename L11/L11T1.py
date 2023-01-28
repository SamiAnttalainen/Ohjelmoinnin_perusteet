######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Sami Anttalainen
# Opiskelijanumero: 001067291
# Päivämäärä: 21.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L11T1.py

def etsiNeliojuuri(Luku):
    Neliojuuri = None
    Numero = 1
    while True:
        Tulo = Numero ** 2
        if round(Tulo) == Luku:
            Neliojuuri = round(Numero)
            break
        else:
            Numero += 0.025

    print("Neliöjuuri on " + str(Neliojuuri))
    return None


def paaohjelma():
    Luku = int(input("Anna luku: "))
    etsiNeliojuuri(Luku)
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()

######################################################################
# eof