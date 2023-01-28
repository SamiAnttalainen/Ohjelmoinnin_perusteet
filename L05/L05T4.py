def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Syötä tiedot")
    print("2) Laske")
    print("3) Tulosta tulokset")
    print("0) Lopeta")
    Valinta = int(input("Anna valintasi: "))
    return Valinta

def kysyLuku(KLuku):
    Luku1 = int(input(KLuku))
    return Luku1

def summa(Luku_1, Luku_2):
    Summa = Luku_1 + Luku_2
    return Summa

def erotus(Luku_1, Luku_2):
    Erotus = Luku_1 - Luku_2
    return Erotus

def tulostaTulokset(Num1, Num2, Num3, Num4):
    print("Luvut ovat " + str(Num1) + " ja " + str(Num2) + ".")
    print("Lukujen summa on " + str(Num3) + " ja erotus on " + str(Num4) + ".")
    return None

def paaohjelma():
    print("Tämä on valikkopohjainen ohjelma, jossa voit valita haluamasi toiminnon.")
    Valinta = valikko()

    while Valinta != 0:

        if Valinta == 1:
            print("Syötä tiedot")
            Luku1 = kysyLuku("Anna kokonaisluku 1: ")
            Luku2 = kysyLuku("Anna kokonaisluku 2: ")
            print()
            Valinta = valikko()


        elif Valinta == 2:
            print("Laske")
            print()
            Summa = summa(Luku1, Luku2)
            Erotus = erotus(Luku1, Luku2)
            Valinta = valikko()

        elif Valinta == 3:
            print("Tulosta tulokset")
            tulostaTulokset(Luku1, Luku2, Summa, Erotus)
            print()
            Valinta = valikko()

        else:
            print("Tuntematon valinta, yritä uudestaan.")
            print()
            Valinta = valikko()
            


    print("Lopetetaan.")
    print()
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
    



    
    
