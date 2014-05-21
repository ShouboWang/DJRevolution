##################
######level#######
##################



#All the imports
import pygame, sys,os, time
from pygame.locals import * 
from pygame.color import THECOLORS
import platform, os
import Exit_Pygame
import Song_Selection

if platform.system() == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'

#Initalize pygame
pygame.init() 


#set the window size,font,get surface,read file,blit the word onto the screen
WINSIZE = pygame.display.set_mode((700, 700))
SCREEN = pygame.display.get_surface()

BACKGROUND = pygame.image.load('image/Level_Sel.jpg')
EASY = pygame.image.load('image/Easy_Button.png').convert_alpha()
EASY_ON = pygame.image.load('image/Easy_Button_ON.png').convert_alpha()
NORMAL = pygame.image.load('image/Normal_Button.png').convert_alpha()
NORMAL_ON = pygame.image.load('image/Normal_Button_ON.png').convert_alpha()
HARD = pygame.image.load('image/Hard_Button.png').convert_alpha()
HARD_ON = pygame.image.load('image/Hard_Button_ON.png').convert_alpha()


#ACC,SCORE,HEAL,BURST
def EASY_SEL(SONG_INFO):
    SONG_INFO.append(100) #the number is the delay time for the notes
    Song_Selection.SONG_SELECTION(SONG_INFO) #this is to go to the next page
def NORMAL_SEL(SONG_INFO):
    SONG_INFO.append(50)
    Song_Selection.SONG_SELECTION(SONG_INFO)
def HARD_SEL(SONG_INFO):
    SONG_INFO.append(25)
    Song_Selection.SONG_SELECTION(SONG_INFO)


#The main selection page for the leve;
def LEVEL(SONG_INFO):
    
    #Blit the background
    SCREEN.blit(BACKGROUND,(0,0))
    SCREEN.blit(EASY,(500,0)) 
    SCREEN.blit(NORMAL,(500,250))
    SCREEN.blit(HARD,(500,500)) 
    pygame.display.flip()
    WORD = pygame.font.SysFont("none", 50)

    
    
    #Main loop
    while True:
        
        #Get all the event on the keyboards and mouse
        EVENTS = pygame.event.get()
        for E in EVENTS:
            #if the user click quit
            if E.type == QUIT:
                
                #import def and from def, it will exit pygame and sys
                Exit_Pygame.EXIT()
            #Get the pos of themouse
            POS = pygame.mouse.get_pos()
            
            #Get the buttons that is pressed on the mouse
            BUTT = pygame.mouse.get_pressed()
            
            
            #Xpos and Ypos
            X = POS[0]
            Y = POS[1]
            
            
            #Blit the screen again
            SCREEN.blit(EASY,(500,0)) 
            SCREEN.blit(NORMAL,(500,250))
            SCREEN.blit(HARD,(500,500))
            
            
            #If the mouse if within a certain range
            if X > 518 and X < 681 and Y > 20 and Y < 183:
                
                #this will blit the image ontop of the previous image
                SCREEN.blit(EASY_ON,(500,0))
                
                #if the user left click
                if BUTT[0] == 1:
                    
                    #this will go though the function on top
                    EASY_SEL(SONG_INFO)
                    
            ###########rest is the same#####################
            elif X > 518 and X < 681 and Y > 270 and Y < 432:
                SCREEN.blit(NORMAL_ON,(500,250))
                if BUTT[0] == 1:
                    NORMAL_SEL(SONG_INFO)
            elif X > 518 and X < 681 and Y > 520 and Y < 680:
                SCREEN.blit(HARD_ON,(500,500))
                if BUTT[0] == 1:
                    HARD_SEL(SONG_INFO)
                    
                    
            #info
            Info = "Only Hard mode can go on Highscore"
            SCREEN.blit(WORD.render(Info, 1, THECOLORS["red"]), (10,430))

            #This update the screen
            pygame.display.flip()