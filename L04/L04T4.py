print("Tämä on valikkopohjainen ohjelma, jossa voit valita haluamasi toiminnon.")
print("Valitse haluamasi toiminto:")
print("1) Syötä tiedot")
print("2) Laske")
print("3) Tulosta tulokset")
print("0) Lopeta")
Valinta = int(input("Anna valintasi: "))

while Valinta != 0:
    
    if Valinta == 1:
        print("Syötä tiedot")
        Luku_1 = input("Anna luku 1: ")
        Luku1 = int(Luku_1)
        Luku_2 = input("Anna luku 2: ")
        Luku2 = int(Luku_2)
        print()
        print("Valitse haluamasi toiminto:")
        print("1) Syötä tiedot")
        print("2) Laske")
        print("3) Tulosta tulokset")
        print("0) Lopeta")
        Valinta = int(input("Anna valintasi: "))

    elif Valinta == 2:
        print("Laske")
        Summa = Luku1 + Luku2
        print()
        print("Valitse haluamasi toiminto:")
        print("1) Syötä tiedot")
        print("2) Laske")
        print("3) Tulosta tulokset")
        print("0) Lopeta")
        Valinta = int(input("Anna valintasi: "))


    elif Valinta == 3:
        print("Tulosta tulokset")
        print("Lukujen summa on " + str(Summa) + ".")
        print()
        print("Valitse haluamasi toiminto:")
        print("1) Syötä tiedot")
        print("2) Laske")
        print("3) Tulosta tulokset")
        print("0) Lopeta")
        Valinta = int(input("Anna valintasi: "))

    elif Valinta == 0:
        print("Lopetetaan")
        

    else:
        print("Tuntematon valinta, yritä uudestaan.")
        print()
        print("Valitse haluamasi toiminto:")
        print("1) Syötä tiedot")
        print("2) Laske")
        print("3) Tulosta tulokset")
        print("0) Lopeta")
        Valinta = int(input("Anna valintasi: "))
print("Lopetetaan.")
print()
print("Kiitos ohjelman käytöstä.")
        
        
        
