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
import sys

class TULOS:
    Pieninarvo = None
    Suurinarvo = None
    Summa = None
    Keskiarvo = None

def lueTiedosto():
    Lista = []
    Edellinenluettava = ""
    print("Luettavan tiedoston nimi on '" + Edellinenluettava + "'.")
    # Kysytään uutta luettavan tiedoston nimeä.
    Luettava = input("Anna uusi nimi, enter säilyttää nykyisen: ")
    if Luettava == "":
        Luettava = Edellinenluettava
    else:
        Edellinenluettava = Luettava
    try:
        Tiedosto = open(Luettava, "r", encoding="UTF-8")
        Rivi = Tiedosto.readline()
        while len(Rivi) > 0:
            Lista.append(int(Rivi))
            Rivi = Tiedosto.readline()
        Tiedosto.close()
    except Exception:
        print("Tiedoston '" + Luettava + "' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    print("Tiedosto '" + Luettava + "' luettu.")
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
    print("Analyysi suoritettu.")
    return Olio

def kirjoitaTiedosto(Olio):
    Edellinenkirjoitettava = ""
    print("Kirjoitettavan tiedoston nimi on '" + Edellinenkirjoitettava + "'.")
    Kirjoitettava = input("Anna uusi nimi, enter säilyttää nykyisen: ")
    if Kirjoitettava == "":
        Kirjoitettava = Edellinenkirjoitettava
    else:
        Edellinenkirjoitettava = Kirjoitettava
    try:
        Tiedosto = open(Kirjoitettava, "w", encoding="UTF-8")
        Tiedosto.write("Analyysin tulokset ovat seuraavat:\n")
        Tiedosto.write("Datan pienin arvo on " + str(Olio.Pieninarvo) + ".\n")
        Tiedosto.write("Datan suurin arvo on " + str(Olio.Suurinarvo) + ".\n")
        Tiedosto.write("Datan summa on " + str(Olio.Summa) + ".\n")
        Tiedosto.write("Datan keskiarvo on " + str(Olio.Keskiarvo) + ".")
        Tiedosto.close()
    except Exception:
        print("Tiedoston '" + Kirjoitettava + "' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    print("Tulokset kirjoitettu tiedostoon.")
    return None
######################################################################
# eof
