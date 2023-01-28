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
# Tehtävä L11T3.py

def tulostaSanat(Sana, Maara, Kerta):
    if Maara > 0:
        print("Sana on '" + Sana + "', " + str(Kerta) + ". kerta.")
        return tulostaSanat(Sana, Maara - 1, Kerta + 1)
    return None

def paaohjelma():
    Sana = input("Anna tulostettava sana: ")
    Maara = int(input("Anna tulostuskertojen määrä: "))
    Kerta = 1
    tulostaSanat(Sana, Maara, Kerta)
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
######################################################################
# eof