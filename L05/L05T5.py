PITUUS_MIN = 5
PITUUS_MAX = 15
EROTIN = ';'

def tulostaOhjeet():
    print("Anna pyydetyn mittaisia merkkijonoja, joissa ei ole kiellettyjä merkkejä.")
    print("Merkkijonojen tulee olla vähintään 5 ja korkeintaan 15 merkkiä pitkiä.")
    print("Merkkijonoissa ei osaa olla merkkiä ';'.")

def kysyMerkkijono(Merkkijono):
    Jono = input(Merkkijono)
    return Jono

def tarkistaMerkkijono(Tjono):
    if len(Tjono) < PITUUS_MIN:
        print("Liian lyhyt, " + str(len(Tjono)) + " merkkiä.")
        return False
    elif len(Tjono) > PITUUS_MAX:
        print("Liian pitkä, " + str(len(Tjono)) + " merkkiä.")
        return False
    elif EROTIN in Tjono:
        print("Merkkijonossa on kielletty merkki ';'.")
        return False
    else:
        return True

def tulostaHyvaksytyt(Mjono):
    print()
    print("Annoit seuraavat hyväksytyt merkkijonot:")
    for i in range(1, len(Mjono)):
        if Mjono[i] == ";":
            print()
        else:
            print(Mjono[i], end="")
    print()
    return None

def paaohjelma():
    print("Tämä ohjelma kysyy merkkijonoja, tarkistaa ne ja tulostaa hyväksytyt merkkijonot.")
    tulostaOhjeet()
    print()
    OK = True
    Merkkijonot = ""
    Merkkijono = kysyMerkkijono("Anna merkkijono 5-15 merkkiä (enter lopettaa): ")
    while (Merkkijono != ""):
    
        if (Merkkijono == ""):
            break
        OK = tarkistaMerkkijono(Merkkijono)
        if OK == True:
            Merkkijonot = Merkkijonot + ";" + Merkkijono
            Merkkijono = kysyMerkkijono("Anna seuraava merkkijono 5-15 merkkiä (enter lopettaa): ")
        else:
            Merkkijono = kysyMerkkijono("Anna uusi merkkijono 5-15 merkkiä (enter lopettaa): ")
    tulostaHyvaksytyt(Merkkijonot)
    print("Kiitos ohjelman käytöstä.")



    return None

paaohjelma()


        
        
        
    

    


    
