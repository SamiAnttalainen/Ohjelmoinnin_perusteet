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
# Tehtävä L08T3.py

import datetime

def valikko():
    print("Mitä haluat tehdä:")
    print("1) Tunnista aika-olion komponentit")
    print("2) Laske ikä päivinä")
    print("3) Tulosta viikonpäivät")
    print("4) Tulosta kuukaudet")
    print("0) Lopeta")
    Valinta = int(input("Anna valintasi: "))
    return Valinta

def tunnistaKomponentit():
    Pvm = input("Anna päivämäärä ja kello muodossa 'pp.kk.vvvv hh:mm': ") # Päivämäärän syöttö
    Paiva = datetime.datetime.strptime(Pvm, "%d.%m.%Y %H:%M") # Muutetaan annettu päivämäärä olioksi
    # Tulostetaan muuttujat
    print("Annoit vuoden " + str(Paiva.year))
    print("Annoit kuukauden " + str(Paiva.month))
    print("Annoit päivän " + str(Paiva.day))
    print("Annoit tunnin " + str(Paiva.hour))
    print("Annoit minuutin " + str(Paiva.minute))
    return None

def laskeIka():
    Paiva = datetime.datetime(2000, 1, 1)
    Syote = input("Anna syntymäpäivä muodossa pp.kk.vvvv: ") #Syntymäpäivän syöte
    Spaiva = datetime.datetime.strptime(Syote, "%d.%m.%Y") # Syntymapaiva oliomuodossa
    Ika = Paiva - Spaiva
    print("{0}.{1}.{2}".format(Paiva.day, Paiva.month, Paiva.year) + " henkilö oli " + str(Ika.days) + " päivää vanha.")
    return None

def tulostaPaivat():
    Paiva = datetime.datetime(2022, 10, 31)
    Kesto = 7
    Lkm = 1
    # Tulostetaan viikonpäivät.
    print(Paiva.strftime("%A"))
    while Lkm < Kesto:
        Lkm = Lkm + 1
        Paiva = Paiva + datetime.timedelta(days=1)
        print(Paiva.strftime("%A"))
    return None

def tulostaKuukaudet():
    Paiva = datetime.datetime(2000, 1, 1)
    Kesto = 12
    Lkm = 1
    # Tulostetaan kuukaudet lyhennettyinä.
    print(Paiva.strftime("%b"))
    while Lkm < Kesto:
        Lkm = Lkm + 1
        Paiva = Paiva + datetime.timedelta(days=31)
        print(Paiva.strftime("%b"))
    return None

def paaohjelma():
    print("Tämä ohjelma käyttää datetime-kirjastoa tehtävien ratkaisemiseen.")
    Valinta = valikko()

    while Valinta != 0:

        if Valinta == 1:
            tunnistaKomponentit()

        elif Valinta == 2:
            laskeIka()

        elif Valinta == 3:
            tulostaPaivat()

        elif Valinta == 4:
            tulostaKuukaudet()
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
