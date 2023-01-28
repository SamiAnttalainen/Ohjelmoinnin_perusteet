def paaohjelma():
    Tnimi = input("Anna luettavan tiedoston nimi: ")
    Summa = 0
    Lkm = 0
    Tiedosto = open(Tnimi, "r", encoding="UTF-8")
    Rivi = Tiedosto.readline()
    while len(Rivi)>0:
        Lkm += 1
        Summa = Summa + len(Rivi)
        Rivi = Tiedosto.readline()
    Tiedosto.close()
    Keskiarvo = str(round(Summa / Lkm-1, 0))[:-2]
    print("Tiedostossa oli " + str(Lkm) + " nimeä ja " + str(Summa) + " merkkiä.")
    print("Keskimäärin nimen pituus oli " + Keskiarvo + " merkkiä.")

    print("Kiitos ohjelman käytöstä.")
    return None
    
paaohjelma()
