print("Selvitetään sanojen aakkosjärjestys.")
Sana1 = input("Anna sana 1: ")
Sana2 = input("Anna sana 2: ")
if (Sana1 < Sana2):
    print("'" + Sana1 + "' on aakkosissa aiemmin kuin '" + Sana2 + "'.")
elif (Sana1 > Sana2):
    print("'" + Sana2 + "' on aakkosissa aiemmin kuin '" + Sana1 + "'.")
else:
    print("Sanat ovat samoja, '" + Sana1 + "'.")
print()

print("Selvitetään merkin sisältyminen merkkijonoon.")
Jono = input("Anna merkkijono: ")
Merkki = input("Anna etsittävä merkki: ")
if Merkki in Jono:
    print("Merkki '" + Merkki + "' sisältyy merkkijonoon '" + Jono +"'.")
else:
    print("Merkki '" + Merkki + "' ei sisälly merkkijonoon '" + Jono +"'.")

print()
print("Selvitetään, onko sana palindromi.")
Sana3 = input("Anna testattava sana: ")
if (Sana3 == Sana3[::-1]):
    print("Sana '" + Sana3 + "' on palindromi.")
else:
    print("Sana ei ole palindromi.")
    print("Sana on etuperin '" + Sana3 + "' ja takaperin '" + Sana3[::-1] + "'.")
print("Kiitos ohjelman käytöstä.")

