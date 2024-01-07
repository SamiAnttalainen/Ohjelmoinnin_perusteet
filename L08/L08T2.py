######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Sami Anttalainen
# Päivämäärä: 1.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L08T2.py

import L08T2Kirjasto

# Valikko
def valikko():
    print("Minkä muunnoksen haluat tehdä?")
    print("1) Anna muunnettava tilavuus")
    print("2) Muunna litra gallon'ksi")
    print("3) Muunna litra pint'ksi")
    print("4) Muunna litra cup'ksi")
    print("5) Muunna litra fluid ounce'ksi")
    print("6) Muunna gallon litroiksi")
    print("7) Muunna pint litroiksi")
    print("8) Muunna cup litroiksi")
    print("9) Muunna fluid ounce litroiksi")
    print("0) Lopeta")
    Valinta = int(input("Anna valintasi: "))
    return Valinta


def paaohjelma():
    print("Käytetään kirjaston versiota " + str(L08T2Kirjasto.VERSIO))
    Muunto = None # Muunnoksen jälkeinen tilavuus
    Valinta = valikko()


    while Valinta != 0:

        if Valinta == 1:
            Tilavuus = L08T2Kirjasto.annaTilavuus()

        elif Valinta == 2:
            Muunto = L08T2Kirjasto.litraGalloniksi(Tilavuus)
            print("Litrat muutettuina gallon'ksi: " + str(round(Muunto, 2)))

        elif Valinta == 3:
            Muunto = L08T2Kirjasto.litraPintiksi(Tilavuus)
            print("Litrat muutettuina pint'ksi: " + str(round(Muunto, 2)))

        elif Valinta == 4:
            Muunto = L08T2Kirjasto.litraCupiksi(Tilavuus)
            print("Litrat muutettuina cup'ksi: " + str(round(Muunto, 2)))

        elif Valinta == 5:
            Muunto = L08T2Kirjasto.litraFluidiksi(Tilavuus)
            print("Litrat muutettuina fluid ounce'ksi: " + str(round(Muunto, 2)))

        elif Valinta == 6:
            Muunto = L08T2Kirjasto.gallonLitroiksi(Tilavuus)
            print("Gallon't muutettuina litroiksi: " + str(round(Muunto, 2)))

        elif Valinta == 7:
            Muunto = L08T2Kirjasto.pintLitroiksi(Tilavuus)
            print("Pint't muutettuina litroiksi: " + str(round(Muunto, 2)))

        elif Valinta == 8:
            Muunto = L08T2Kirjasto.cupLitroiksi(Tilavuus)
            print("Cup't muutettuina litroiksi: " + str(round(Muunto, 2)))

        elif Valinta == 9:
            Muunto = L08T2Kirjasto.fluidLitroiksi(Tilavuus)
            print("Fluid ounce't muutettuina litroiksi: " + str(round(Muunto, 2)))

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
