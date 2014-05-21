###################################
############## Main menu ##########
###################################


#All the imports
import pygame, sys,os, time
from pygame.locals import * 
from pygame.color import THECOLORS
import platform, os
import random
import Level
import Exit_Pygame
import Def
import Control
import SCORE_DISPLAY
if platform.system() == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'
    
    
#initalize the pygame
pygame.init() 

#Set all screen size and get the screen serface
window = pygame.display.set_mode((700, 700))
screen = pygame.display.get_surface()


#the  main function
def Main(SONG_INFO):
    
    
    #all the background and font of the words
    background = pygame.image.load('image/Main.jpg').convert()
    Start_button = pygame.image.load('image/Start_button.png').convert_alpha()
    Control_Button= pygame.image.load('image/Control_Button.png').convert_alpha()
    High_Score_Button = pygame.image.load('image/High_Score_Button.png').convert_alpha()
    ACCEPT = pygame.image.load('image/ACCEPT.png').convert_alpha()
    ACCEPT_ON = pygame.image.load('image/ACCEPT_ON.png').convert_alpha()
    pygame.display.set_caption('MEGA MUSIC KEY-BUSTER')
    WORD = pygame.font.SysFont("none", 50)
    WORD2 = pygame.font.SysFont("none", 30)
    
    
    #this will randomly creat a mission, player will have 50% chance of reciving a mission
    MISSION = random.randint(0,1)
    
    #blit the background
    screen.blit(background,(0,0))
    
    
    #Up dates the screen
    pygame.display.flip()
    
    #delay
    pygame.time.delay(500)
        
    
    #Main loop
    while True:
        
        
        #Get the event of the screen
        events = pygame.event.get( )  
        for e in events:
            #if the user click quit
            if e.type == QUIT:
                
                #import def and from def, it will exit pygame and sys
                Exit_Pygame.EXIT()
            #get the position of mouse
            pos = pygame.mouse.get_pos()
            butt = pygame.mouse.get_pressed()
            x=pos[0]
            y=pos[1]
            
            
            #if the mouse is within the mouse
            if x > 267 and x < 437 and y > 464 and y < 634:
                
                #blit the image onto the screen
                screen.blit(Start_button,(252,450))
                
                #if the button is pressed down
                if butt[0]==1:
                    
                    #goes to next page
                    Def.NORMAL(SONG_INFO)
                    
                    
            ##########   EVERYTHING IS THE SAME, EXCEPT for the location and page ############
            elif x > 64 and x < 236 and y > 464 and y < 634 and (butt[0]==0 or butt[0]==1):
                screen.blit(Control_Button,(52,450))
                if butt[0]==1:
                    total = Control.Control(SONG_INFO)
                    
            elif x > 466 and x < 634 and y > 464 and y < 634 and (butt[0]==0 or butt[0]==1):
                screen.blit(High_Score_Button,(452,450))
                if butt[0]==1:
                    SCORE_DISPLAY.SCORE_DISPLAY(SONG_INFO)
            elif x > 514 and x < 685 and y > 218 and y < 383 and MISSION == 0:
                screen.blit(ACCEPT_ON,(500,200))
                if butt[0] == 1:
                    Def.RANDOM_MISSION(SONG_INFO)
            else:
                
                
                # blit the background
                screen.blit(background,(0,0))
                
                #if the mission is 0, this will show up
                if MISSION == 0:
                    
                    #display the message
                    MISSION_NAME = 'New Challenge, do you accept?'
                    
                    #blit the message
                    screen.blit(WORD2.render(MISSION_NAME, 1, THECOLORS["red"]), (10,280))
                    
                    #Blit the image ACCEPT
                    screen.blit(ACCEPT,(500,200))
                    
                    
        #said welcome to the name that player has entered
        NAME = 'Welcome DJ '+SONG_INFO[0]
        
        #gives the current score
        SCORE = 'Your current EXP is: '+str(SONG_INFO[1])
        
        #info
        Info = 'If you dont know the keys, go to control'
        
        #blit the word and name
        screen.blit(WORD.render(Info, 1, THECOLORS["green"]), (10,400))
        screen.blit(WORD.render(NAME, 1, THECOLORS["green"]), (220,100))
        screen.blit(WORD.render(SCORE, 1, THECOLORS["green"]), (220,150))
        
        
        
        #update the screen
        pygame.display.flip()