######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Sami Anttalainen
# Päivämäärä: 6.12.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L13T1.py
import sys

class TIEDOT:
    Nimi = None
    Ika = None
    Numero = None # Puhelinnumero

def annaNimi(Syote):
    Nimi = input(Syote)
    return Nimi

def lueTiedosto(Nimi, Lista):
    try:
        Tiedosto = open(Nimi, "r", encoding="UTF-8")
        Rivi = Tiedosto.readline()[:-1]
        while len(Rivi) > 0:
            Lista.append(Rivi)
            Rivi = Tiedosto.readline()[:-1]
        Tiedosto.close()
    except Exception:
        print("Tiedoston '" + Nimi + "' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)

    TiedotLista = []
    for Rivi in Lista:
        Sarakkeet = Rivi.split(";")
        Tiedot = TIEDOT()
        Tiedot.Nimi = Sarakkeet[0]
        Tiedot.Ika = Sarakkeet[2]
        Tiedot.Numero = Sarakkeet[1]
        TiedotLista.append(Tiedot)
    Lista.clear()
    return TiedotLista

def tulostaTiedot(Lista):
    for Olio in Lista:
        print(Olio.Nimi + " on " + Olio.Ika + " vuotta vanha ja hänen puhelinnumero on " + Olio.Numero + ".")
    return None

def kirjoitaTiedosto(Nimi, Lista):
    Maara = 0
    Raja = int(input("Minkä ikäiset ihmiset otetaan mukaan tiedostoon (vuosia): "))
    KirjoitusLista = []
    for Olio in Lista:
        if int(Olio.Ika) >= Raja:
            KirjoitusLista.append(Olio)
            Maara += 1
    try:
        Tiedosto = open(Nimi, "w", encoding="UTF-8")
        Tiedosto.write("Tiedostossa on mukana {0:d} vähintään {1:d} vuotiasta henkilöä:\n".format(Maara, Raja))
        for Olio in KirjoitusLista:
            Tiedosto.write("{0};{1};{2}\n".format(Olio.Nimi, Olio.Numero, Olio.Ika))
        Tiedosto.close()
    except Exception:
        print("Tiedoston '" + Nimi + "' käsittelyssä virhe, lopetetaan.")
    return None

######################################################################
# eof
