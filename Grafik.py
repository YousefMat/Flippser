"""Spelet som sätter ihop knapp-file och spel-filen samt pygame
för att spelet skall visas grafiskt och kunna spelas"""
import pygame, knapp, spel

pygame.init() #Pygame initieras

# Bredd och höjd på spelfönster i pixlar
width = 800
height = 600


run = True #Ser till att pygame är igång
spelloop = True #spelogiken spelas så länge denna är True, annars spelas en "spela igen?" skärm

screen = pygame.display.set_mode((width, height)) #Fixar spelfönstret
pygame.display.set_caption("Flippser") #Byter spelfönstrets namn till "Flippser"

#Laddar lokala filer som kan användas som bilder i spelet
en_knp = pygame.image.load("en_knp.png").convert_alpha()
fem_knp = pygame.image.load("fem_knp.png").convert_alpha()
hdr_knp = pygame.image.load("hdr_knp.png").convert_alpha()
fsk_knp = pygame.image.load("fsk_knp.png").convert_alpha()
ja_knp = pygame.image.load("ja_knp.png").convert_alpha()
nej_knp = pygame.image.load("nej_knp.png").convert_alpha()

#Definierar knapparnas egenskaper men ritar inte de
en_knapp = knapp.Knapp(150, 350, en_knp, 0.8)
fem_knapp = knapp.Knapp(450, 350, fem_knp, 0.8)
hederlig_knapp = knapp.Knapp(150, 475, hdr_knp, 0.8)
fusk_knapp = knapp.Knapp(450, 475, fsk_knp, 0.8)
ja_knapp = knapp.Knapp(175, 150, ja_knp, 0.8)
nej_knapp = knapp.Knapp(425, 150, nej_knp, 0.8)

def rita_annat(): # Ritar användbar information under spelets gång
    #Olika typsnitt i olika storlekar för texten att skrivas i
    font = pygame.font.SysFont("shrikhand", 32)
    font2 = pygame.font.SysFont("shrikhand", 25)

    #Text för antal kast kvar per spelrunda
    kast_kvar_text = font.render("Kast kvar: " + str(spel.kast_kvar), True, (0, 0, 0))
    screen.blit(kast_kvar_text, (20, 10))

    #Text för antal krona per gissning
    krona_text = font2.render("Krona: " + str(spel.krona), True, (0, 0, 0))
    screen.blit(krona_text, (150, 315))

    #Text för antal klave per gissning
    klave_text = font2.render("Klave : " + str(spel.klave), True, (0, 0, 0))
    screen.blit(klave_text, (150, 285))

    #Antal korrekta gissningar per spelrunda
    korrekt_text = font2.render("Antal rätt: " + str(spel.korrekt), True, (0, 0, 0))
    screen.blit(korrekt_text, (535, 315))

def gameover(): #När spelaren har förlorat spelas denna skärm som frågar ifall spelaren vill spela igen
    global spelloop, run
    screen.fill((0,108,180)) #Byter bakgrundsfärg på skärmen
    font = pygame.font.SysFont("shreikhand", 32) #Typsnitt för texten
    text = font.render("Du förlorade, vill du spela igen?", True, (255, 255, 255)) #Laddar in textrutan
    #Centrerar textrutan i x-led
    textRect = text.get_rect()
    textRect.center = (width//2, 100)
    screen.blit(text, textRect)
    #Ritar som kan besvara "spela igen?" frågan
    if ja_knapp.rita(screen): #Ritar knappen, kollar ifall den trycks
        spel.kast_kvar = 100 #Återställs korrekta gissningar till 0
        spel.korrekt = 0 #Spelaren får tillbaka sina 100 kast
        spelloop = True #Spellogiken påbörjas igen
    if nej_knapp.rita(screen): #Ritar knappen, kollar ifall den trycks
        run = False #Pygame avslutas
    pygame.display.update() #Updaterar skärmen så att allt som ritats visas på skärmen

def spelet(): #Kopplar logiken i "spel" med knapparna som ritas på skärmen
    global spelloop
    screen.fill((202, 230, 241)) #Bakgrundsfärg för spelet
    if en_knapp.rita(screen): #Ifall knappen trycks kastas ett mynt
        spel.main(1) #argumentet 1 används i spellogiken
        spel.kast_kvar -= 1 #Antal kast kvar minskar med 1
    if fem_knapp.rita(screen): #Ifall knappen trycks kastas fem mynt
        spel.main(5) #argumentet 5 används i spellogiken
        spel.kast_kvar -= 5 #Antal kast kvar minskar med 5
    if fusk_knapp.rita(screen): #Ifall knappen trycks anklagas gubben för fusk
        spel.main("f") #argumentet f används i spellogiken
    if hederlig_knapp.rita(screen):#Ifall knappen trycks anklagas gubben inte för fusk
        spel.main("h") #argumentet h används i spellogiken
    if spel.kast_kvar < 0: #När spelaren kast kvar är mindre änd 0 så är spelrundan över
        spelloop = False
        spel.klave = 0
        spel.krona = 0
    rita_annat() #Avnändbar info ritas på skärmen
    pygame.display.update() #Skärmen uppdateras för att visa uppdaterad användbar info

while run: #Programloopen som ser till att rätt skärm visas vid rätt tillfälle
    if spelloop is True: #Spelet spelas
        spelet()
    if spelloop is False: #Spela igen? skärmen visas, ifall spelaren väljer "nej" avslutas programloopen
        gameover()

    #Kollar ifall stäng fönster knappen har klickats och avlutar programloopen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit() #Avlutar programmet
