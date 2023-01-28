def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Anna tiedostonimet")
    print("2) Analysoi")
    print("3) Kirjoita tiedosto")
    print("0) Lopeta")
    Valinta = int(input("Anna valintasi: "))
    return Valinta

def kysyNimi(Nimi):
    Nimi = input(Nimi)
    return Nimi

def selvitaPienin(Luku_1, Luku2):
    Luku1 = int(Luku_1)
    if 0 <= Luku1 < Luku2 or Luku2 < 0:
        return Luku1
    else:
        return Luku2

def selvitaSuurin(Luku_1, Luku2):
    Luku1 = int(Luku_1)
    if Luku1 > Luku2 or Luku2 < 0:
        return Luku1
    else:
        return Luku2


def kirjoitaTulokset(Nimi, Parvo, Sarvo):
    # Parvo = pienin arvo ja Sarvo on suurin arvo.
    # Avataan tiedosto.
    Tiedosto = open(Nimi, "w", encoding="UTF-8")
    # Kirjoitetaan tiedostoon.
    Tiedosto.write("Analyysin tulokset ovat seuraavat:\n" )
    Tiedosto.write("Datan pienin arvo on " + str(Parvo) + ".\n")
    Tiedosto.write("Datan suurin arvo on " + str(Sarvo) + ".")
    # Suljetaan tiedosto.
    Tiedosto.close()

def paaohjelma():
    print("Tämä on valikkopohjainen ohjelma, jossa voit valita haluamasi toiminnon.")

    Valinta = valikko()

    while Valinta != 0:

        if Valinta == 1:
            # Tiedostonimet.
            Luettava = "''"
            Kirjoitettava = "''"
            print("Anna tiedostonimet")
            print("Luettavan tiedoston nimi on " + Luettava + ".")
            # Kysytään uutta luettavan tiedoston nimeä.
            Luettava = kysyNimi("Anna uusi nimi, enter säilyttää nykyisen: ")
            if Luettava == "":
                Luettava = "''"
            print("Kirjoitettavan tiedoston nimi on " + Kirjoitettava + ".")
            # Kysytään uuden kirjoitettavan tiedoston nimeä.
            Kirjoitettava = kysyNimi("Anna uusi nimi, enter säilyttää nykyisen: ")
            if Kirjoitettava == "":
                Kirjoitettava = "''"
            print()
            
            Valinta = valikko()


        elif Valinta == 2:
            # Pienin luku.
            Pluku = -1
            # Suurin luku.
            Sluku = -1
            print("Suoritetaan analyysi")
            print()
            # Avataan tiedosto luettavaan muotoon.
            Tiedosto = open(Luettava, "r", encoding="UTF-8")
            Rivi = Tiedosto.readline()
            while len(Rivi) > 0:
                Pluku = selvitaPienin(Rivi, Pluku)
                Sluku = selvitaSuurin(Rivi, Sluku)
                Rivi = Tiedosto.readline()
            Tiedosto.close()

            
            
            Valinta = valikko()

        elif Valinta == 3:
            print("Kirjoitetaan tulokset tiedostoon")
            print()
            kirjoitaTulokset(Kirjoitettava, Pluku, Sluku)
            Valinta = valikko()

        else:
            print("Tuntematon valinta, yritä uudestaan.")
            print()
            Valinta = valikko()
            


    print("Lopetetaan")
    print()
    print("Kiitos ohjelman käytöstä.")
    return None


paaohjelma()
