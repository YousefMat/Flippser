import pygame


class Knapp():

    """Knapp klassen bildar en interaktiv ruta som är anpassad
    till en bilds bredd och höjd och sedan anpassar storleken"""

    def __init__(self, x, y, bild, skala):
        bredd = bild.get_width()
        höjd = bild.get_height()
        self.bild = pygame.transform.scale(bild, (int(bredd * skala), int(höjd * skala)))
        self.rect = self.bild.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def rita(self, skärm):
        action = False
        #Får musens position
        pos = pygame.mouse.get_pos()

        #kollar ifall musen är över knappen och ifall den är klickad
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        #Ser till att knappen kan klickas igen efter att musen har avslutat sitt klick
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #Ritar knappen på skärmen
        skärm.blit(self.bild, (self.rect.x, self.rect.y))

        return action
