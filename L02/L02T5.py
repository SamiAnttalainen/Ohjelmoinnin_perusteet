print("Tämä ohjelma tekee painolle ja pituudelle yksikkömuunnoksia.")
PainoKG = int(input("Anna paino kiloina: "))
PainoNaula = float(round(PainoKG / 0.4536,1))
print("Paino on " + str(float(PainoKG)) + " kg eli " + str(PainoNaula) + " naulaa.")
print()
PituusCM = int(input("Anna pituus sentteinä: "))
PituusM = float(round((PituusCM / 100),2))
PituusInch = PituusCM / 2.54
PituusFoot = int(PituusInch / 12)
PituusFootR = float(round(PituusFoot,1))
PituusInches = float(round((PituusInch - 12 * PituusFoot),1))
print("Pituus on", str(PituusM), "metriä",sep=" ", end=" ")
print("eli amerikkalaisittain", str((PituusFootR)), "jalkaa ja",sep=" ", end=" ")
print(str(PituusInches), "tuumaa.",sep=" ")
print("Kiitos ohjelman käytöstä.")


