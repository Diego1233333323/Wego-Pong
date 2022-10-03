import pygame


#Inicio del Pygame
pygame.init()


#altura
screen_width = 800
screen_height = 800


#tamaño_de_variable
size = (screen_width, screen_height)

#Mostracion
screen = pygame.display.set_mode( size )

#Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
















