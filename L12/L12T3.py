######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Sami Anttalainen
# Opiskelijanumero: 001067291
# Päivämäärä: 29.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L12T3.py
import sys
import jsonpickle

class TIEDOT:
    Nimike = None
    Tekija = None
    ISBN = None
    Varauksia = None
    Niteita = None
    Lisakappaleita = None
    VarauksiaPerNide = None

def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Lue CSV tiedosto")
    print("2) Lue JSON tiedosto")
    print("3) Kirjoita CSV tiedosto")
    print("4) Kirjoita JSON tiedosto")
    print("0) Lopeta")
    Valinta = int(input("Anna valintasi: "))
    return Valinta

def annaNimi(Syote):
    Nimi = input(Syote)
    return Nimi

def lueCSV(Nimi, Oliolista):
    try:
        Tiedosto = open(Nimi, "r", encoding="UTF-8")
        Tiedosto.readline()
        Rivit = []
        Rivi = Tiedosto.readline()
        while len(Rivi) > 0:
            Rivit.append(Rivi)
            Rivi = Tiedosto.readline()
        Tiedosto.close()
    except Exception:
        print("Tiedoston '" + Nimi + "' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    for Rivi in Rivit:
        Sarakkeet = Rivi.split(";")
        Olio = TIEDOT()
        Olio.Nimike = Sarakkeet[0]
        Olio.Tekija = Sarakkeet[1]
        Olio.ISBN = Sarakkeet[2]
        Olio.Varauksia = int(Sarakkeet[3])
        Olio.Niteita = int(Sarakkeet[4])
        Olio.Lisakappaleita = int(Sarakkeet[5])
        Olio.VarauksiaPerNide = float(Sarakkeet[6].replace(",", "."))
        Oliolista.append(Olio)
    print("Luettu " + str(len(Rivit)) + " kirjan tiedot.")
    Rivit.clear()
    return Oliolista
    
def lueJSON(Nimi, Oliolista):
    try:
        Tiedosto = open(Nimi, "r", encoding="UTF-8")
        Koodattu = Tiedosto.read()
        Oliolista = jsonpickle.decode(Koodattu)
        Tiedosto.close()
    except Exception:
        print("Tiedoston '" + Nimi + "' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    print("Luettu " + str(len(Oliolista)) + " kirjan tiedot.")
    return Oliolista

def kirjoitaCSV(Nimi, Oliolista):
    try:
        Tiedosto = open(Nimi, "w", encoding="UTF-8")
        Tiedosto.write("Nimike;Tekijä;ISBN;Varauksia;Niteitä;Tilattuja lisäkappaleita;Varauksia / nide\n")
        for Olio in Oliolista:
            Tiedosto.write("{0};{1};{2};{3:d};{4:d};{5:d};{6:.1f}\n".format(Olio.Nimike, Olio.Tekija, Olio.ISBN, Olio.Varauksia, Olio.Niteita, Olio.Lisakappaleita, Olio.VarauksiaPerNide))
    except Exception:
        print("Tiedoston '" + Nimi + "' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    print("Tiedosto " + Nimi + " kirjoitettu.")
    Tiedosto.close()
    return None

def kirjoitaJSON(Nimi, Oliolista):
    try:
        Tiedosto = open(Nimi, "w", encoding="UTF-8")
        Koodattu = jsonpickle.encode(Oliolista, indent=4)
        Tiedosto.write(Koodattu)
        Tiedosto.close()
    except Exception:
        print("Tiedoston '" + Nimi + "' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    print("Tiedosto " + Nimi + " kirjoitettu.")
    return None


def paaohjelma():
    Oliolista = []
    
    while True:
        Valinta = valikko()

        if Valinta == 1:
            Oliolista.clear()
            Nimi = annaNimi("Anna luettavan CSV tiedoston nimi: ")
            Oliolista = lueCSV(Nimi, Oliolista)

        elif Valinta == 2:
            Oliolista.clear()
            Nimi = annaNimi("Anna luettavan JSON tiedoston nimi: ")
            Oliolista = lueJSON(Nimi, Oliolista)

        elif Valinta == 3:
            Nimi = annaNimi("Anna kirjoitettavan CSV tiedoston nimi: ")
            kirjoitaCSV(Nimi, Oliolista)

        elif Valinta == 4:
            Nimi = annaNimi("Anna kirjoitettavan JSON tiedoston nimi: ")
            kirjoitaJSON(Nimi, Oliolista)

        elif Valinta == 0:
            print()
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.")
        print()
    print("Kiitos ohjelman käytöstä.")
    Oliolista.clear()
    return None
paaohjelma()
######################################################################
#eof