# gameOfLife
import pygame
import numpy as np
import matplotlib.pyplot as plt
import time



pygame.init()

size = width, height = 700, 700

nXC = 70
nYC = 70

dimCW = width / nXC
dimCH = height / nYC

bg = 25, 25, 25

screen = pygame.display.set_mode(size)
screen.fill(bg)

# gameState = np.random.randint(0,2,(nXC,nYC))
gameState = np.zeros((nXC, nYC))
gameState[20,20] = 1
gameState[21,20] = 1
gameState[22,20] = 1
gameState[23,20] = 1
gameState[24,20] = 1

gameState[20,22] = 1
gameState[24,22] = 1

gameState[24,20] = 1
gameState[24,21] = 1
gameState[24,22] = 1
gameState[24,23] = 1
gameState[24,24] = 1

#Control de la ejecucion del juego
pauseExect = False


while 1:
    new_gameState = np.copy(gameState)
    screen.fill(bg)
    time.sleep(0.001)

    #Registramos eventos de teclado y raton
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.KEYDOWN:
            pauseExect = not pauseExect

        mouseClick = pygame.mouse.get_pressed()

        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
            new_gameState[celX, celY] = not mouseClick[2]

    for y in range(0, nYC):
        for x in range(0, nXC):
            if not pauseExect:
                n_neigh = gameState[(x-1) % nXC,(y-1) % nYC] +\
                          gameState[(x) % nXC,(y-1) % nYC] +\
                          gameState[(x + 1) % nXC,(y-1) % nYC] +\
                          gameState[(x-1) % nXC,(y) % nYC] +\
                          gameState[(x + 1) % nXC,(y) % nYC] +\
                          gameState[(x-1) % nXC,(y+1) % nYC] +\
                          gameState[(x) % nXC,(y+1) % nYC] +\
                          gameState[(x + 1) % nXC,(y+1) % nYC]

                # Una célula muerta con exactamente 3 células vecinas vivas "nace" (es decir, al turno siguiente estará viva).
                if gameState[x, y] == 0 and n_neigh == 3:
                    new_gameState[x, y] = 1
                elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    new_gameState[x, y] = 0

            # Una célula viva con 2 o 3 células vecinas vivas sigue viva, en otro caso muere (por "soledad" o "superpoblación").

            poly = [((x)*dimCW,(y)*dimCH),
                    ((x+1)*dimCW,(y)*dimCH),
                    ((x+1)*dimCW,(y+1)*dimCH),
                    ((x)*dimCW,(y+1)*dimCH)]
            if new_gameState[x, y] == 0:
                pygame.draw.polygon(screen,(128,128,128),poly,1)
            else:
                pygame.draw.polygon(screen,(255,255,255),poly,0)

    gameState = np.copy(new_gameState)

    pygame.display.flip()






