print("Selvitetään tuotteen alennusprosentti ja myyntihinta.")
Hinta = float(input("Mikä on tuotteen listahinta: "))
print("Lasketaanko hinta")
print("1) yhdellä monihaaraisella valintarakenteella")
print("2) useilla erillisillä valintarakenteilla?")

Valinta = int(input("Anna valintasi: "))

if (Valinta == 1):
    print("Yhdellä monihaaraisella valintarakenteella tulokset ovat seuraavat:")
    if (Hinta >= 300):
        Hinta = (Hinta * 0.70)
        print("Tuotteen alennus on 30% ja hinnaksi jää " + str(round(Hinta, 2)) + "e.")
    elif (Hinta >= 200):
        Hinta = (Hinta * 0.80)
        print("Tuotteen alennus on 20% ja hinnaksi jää " + str(round(Hinta, 2)) + "e.")
    elif (Hinta >= 100):
        Hinta = (Hinta * 0.90)
        print("Tuotteen alennus on 10% ja hinnaksi jää " + str(round(Hinta, 2)) + "e.")

elif (Valinta == 2):
    print("Monella erillisellä valintarakenteella tulokset ovat seuraavat:")
    if (Hinta >= 300):
        Hinta = Hinta * 0.70
        Alennus = "30%"
    if (Hinta >= 200):
        Hinta = Hinta * 0.80
        Alennus = "20%"
    if (Hinta >= 100):
        Hinta = Hinta * 0.90
        Alennus = "10%"
    else:
        print("Tuotteen hinta on " + str(round(Hinta, 2)) + ".")
    print("Tuotteen alennus on " + Alennus + " ja hinnaksi jää " + str(round(Hinta, 2)) + "e.")

else:
    print("Tuntematon valinta.")
    print("Tuotteen alennus on 0% ja hinnaksi jää " + str(round(Hinta, 2)) + "e.")
print("Kiitos ohjelman käytöstä.")
