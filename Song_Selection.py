################################################################################
################################################################################
########################   song selection ######################################
################################################################################
################################################################################


#import all the fuctions
import pygame, sys,os, time
from pygame.locals import * 
from pygame.color import THECOLORS
import Note_Selection
import Exit_Pygame
import pygame_def
import platform, os
if platform.system() == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'
    
#initalize pygame
pygame.init() 

#set the window size and get the surface
WINDOW = pygame.display.set_mode((700, 700))
SCREEN = pygame.display.get_surface()

#load and convert all the images to pygame
START_BUTTON = pygame.image.load('image/Song_Sel_Play.jpg').convert()
START_BUTTON_ON = pygame.image.load('image/Song_Sel_Play_Mouse_on.jpg').convert()
NEXT_BUTTON = pygame.image.load('image/Song_Sel_Next.jpg').convert()
NEXT_BUTTON_ON = pygame.image.load('image/Song_Sel_Next_Mouse_on.jpg').convert()
PRE_BUTTON = pygame.image.load('image/Song_Sel_Pre.jpg').convert()
PRE_BUTTON_ON = pygame.image.load('image/Song_Sel_Pre_mouse_on.jpg').convert()
pygame.display.set_caption('DJ Revolution - Song Selection')


#set the background
VIRUS_BACKGROUND = pygame.image.load('image/Virus_Page2.jpg').convert()
CANON_BACKGROUND = pygame.image.load('image/Canon_Page.jpg').convert()


#def song virus
def VIRUS(SONG_INFO):
    
    #song name
    SONG_INFO.append("VIRUS.ogg")
    
    #name without ogg
    SONG_INFO.append("VIRUS")
    
    #son length
    SONG_INFO.append(22000)
    
    #next step
    Note_Selection.NOTE_SELECTION(SONG_INFO)

############# this is the same, only different is the info ###################
def CANON(SONG_INFO):
    SONG_INFO.append("CANON.ogg")
    SONG_INFO.append("CANON")
    SONG_INFO.append(32000)
    Note_Selection.NOTE_SELECTION(SONG_INFO)






#main function
def SONG_SELECTION(SONG_INFO):
    
    #song number is preset to 1
    SONG_NUM = 1
    
    #blit the images
    SCREEN.blit(VIRUS_BACKGROUND,(0,0))
    SCREEN.blit(PRE_BUTTON,(0,600))
    SCREEN.blit(START_BUTTON,(250,600))
    SCREEN.blit(NEXT_BUTTON,(500,600))
    
    #update the image
    pygame.display.flip()
    
    #delay the page
    pygame.time.delay(500)
    
    #main loop
    while True:
        
        #if the song num is less than 1
        if SONG_NUM < 1:
            
            #song num will be one
            SONG_NUM = 1
            
        #is song num is greater than 2
        if SONG_NUM > 2:
            
            #song num will be 2
            SONG_NUM = 2
            
        #if song num is 1
        if SONG_NUM == 1:
            
            #background
            BACKGROUND = VIRUS_BACKGROUND
        
        #if the song num is 2
        elif SONG_NUM == 2:
            
            #background
            BACKGROUND = CANON_BACKGROUND
            
        #blit the screen
        SCREEN.blit(BACKGROUND,(0,0))
        SCREEN.blit(PRE_BUTTON,(0,600))
        SCREEN.blit(START_BUTTON,(250,600))
        SCREEN.blit(NEXT_BUTTON,(500,600))
        
        
        #get the event of the mouse
        EVENTS = pygame.event.get( )
        
        #for loop
        for EVENT in EVENTS:
            #if the user click quit
            if EVENT.type == QUIT:
                
                #import def and from def, it will exit pygame and sys
                Exit_Pygame.EXIT()
            #get the pos of the mouse
            POS = pygame.mouse.get_pos()
            
            #get the button stat of the mouse
            BUTT = pygame.mouse.get_pressed()
            
            #mouse x,y
            X = POS[0]
            Y = POS[1]
        
            #if the mouse is within a certin range
            if X > 0 and X < 200 and Y > 600:
                
                #bit the screen
                SCREEN.blit(PRE_BUTTON_ON,(0,600))
                
                #if the plaer press left button
                if BUTT[0] == 1:
                    
                    #song num will decrease by 1
                    SONG_NUM -= 1
            
            #############  these are the same except the loaction, numnber and next step ##
            elif X > 250 and X < 450 and Y > 600:
                SCREEN.blit(START_BUTTON_ON,(250,600))
                if BUTT[0]==1:
                    if SONG_NUM == 1:
                        VIRUS(SONG_INFO)
                    if SONG_NUM == 2:
                        CANON(SONG_INFO)
            elif X > 500 and X < 700 and Y > 600:
                SCREEN.blit(NEXT_BUTTON_ON,(500,600))
                if BUTT[0] == 1:
                    SONG_NUM += 1
                    
            #update the screen
            pygame.display.flip()
                
                