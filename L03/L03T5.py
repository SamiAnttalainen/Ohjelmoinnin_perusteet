Chytti = 79
Bhytti = round(Chytti * 1.10)
Ahytti = round(Chytti * 1.60)
Hythinta = 0
print("Tämä ohjelma laskee risteilyhintoja.")
Hytti = input("Minkälainen hytti on kyseessä - A, B vai C-hytti: ")
Aika = input("Onko sesonkiaika (k/e): ") 

if Aika == "k" or Aika == "K":
    if Hytti == "C":
        Hythinta = Chytti * 1.50
    elif Hytti == "B":
        Hythinta = Bhytti * 1.75
    else:
        Hythinta = Ahytti * 2.75
else:
    if Hytti == "C":
        Hythinta = Chytti
    elif Hytti == "B":
        Hythinta = Bhytti
    else:
        Hythinta = Ahytti

Kasiakkuus = input("Onko kanta-asiakas (k/e): ")

if Kasiakkuus == "k" or Kasiakkuus == "K":
    Hythinta = Hythinta * 0.90

else:
    Hythinta = Hythinta

print(Hytti + "-hytti maksaa " + str(float(round(Hythinta,2))) + " euroa.")

print("Kiitos ohjelman käytöstä.")
            
            
                
