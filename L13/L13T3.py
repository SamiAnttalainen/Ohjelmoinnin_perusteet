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
import datetime
import sys

def valikko():
    print("Anna haluamasi toiminnon numero seuraavasta valikosta: ")
    print("1) Lue tiedosto")
    print("2) Analysoi tiedot viikonpäivittäin")
    print("0) Lopeta")
    Valinta = int(input("Valintasi: "))
    return Valinta

def lueTiedosto(Nimi, Lista):
    try:
        Tiedosto = open(Nimi, "r", encoding="UTF-8")
        Tiedosto.readline()
        Rivit = []
        Rivi = Tiedosto.readline()[:-1]
        while len(Rivi) > 0:
            Rivit.append(Rivi)
            Rivi = Tiedosto.readline()[:-1]
        Tiedosto.close()
    except Exception:
        print("Tiedoston '" + Nimi +"' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)

    for Rivi in Rivit:
        Sarakkeet = Rivi.split(";")
        for Alkio in Sarakkeet:
            if Alkio != "":
                Lista.append(Alkio)
    Rivit.clear
    print("Tiedosto luettu.")
    return Lista

def analysoiTiedot(Lista):
    Paivat = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    Summat = [0, 0, 0, 0, 0, 0, 0]
    for Alkio in Lista:
        Pvm = Alkio[:-3]
        Paiva = datetime.datetime.strptime(Pvm, "%A, %d %B %Y, %H:%M")
        Indeksi = int(Paiva.weekday())
        Summat[Indeksi] += 1
    Summa = sum(Summat)
    print(";Palautuksia viikonpäivittäin")
    for i in range(len(Summat)):
        print(Paivat[i] + ";" + str(Summat[i]))
    print("Yhteensä;" + str(Summa))
    
    return None

def paaohjelma():
    Lista = []
    Nimi = ""
    while True:
        Valinta = valikko()

        if Valinta == 1:
            Lista.clear()
            Nimi = input("Anna luettavan tiedoston nimi: ")
            Lista = lueTiedosto(Nimi, Lista)

        elif Valinta == 2:
            analysoiTiedot(Lista)

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