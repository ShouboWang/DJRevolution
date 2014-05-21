#   DJ Revoluation
#   JACK WANG
#   Last updated June 6,10



#All the necessary imports(pygame, platform, color)
import pygame, sys,os, time
from pygame.locals import * 
from pygame.color import THECOLORS
import Main_Menu
import Def
import Exit_Pygame
import platform, os


#Incase the system is windows, it prevent unwanted error(no available video device error)
if platform.system() == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'

#initalize pygame
pygame.init() 


#the main function
def MAIN():
    
    
    #set the window size,font,get surface,read file,blit the word onto the screen
    WINSIZE = pygame.display.set_mode((700, 700))
    SCREEN = pygame.display.get_surface()
    WORD = pygame.font.SysFont("none", 50)
    myfont = pygame.font.SysFont("none", 50)
    SCREEN.fill(THECOLORS["black"])
    BACKGROUND = pygame.image.load('image/Username_Enter.jpg').convert()
    
    #open the file and setthe mode to read
    USER_FILE_1 =open('DATA/ACCOUNTS.txt','r') #Read the file
    USER_FILE = USER_FILE_1.readlines() #put it as a list
    USER_FILE_1.close() #close the file
    PASS_FILE_1=open('DATA/PASSWORD.txt','r')
    PASS_FILE = PASS_FILE_1.readlines()
    PASS_FILE_1.close()
    SCORE_FILE_1 =open('DATA/SCORE.txt','r')
    SCORE_FILE = SCORE_FILE_1.readlines()
    SCORE_FILE_1.close()
    
    
    #blit the words onto the screen
    SCREEN.blit(WORD.render('ID', 1, THECOLORS["red"]), (200,100))
    SCREEN.blit(WORD.render('Password', 1, THECOLORS["red"]), (100,150))
    SCREEN.blit(WORD.render('Enter a new ID and Pass', 1, THECOLORS["red"]), (150,200))
    SCREEN.blit(WORD.render('Press enter to continue', 1, THECOLORS["red"]), (150,600))
    
    #set the Y,X pos for the text box
    USER_POS_X = 300
    USER_POS_Y = 100
    PASS_POS_X = 300
    PASS_POS_Y = 150
    
    
    #Blit the text box onto the screen
    SCREEN.blit(BACKGROUND,(USER_POS_X,USER_POS_Y))
    SCREEN.blit(BACKGROUND,(PASS_POS_X,PASS_POS_Y))
    
    #Set a empty PASS and USER
    PASS = ""
    USER = ""
    
    #if the username already exit, then it will say again,defalt to False
    AGAIN = False
    
    
    #this is when the username player entered will be recorded into the user txt file, if the name already exit, then the missage'username already exit will show up'
    def ADD_FILE(USER_FILE,PASS_FILE,SCORE_FILE,USER,PASS,AGAIN): 
        
        #check the length of the username list
        USER_LENGTH = len(USER_FILE)
        
        #for loop goes though every name in the list
        for X in xrange(0,USER_LENGTH):
            
            #check if the username is already in use
            if USER+'\n' == USER_FILE[X]:
                
                #if in use,message will show up (AGIAN = True)
                AGAIN = True
                
                
                #goes back to the username enter
                USERNAME(USER_POS_X,USER_POS_Y,USER,PASS,AGAIN)
        
        #if the name is not in use, it will open all the necessary files in write mode
        NEW_USER = open('DATA/ACCOUNTS.txt','w')
        NEW_PASS = open('DATA/PASSWORD.txt','w')
        NEW_SCORE = open('DATA/SCORE.txt','w')
        
        #add \n at the end of username, pass, that the player entered. it will also add 0 to the score list
        USER_FILE+='\n'
        PASS_FILE+='\n'
        SCORE_FILE+='\n'
        
        #it will append it to the username list,pass and score
        USER_FILE.append(USER)
        PASS_FILE.append(PASS)
        SCORE_FILE.append(str(0)) #<- change the int into a str
        
        #write everything into the file
        NEW_USER.writelines(USER_FILE)
        NEW_PASS.writelines(PASS_FILE)
        NEW_SCORE.writelines(SCORE_FILE)
        
        #close all the file
        NEW_USER.close()
        NEW_PASS.close()
        NEW_SCORE.close()
        
        #set the song info with the new username and score
        SONG_INFO = [USER,0]
        
        #goes to main menu
        Main_Menu.Main(SONG_INFO)
        
        
    #when player enter the username
    def USERNAME(USER_POS_X,USER_POS_Y,USER,PASS,AGAIN):
        while True:
            #get events from the queue (ref to pygame.org)
            events = pygame.event.get()
            for e in events:
                
                #get the pos of the mouse and the button stat on the mouse
                POS = pygame.mouse.get_pos()
                BUTT = pygame.mouse.get_pressed()
                X = POS[0]
                Y = POS[1]
                
                #if the user click quit
                if e.type == QUIT:
                    
                    #import def and from def, it will exit pygame and sys
                    Exit_Pygame.EXIT()
                
                #if the username has a conflict (defalt to False)
                if AGAIN == True:
                    #bilt the message onto the screen
                    SCREEN.blit(myfont.render('The username is already in use', 1, THECOLORS["red"]), (150,350))
                
                #if the mouse is within this range
                if X < 600 and X > 300 and Y > 150 and Y < 185:
                    
                    #if left button clicked
                    if BUTT[0] == 1:
                        #brings it to password enter
                        PASSWORD(PASS_POS_X,PASS_POS_Y,USER,PASS,AGAIN)
                        
                #limit the username to 10 char
                LENGTH = len(USER)
                
                #can only enter username when its less than 11 char
                if LENGTH < 11:
                    #get he name of key pressed
                    if e.type == KEYDOWN :
                        
                        #if the key is space, it will add a space to the str
                        if pygame.key.name(e.key) == 'space':
                            USER += ''
                            
                        # if the user press backspace
                        elif pygame.key.name(e.key) == 'backspace':
                            
                             #this will check the USER list and only take 1 less than the total length of the string. therefore taking away the last entyered key
                            USER = USER[:(len(USER) - 1 )]
                            
                        #if the user press tab
                        elif pygame.key.name(e.key) == 'tab':
                            
                            #bring it to the pass enter function
                            PASSWORD(PASS_POS_X,PASS_POS_Y,USER,PASS,AGAIN)
                            
                        # if the key is return it will also bring it to passenter
                        elif pygame.key.name(e.key) == 'return':
                            PASSWORD(PASS_POS_X,PASS_POS_Y,USER,PASS,AGAIN)
                            
                        #other keys will be appended to the key list
                        elif pygame.key.name(e.key).isalpha():
                            USER+=pygame.key.name(e.key)
                        else:
                            pass
                    # if the user press backspace
                
                #if the username is 10 char, thsi will still alow player to backspace letters
                if e.type == KEYDOWN and LENGTH >= 11:
                    
                    if pygame.key.name(e.key) == 'backspace':
                                
                        #this will check the USER list and only take 1 less than the total length of the string. therefore taking away the last entyered key
                        USER = USER[:(len(USER) - 1 )]
                        
            #blit the textbox and the str(USERNAME) on to the screen
            SCREEN.blit(BACKGROUND,(USER_POS_X,USER_POS_Y))
            SCREEN.blit(myfont.render(USER, 1, THECOLORS["black"]), (USER_POS_X,USER_POS_Y))
            
            #update the screen
            pygame.display.flip() 
    
    
    #same as USERNAME, excpet its pass instead of username
    def PASSWORD(PASS_POS_X,PASS_POS_Y,USER,PASS,AGAIN):
        while True:
            events = pygame.event.get( ) #This command will read everything that is user doing something (an event)
            for e in events:
                POS = pygame.mouse.get_pos()
                BUTT = pygame.mouse.get_pressed()
                X = POS[0]
                Y = POS[1]
                    #if the user click quit
                if e.type == QUIT:
                    
                    #import def and from def, it will exit pygame and sys
                    Def.EXIT_GAME()
                if AGAIN == True:
                    SCREEN.blit(myfont.render('The username is already in use', 1, THECOLORS["red"]), (150,350))
                if X < 600 and X > 300 and Y > 100 and Y < 135:
                    if BUTT[0] == 1:
                        USERNAME(USER_POS_X,USER_POS_Y,USER,PASS,AGAIN)
                if e.type == KEYDOWN :
                    if pygame.key.name(e.key) == 'return':
                        ADD_FILE(USER_FILE,PASS_FILE,SCORE_FILE,USER,PASS,AGAIN)
                    elif pygame.key.name(e.key) == 'enter':
                        ADD_FILE(USER_FILE,PASS_FILE,SCORE_FILE,USER,PASS,AGAIN)
                    elif pygame.key.name(e.key) == 'space':
                        PASS += ''
                    elif pygame.key.name(e.key) == 'backspace':
                        PASS = PASS[:(len(PASS) - 1 )]
                    elif pygame.key.name(e.key) == 'tab':
                        USERNAME(USER_POS_X,USER_POS_Y,USER,PASS,AGAIN)
                    elif pygame.key.name(e.key) == '[1]':
                        PASS += '1'
                    elif pygame.key.name(e.key) == '[2]':
                        PASS += '2'
                    elif pygame.key.name(e.key) == '[3]':
                        PASS += '3'
                    elif pygame.key.name(e.key) == '[4]':
                        PASS += '4'
                    elif pygame.key.name(e.key) == '[5]':
                        PASS += '5'
                    elif pygame.key.name(e.key) == '[6]':
                        PASS += '6'
                    elif pygame.key.name(e.key) == '[7]':
                        PASS += '7'
                    elif pygame.key.name(e.key) == '[8]':
                        PASS += '8'
                    elif pygame.key.name(e.key) == '[9]':
                        PASS += '9'
                    elif pygame.key.name(e.key) == '[0]':
                        PASS += '0'
                    elif pygame.key.name(e.key).isalpha():
                        USER+=pygame.key.name(e.key)
                    else:
                        pass
            SCREEN.blit(BACKGROUND,(PASS_POS_X,PASS_POS_Y))
            SCREEN.blit(myfont.render(len(PASS)*'*', 1, THECOLORS["black"]), (PASS_POS_X,PASS_POS_Y))
            pygame.display.flip()
            
            
    #start by going to the username function
    USERNAME(USER_POS_X,USER_POS_Y,USER,PASS,AGAIN)