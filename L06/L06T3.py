
def onkoPalindromi(Nimi):
    Siivottu = ""
    Hyvaksytty = ""
    # Muutetaan isot kirjaimet pieniksi.
    Jono = Nimi.lower()
    #if "#" == Jono[0]:
        #return None
    # Poistetaan välimerkit for-lauseella.
    for i in Jono:
        if i.isalnum() == True:
            Siivottu = Siivottu + i
    # Selvitetään, onko kyseessä palindromi.
    if (Siivottu == Siivottu[::-1]) and (len(Siivottu) > 2) and Siivottu.isalpha() == True:
        Hyvaksytty = Siivottu
        return Hyvaksytty
        
    else:
        return None


def kirjoitaPalindromi(Nimi, Alkuperäinen, Korjattu):
    Alkuperäinen = Alkuperäinen[:-1]
    # Avataan tiedosto kirjoitettavaksi.
    Tiedosto = open(Nimi, "a", encoding="UTF-8")
    if Korjattu != None:
        Tiedosto.write(Alkuperäinen + "\n")
        Tiedosto.write("----> " + Korjattu + "\n")
        print("OK: '" + Alkuperäinen + "'")
    else:
        print("Ei OK: '" + Alkuperäinen + "'")
    # Suljetaan tiedosto.
    Tiedosto.close()
    return None
    

def paaohjelma():
    #Kysytään luettavan ja kirjoitettavien tiedostojen nimet.
    Luettava = input("Anna luettavan tiedoston nimi: ")
    Kirjoitettava = input("Anna kirjoitettavan tiedoston nimi: ")
    # Varmistetaan, että kirjoitettava tiedosto on tyhjä.
    Varmistus = open(Kirjoitettava, "w", encoding="UTF-8")
    Varmistus.close()
    # Avataan luettava tiedosto luettavaksi.
    Tiedosto = open(Luettava, "r", encoding="UTF-8")
    Rivi = Tiedosto.readline()
    # Käydään tiedoston rivejä läpi While-silmukalla.
    while len(Rivi) > 0:
        Vastaus = onkoPalindromi(Rivi)
        kirjoitaPalindromi(Kirjoitettava, Rivi, Vastaus)
        Rivi = Tiedosto.readline()
    # Suljetaan luettava tiedosto.
    Tiedosto.close()
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
    
