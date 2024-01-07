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
# Tehtävä L11T2.py

def selvitaMaara(Luku):
    Edellinen = 1
    Seuraava = 0
    Kesto = 0
    while Kesto < Luku:
        Maara = Edellinen + Seuraava
        Seuraava = Edellinen
        Edellinen = Maara
        Kesto += 1
    print("Kanipariskuntia on " + str(Luku) + " kuukauden kuluttua " + str(Maara))
    return None

def paaohjelma():
    Luku = int(input("Anna kuukausien lukumäärä: "))
    selvitaMaara(Luku)
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()


######################################################################
# eof
