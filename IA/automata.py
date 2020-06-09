#!python3

import sys,pygame
import matplotlib.pyplot as plt
import  numpy as np
import time



pygame.init()

bg=25,25,25

nY_cell = 60
nX_cell = 60

size = width, height =600 ,600 

dimX = (width-1)/nX_cell

dimY = (height-1)/nY_cell

screen = pygame.display.set_mode(size)



gamestate = np.zeros((nX_cell,nY_cell))
# gamestate = np.random.randint(0,2,((nX_cell,nY_cell)))


gamestate[21,21] = 1
gamestate[22,22] = 1
gamestate[22,23] = 1
gamestate[21,23] = 1
gamestate[20,23] = 1

# print(gamestate)

while True :

    new_gamestate = np.copy(gamestate)

    screen.fill(bg)
    
    # se hace una cuadricula
    for y in range(0,nY_cell):
        for x in range(0,nX_cell):
            # se hara que dicha cuadricula sea toroidal
            n_neigh =gamestate[(x-1) % nX_cell ,(y-1) % nY_cell]+\
                     gamestate[(x) % nX_cell ,(y-1) % nY_cell]+\
                     gamestate[(x+1) % nX_cell ,(y-1) % nY_cell]+\
                     gamestate[(x-1) % nX_cell ,(y) % nY_cell]+\
                     gamestate[(x+1) % nX_cell ,(y) % nY_cell]+\
                     gamestate[(x-1) % nX_cell ,(y+1) % nY_cell]+\
                     gamestate[(x) % nX_cell ,(y+1) % nY_cell]+\
                     gamestate[(x+1) % nX_cell ,(y+1) % nY_cell]\
                              

            # celula muerta con tre vecinas vivas ...nace

            if gamestate[x,y] == 0 and n_neigh == 3:
                new_gamestate[x,y]=1
                # una celula viva con dos o tres vivas sigue viva en otro caso muere
            elif gamestate[x,y] ==1 and (n_neigh < 2 or n_neigh > 3) :
                new_gamestate[x,y] = 0
            

            # np.sum(gamestate[x-1:x+2,y-1:y+2] -  gamestate[x,y] )

            poly = [
                ((x)* dimX,(y)* dimY),
                ((x+1)* dimX,(y)* dimY),
                ((x+1)* dimX,(y+1)* dimY),
                ((x)* dimX,(y+1)* dimY)

             
                
            ]
            
            
            
            
            pygame.draw.polygon(screen,(128,128,128),poly,int(abs(1-new_gamestate[x,y])))    
            
    gamestate = new_gamestate

    # time.sleep(0.1)
    # plt.matshow(gamestate)
    # plt.show()

    # time.sleep(1)

    # plt.close()
        
    
    pygame.display.flip()







