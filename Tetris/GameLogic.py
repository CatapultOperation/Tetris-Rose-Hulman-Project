import pygame
import random
import GraphicsUtil as Graph

import block_class
from block_class import Block

# import squareBlock
from squareBlock import squareBlock

# import lineBlock
from lineBlock import lineBlock

# import lBlock
from lBlock import lBlock

# import squiggleBlock
from squiggleBlock import squiggleBlock

# import Tblock
from Tblock import TBlock

#import squiggleBlock2
from squiggleBlock2 import squiggleBlock2

from lBlock2 import lBlock2

#list of tetraminos
# tetraminoList = [squiggleBlock, squiggleBlock2, squiggleBlock, lBlock, 
#     lBlock2, lBlock, squareBlock, lineBlock, TBlock]
tetraminoList = [lineBlock, squareBlock]



BLACK = (0,0,0)
GREEN = (0, 255, 0)
x = 5
y = 0
ychange = 0
score = 0


def randomeBlock():
    b = tetraminoList[random.randint(0, len(tetraminoList)-1)]
    return b()

# currentblock = randomeBlock()
currentblock = lineBlock()
    
    
# update the game
def updateGame():
	# if you want to assign a global variable in Python, you need to let Python know
    global x,y, ychange
    ychange += 1
    if ychange == 4:
        y+=1
        ychange = 0
    if isinstance(currentblock, squareBlock):    
        if Graph.TGrid[y+2][x] != 0 or Graph.TGrid[y+2][x+1] != 0 or y == 15:
            Graph.TGrid[y+1][x] = 1
            Graph.TGrid[y+1][x+1] = 1
            Graph.TGrid[y][x+1] = 1
            Graph.TGrid[y][x] = 1
    if isinstance(currentblock, lineBlock): 
        if currentblock.rotate%2==0:   
            if Graph.TGrid[y+4][x] != 0 or y == 13:
                Graph.TGrid[y+3][x] = 2
                Graph.TGrid[y+2][x] = 2
                Graph.TGrid[y+1][x] = 2
                Graph.TGrid[y][x] = 2
        else:
            if Graph.TGrid[y+1][x+3] !=0 or Graph.TGrid[y+1][x+2]!=0 or Graph.TGrid[y+1][x+1]!=0 or Graph.TGrid[y+1][x] != 0 or y == 16:
                Graph.TGrid[y][x+3] = 2
                Graph.TGrid[y][x+2] = 2
                Graph.TGrid[y][x+1] = 2
                Graph.TGrid[y][x] = 2
    
    
   
   
# A method that flips the tetraminos
def rotate(tetramino):
    tetramino.surface = pygame.transform.rotate(tetramino.surface, 90)
    tetramino.rotate += 1
    
# A method that keeps track of the block graphics
#def 


# A method that does all the drawing for you.
def draw(screen):
    global currentblock, y, x
    # setup a differnt background, 
    if Graph.TGrid[y][x] != 0 or y == 16:
        y = 0
        x = 5
        currentblock = randomeBlock()
    else:
        screen.fill(Graph.BLACK)
    screen.blit(Graph.grid, (0, 0))
    currentblock.draw(screen, x, y)

    for i in range (len(Graph.TGrid)):
        for j in range (len(Graph.TGrid[i])):
            loc = Graph.TGrid [i][j]
            if loc != 0:
                if loc == 1:
                    b = Block(25,25, (255,0,0), j, i)
                    b.indBlock(screen,block_class.yellowBlock)
                if loc == 2:
                    b = Block(25,25, (255,0,0), j, i)
                    b.indBlock(screen,block_class.tealBlock)

    # Clear a row when complete
    for i in Graph.TGrid:
        global score
        if 0 not in i:
            Graph.TGrid.remove(i)
            Graph.TGrid.insert(0,[0,0,0,0,0,0,0,0,0,0])
            score += 1
                


    # Sq1 = squareBlock(200,200)
    # Sq1.draw(screen)
    
    # Line1 = lineBlock (100,100)
    # Line1.draw(screen)
    
        
       
    
    
    # Sq1 = squareBlock(0,0)
    # Sq1.draw(screen)
    

    #Draws Boxes On The Side
    screen.blit(Graph.scoreSurface, (290, 400))
    
    screen.blit(Graph.scoreWordSurface, (290, 330))
    
    screen.blit(Graph.nextSurface, (290, 50))

    screen.blit(Graph.nextShowSurface, (290, 115))




