######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Sami Anttalainen
# Opiskelijanumero: 001067291
# Päivämäärä: 1.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L08T4.py

import L08T4Kirjasto

def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Lue tiedosto")
    print("2) Analysoi")
    print("3) Kirjoita tiedosto")
    print("0) Lopeta")
    Valinta = int(input("Anna valintasi: "))
    return Valinta

def paaohjelma():
    print("Tämä on valikkopohjainen ohjelma, jossa voit valita haluamasi toiminnon.")
    Valinta = valikko()
    while Valinta != 0:

        if Valinta == 1:
            Lista = L08T4Kirjasto.lueTiedosto()

        elif Valinta == 2:
            Lista = L08T4Kirjasto.analysoi(Lista)

        elif Valinta == 3:
            L08T4Kirjasto.kirjoitaTiedosto(Lista)
        else:
            print("Tuntematon valinta, yritä uudestaan.")
        print()
        Valinta = valikko()
    print("Lopetetaan")
    print()
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()



# eof