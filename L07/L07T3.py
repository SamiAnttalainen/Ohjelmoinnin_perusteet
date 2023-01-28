######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Sami Anttalainen
# Opiskelijanumero: 001067291
# Päivämäärä: 20.10.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L07T3.py

def paaohjelma():
    Tnimi = input("Anna tiedoston nimi: ")
    print("Kalastuskilpailun tulokset ovat seuraavat:")
    Tiedosto = open(Tnimi, "r", encoding="UTF-8")
    Rivi = Tiedosto.readline()
    Rivi = Tiedosto.readline()[:-1]
    while len(Rivi) > 0:
        Lista = Rivi.split(";")
        print("Joukkue '" + Lista[0] + "' sai kalan " + Lista[1] + ", joka oli " + Lista[2] + " cm.")
        Rivi = Tiedosto.readline()[:-1]
    Tiedosto.close()
    Lista.clear()
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()

# eof