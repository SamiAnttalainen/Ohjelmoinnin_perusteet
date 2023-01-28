######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Sami Anttalainen
# Opiskelijanumero: 001067291
# Päivämäärä: 20.10.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L07T4.py

class TULOS:
    Pieninarvo = None
    Suurinarvo = None
    Summa = None
    Keskiarvo = None

def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Anna tiedostonimet")
    print("2) Lue tiedosto")
    print("3) Analysoi")
    print("4) Kirjoita tiedosto")
    print("0) Lopeta")
    Valinta = int(input("Anna valintasi: "))
    return Valinta

def kysyNimi(Nimi):
    Nimi = input(Nimi)
    return Nimi

def lueTiedosto(Tiedot):
    Lista = []
    Tiedosto = open(Tiedot, "r", encoding="UTF-8")
    Rivi = Tiedosto.readline()
    while len(Rivi) > 0:
        Lista.append(int(Rivi))
        Rivi = Tiedosto.readline()
    Tiedosto.close()
    return Lista


def analysoi(Lista, Olio):
    Pienin = -1
    Suurin = -1
    Summa = 0
    Koko = len(Lista)
    for i in Lista:
        Summa = Summa + i
        if 0 < i < Pienin or Pienin < 0:
            Pienin = i
        elif i > Suurin or Suurin < 0:
            Suurin = i
    Keskiarvo = round(Summa / Koko, 0)
    Olio.Pieninarvo = Pienin
    Olio.Suurinarvo = Suurin
    Olio.Summa = Summa
    Olio.Keskiarvo = Keskiarvo
    return Olio
        

def kirjoitaTiedosto(Olio, Kirjoitettava):
    Tiedosto = open(Kirjoitettava, "w", encoding="UTF-8")
    Tiedosto.write("Analyysin tulokset ovat seuraavat:\n")
    Tiedosto.write("Datan pienin arvo on " + str(Olio.Pieninarvo) + ".\n")
    Tiedosto.write("Datan suurin arvo on " + str(Olio.Suurinarvo) + ".\n")
    Tiedosto.write("Datan summa on " + str(Olio.Summa) + ".\n")
    Tiedosto.write("Datan keskiarvo on " + str(Olio.Keskiarvo) + ".")
    Tiedosto.close()
    return None

def paaohjelma():
    Tulos = TULOS()
    Numerolista = None
    print("Tämä on valikkopohjainen ohjelma, jossa voit valita haluamasi toiminnon.")
    Valinta = valikko()
    Edellinenluettava = ""
    Edellinenkirjoitettava = ""
    while Valinta != 0:

        if Valinta == 1:
            Luettava = ""
            Kirjoitettava = ""
            print("Anna tiedostonimet")
            print("Luettavan tiedoston nimi on '" + Edellinenluettava + "'.")
            # Kysytään uutta luettavan tiedoston nimeä.
            Luettava = kysyNimi("Anna uusi nimi, enter säilyttää nykyisen: ")
            if Luettava == "":
                Luettava = Edellinenluettava
            else:
                Edellinenluettava = Luettava

            print("Kirjoitettavan tiedoston nimi on '" + Edellinenkirjoitettava + "'.")
            Kirjoitettava = kysyNimi("Anna uusi nimi, enter säilyttää nykyisen: ")
            if Kirjoitettava == "":
                Kirjoitettava = Edellinenkirjoitettava
            else:
                Edellinenkirjoitettava = Luettava
            
            print()

        elif Valinta == 2:
            Numerolista = lueTiedosto(Luettava)
            print("Tiedosto '" + Luettava + "' luettu.")
            print()

        elif Valinta == 3:
            Tulos = analysoi(Numerolista, Tulos)
            print("Analyysi suoritettu.")
            print()

        elif Valinta == 4:
            kirjoitaTiedosto(Tulos, Kirjoitettava)
            print("Tulokset kirjoitettu tiedostoon.")
            print()

        else:
            print("Tuntematon valinta, yritä uudestaan.")
            print()

        Valinta = valikko()
        
    print("Lopetetaan")
    print()
    Numerolista.clear()
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()

# eof