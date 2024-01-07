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
# Tehtävä L12T1.py


def tarkistaTunnus(Tunnus):
    Luku = None
    Jako = None
    Muuttujalista = ["-", "+", "a"] # Sallitut välimerkit.
    Merkkilista = ["G", "I", "O", "Q", "Z"] # Kielletyt merkit.
    Kuukaudet = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "12"]
    Tunnus = Tunnus.lower()
    Taulukko = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f", 16: "H", 17: "j", 18: "k", 19: "l", 20: "m", 21: "n",
         22: "p", 23: "r", 24: "s", 25: "t", 26: "u", 27: "v", 28: "w", 29: "x", 30: "y"}
    if Tunnus[0:6].isdigit() == True and Tunnus[7:10].isdigit() == True:
        if Tunnus[0] == 0:
            Luku = Tunnus[1:6] + Tunnus[7:10]
        elif Tunnus[7] == 0:
             Luku = Tunnus[0:6] + Tunnus[8:10]
        elif Tunnus[0] == 0 and Tunnus[7] == 0:
             Luku = Tunnus[1:6] + Tunnus[8:10]
        else:
             Luku = Tunnus[0:6] + Tunnus[7:10]
        Jako = int(Luku) % 31
        

    if (Tunnus[-1].isalpha() == True) and (Tunnus[6] in Muuttujalista) and (len(Tunnus) == 11) and Tunnus[2:4] in Kuukaudet and Tunnus[0:6].isdigit() == True and Tunnus[7:10].isdigit() == True and Tunnus[-1] not in Merkkilista and Taulukko[Jako] == Tunnus[-1]:
        
            print("Henkilötunnus hyväksytty.")
    else:
        print("Henkilötunnusta ei hyväksytä.")
    Muuttujalista.clear()
    Merkkilista.clear()
    Kuukaudet.clear()
    Taulukko.clear()
    return None

def paaohjelma():
    Tunnus = input("Anna henkilötunnus: ")
    tarkistaTunnus(Tunnus)
    print("Kiitos ohjelman käytöstä.")
    return None
paaohjelma()

######################################################################
# eof
