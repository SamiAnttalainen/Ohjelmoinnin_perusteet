Alaraja = float(30)
Ylaraja = float(130)
Summa = 0 #Painojen kokonaispaino
Maara = 0 #Painojen määrä
while (True):
    Paino = float(input("Anna paino väliltä 30-130 kg (0 lopettaa): "))
    if (Paino >= Alaraja) and (Paino <= Ylaraja):
        Summa = Summa + Paino
        Maara = Maara + 1
        Keskiarvo = Summa / Maara
        
    elif (0 < Paino < 30) or (Paino > 130):
        print("Väärä syöte. Painon tulee olla 30 ja 130 kg välillä (0 lopettaa).")
    
    
    if (Paino == 0):
        break

print("Painojen keskiarvo on " + str(round(Keskiarvo,1)) + ".")
print("Kiitos ohjelman käytöstä.")
