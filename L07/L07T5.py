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
# Tehtävä L07T5.py

class AUTO:
    Merkki = None
    Hinta = None


def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Anna auton tiedot")
    print("2) Tulosta autojen tiedot")
    print("3) Tallenna autojen tiedot tiedostoon")
    print("0) Lopeta")
    Valinta = int(input("Anna valintasi: "))
    return Valinta

def kysyNimi():
    Nimi = input("Anna tallennettavan tiedoston nimi: ")
    return Nimi

def annaTiedot(Lista):
    Auto = AUTO()
    Auto.Merkki = input("Anna auton merkki: ")
    Auto.Hinta = input("Anna auton hinta: ")
    Lista.append(Auto.Merkki)
    Lista.append(" ")
    Lista.append(Auto.Hinta)
    Lista.append("\n")
    return Lista

def tulostaTiedot(Lista):
    print("Listalta löytyy seuraavat autot ja hinnat:")
    Autolista = ""
    for i in Lista:
        Autolista = Autolista + i
    print(Autolista)
    return None


def tallennaTiedot(Nimi, Lista):
    Tiedosto = open(Nimi, "w", encoding="UTF-8")
    Tiedosto.write("Auton merkki;Auton hinta\n")
    Tiedosto.close()
    Tiedosto = open(Nimi, "a", encoding="UTF-8")
    for i in Lista:
        if i == " ":
            Tiedosto.write(";")
        else:
            Tiedosto.write(i)
    Tiedosto.close()
    print("Tapahtumat kirjoitettu tiedostoon '" + Nimi + "'.")
    return None



def paaohjelma():
    Autolista = []
    Tiedostonimi = kysyNimi()
    print("Tämä ohjelma hallitsee autojen tietoja listalla.")
    Valinta = valikko()
    while Valinta != 0:

        if Valinta == 1:
            Autolista = annaTiedot(Autolista)
            print()
        
        elif Valinta == 2:
            tulostaTiedot(Autolista)

        elif Valinta == 3:
            tallennaTiedot(Tiedostonimi, Autolista)
            print()
        
        else:
            print("Tuntematon valinta, yritä uudestaan.")
            print()
        Valinta = valikko()
    print("Lopetetaan.")
    Autolista.clear()
    print()
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()

# eof
