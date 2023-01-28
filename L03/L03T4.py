print("Tämä on valikkopohjainen ohjelma, jossa voit valita haluamasi toiminnon.")
print("Valitse haluamasi toiminto:")
print("1) Tulosta merkkijono etuperin")
print("2) Tulosta merkkijono takaperin")
print("3) Tulosta merkkijonon pituus")
print("0) Lopeta")
Valinta = int(input("Anna valintasi: "))

if (Valinta == 1):
    Jono = input("Anna merkkijono: ")
    print("Merkkijono on etuperin '" + Jono + "'.")
elif (Valinta == 2):
    Jono = input("Anna merkkijono: ")
    print("Merkkijono on takaperin '" + Jono[::-1] + "'.")
elif (Valinta == 3):
    Jono = input("Anna merkkijono: ")
    print("Merkkijonon pituus on " + str(len(Jono)) + ".")
elif (Valinta == 0):
    print("Lopetetaan")
else:
    print("Tuntematon valinta.")
print("Kiitos ohjelman käytöstä.")
