import pygame
import GraphicsUtil as Graph


# update the game
def updateGame():
	# if you want to assign a global variable in Python, you need to let Python know
    pass

# A method that keeps track of the block graphics
#def 


# A method that does all the drawing for you.
def draw(screen):
    # setup a differnt background, 
    # screen.fill(Graph.BLACK)
    # draw the graph 
    screen.blit(Graph.bckgdSurface, (0,0))
    screen.blit(Graph.grid, (0, 0))

    screen.blit(Graph.scoreSurface, (290, 200))