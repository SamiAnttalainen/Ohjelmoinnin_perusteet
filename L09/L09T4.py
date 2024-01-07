######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Sami Anttalainen
# Päivämäärä: 8.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L09T4.py
import L09T4Kirjasto

def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Lue tiedosto")
    print("2) Analysoi")
    print("3) Kirjoita tiedosto")
    print("0) Lopeta")
    while True:
        try:
            Valinta = int(input("Anna valintasi: "))
            break
        except ValueError:
            print("Anna kokonaisluku.")
    return Valinta

def paaohjelma():
    print("Tämä on valikkopohjainen ohjelma, jossa voit valita haluamasi toiminnon.")
    Tulos = L09T4Kirjasto.TULOS()
    Valinta = valikko()
    Lista = []
    while True:

        if Valinta == 1:
            Lista = L09T4Kirjasto.lueTiedosto()

        elif Valinta == 2:
            if len(Lista) != 0:
                Lista = L09T4Kirjasto.analysoi(Lista, Tulos)
            else:
                print("Ei analysoitavia tietoja, ei analysoitu.")

        elif Valinta == 3:
            if Tulos.Pieninarvo != None or Tulos.Suurinarvo != None or Tulos.Summa != None or Tulos.Keskiarvo != None:
                L09T4Kirjasto.kirjoitaTiedosto(Lista)
            else:
                print("Ei tallennettavia tietoja, tiedostoa ei tallennettu.")
        elif Valinta == 0:
            print("Lopetetaan")
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.")
        print()
        Valinta = valikko()
    print()
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
######################################################################
# eof
