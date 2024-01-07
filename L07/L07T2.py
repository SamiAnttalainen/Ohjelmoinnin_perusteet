######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Sami Anttalainen
# Päivämäärä: 20.10.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L07T2.py

class TILI:
    Nimi = None
    Saldo = None

def kysyTiedot(Luokka):
    Luokka.Nimi = input("Anna pankkitilin nimi: ")
    Luokka.Saldo = round(float(input("Anna pankkitilin saldo: ")), 2)
    return Luokka

def tulostaTiedot(Luokka):
    print("Pankkitilillä '" + Luokka.Nimi + "' on nyt rahaa " + str(Luokka.Saldo) + "e.")
    return None


def paaohjelma():
    Tili = TILI()
    Tili = kysyTiedot(Tili)
    tulostaTiedot(Tili)
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()

# eof
