################################################################################
#################   exit game  #################################################
################################################################################


#import all the functions
import pygame, sys,os, time
from pygame.locals import * 
from pygame.color import THECOLORS
import sys
import platform,os  
if platform.system()=="Windows":           
    os.environ['SDL_VIDEODRIVER']='windib'
pygame.init()
#initalize pygame
pygame.init() 


#set the window size and get the mode
WINSIZE = pygame.display.set_mode((700, 700))
SCREEN = pygame.display.get_surface()


#function exit
def EXIT():
    
    #fill the screen white
    SCREEN.fill(THECOLORS["white"])
    
    #set the word font
    WORD = pygame.font.SysFont("none", 60)
    
    #display the word
    SCREEN.blit(WORD.render("Good Bye", 1, THECOLORS["red"]), (250,50))
    
    #update the screen
    pygame.display.flip()
    
    #delay for 2 sec
    pygame.time.delay(2000)
    
    #exit the game
    pygame.quit()
    sys.exit()
    