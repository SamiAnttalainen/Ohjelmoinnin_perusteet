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
# Tehtävä L07T1.py

def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Lisää tuote listaan")
    print("2) Poista tuote listasta")
    print("0) Lopeta")
    Valinta = int(input("Valintasi: "))
    return Valinta



def paaohjelma():
    Ostoslista = []
    Koko = None
    print("Ostoslistasi sisältää seuraavat tuotteet:")
    print()
    Valinta = valikko()
    while Valinta != 0:
        Koko = len(Ostoslista)

        if Valinta == 1:
            Tuote = input("Anna lisättävä tuote: ")
            Ostoslista.append(Tuote)
            print()

        elif Valinta == 2:
            print("Ostoslistassasi on " + str(Koko) + " tuotetta.")
            Poisto = int(input("Anna poistettavan tuotteen järjestysnumero: "))
            if Poisto < 1 or Poisto > Koko:
                print("Indeksiä " + str(Poisto) + " ei löydy.")
                print("Tuotteiden järjestysnumerot alkavat numerosta 1.")
            else:
                del Ostoslista[Poisto-1]
            print()
            
        else:
            print("Tuntematon valinta, yritä uudestaan.")
            print()
        print("Ostoslistasi sisältää seuraavat tuotteet:")
        for Tuote in Ostoslista:
            print(Tuote, end=" ")
        print()
        Valinta = valikko()
    print("Lopetetaan")
    print("Sinulta jäi ostamatta seuraavat tuotteet:")
    for Tuote in Ostoslista:
        print(Tuote, end=" ")
    Ostoslista.clear()
    print("\n")
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()

# eof