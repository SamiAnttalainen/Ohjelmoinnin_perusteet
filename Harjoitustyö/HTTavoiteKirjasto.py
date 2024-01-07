######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Sami Anttalainen
# Päivämäärä: 11.12.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä HTTavoite.py

# Kirjastot
import datetime
import sys
import numpy

# Luokat
class SAHKO:
    Pvm = None
    Paiva = None
    Hinta = None
    Lasku = None

class TULOKSET:
    Pienin = None
    PieninPaiva = None
    Suurin = None
    SuurinPaiva = None
    KeskiHinta = None
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
def annaNimi(Syote): # Aliohjelma kysyy tiedoston nimen.
    Nimi = input(Syote) # Tiedoston nimi
    return Nimi

def lueTiedosto(Nimi, Lista): # Aliohjelma lukee annetun tiedoston ja tallentaa tiedoston rivit oliolistaan.
    Rivit = []
    try:
        Tiedosto = open(Nimi, "r", encoding="UTF-8") # Luetaan kaikki paitsi ensimmäinen rivi ja lisätään ne listaan.
        Rivi = Tiedosto.readline() # Ensimmäisen rivin ohitus.
        Rivi = Tiedosto.readline()[:-1]
        while len(Rivi) > 0:
            Rivit.append(Rivi)
            Rivi = Tiedosto.readline()[:-1]
        Tiedosto.close() # Suljetaan tiedosto.
    except Exception:
        print("Tiedoston '" + Nimi + "' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)

    for Rivi in Rivit: # Käydään listan alkiot läpi ja tallennetaan halutut tiedot oliolistaan.
        Sarakkeet = Rivi.split(";")
        Sahko = SAHKO()
        Sahko.Pvm = Sarakkeet[0]
        Sahko.Hinta = float(Sarakkeet[1])
        Lista.append(Sahko)
    print("Tiedosto '" + Nimi + "' luettu.")
    Rivit.clear()
    return Lista


def analysoiTulokset(Sahkolista): # Aliohjelma selvittää pienimmän ja suurimman hinnan sekä niiden päivämäärät. Samalla laskee myös sähkön keskihinnan. Lopuksi aliohjelma tallentaa tulokset Tulos-olioon.
    Pienin = Sahkolista[0].Hinta
    PvmMin = Sahkolista[0].Pvm[1:17]  # Pienin päivämäärä
    Suurin = Sahkolista[0].Hinta
    PvmMax = Sahkolista[0].Pvm[1:17] # Suurin päivämäärä
    Summa = 0
    Koko = len(Sahkolista) # Alkioiden lukumäärä.
    for Alkio in Sahkolista:
        Summa = Summa + float(Alkio.Hinta)
        if Alkio.Hinta < Pienin:
            Pienin = Alkio.Hinta
            PvmMin = Alkio.Pvm[1:17] 
        elif Alkio.Hinta > Suurin:
            Suurin = Alkio.Hinta
            PvmMax = Alkio.Pvm[1:17]
    Halvinpaiva = datetime.datetime.strptime(PvmMin, "%Y-%m-%d %H:%M")
    Kalleinpaiva = datetime.datetime.strptime(PvmMax, "%Y-%m-%d %H:%M")
    Keskiarvo = Summa / Koko # Sähkön keskihinta.

    Tulos = TULOKSET() # Lisätään analyysin tulokset olioon.
    Tulos.Pienin = Pienin
    Tulos.PieninPaiva = Halvinpaiva
    Tulos.Suurin = Suurin
    Tulos.SuurinPaiva = Kalleinpaiva
    Tulos.KeskiHinta = Keskiarvo
    Tulos.Tunnit = Koko
    print("Tilastotietojen analyysi suoritettu " + str(Koko) + " alkiolle.")
    return Tulos

def analysoiPaivat(Sahkolista, PaivaLista): # Aliohjelma analysoi päivittäiset sähköjen hinnat.
    Summa = 0
    Lkm = 0
    Edellinen = Sahkolista[0].Pvm[1:11]
    
    for Alkio in Sahkolista: # Käydään listan kaikki alkiot läpi ja analysoidaan sekä lisätään tiedot uuteen oliolistaan.
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
            PaivaLista.append(Tulos)
            Edellinen = Seuraava
            Summa = Kulutus
            Lkm = 1

    Pvm = datetime.datetime.strptime(Edellinen, "%Y-%m-%d") # Lisätään viimeinen olio listaan, koska silmukka ei huomioi sitä.
    Paiva = Pvm.strftime("%d.%m.%Y")
    Tulos = TULOS()
    Tulos.Pvm = Paiva
    Tulos.PvmKeskiarvo = Summa / Lkm
    PaivaLista.append(Tulos)
    PaivienLkm = len(PaivaLista)
    print("Päivittäiset keskiarvot laskettu " + str(PaivienLkm) + " päivälle.")
    return PaivaLista

def kirjoitaTiedosto(Nimi, Tuloslista, Analyysi): # Aliohjelma kirjoittaa tiedostoon analyysin tulokset sekä tiedoston sisällön toisessa muodossa.
    try:
        Tiedosto = open(Nimi, "w", encoding="UTF-8")
        Tiedosto.write("Analyysin tulokset " + str(Analyysi.Tunnit) + " tunnilta ovat seuraavat:\n")
        Tiedosto.write("Sähkön keskihinta oli " + str(round(Analyysi.KeskiHinta, 1)) + " snt/kWh.\n")
        Tiedosto.write("Halvimmillaan sähkö oli " + str(Analyysi.Pienin) + " snt/kWh, " + Analyysi.PieninPaiva.strftime("%d.%m.%Y %H:%M.") + "\n")
        Tiedosto.write("Kalleimmillaan sähkö oli " + str(Analyysi.Suurin) + " snt/kWh, " + Analyysi.SuurinPaiva.strftime("%d.%m.%Y %H:%M.") + "\n")
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

def analysoiTilastot(SahkoLista): # Aliohjelma analysoi viikonpäivien hinnat.
    SahkoSummat = [0, 0, 0, 0, 0, 0, 0] # Päivien sähköhintojen summalista. Ensimmäinen alkio on maanantai ja viimeinen sunnuntai.
    PaivaLkm = [0, 0, 0, 0, 0, 0, 0] # Päivien lukumäärälista.
    for Alkio in SahkoLista: # Käydään listaa läpi ja lasketaan viikonpäivien sähköhintojen summat.
        Paiva = datetime.datetime.strptime(Alkio.Pvm[1:11], "%Y-%m-%d")
        Vluku = int(Paiva.weekday()) # Viikonpäivän numero
        SahkoSummat[Vluku] = SahkoSummat[Vluku] + Alkio.Hinta
        PaivaLkm[Vluku] = PaivaLkm[Vluku] + 1
    TulosLista = []
    for i in range(len(PaivaLkm)): # Lisätään tuloslistaan tulokset.
        if PaivaLkm[i] != 0:
            TulosLista.append(SahkoSummat[i] / PaivaLkm[i])
        elif PaivaLkm[i] == 0:
            TulosLista.append(0)
    Tilastot = PAIVA()  # Tehdään olio ja lisätään jäsenmuuttujat
    Tilastot.MaHinta = TulosLista[0]
    Tilastot.TiHinta = TulosLista[1]
    Tilastot.KeHinta = TulosLista[2]
    Tilastot.ToHinta = TulosLista[3]
    Tilastot.PeHinta = TulosLista[4]
    Tilastot.LaHinta = TulosLista[5]
    Tilastot.SuHinta = TulosLista[6]
    SahkoSummat.clear()
    PaivaLkm.clear()
    TulosLista.clear()
    return Tilastot

def kirjoitaTilastot(Nimi, Tilastot): # Aliohjelma kirjoittaa tiedostoon viikonpävien analyysin tulokset.
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

def lueData(Nimi, Oliolista): # Aliohjelma lukee kulutusdatan ja lisää kulutustiedot oliolistan tietoihin.   
    Rivit = [] # Lista, johon tiedoston rivit tallennetaan.
    Sanakirja = {} # Sanakirja, johon tallennetaan rivit-listan tiedot.
    Summa = 0 # Laskun kokonaissumma sentteinä.
    try:
        Tiedosto = open(Nimi, "r", encoding="UTF-8")
        Tiedosto.readline()
        Rivi = Tiedosto.readline()[:-1]
        while len(Rivi) > 0:
            Rivit.append(Rivi)
            Rivi = Tiedosto.readline()[:-1]
        Tiedosto.close()
    except Exception:
        print("Tiedoston '" + Nimi + "' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)

    for Rivi in Rivit:
        Sarakkeet = Rivi.split(";")
        Paivamaara = Sarakkeet[0]
        if Paivamaara not in Sanakirja: # Jos päivääärä ei ole sanakirjassa, niin lisätään se ja sen kulutusarvo.
            Sanakirja[Sarakkeet[0]] = float(Sarakkeet[1]) + float(Sarakkeet[2])
        elif Paivamaara in Sanakirja: # Jos päivämäärä on jo sanakirjassa, niin lisätään kyseiseen päivään kulutusarvo.
            Sanakirja[Sarakkeet[0]] += float(Sarakkeet[1]) + float(Sarakkeet[2])

    for Olio in Oliolista:
        Pvm = datetime.datetime.strptime(Olio.Pvm[1:17], "%Y-%m-%d %H:%M") # Muutetaan oliolistan aikaleimat sanakirjan aikaleimojen muotoon.
        Paiva = "{0}.{1}.{2} {3}:{4}".format(Pvm.day, Pvm.month, Pvm.year, Pvm.hour, Pvm.strftime("%M"))
        if Paiva in Sanakirja: # Lisätään olioon tiedot
            Olio.Paiva = Pvm
            Olio.Lasku = Olio.Hinta * Sanakirja[Paiva]
            Summa = Summa + Olio.Lasku

    Euroina = Summa / 100 # Muutetaan sentit euroiksi.
    print("Tiedosto '" + Nimi + "' luettu.")
    print("Hinta- ja kulutustiedot yhdistetty. Lasku on yhteensä {0:.2f} euroa.".format(Euroina))
    Rivit.clear()
    Sanakirja.clear()
    return Oliolista

def analysoiTuntilaskut(Oliolista, Matriisi): # Aliohjema analysoi oliolistan datan matriisiin.
    for Olio in Oliolista:
        if Olio.Paiva != None:
            Rivi = int(Olio.Paiva.strftime("%#W"))
            Sarake = int(Olio.Paiva.hour)
            Matriisi[Rivi, Sarake] += Olio.Lasku
    Sarakesumma = Matriisi.sum(axis=0)
    Matriisi = numpy.vstack([Matriisi, Sarakesumma]) # Lisätään sarakesumma matriisin pohjalle.
    Rivisumma = Matriisi.sum(axis=1)
    Matriisi = numpy.column_stack([Matriisi, Rivisumma]) # Lisätään rivisumma matriisiin oikealle puolelle.
    print("Tuntikohtaiset hinnat analysoitu.")
    return Matriisi

def kirjoitaData(Nimi, Matriisi): # Aliohjelma kirjoittaa tiedostoon matriisin sisällön.
    try:
        Tiedosto = open(Nimi, "w", encoding="UTF-8")
        Tiedosto.write("Viikko\Tunti;0;1;2;3;4;5;6;7;8;9;10;11;12;13;14;15;16;17;18;19;20;21;22;23;YHT")
        for Rivi in range(55):
            if 0 <= Rivi < 54:
                Tiedosto.write("\n")
                Tiedosto.write("Vko " + str(Rivi) + ";")
            elif Rivi == 54:
                Tiedosto.write("\n")
                Tiedosto.write("YHT;")
            for Sarake in range(25):
                if 0 <= Sarake < 24:
                    Tiedosto.write("{0:.1f};".format(Matriisi[Rivi, Sarake]))
                elif Sarake == 24:
                    Tiedosto.write("{0:.1f}".format(Matriisi[Rivi, Sarake]))
        Tiedosto.write("\n")
        Tiedosto.close()
    except Exception:
        print("Tiedoston '" + Nimi + "' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    print("Tiedosto '" + Nimi + "' kirjoitettu.")
    return None
######################################################################
# eof
