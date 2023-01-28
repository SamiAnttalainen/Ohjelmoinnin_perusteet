print("Ohjelma kysyy merkkijonoja ja etsii niistä pisimmän.")
Kesto = int(input("Kuinka monta merkkijonoa kysytään: "))
Minimi = int(input("Mikä on merkkijonon minimipituus: "))
Kielto = input("Mitä merkkiä merkkijonossa ei saa olla: ")
Merkkijono = ""

for Jono in range(Kesto):
    Jonot = input("Anna merkkijono: ")
    if (len(Jonot) > len(Merkkijono)):
        Merkkijono = Jonot
    if len(Jonot) < Minimi:
        print("Ohjelma päättyi, koska merkkijonon minimipituus ei täyttynyt.")
        break
    
    elif Kielto in Jonot:
        print("Ohjelma päättyi, koska merkkijonossa oli kielletty merkki.")
        break
    
    if Jono == Kesto-1:
        print("Ohjelma päättyi, koska maksimimäärä merkkijonoja tuli täyteen.")

print("Annoit " + str(Jono+1) + " merkkijonoa.")
print("Pisin merkkijono oli '" + Merkkijono + "', jossa oli " + str(len(Merkkijono)) + " merkkiä.")




print("Kiitos ohjelman käytöstä.")


    
        
        
