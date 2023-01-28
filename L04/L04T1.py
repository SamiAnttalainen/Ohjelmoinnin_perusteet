Aloitus = int(input("Anna aloitusarvo: ")) #Aloitusarvo
Lopetus = int(input("Anna lopetusarvo: ")) #Lopetusarvo
print()
print("Toteutus for-lauseella:")
for i in range(Aloitus, Lopetus + 1):  #for-silmukka, joka tulostaa luvut väliltä [1, 10]
    print(i,  end=" ")

print()
print()
print("Toteutus while-lauseella:")
while (Aloitus <= Lopetus):
    print(Aloitus, end=" ")
    Aloitus = Aloitus + 1
print()
print()
print("Kiitos ohjelman käytöstä.")
