######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Sami Anttalainen
# Päivämäärä: 11.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä HTPerus.py

import HTPerusKirjasto

def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Lue tiedosto")
    print("2) Analysoi")
    print("3) Kirjoita tiedosto")
    print("4) Analysoi viikonpäivittäiset keskiarvot")
    print("0) Lopeta")
    Valinta = int(input("Anna valintasi: "))
    return Valinta

def paaohjelma():
    Lista = []
    Paivalista = []
    Tulokset = None
    Tilastot = None
    while True:
        Valinta = valikko()
        if Valinta == 1:
            Lista.clear()
            Nimi = HTPerusKirjasto.annaNimi("Anna luettavan tiedoston nimi: ")
            Lista = HTPerusKirjasto.lueTiedosto(Nimi)

        elif Valinta == 2:
            Paivalista.clear()
            if len(Lista) != 0:
                Tulokset = HTPerusKirjasto.analysoi(Lista)
                Paivalista = HTPerusKirjasto.analysoiPaivat(Lista)
            else:
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.")

        elif Valinta == 3:
            if len(Paivalista) != 0 or Tulokset != None:
                Nimi = HTPerusKirjasto.annaNimi("Anna kirjoitettavan tiedoston nimi: ")
                HTPerusKirjasto.kirjoitaTiedosto(Nimi, Paivalista, Tulokset)
            else:
                print("Ei tietoja tallennettavaksi, analysoi tiedot ennen tallennusta.")

        elif Valinta == 4:
            if len(Lista) != 0:
                Tilastot = HTPerusKirjasto.analysoiTilastot(Lista)
                Nimi = HTPerusKirjasto.annaNimi("Anna kirjoitettavan tiedoston nimi: ")
                HTPerusKirjasto.kirjoitaTilastot(Nimi, Tilastot)
            else:
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.")
        
        elif Valinta == 0:
            print("Lopetetaan.")
            break
        
        else:
            print("Tuntematon valinta, yritä uudestaan.")
        print()
    print()
    Lista.clear()
    Paivalista.clear()
    print("Kiitos ohjelman käytöstä.")
    return None
paaohjelma()
######################################################################
# eof
