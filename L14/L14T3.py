######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Sami Anttalainen
# Päivämäärä: 15.12.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L14T3.py
import datetime

def tulostaKalenteri(Vuosi, Kuukausi):
    Valimerkit = {0: "{0:>2s}".format(""), 1: "{0:>5s}".format(""), 2: "{0:>8s}".format(""), 3: "{0:>11s}".format(""), 4: "{0:>14s}".format(""), 5: "{0:>17s}".format(""), 6: "{0:>20s}".format("")}
    Paiva = 1
    Paivamaara = datetime.datetime(Vuosi, Kuukausi, Paiva)
    JarjestysNro = int(Paivamaara.weekday())
    if Kuukausi != 12:
        SeuraavaKuukausi = datetime.datetime(Vuosi, Kuukausi+1, Paiva)
        Kesto = (SeuraavaKuukausi - Paivamaara).days
    else:
        SeuraavaKuukausi = datetime.datetime(Vuosi+1, Kuukausi-11, Paiva)
        Kesto = (SeuraavaKuukausi - Paivamaara).days
    Lkm = 0
    print("Kalenteri näyttää seuraavalle:")
    print(" Ma Ti Ke To Pe La Su")
    print(Valimerkit[JarjestysNro], end="")

    while Lkm < Kesto:
        if JarjestysNro != 6:
            if Paivamaara.day < 9:
                print(Paivamaara.day, end="  ")
            elif Paivamaara.day >= 9:
                if Paivamaara.day != Kesto:
                    print(Paivamaara.day, end=" ")
                else:
                    print(Paivamaara.day, end="")
            Paivamaara = Paivamaara + datetime.timedelta(days=1)
            JarjestysNro = int(Paivamaara.weekday())
            Lkm = Lkm + 1


        elif JarjestysNro == 6:
            print(Paivamaara.day)
            Paivamaara = Paivamaara + datetime.timedelta(days=1)
            if Paivamaara.day <= 9:
                print("{0:>2s}".format(""), end="")
            elif Paivamaara.day > 9:
                if Paivamaara.day != Kesto:
                    print("{0:>1s}".format(""), end="")
            JarjestysNro = int(Paivamaara.weekday())
            Lkm = Lkm + 1
    return None

def paaohjelma():
    Vuosi = int(input("Anna vuosi: "))
    Kuukausi = int(input("Anna kuukausi: "))
    tulostaKalenteri(Vuosi, Kuukausi)
    return None
paaohjelma()

######################################################################
# eof
