def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Anna merkkijono")
    print("2) Määritä askel")
    print("3) Tulosta merkkijono")
    print("0) Lopeta", end="\n")
    Valinta = int(input("Anna valintasi: "))
    return Valinta

def kysyMerkkijono():
    Jono = input("Anna merkkijono: ")
    print()
    return Jono

def kysyAskel():
    Askel = int(input("Anna tulostuksessa käytettävä askel: "))
    print()
    return Askel

def tulostaMerkkijono(Jono, Askel1):
    if Askel1 > 0 or Askel1 < 0:
        print(Jono[::Askel1])
        print()
    else:
        print(Jono)
        Kesto = len(Jono)
        while Kesto > 0:
            print(Jono[:Kesto -1])
            Kesto -= 1
        print()
    return None

def paaohjelma():
    print("Tällä ohjelmalla voi tulostaa merkkijonoja eri tavoin.")
    Valinta = valikko()
    Merkkijono = ""
    while Valinta != 0:

        if Valinta == 1:
            Merkkijono = kysyMerkkijono()
            Valinta = valikko()

        elif Valinta == 2:
            Askel = kysyAskel()
            Valinta = valikko()

        elif Valinta == 3:
            tulostaMerkkijono(Merkkijono, Askel)
            Valinta = valikko()

        else:
            print("Tuntematon valinta, yritä uudestaan.")
            Valinta = valikko()
            
    print("Lopetetaan.")
    print()
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
            
