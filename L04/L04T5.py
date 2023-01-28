print("Tämä ohjelma etsii luvuilla 5 ja 7 jaollista lukua annetulta lukualueelta.")
Alaraja = int(input("Anna lukualueen alaraja: "))
Ylaraja = int(input("Anna lukualueen yläraja: "))

for i in range(Alaraja, Ylaraja+1):
    if ((i % 5) != 0):
        print(str(i) + " ei ole jaollinen viidellä, hylätään.")
            
    elif ((i % 7) != 0):
        print(str(i) + " ei ole jaollinen seitsemällä, hylätään.")

                
    elif ((i % 7) == 0) and ((i % 5) == 0):
        print("Luku " + str(i) + " on jaollinen 5:llä ja 7:llä.")
        print("Lopetetaan etsintä.")
        break

    if (i == Ylaraja):
        print("Alueelta ei löytynyt sopivaa lukua.")
        
        


            
            


print("Kiitos ohjelman käytöstä.")
            
