def tallennaTiedot(Nimi, Pvm, kWh):
    Tiedosto = open(Nimi, "a", encoding="UTF-8")
    Tiedosto.write("{0:>10s}:{1:>5.0f}\n".format(Pvm, kWh))
    Tiedosto.close()
    return None
    
def paaohjelma():
    Pvm = "Pvm"
    KulutusO = "kWh"
    Summa = 0
    Luettava = input("Anna luettavan tiedoston nimi: ")
    Kirjoitettava = input("Anna tallennettavan tiedoston nimi: ")
    Tiedosto = open(Kirjoitettava, "w", encoding="UTF-8")
    Tiedosto.write("{0:>10s}:{1:>5s}\n".format(Pvm, KulutusO))
    Tiedosto.close()
    LukuTiedosto = open(Luettava, "r", encoding="UTF-8")
    Rivi = LukuTiedosto.readline()
    Rivi = LukuTiedosto.readline()
    Paiva1 = Rivi[0:10]
    while len(Rivi) > 0:
        Paiva = Rivi[0:10]
        Paivakulutus = float(Rivi[14:18]) + float(Rivi[19:23])
        if Paiva == Paiva1:
            Summa = Summa + Paivakulutus
            
        else:
            tallennaTiedot(Kirjoitettava, Paiva1, Summa) 
            Paiva1 = Paiva
            Summa = Paivakulutus
        Rivi = LukuTiedosto.readline()

    tallennaTiedot(Kirjoitettava, Paiva1, Summa) 
    LukuTiedosto.close()
    print("Kiitos ohjelman käytöstä.")

paaohjelma()
