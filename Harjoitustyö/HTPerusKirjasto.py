######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Sami Anttalainen
# Opiskelijanumero: 001067291
# Päivämäärä: 18.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä HTPerus.py

# Kirjastot
import datetime
import sys

# Luokat
class SAHKO:
    Pvm = None
    Hinta = None

class TULOKSET:
    Pienin = None
    Ppaiva = None
    Suurin = None
    Spaiva = None
    Khinta = None
    Tunnit = None

class TULOS:
    Pvm = None
    PvmKeskiarvo = None

class PAIVA:
    MaHinta = None
    TiHinta = None
    KeHinta = None
    ToHinta = None
    PeHinta = None
    LaHinta = None
    SuHinta = None


# Aliohjelmat

# Aliohjelma kysyy tiedoston nimen.
def annaNimi(Syote):
    Nimi = input(Syote) # Tiedoston nimi
    return Nimi

# Aliohjelma lukee annetun tiedoston ja tallentaa tiedoston rivit oliolistaan.
def lueTiedosto(Nimi):
    Rivit = []
    try:
        Tiedosto = open(Nimi, "r", encoding="UTF-8")
        # Luetaan kaikki paitsi ensimmäinen rivi ja lisätään ne listaan.
        Rivi = Tiedosto.readline() # Ohitetaan ensimmäinen rivi.
        Rivi = Tiedosto.readline()[:-1]
        while len(Rivi) > 0:
            Rivit.append(Rivi)
            Rivi = Tiedosto.readline()[:-1]
        # Suljetaan tiedosto.
        Tiedosto.close()
    except Exception:
        print("Tiedoston '" + Nimi + "' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    # Käydään listan alkiot läpi ja tallennetaan halutut tiedot oliolistaan.
    Sahkolista = [] # Oliolista sähkön hinnoille ja päivämäärille.
    
    for Rivi in Rivit:
        Sarakkeet = Rivi.split(";")
        Sahko = SAHKO()
        Sahko.Pvm = Sarakkeet[0]
        Sahko.Hinta = float(Sarakkeet[1])
        Sahkolista.append(Sahko)
    print("Tiedosto '" + Nimi + "' luettu.")
    Rivit.clear()
    return Sahkolista

# Aliohjelma selvittää pienimmän ja suurimman hinnan sekä niiden päivämäärät. Samalla laskee myös sähkön keskihinnan. Lopuksi aliohjelma tallentaa tulokset Tulos-olioon.
def analysoi(Sahkolista):
    Pienin = 0
    Pvm1 = None  # Pienin päivämäärä
    Suurin = 0
    Pvm2 = None # Suurin päivämäärä
    Summa = 0
    Koko = len(Sahkolista) # Alkioiden lukumäärä.
    for Alkio in Sahkolista:
        Summa = Summa + float(Alkio.Hinta)
        if Alkio.Hinta < Pienin:
            Pienin = Alkio.Hinta
            Pvm1 = Alkio.Pvm[1:17] 
        elif Alkio.Hinta > Suurin or Suurin < -10:
            Suurin = Alkio.Hinta
            Pvm2 = Alkio.Pvm[1:17]
    Halvinpaiva = datetime.datetime.strptime(Pvm1, "%Y-%m-%d %H:%M")
    Kalleinpaiva = datetime.datetime.strptime(Pvm2, "%Y-%m-%d %H:%M")
    # Lasketaan sähkön keskihinta.
    Keskiarvo = Summa / Koko
    # Lisätään analyysin tulokset olioon.
    Tulos = TULOKSET()
    Tulos.Pienin = Pienin
    Tulos.Ppaiva = Halvinpaiva
    Tulos.Suurin = Suurin
    Tulos.Spaiva = Kalleinpaiva
    Tulos.Khinta = Keskiarvo
    Tulos.Tunnit = Koko
    print("Tilastotietojen analyysi suoritettu " + str(Koko) + " alkiolle.")
    return Tulos

# Aliohjelma analysoi päivittäiset sähköjen hinnat.
def analysoiPaivat(Sahkolista):
    Paivalista = []
    Summa = 0
    Lkm = 0
    Edellinen = Sahkolista[0].Pvm[1:11]
    # Käydään listan kaikki paitsi viimeinen alkio läpi ja analysoidaan tiedot sekä lisätään uuteen oliolistaan.
    for Alkio in Sahkolista:
        Seuraava = Alkio.Pvm[1:11]
        Kulutus = float(Alkio.Hinta)

        if Edellinen == Seuraava:
            Summa = Summa + Kulutus
            Lkm = Lkm + 1

        else:
            Pvm = datetime.datetime.strptime(Edellinen, "%Y-%m-%d") 
            Paiva = Pvm.strftime("%d.%m.%Y")
            Tulos = TULOS()
            Tulos.Pvm = Paiva
            Tulos.PvmKeskiarvo = Summa / Lkm
            Paivalista.append(Tulos)
            Edellinen = Seuraava
            Summa = Kulutus
            Lkm = 1
    # Lisätään viimeinen olio listaan, koska silmukka ei huomioi sitä.
    Pvm = datetime.datetime.strptime(Edellinen, "%Y-%m-%d") 
    Paiva = Pvm.strftime("%d.%m.%Y")
    Tulos = TULOS()
    Tulos.Pvm = Paiva
    Tulos.PvmKeskiarvo = Summa / Lkm
    Paivalista.append(Tulos)
    PaivienLkm = len(Paivalista)
    print("Päivittäiset keskiarvot laskettu " + str(PaivienLkm) + " päivälle.")
    return Paivalista

# Aliohjelma kirjoittaa tiedostoon analyysin tulokset sekä tiedoston sisällön toisessa muodossa.
def kirjoitaTiedosto(Nimi, Tuloslista, Analyysi):
    try:
        Tiedosto = open(Nimi, "w", encoding="UTF-8")
        Tiedosto.write("Analyysin tulokset " + str(Analyysi.Tunnit) + " tunnilta ovat seuraavat:\n")
        Tiedosto.write("Sähkön keskihinta oli " + str(round(Analyysi.Khinta, 1)) + " snt/kWh.\n")
        Tiedosto.write("Halvimmillaan sähkö oli " + str(Analyysi.Pienin) + " snt/kWh, " + Analyysi.Ppaiva.strftime("%d.%m.%Y %H:%M.") + "\n")
        Tiedosto.write("Kalleimmillaan sähkö oli " + str(Analyysi.Suurin) + " snt/kWh, " + Analyysi.Spaiva.strftime("%d.%m.%Y %H:%M.") + "\n")
        Tiedosto.write("\n")
        Tiedosto.write("Päivittäiset keskiarvot (Pvm;snt/kWh):\n")
        for Arvo in Tuloslista:
            Tiedosto.write(Arvo.Pvm + ";" + str(round(Arvo.PvmKeskiarvo, 1)) + "\n")
        Tiedosto.close()
    except Exception:
        print("Tiedoston '" + Nimi + "' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    print("Tiedosto '" + Nimi + "' kirjoitettu.")
    return None

# Aliohjelma analysoi viikonpäivien hinnat.
def analysoiTilastot(Sahkolista):
    # Päivien sähköhintojen summalista. Ensimmäinen alkio on maanantai ja viimeinen sunnuntai.
    Sahkosummat = [0, 0, 0, 0, 0, 0, 0]
    # Päivien lukumäärälista.
    Paivalkm = [0, 0, 0, 0, 0, 0, 0]
    # Käydään listaa läpi ja lasketaan viikonpäivien sähköhintojen summat.
    for Alkio in Sahkolista: # Käydään listaa läpi ja lasketaan viikonpäivien sähköhintojen summat.
        Paiva = datetime.datetime.strptime(Alkio.Pvm[1:11], "%Y-%m-%d")
        Vluku = int(Paiva.weekday()) # Viikonpäivän numero
        Sahkosummat[Vluku] = Sahkosummat[Vluku] + Alkio.Hinta
        Paivalkm[Vluku] = Paivalkm[Vluku] + 1
    Tuloslista = []
    for i in range(len(Paivalkm)): # Lisätään tuloslistaan tulokset.
        if Paivalkm[i] != 0:
            Tuloslista.append(Sahkosummat[i] / Paivalkm[i])
        elif Paivalkm[i] == 0:
            Tuloslista.append(0)
    Tilastot = PAIVA()  # Tehdään olio ja lisätään jäsenmuuttujat
    Tilastot.MaHinta = Tuloslista[0]
    Tilastot.TiHinta = Tuloslista[1]
    Tilastot.KeHinta = Tuloslista[2]
    Tilastot.ToHinta = Tuloslista[3]
    Tilastot.PeHinta = Tuloslista[4]
    Tilastot.LaHinta = Tuloslista[5]
    Tilastot.SuHinta = Tuloslista[6]
    Sahkosummat.clear()
    Paivalkm.clear()
    Tuloslista.clear()
    return Tilastot

# Aliohjelma kirjoittaa tiedostoon viikonpäivien analyysin tulokset.
def kirjoitaTilastot(Nimi, Tilastot):
    try:
        Tiedosto = open(Nimi, "w", encoding="UTF-8")
        Tiedosto.write("Viikonpäivä;Keskimääräinen hinta snt/kWh\n")
        Tiedosto.write("Maanantai;{0:.1f}\n".format(Tilastot.MaHinta))   
        Tiedosto.write("Tiistai;{0:.1f}\n".format(Tilastot.TiHinta))
        Tiedosto.write("Keskiviikko;{0:.1f}\n".format(Tilastot.KeHinta))
        Tiedosto.write("Torstai;{0:.1f}\n".format(Tilastot.ToHinta))
        Tiedosto.write("Perjantai;{0:.1f}\n".format(Tilastot.PeHinta))
        Tiedosto.write("Lauantai;{0:.1f}\n".format(Tilastot.LaHinta))
        Tiedosto.write("Sunnuntai;{0:.1f}\n".format(Tilastot.SuHinta))
        Tiedosto.close()
    except Exception:
        print("Tiedoston '" + Nimi + "' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    
    print("Tiedosto '" + Nimi + "' kirjoitettu.")
    return None
######################################################################
# eof