######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Sami Anttalainen
# Opiskelijanumero: 001067291
# Päivämäärä: 6.12.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L13T1.py
import L13T1Kirjasto

def valikko():
    print("1) Anna tiedoston nimi")
    print("2) Lue tiedosto")
    print("3) Tulosta tiedot")
    print("4) Kirjoita tiedosto")
    print("0) Lopeta")
    Valinta = int(input("Anna valintasi: "))
    return Valinta

def paaohjelma():
    print("Tämä ohjelma lukee tiedoston ja tulostaa sen tiedot näytölle.")
    Lista = []
    Nimi = None
    Kirjoitettava = "tulos.txt"
    while True:
        Valinta = valikko()

        if Valinta == 1:
            Nimi = L13T1Kirjasto.annaNimi("Anna luettavan tiedoston nimi: ")

        elif Valinta == 2:
            Lista = L13T1Kirjasto.lueTiedosto(Nimi, Lista)

        elif Valinta == 3:
            L13T1Kirjasto.tulostaTiedot(Lista)

        elif Valinta == 4:
            L13T1Kirjasto.kirjoitaTiedosto(Kirjoitettava, Lista)

        elif Valinta == 0:
            print("Lopetetaan.")
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.")
        print()

    print()
    print("Kiitos ohjelman käytöstä.")
    Lista.clear()
    return None

paaohjelma()

######################################################################
# eof