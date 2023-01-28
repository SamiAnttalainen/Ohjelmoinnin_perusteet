######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Sami Anttalainen
# Opiskelijanumero: 001067291
# Päivämäärä: 1.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L08T4.py


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
    Tiedosto = open(Luettava, "r", encoding="UTF-8")
    Rivi = Tiedosto.readline()
    while len(Rivi) > 0:
        Lista.append(int(Rivi))
        Rivi = Tiedosto.readline()
    Tiedosto.close()
    print("Tiedosto '" + Luettava + "' luettu.")
    return Lista


def analysoi(Lista):
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
    Tiedot = []
    Tiedot.append(Pienin)
    Tiedot.append(Suurin)
    Tiedot.append(Summa)
    Tiedot.append(Keskiarvo)
    print("Analyysi suoritettu.")
    return Tiedot

def kirjoitaTiedosto(Lista):
    Edellinenkirjoitettava = ""
    print("Kirjoitettavan tiedoston nimi on '" + Edellinenkirjoitettava + "'.")
    Kirjoitettava = input("Anna uusi nimi, enter säilyttää nykyisen: ")
    if Kirjoitettava == "":
        Kirjoitettava = Edellinenkirjoitettava
    else:
        Edellinenkirjoitettava = Kirjoitettava
    Tiedosto = open(Kirjoitettava, "w", encoding="UTF-8")
    Tiedosto.write("Analyysin tulokset ovat seuraavat:\n")
    Tiedosto.write("Datan pienin arvo on " + str(Lista[0]) + ".\n")
    Tiedosto.write("Datan suurin arvo on " + str(Lista[1]) + ".\n")
    Tiedosto.write("Datan summa on " + str(Lista[2]) + ".\n")
    Tiedosto.write("Datan keskiarvo on " + str(Lista[3]) + ".")
    Tiedosto.close()
    print("Tulokset kirjoitettu tiedostoon.")
    return None


# eof