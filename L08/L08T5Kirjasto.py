######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Sami Anttalainen
# Päivämäärä: 2.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L08T5.py

class TUOTE:
    Tunniste = None
    Maara = None
    Hinta = None

def annaNimi(Syote, Nimi):
    Edellinen = "" # Edellinen nimi
    print("Anna "+ Nimi + " tiedoston nimi, nykyinen on '" + Edellinen + "'.")
    Uusi = input(Syote) # Uusi nimi
    if Uusi == "":
        Uusi = Edellinen
    else:
        Edellinen = Uusi
    return Uusi

def lueTiedosto(Nimi):
    Rivit = []
    Tuotelista = []
    # Luettavan tiedoston nimi.
    Luettava = Nimi
    # Avataan tiedosto luettavaksi
    Tiedosto = open(Luettava, "r", encoding="UTF-8")
    Rivi = Tiedosto.readline()[:-1]
    Lkm = 0 # Rivien lukumäärä.
    # Käydään kaikki rivit läpi ja lisätään ne alkioiksi listaan.
    while len(Rivi) > 0:
        Rivit.append(Rivi)
        Rivi = Tiedosto.readline()[:-1]
        Lkm = Lkm + 1
    # Suljetaan tiedosto.    
    Tiedosto.close()
    # Luodaan jokaisesta rivistä olio ja lisätään oliolistaan.
    for Rivi in Rivit:
        Sarakkeet = Rivi.split(";")
        Tuote = TUOTE()
        Tuote.Tunniste = Sarakkeet[0]
        Tuote.Maara = int(Sarakkeet[1])
        Tuote.Hinta = float(Sarakkeet[2])
        Tuotelista.append(Tuote)
    # Tulostetaan tapahtumat.
    print("Tiedosto '" + Luettava + "' luettu, " + str(Lkm) + " riviä.")
    return Tuotelista
        

def analysoi(Tuotelista):
    Tulolista = []
    Summa = 0
    # Lasketaan jokaisen tuotemäärän arvo ja lisätään tulolistaan. Lasketaan samalla inventaarion kokonaisarvo.
    for Tuote in Tuotelista:
        Tulo = Tuote.Maara * Tuote.Hinta
        Tulolista.append(Tulo)
        Summa = Summa + Tulo
    print("Tiedot analysoitu, varaston arvo on {0:.2f} EUR.".format(Summa))
    return Tulolista

    
def tallennaTulokset(Tulolista, Nimi):
    # Kirjoitettavan tiedoston nimi.
    Kirjoitettava = Nimi
    # Avataan tiedosto kirjoittavaksi.
    Tiedosto = open(Kirjoitettava, "w", encoding="UTF-8")
    # Kirjoitetaan jokainen arvo omalle riville.
    for Arvo in Tulolista:
        Tiedosto.write("{0:.2f}\n".format(Arvo))
    Tiedosto.close()
    print("Tulokset tallennettu tiedostoon '" + Kirjoitettava + "'.")
    return None


# eof
