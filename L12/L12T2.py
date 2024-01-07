######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Sami Anttalainen
# Päivämäärä: 28.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L12T2.py

def laskeErotus(Luku1, Luku2):
    Luku1 = Luku1[::-1] # Käännetään bitit, koska laskut lasketaan oikealta vasemmalle, mutta luku tapahtuu vasemmalta oikealle.
    Luku2 = Luku2[::-1]
    Potenssi = 0
    Numero1 = 0 # Luku1 kymmenkantalukuna.
    Numero2 = 0 # Luku2 kymmenkantalukuna.

    for Luku in Luku1:  # Muutetaan luvut kymmenkantaluvuiksi.
        Numero1 += int(Luku) * (2 ** Potenssi)
        Potenssi += 1

    Potenssi = 0
    for Luku in Luku2:
        Numero2 += int(Luku) * (2 ** Potenssi)
        Potenssi += 1

    Erotus = Numero1 - Numero2 # Kymmenkantalukujen erotus.
    print("Bittijonosi " + Luku1[::-1] + " on kymmenkantaisena kokonaislukuna " + str(Numero1))
    print("Bittijonosi " + Luku2[::-1] + " on kymmenkantaisena kokonaislukuna " + str(Numero2))
    print("Lukujen " + str(Numero1) + " ja " + str(Numero2) + " erotus on " + str(Erotus))
    return None

def paaohjelma():
    Luku1 = input("Anna ensimmäinen binaariluku: ")
    Luku2 = input("Anna toinen binaariluku: ")
    laskeErotus(Luku1, Luku2)
    print("Kiitos ohjelman käytöstä.")
    return None
paaohjelma()
######################################################################
# eoc
