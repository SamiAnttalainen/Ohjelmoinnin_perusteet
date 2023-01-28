
def tulostaOhjeet():
    print("Tämä ohjelma kysyy ja tulostaa tietoja.")
    print("Tämä aliohjelma tulostaa ohjeita käyttäjälle.")
    print("Anna nimesi kahdessa osassa.")
    return None

def kysyNimi():
    print("Tämä aliohjelma kysyy nimen.")
    Etunimi = input("Anna etunimi: ")
    print("Tämä aliohjelma kysyy nimen.")
    Sukunimi = input("Anna Sukunimi: ")
    Nimi = Etunimi + " " + Sukunimi
    return Nimi

def tulostaTulokset(Nimi):
    print("Tämä aliohjelma tulostaa nimesi.")
    print("Hei " + str(Nimi))
    return None

def paaohjelma():
    tulostaOhjeet()
    Nimi = kysyNimi()
    tulostaTulokset(Nimi)
    print("Kiitos ohjelman käytöstä.")

paaohjelma()
