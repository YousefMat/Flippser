"""Detta program kopplas ihop med ett GUI i pygame som har knappar som motsvarar inputs,
spelloopar utförs i andra filer för få rätt sannolikheter för myntkasten"""
import random

klave = 0 #Antal kast som landar klave per gissning
krona = 0 #antal kast som landar krona per gissning
kast_kvar = 100 #Antal kast per spelrunda
korrekt = 0 #Antal korrekt per spelrunda

def laglig(): # Ett vanligt mynt
    return random.choice(["krona","klave"]) #Ger tillbaka resultatet ifall det är krona eller klave

def olaglig(): # Ett fusk mynt som har 75% chans att få krona
    flip = random.random()
    if flip > 0.25:
        mynt = "krona"
    else:
        mynt = "klave"
    return mynt #Ger tillbaka resultatet ifall det är krona eller klave

def ny_gubbe(): # Varje gång funktionen kallas genereras en ny gubbe med sin respektive fusksannolikhet
    personer = {"Orvar":0.35, "Pernilla":0.4, "Alejandro":0.5, "Binne":0.55, "Marsell":0.6} #Gubbens namn och sannolikhet att fuska
    fusk = list(personer.keys())
    nuv_gubbe = random.choice(fusk) #Nuvarande gubbe
    nuv_fusk =  personer.get(nuv_gubbe) #Nuvarande fusksannolikhet
    avgörare = random.random() #Variabel (float 0-1) som avgör ifall spelaren ska fuska
    return nuv_gubbe, nuv_fusk, avgörare

nuv_gubbe, nuv_fusk, avgörare = ny_gubbe() #Gubben kallas här för att påbörja spelloopen

def main(fråga): #Självaste spellogiken som kräver "fråga" som argument för att sätta igång

    global krona, klave, avgörare, nuv_fusk, nuv_gubbe, kast_kvar, korrekt #Variabler som stannar utanför för att undivka problem med spellopen

    if type(fråga) is int: #Ser ifall "fråga" är en siffra
        for i in range(int(fråga)): #Börjar kasta mynt beroende på talet som angivits
            if avgörare > nuv_fusk: #Ifall spelaren fuskar körs denna kallas fuskmynt funktionen
                variant = olaglig() #Här kallas fuskmyntet och kastet
                if variant == "krona": #Ifall resultatet är krona för detta kast så ökar antalet kast som landat krona med ett
                    krona += 1
                if variant == "klave": #Ifall resultatet är krona för detta kast så ökar antalet kast som landat klave med ett
                    klave += 1
            if avgörare <= nuv_fusk: #Samma logik som i de övre nästlade if-satserna fast med det vanliga myntet
                variant = laglig()
                if variant == "krona":
                    krona += 1
                if variant == "klave":
                    klave += 1
    else: #Ifall "fråga" inte är en siffra så antar spelet att spelaren gissar ifall gubben fuskar eller ej
        if fråga == "f" and avgörare > nuv_fusk: #Spelare anklagar inte för fusk, gubben fuskade inte
            kast_kvar += 15 #Antal kast för spelrundan ökar med 15
            korrekt += 1 #Antal korrekt gissningar ökar med ett

        if fråga == "f" and avgörare <= nuv_fusk: #Spelare anklagar felaktigt för fusk, gubben fuskade inte
            kast_kvar -= 30 #Antal kast för spelrundan minskar med 30

        if fråga == "h" and avgörare <= nuv_fusk: #Spelare anklagar korrekt för fusk, gubben fuskade inte
            kast_kvar += 15 #Antal kast för spelrundan ökar med 15
            korrekt += 1 #Antal korrekt gissningar ökar med ett

        if fråga == "h" and avgörare > nuv_fusk: #Spelare anklagar inte för fusk, gubben fuskade
            kast_kvar -= 30 #Antal kast för spelrundan minskar med 30
        klave = 0 #Antalet krona och klave återställs till 0 eftersom en ny gubbe skall kallas
        krona = 0
        nuv_gubbe, nuv_fusk, avgörare = ny_gubbe() #Ny gubbe kallas och spelaren kan börja gissa för den nya gubben
