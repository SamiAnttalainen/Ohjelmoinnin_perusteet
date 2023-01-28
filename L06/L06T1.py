def tiedostoKirjoita(Nimi):
    # Avataan tiedosto kirjoitusmuotoon.
    Tiedosto = open(Nimi, "w")
    Etunimi = None
    # Kirjoitetaan tiedostoon etunimiä.
    while Etunimi != "":
        Etunimi = input("Anna tiedostoon tallennettava nimi (enter lopettaa): ")
        Tiedosto.write(Etunimi + "\n")
    # Suljetaan tiedosto.
    Tiedosto.close()
    return None

def tiedostoLue(Nimi):
    # Avataan tiedosto luettavaan muotoon.
    Tiedosto = open(Nimi, "r")
    print("Tiedostoon '" + Nimi + "' on tallennettu seuraavat nimet:")
    # Luetaan tiedoston rivit läpi.
    Rivi = Tiedosto.readline()
    while len(Rivi)>1:
        print(Rivi, end="")
        Rivi = Tiedosto.readline()
    # Suljetaan tiedosto.
    Tiedosto.close()

    return None


def paaohjelma():
    # Kysytään tallennettavan tiedoston nimi.
    Tnimi = input("Anna tallennettavan tiedoston nimi: ")
    # Kirjoitetaan.
    tiedostoKirjoita(Tnimi)
    # Luetaan.
    tiedostoLue(Tnimi)
    print("Kiitos ohjelman käytöstä.")
    return None


paaohjelma()

