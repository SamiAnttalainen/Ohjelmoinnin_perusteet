######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Sami Anttalainen
# Päivämäärä: 7.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L09T2.py

def valikko():
    print("Mitä haluat tehdä:")
    print("1) Testaa ValueError")
    print("2) Testaa IndexError")
    print("3) Testaa ZeroDivisionError")
    print("4) Testaa TypeError")
    print("0) Lopeta")
    while True:
        try:
            Valinta = int(input("Valintasi: "))
            break
        except ValueError:
            print("Anna Valinta kokonaislukuna.")  
    return Valinta

def testaaIndexerror():
    Lista = [11, 22, 33, 44, 55]
    try:
        Luku = int(input("Anna indeksi 0-4: "))
        print("Listan arvo on " + str(Lista[Luku]) + " indeksillä " + str(Luku) + ".")
    except IndexError:
        print("Tuli IndexError, indeksi " + str(Luku) + ".")
    return None

def testaaNollajako():
    Jaettava = 4
    try:
        Jakaja = int(input("Anna jakaja: "))
        Jako = Jaettava / Jakaja
        print("4/" + str(Jakaja) + " on {0:.2f}.".format(Jako))
    except ZeroDivisionError:
        print("Tuli ZeroDivisionError, jakaja " + str(Jakaja) + ".")
    return None


def testaaTyperror():
    try:
        Luku = input("Anna numero: ")
        Tulo = Luku * Luku
    except TypeError:
        print("Tuli TypeError, " + Luku + "*" + Luku + " merkkijonoilla ei onnistunut.")
    return None

def paaohjelma():
    Valinta = valikko()
    while Valinta != 0:

        if Valinta == 1:
            print("Valikko-ohjelma testaa ValueError'n.")
        elif Valinta == 2:
            testaaIndexerror()
        elif Valinta == 3:
            testaaNollajako()
        elif Valinta == 4:
            testaaTyperror()
        else:
            print("Tuntematon valinta, yritä uudestaan.")
        print()
        Valinta = valikko()
    print("Lopetetaan")
    print()
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
######################################################################
# eof
