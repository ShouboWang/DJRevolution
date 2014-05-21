###############################
#########  SCORE DISPLAY   ####
###############################


#all the imports
import pygame, sys,os, time
from pygame.locals import * 
from pygame.color import THECOLORS
import platform, os
import Exit_Pygame
import Transition_Point

if platform.system() == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'

#initalize pyagme
pygame.init() 


#set the window size and the surface
WINSIZE = pygame.display.set_mode((700, 700))
SCREEN = pygame.display.get_surface()

#set the image and convert then into a format which pygame can easily read
CANON = pygame.image.load('image/Score_Canon.png').convert_alpha()
CANON_ON = pygame.image.load('image/Score_Canon_ON.png').convert_alpha()
VIRUS = pygame.image.load('image/Score_Virus.png').convert_alpha()
VIRUS_ON = pygame.image.load('image/Score_Virus_ON.png').convert_alpha()
OTHER = pygame.image.load('image/Score_Other.png').convert_alpha()
OTHER_ON = pygame.image.load('image/Score_Other_ON.png').convert_alpha()
MAIN = pygame.image.load('image/Score_Main.png').convert_alpha()
MAIN_ON = pygame.image.load('image/Score_Main_ON.png').convert_alpha()

#set the font of the word and the screen
WORD = pygame.font.SysFont("none", 50)
SCREEN.fill(THECOLORS["black"])

#the classto show the score
class SHOW_SCORE(object):
    
    #def to shown the score
    def SHOW(self,INFO):
        
        #how many run this is 
        RUN = 0
        
        #first one
        FIRST = 1
        
        #second one
        SECOND = 2
        
        #third one
        THIRD = 3
        
        #main koop
        while RUN < 3:
            
            #get the path
            PATH = INFO[0]
            
            #this name is preset to first
            NAME = INFO[FIRST]
            
            #file name
            FILE_NAME = INFO[SECOND]
            
            #xpos is the third
            X_POS = INFO[THIRD]
            
            #set the words
            SCORE_WORD = pygame.font.SysFont("none", 30)
            PATH_WORD = pygame.font.SysFont("none", 60)
            
            #blit the name of the song
            SCREEN.blit(PATH_WORD.render(PATH, 1, THECOLORS["red"]), (250,50))
            
            #join the path
            PATH = os.path.join("HIGHSCORE",PATH,FILE_NAME)
            
            #blit the song 
            SCREEN.blit(SCORE_WORD.render(NAME, 1, THECOLORS["red"]), (X_POS+70,150))
            
            #open the file
            FILE = open(PATH,'r')
            
            #read the file and put them as a list
            FILE = FILE.readlines()
            
            #get he length of the file
            LENGTH = len(FILE)
            
            #set the position of the Ypos
            Y_POS = 200 
            
            #if the file is greater than 10 item long, this will only take the first 10 score
            if LENGTH > 10:
                LENGTH = 10
                
            #goes though the list
            for X in xrange(0,LENGTH):
                
                #set print screen as the score
                PRINT_SCREEN = FILE[X]
                
                #find the space between names
                PLACE = PRINT_SCREEN.find(' ')
                
                #get the length of the name
                WORD_LENGTH = len(PRINT_SCREEN[:PLACE])
                
                #get the score
                NAME = PRINT_SCREEN[:PLACE]
                
                #get the score
                SCORE = int(PRINT_SCREEN[PLACE+1:])
                
                #black is the space between the name and the score
                BLANK = (10-WORD_LENGTH) * ' '
                
                #set the value of PRINTSCREEN 
                PRINT_SCREEN = NAME+BLANK+str(SCORE)
                
                #blit the words
                SCREEN.blit(SCORE_WORD.render(PRINT_SCREEN, 1, THECOLORS["red"]), (X_POS+10,Y_POS))
                
                #set the Ypos for the next word
                Y_POS += 20
                
            #next first
            FIRST += 3
            
            #next second
            SECOND += 3
            
            #next third
            THIRD += 3
            
            #Run value
            RUN += 1
            
            #update the screen
            pygame.display.flip()
        
'''   to display the score '''
#funsction to display the screen
def DISPLAY(INFO,SONG_INFO):
    
    #fill the screen back
    SCREEN.fill(THECOLORS["black"])
    
    #append the necessary infomation for the song
    INFO.append('ACCURACY')
    INFO.append('ACCURACY.txt')
    INFO.append(0) #<- the x pos
    INFO.append('COMBO')
    INFO.append('COMBO.txt')
    INFO.append(233) #<- x pos
    INFO.append('SCORE')
    INFO.append('SCORE.txt')
    INFO.append(466) #<- x pos
    
    #goto the showscore class
    PRINT = SHOW_SCORE()
    
    #for the function
    PRINT.SHOW(INFO)
    
    #blit the two options
    SCREEN.blit(MAIN,(100,500))
    SCREEN.blit(OTHER,(400,500))
    pygame.time.delay(500)
    
    #main loop
    while True:
        
        #get the event of the mouse/key board
        EVENTS = pygame.event.get()
        
        #goes though the events
        for E in EVENTS:
            
            #if the user click quit
            if E.type == QUIT:
                
                #import def and from def, it will exit pygame and sys
                Exit_Pygame.EXIT()
            #get the pos of the mouse
            POS = pygame.mouse.get_pos()
            
            #get the buttons that were pressed
            BUTT = pygame.mouse.get_pressed()
            
            #mouse pos x,y
            X = POS[0]
            Y = POS[1]
            
            #blit the twon images
            SCREEN.blit(MAIN,(100,500))
            SCREEN.blit(OTHER,(400,500))
            
            #if the mouse is within a ceratin range
            if X < 289 and X > 113 and Y < 689 and Y > 514:
                
                #this will show
                SCREEN.blit(MAIN_ON,(100,500))
                
                #if the player clicks
                if BUTT[0]==1:
                    
                    #this will bringthem to the next page
                    Transition_Point.Main(SONG_INFO)
                    
            #these after is the same as the one ablve, excpet different image and different next page
            elif X <590 and X > 411 and Y < 689 and Y > 514:
                SCREEN.blit(OTHER_ON,(400,500))
                if BUTT[0] == 1:
                    SCORE_DISPLAY(SONG_INFO)
                    
            #update the screen
            pygame.display.flip()
        

''' this is the song selection to see the score '''
def SCORE_DISPLAY(SONG_INFO):
    
    #fill the screen as black
    SCREEN.fill(THECOLORS["black"])
    pygame.time.delay(500)
    #main loop
    while True:
        
        #get the event of the mouse and keyboard
        EVENTS = pygame.event.get()
        
        #blit the screen
        SCREEN.blit(WORD.render('Select a song', 1, THECOLORS["red"]), (250,100))
        
        #for loop
        for E in EVENTS:
            
            #if the user click quit
            if E.type == QUIT:
                
                #import def and from def, it will exit pygame and sys
                Exit_Pygame.EXIT()
            #get the position of the mouse
            POS = pygame.mouse.get_pos()
            
            #get the button state of the mouse
            BUTT = pygame.mouse.get_pressed()
            
            #mouse x,y
            X = POS[0]
            Y = POS[1]
            
            #blit the screen
            SCREEN.blit(VIRUS,(100,500))
            SCREEN.blit(CANON,(400,500))
            
            #if the mouse is within a certain range
            if X < 289 and X > 113 and Y < 689 and Y > 514:
                
                #blit the screen with the image
                SCREEN.blit(VIRUS_ON,(100,500))
                
                #if the user click
                if BUTT[0]==1:
                    
                    #this will append the name of the song
                    INFO = ['VIRUS']
                    
                    #goto the function
                    DISPLAY(INFO,SONG_INFO)
                    
            #these are the ssme after wards, except different position and didderent song
            elif X <590 and X > 411 and Y < 689 and Y > 514:
                SCREEN.blit(CANON_ON,(400,500))
                if BUTT[0] == 1:
                    INFO = ['CANON']
                    DISPLAY(INFO,SONG_INFO)
                    
            #update the screen
            pygame.display.flip()
        