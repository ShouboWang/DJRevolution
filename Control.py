#############
###control###
#############


###Inputs###

import pygame, sys,os, time
from pygame.locals import * 
from pygame.color import THECOLORS
import Def
import Exit_Pygame
import Transition_Point
import platform, os
if platform.system() == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'
pygame.init() 



#this is function where it displaies the page
def Control(SONG_INFO):
    
    #set the window size,font,get surface,read file,blit the word onto the screen
    WINDOW = pygame.display.set_mode((700, 700))
    SCREEN = pygame.display.get_surface()  
    BACKGROUND = pygame.image.load('image/Control_Page_1.jpg').convert()
    BACKGROUND1 = pygame.image.load('image/Control_Page2.jpg').convert()
    BACKGROUND2 = pygame.image.load('image/Control_Page3.jpg').convert()
    BACKGROUND3 = pygame.image.load('image/Control_Page4.jpg').convert()
    BACKGROUND4 = pygame.image.load('image/Control_Page.jpg').convert()
    pygame.display.set_caption('DJ Revolution - Control')
    CONTROL_FONT_1 = pygame.font.SysFont("Times New Roman", 25)
    CONTROL_FONT = pygame.font.SysFont("Times New Roman", 40)
    
    
    #key is set to page 1
    KEY = 1
    
    #the main loop
    while True:
        
        
        #get the event on the mouse
        events = pygame.event.get( ) #This command will read everything that is user doing something (an event)
        
        for e in events:
            POS = pygame.mouse.get_pos() # get the position of the mouse
            BUTT = pygame.mouse.get_pressed() #what is been pressed on the mouse
            X = POS[0] #X pos for mouse
            Y = POS[1] #y pos for the mouse
            
            
            #if the user click quit
            if e.type == QUIT:
                
                #import def and from def, it will exit pygame and sys
                Exit_Pygame.EXIT()
                
            # if the user click left button
            if BUTT[0] == 1:
                # the page will add one(to the next page)
                KEY += 1
                
        #if the key is equal to a certain page, then the background will change
        if KEY == 1:
            BACKGROUND = BACKGROUND
        elif KEY == 2:
            BACKGROUND = BACKGROUND1
        elif KEY == 3:
            BACKGROUND = BACKGROUND2
        elif KEY == 4:
            BACKGROUND = BACKGROUND3
        elif KEY == 5:
            BACKGROUND = BACKGROUND4
        elif KEY == 6:
            
            #if the page is 6, the next page 
            Transition_Point.Main(SONG_INFO)
            
            
        #blit the backgroud onto the screen
        SCREEN.blit(BACKGROUND,(0,0))
        
        #blit the words onto the screen
        SCREEN.blit(CONTROL_FONT_1.render('Left click to continue', 1, THECOLORS["red"]), (10,100))
        
        
        
        #if the page is 5, then it will put the instructions on the screen
        if KEY == 5:
            SCREEN.blit(CONTROL_FONT.render('This is a game that would test your hand', 1, THECOLORS["red"]), (10,200))
            SCREEN.blit(CONTROL_FONT.render('eye coordination skills', 1, THECOLORS["red"]), (10,250))
            SCREEN.blit(CONTROL_FONT.render('Also, this is a test for your music talent.', 1, THECOLORS["red"]), (10,300))
            SCREEN.blit(CONTROL_FONT.render(' see if you can follow the beats in music', 1, THECOLORS["red"]), (10,350))
            SCREEN.blit(CONTROL_FONT.render('left click to exit to Main menu', 1, THECOLORS["red"]), (10,500))
            
            
    
        #Up date everything onto the screen
        pygame.display.flip()