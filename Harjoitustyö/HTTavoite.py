######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Sami Anttalainen
# Päivämäärä: 11.12.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä HTTavoite.py

# Kirjastot
import HTTavoiteKirjasto

# Kiintoarvot
RIVEJA = 54
SARAKKEITA = 24

# Valikko
def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Lue tiedosto")
    print("2) Analysoi")
    print("3) Kirjoita tiedosto")
    print("4) Analysoi viikonpäivittäiset keskiarvot")
    print("5) Lue sähkönkulutusdata")
    print("6) Analysoi viikoittaiset tuntilaskut")
    print("0) Lopeta")
    Valinta = int(input("Anna valintasi: "))
    return Valinta

# Pääohjelma
def paaohjelma():
    Lista = []
    PaivaLista = []
    Tulokset = None
    Tilastot = None
    Matriisi = None
    DataLuettu = False
    while True:
        Valinta = valikko()
        if Valinta == 1:
            Lista.clear() # Tyhjennetään lista uuden tiedoston lukemisen varalta.
            Nimi = HTTavoiteKirjasto.annaNimi("Anna luettavan tiedoston nimi: ")
            Lista = HTTavoiteKirjasto.lueTiedosto(Nimi, Lista)
            DataLuettu = False

        elif Valinta == 2:
            if len(Lista) != 0:
                PaivaLista.clear() # Tyhjennetään lista uuden analyysin varalta.
                Tulokset = HTTavoiteKirjasto.analysoiTulokset(Lista)
                PaivaLista = HTTavoiteKirjasto.analysoiPaivat(Lista, PaivaLista)
            else:
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.")

        elif Valinta == 3:
            if len(PaivaLista) != 0 or Tulokset != None:
                Nimi = HTTavoiteKirjasto.annaNimi("Anna kirjoitettavan tiedoston nimi: ")
                HTTavoiteKirjasto.kirjoitaTiedosto(Nimi, PaivaLista, Tulokset)
            else:
                print("Ei tietoja tallennettavaksi, analysoi tiedot ennen tallennusta.")

        elif Valinta == 4:
            if len(Lista) != 0:
                Tilastot = HTTavoiteKirjasto.analysoiTilastot(Lista)
                Nimi = HTTavoiteKirjasto.annaNimi("Anna kirjoitettavan tiedoston nimi: ")
                HTTavoiteKirjasto.kirjoitaTilastot(Nimi, Tilastot)
            else:
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.")

        elif Valinta == 5:
            if len(Lista) != 0:
                Nimi = HTTavoiteKirjasto.annaNimi("Anna luettavan tiedoston nimi: ")
                Lista = HTTavoiteKirjasto.lueData(Nimi, Lista)
                DataLuettu = True
            else:
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.")

        elif Valinta == 6:
            if len(Lista) != 0 and DataLuettu == True:
                Matriisi = HTTavoiteKirjasto.numpy.zeros((RIVEJA, SARAKKEITA)) # Luodaan nollamatriisi/tyhjennetään matriisi uuden analyysin varalta.
                Matriisi = HTTavoiteKirjasto.analysoiTuntilaskut(Lista, Matriisi)
                Nimi = HTTavoiteKirjasto.annaNimi("Anna kirjoitettavan tiedoston nimi: ")
                HTTavoiteKirjasto.kirjoitaData(Nimi, Matriisi)
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
    PaivaLista.clear()
    Matriisi = HTTavoiteKirjasto.numpy.delete(Matriisi, HTTavoiteKirjasto.numpy.s_[:], None)
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
######################################################################
# eof
