###########################################
############## Note selection #############
###########################################



#import all the imputs
import pygame, sys,os, time
from pygame.locals import * 
from pygame.color import THECOLORS
import platform, os
import Exit_Pygame
import Transition_Point
import MUSIC_GAME_FINAL

if platform.system() == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'

#initalize pygame
pygame.init() 


#set the window size and get the mode
WINSIZE = pygame.display.set_mode((700, 700))
SCREEN = pygame.display.get_surface()



#prepare all the images
BACKGROUND = pygame.image.load('image/Note_Sel.jpg').convert()
MOUSE_HEAL = pygame.image.load('image/Mouse_Heal.jpg').convert()
MOUSE_BURST = pygame.image.load('image/Mouse_Burst.jpg').convert()
MOUSE_NORMAL = pygame.image.load('image/Mouse_Normal.jpg').convert()
MOUSE_ACCURACY = pygame.image.load('image/Mouse_Accuracy.jpg').convert()
MOUSE_GOD = pygame.image.load('image/Mouse_God.jpg').convert()
MOUSE_SCORE = pygame.image.load('image/Mouse_Score.jpg').convert()
BURST = pygame.image.load('image/Burst.jpg').convert()
HEAL = pygame.image.load('image/Heal.jpg').convert()
NORMAL = pygame.image.load('image/Normal.jpg').convert()
ACCURACY = pygame.image.load('image/Accuracy.jpg').convert()
GOD = pygame.image.load('image/God.jpg').convert()
SCORE = pygame.image.load('image/Score.jpg').convert()







#ACC,SCORE,HEAL,BURST

#get the level of the player
def LEVEL(SONG_INFO):
    
    #exp is the second info in the SONG_LIST
    EXP = SONG_INFO[1]
    
    #if the username is guest
    if SONG_INFO[0] == 'GUEST':
        #diferent level is applied depending on the exp
        DJ_LEVEL = 0
    elif EXP > 1600:
        DJ_LEVEL = 5
    elif EXP > 800:
        DJ_LEVEL = 4
    elif EXP > 400:
        DJ_LEVEL = 3
    elif EXP > 200:
        DJ_LEVEL = 2
    elif EXP < 100:
        DJ_LEVEL = 1
        
        
    #return the level of the player
    return DJ_LEVEL




###############################################################################
############################    keys ##########################################
###############################################################################

#the order is accuracy,score,heal,burst
def NOTE_BURST(SONG_INFO):
    SONG_INFO.append(1)
    SONG_INFO.append(1)
    SONG_INFO.append(1)
    SONG_INFO.append(3)
    
    #different color of the note
    SONG_INFO.append('red')
    
    #goes to the next page
    MUSIC_GAME_FINAL.Main(SONG_INFO)
    
    
###########    SAME thing except the effect is different #############
def NOTE_ACC(SONG_INFO):
    SONG_INFO.append(10)
    SONG_INFO.append(1)
    SONG_INFO.append(1)
    SONG_INFO.append(1)
    SONG_INFO.append('blue')
    MUSIC_GAME_FINAL.Main(SONG_INFO)
def NOTE_SCORE(SONG_INFO):
    SONG_INFO.append(1)
    SONG_INFO.append(100)
    SONG_INFO.append(1)
    SONG_INFO.append(1)
    SONG_INFO.append('purple')
    MUSIC_GAME_FINAL.Main(SONG_INFO)
def NOTE_HEAL(SONG_INFO):
    SONG_INFO.append(1)
    SONG_INFO.append(1)
    SONG_INFO.append(5)
    SONG_INFO.append(1)
    SONG_INFO.append('green')
    MUSIC_GAME_FINAL.Main(SONG_INFO)
def NOTE_GOD(SONG_INFO):
    SONG_INFO.append(10)
    SONG_INFO.append(100)
    SONG_INFO.append(5)
    SONG_INFO.append(3)
    SONG_INFO.append('yellow')
    MUSIC_GAME_FINAL.Main(SONG_INFO)
def Note_Normal(SONG_INFO):
    SONG_INFO.append(1)
    SONG_INFO.append(1)
    SONG_INFO.append(1)
    SONG_INFO.append(1)
    SONG_INFO.append('white')
    MUSIC_GAME_FINAL.Main(SONG_INFO)



#main song selection
def NOTE_SELECTION(SONG_INFO):
    
    #blit the background and everything else
    SCREEN.blit(BACKGROUND,(0,0))
    SCREEN.blit(NORMAL,(0,340)) 
    
    #check if random mission is on
    Transition_Point.CHECK(SONG_INFO)
    
    #update the screen
    pygame.display.flip()
    
    #delay for half a sec
    pygame.time.delay(500)
    
    #get the DJ's level
    DJ_LEVEL = LEVEL(SONG_INFO)

    #main loop
    while True:
        
        #get the event of the mouse and keyboard
        EVENTS = pygame.event.get()
        
        #for loop
        for E in EVENTS:
            
            #if the user click quit
            if E.type == QUIT:
                
                #import def and from def, it will exit pygame and sys
                Exit_Pygame.EXIT()
            #get the pos of the mouse
            POS = pygame.mouse.get_pos()
            
            #get the stat of the buttons on the mouse
            BUTT = pygame.mouse.get_pressed()
            
            #mouse x,y
            X = POS[0]
            Y = POS[1]
            
            #see which note is available
            if DJ_LEVEL <= 0 or DJ_LEVEL>=0:
                
                #blit the image
                SCREEN.blit(NORMAL,(0,340))
                
                #if the mouse is on the image
                if Y > 340 and Y < 400:
                    
                    #blit the new image ontop of the image
                    SCREEN.blit(MOUSE_NORMAL,(0,340))
                    
                    #if the user clicks
                    if BUTT[0] == 1:
                        
                        #goto the function
                        Note_Normal(SONG_INFO)
                        
            #these onwards is the same, except the image is different
            if DJ_LEVEL >= 1:
                SCREEN.blit(HEAL,(0,400))
                if Y > 400 and Y < 460:
                    SCREEN.blit(MOUSE_HEAL,(0,400))
                    if BUTT[0] == 1:
                        NOTE_HEAL(SONG_INFO)
            if DJ_LEVEL >= 2: 
                SCREEN.blit(ACCURACY,(0,460))
                if Y > 460 and Y < 520:
                    SCREEN.blit(MOUSE_ACCURACY,(0,460))
                    if BUTT[0] == 1:
                        NOTE_ACC(SONG_INFO)
            if DJ_LEVEL >= 3: 
                SCREEN.blit(SCORE,(0,520))
                if Y > 520 and Y < 580:
                    SCREEN.blit(MOUSE_SCORE,(0,520))
                    if BUTT[0] == 1:
                        NOTE_SCORE(SONG_INFO)
            if DJ_LEVEL >= 4:
                SCREEN.blit(BURST,(0,580))
                if Y > 580 and Y < 640:
                    SCREEN.blit(MOUSE_BURST,(0,580))
                    if BUTT[0] == 1:
                        NOTE_BURST(SONG_INFO)
            if DJ_LEVEL >= 5:
                SCREEN.blit(GOD,(0,640)) 
                if Y > 640 and Y < 700:
                    SCREEN.blit(MOUSE_GOD,(0,640))
                    pygame.display.flip()
                    if BUTT[0] == 1:
                        NOTE_GOD(SONG_INFO)
                        
            #flip the background
            pygame.display.flip()