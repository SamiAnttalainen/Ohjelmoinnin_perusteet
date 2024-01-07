######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Sami Anttalainen
# Päivämäärä: 1.11.2022
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä L08T2.py

#Kiintoarvo
VERSIO = 1.0

# Tilavuuden syöttö
def annaTilavuus():
    Tilavuus = float(input("Anna muunnettava tilavuus desimaalilukuna: "))
    return Tilavuus

# Muunnosfunktiot
def litraGalloniksi(Litra):
    Tilavuus = Litra / 3.79
    return Tilavuus

def litraPintiksi(Litra):
    Tilavuus = Litra / 0.47
    return Tilavuus

def litraCupiksi(Litra):
    Tilavuus = Litra / 0.24
    return Tilavuus

def litraFluidiksi(Litra):
    Tilavuus = Litra / 0.0296
    return Tilavuus

def gallonLitroiksi(Gallon):
    Tilavuus = Gallon * 3.79
    return Tilavuus

def pintLitroiksi(Pint):
    Tilavuus = Pint * 0.47
    return Tilavuus

def cupLitroiksi(Cup):
    Tilavuus = Cup * 0.24
    return Tilavuus

def fluidLitroiksi(Fluid):
    Tilavuus = Fluid * 0.0296
    return Tilavuus

# eof
