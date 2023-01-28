######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Sami Anttalainen
# Opiskelijanumero: 001067291
# Päivämäärä: 2.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L08T5.py
import L08T5Kirjasto


def valikko():
    print("Mitä haluat tehdä:")
    print("1) Lue tiedosto")
    print("2) Analysoi tiedot")
    print("3) Tallenna tulokset")
    print("0) Lopeta")
    Valinta = int(input("Valintasi: "))
    return Valinta

def paaohjelma():
    Valinta = valikko()
    Lista = []
    Tiedot = []

    while Valinta != 0:

        if Valinta == 1:
            # Annetaan luettavan tiedoston nimi.
            Luettava = L08T5Kirjasto.annaNimi("Anna uusi nimi, enter säilyttää nykyisen: ", "luettavan")
            # Luetaan tiedosto.
            Lista = L08T5Kirjasto.lueTiedosto(Luettava)

        elif Valinta == 2:
            # Analysoidaan tiedosto.
            Tiedot = L08T5Kirjasto.analysoi(Lista)

        elif Valinta == 3:
            # Annetaan kirjoitettavan tiedoston nimi.
            Kirjoitettava = L08T5Kirjasto.annaNimi("Anna uusi nimi, enter säilyttää nykyisen: ", "kirjoitettavan")
            # Kirjoitetaan tiedostoon.
            L08T5Kirjasto.tallennaTulokset(Tiedot, Kirjoitettava)

        else:
            print("Tuntematon valinta, yritä uudestaan.")
        print()
        Valinta = valikko()
    print("Lopetetaan.")
    print()
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()

# eof