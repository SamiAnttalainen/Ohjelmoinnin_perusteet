print("Anna kaksi kokonaislukua.")
Luku1 = int(input("Anna luku 1: "))
Luku2 = int(input("Anna luku 2: "))
print("Selvitetään, ovatko antamasi luvut parillisia.")
if (Luku1 % 2) == 1:
    print("Luku " + str(Luku1) + " on pariton.")
else:
    print("Luku " + str(Luku1) + " on parillinen.")

if (Luku2 % 2) == 1:
    print("Luku " + str(Luku2) + " on pariton.")
else:
    print("Luku " + str(Luku2) + " on parillinen.")

print("Selvitetään, kumpi antamistasi luvuista on pienempi.")

if (Luku1 < Luku2):
    print("Luku " + str(Luku1) + " on pienempi.")
elif (Luku1 > Luku2):
    print("Luku " + str(Luku2) + " on pienempi.")
else:
    print("Luvut " + str(Luku1) + " ja " + str(Luku2) + " ovat yhtäsuuria.")
print("Kiitos ohjelman käytöstä.")

