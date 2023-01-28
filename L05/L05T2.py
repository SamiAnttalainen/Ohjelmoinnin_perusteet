def tulostaOhjeet():
    print("Tämä ohjelma etsii antamistasi luvuista pienimmän.")
    print("Ohjelman lopussa se kertoo pienimmän luvun lisäksi antamiesi")
    print("lukujen lukumäärän.")
    print()
    return None

def kysyLuku(Numero):
    Luku = int(input(Numero))
    return Luku

def vertaileLukuja(Luku1, Luku2):
    if Luku1 < Luku2:
        Luku = Luku1
    else:
        Luku = Luku2

    return Luku

def tulostaTiedot(Lkm, Pienin):
    print()
    print("Annoit " + str(Lkm) + " lukua.")
    print("Annetuista luvuista pienin oli " + str(Pienin) + ".")
    return None

def paaohjelma():
    Lkm = 1
    tulostaOhjeet()
    Luku_1 = kysyLuku("Anna positiivinen kokonaisluku: ")
    Luku_2 = kysyLuku("Anna vertailtava positiivinen kokonaisluku (0 lopettaa): ")
    Pienin = vertaileLukuja(Luku_1, Luku_2)
    print("Annetuista luvuista pienempi oli " + str(Pienin) + ".")
    while Luku_2 != 0:
        Lkm += 1
        Luku_2 = kysyLuku("Anna uusi positiivinen kokonaisluku (0 lopettaa): ")
        if Luku_2 == 0:
            break
        Pienempi = vertaileLukuja(Pienin, Luku_2)
        print("Annetuista luvuista pienempi oli " + str(Pienempi) + ".")
        if Pienempi < Pienin:
            Pienin = Pienempi
    tulostaTiedot(Lkm, Pienin)
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()
    
    
    
