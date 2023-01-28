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
import sys

def paaohjelma():
    print("Syötteen parilliset luvut ovat seuraavat:")
    Summa = 0
    Lista = []
    LukuLista = []
    Maara = 0
    for Parametri in sys.argv:
        Lista.append(Parametri)
    Lista.remove("L13T2.py")
    for i in Lista:
        Luku = int(i)
        Jakojaannos = Luku % 2
        if Jakojaannos == 0:
            Summa += Luku
            LukuLista.append(Luku)
            Maara += 1
    Keskiarvo = float(Summa / Maara)
    for i in LukuLista:
        print(i, end=" ")
    print()
    print("Lukujen keskiarvo on {0:.2f}.".format(Keskiarvo))
    print("Kiitos ohjelman käytöstä.")
    Lista.clear()
    LukuLista.clear()
    return None
paaohjelma()


######################################################################
# eof
