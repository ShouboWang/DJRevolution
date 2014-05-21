#   DJ Revoluation
#   JACK WANG
#   Last updated June 6,10



#All the necessary imports(pygame, platform, color)
import pygame, sys,os, time
from pygame.locals import * 
from pygame.color import THECOLORS
import platform, os 
import Exit_Pygame
import Def #<-- To include function that quit pygame
import Main_Menu #<--Go to main menu
import Account_Creat #<-- To creat an account

#Incase the system is windows, it prevent unwanted error(no available video device error)
if platform.system() == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'

#Initalize pygame
pygame.init() 

#Set the window size 
WINSIZE = pygame.display.set_mode((700, 700))

#Get a reference to the currently set display surface (ref to pygame.org)
SCREEN = pygame.display.get_surface()

#Set the font of the word for the display (word font, size)
WORD = pygame.font.SysFont("none", 50)
myfont = pygame.font.SysFont("none", 50)


#Fill the background of the screen to black (THECOLOR[color])
SCREEN.fill(THECOLORS["black"])

#Load the images and convert them into a format which pygame can easily read from (image location)
BACKGROUND = pygame.image.load('image/Username_Enter.jpg').convert() #<-- BACKGROUND is the name of the text box
GUEST = pygame.image.load('image/Guest.jpg').convert()
GUEST_ON = pygame.image.load('image/Guest_ON.jpg').convert()
ACCOUNT = pygame.image.load('image/account.jpg').convert()
ACCOUNT_ON = pygame.image.load('image/account_ON.jpg').convert()


#Open and read the file (file location, read'r' or write'w')
USER_FILE_1 =open('DATA/ACCOUNTS.txt','r') #<-- open and set the mode to read
USER_FILE = USER_FILE_1.readlines() #<-- read the file @return in list form
USER_FILE_1.close() #<--close the file
PASS_FILE_1 =open('DATA/PASSWORD.txt','r')
PASS_FILE = PASS_FILE_1.readlines()
PASS_FILE_1.close()
SCORE_FILE_1 =open('DATA/SCORE.txt','r')
SCORE_FILE = SCORE_FILE_1.readlines()
SCORE_FILE_1.close()



#Set up text message to display using the myfont settings (MSG in string, always True, what colour)
SCREEN.blit(WORD.render('ID', 1, THECOLORS["red"]), (200,100))
SCREEN.blit(WORD.render('Password', 1, THECOLORS["red"]), (100,150))
SCREEN.blit(WORD.render('Press enter to continue', 1, THECOLORS["red"]), (150,200))

#set the POS for the text box
USER_POS_X = 300
USER_POS_Y = 100
PASS_POS_X = 300
PASS_POS_Y = 150

#blit things onto the screen(image,(posx,posy))
SCREEN.blit(BACKGROUND,(USER_POS_X,USER_POS_Y))
SCREEN.blit(BACKGROUND,(PASS_POS_X,PASS_POS_Y))
SCREEN.blit(ACCOUNT,(100,500))
SCREEN.blit(GUEST,(400,500))


#Set an empty string so user can type the ID and pass
PASS = ""
USER = ""

#creat an empty list, all the imformation about the song will be appended to this list
SONG_INFO = []

#If the user type a wrong ID or pass. it is defalted to False
WRONG = False

#creat a function that check if the username and pass is correct
def USER_CHECK(USER,PASS,USER_FILE,PASS_FILE,SCORE_FILE,WRONG):
    
    #Get the length of the whole USER file
    LENGTH = len(USER_FILE)
    
    #Use for loop to go though all the name in the list
    for X in xrange(0,LENGTH):
        
        #find the USERNAME in the file from 0 to the last one
        TEST = USER_FILE[X]
        
        #take away the \n
        TEST = TEST.replace('\n','')
        
        #if the user does exist in the userfile
        if TEST == USER:
            
            #find the corresponding pass
            PASS_IN_FILE = PASS_FILE[X]
            
            #take away the =n
            PASS_IN_FILE = PASS_IN_FILE.replace('\n','')
            
            #if the pass is the same as the user entered
            if PASS_IN_FILE == PASS:
                
                #find the score in the score file
                SCORE = SCORE_FILE[X]
                
                #Take away the \n at the end of the score and change it into a int
                SCORE = int(SCORE.replace('\n',''))
                
                #add the USER name and score to SONG_INFO list
                SONG_INFO.append(USER)
                SONG_INFO.append(SCORE)
                
                #Continue to Main menu
                Main_Menu.Main(SONG_INFO)
                
    #if the user name or pass is wrong or it dosent exit
    else:
        
        #display saying "invalid pass or id" will appear
        WRONG = True
        
        #go to the function, importing the WRONG variable
        USERNAME(USER_POS_X,USER_POS_Y,USER,PASS,WRONG)

        
#if the user entered as a guest
def GUEST_LOGIN():
    
    #this will append the GUEST and score(as a guest will not be able to enter highscore or use extra keys)
    SONG_INFO.append('GUEST')
    SONG_INFO.append(0)
    
    #go to the Main menu
    Main_Menu.Main(SONG_INFO)
    
#this is the USERNAME enter
def USERNAME(USER_POS_X,USER_POS_Y,USER,PASS,WRONG):
    
    #loop
    while True:
        
        #get events from the queue (ref to pygame.org)
        events = pygame.event.get()
        
        #for loop
        for e in events:
            
            #get the POS of the mouse
            POS = pygame.mouse.get_pos()
            
            #Get the buttons on the mouse [left,middle,right]
            BUTT = pygame.mouse.get_pressed()
            
            #get the X pos and Y pos of the mouse
            X = POS[0]
            Y = POS[1]
            
            #blit the image account on to the screen
            SCREEN.blit(ACCOUNT,(100,500))
            SCREEN.blit(GUEST,(400,500))
            
            #if the user click quit
            if e.type == QUIT:
                
                #import def and from def, it will exit pygame and sys
                Exit_Pygame.EXIT()
                
                
            #if mouse if within a certain range
            if X < 600 and X > 300 and Y > 150 and Y < 185:
                #this is when the user click on pass text box to enter pass
                if BUTT[0] == 1:
                    
                    #if the user left click then it will goto pass
                    PASSWORD(PASS_POS_X,PASS_POS_Y,USER,PASS,WRONG)
                    
            #if mouse id within the creat account image
            if X < 300 and X > 100 and Y < 600 and Y > 500:
                
                #the image will change to ACCOUNT_ON and blit onto the screen
                SCREEN.blit(ACCOUNT_ON,(100,500))
                
                #if the user click left button,
                if BUTT[0]==1:
                    
                    #this will bring it to creat account page
                    Account_Creat.MAIN()
                    
            #if the mouse is with in the guest login image
            elif X < 600 and X > 400 and Y < 600 and Y > 500:
                
                #this will blit it to GUEST_ON
                SCREEN.blit(GUEST_ON,(400,500))
                
                #if the user lift click
                if BUTT[0] == 1:
                    
                    #this will goto GUEST_LOGIN function
                    GUEST_LOGIN()
                    
            #if the user type something
            if e.type == KEYDOWN :
                #if the user press space, it will add a space to the list
                if pygame.key.name(e.key) == 'space':
                    USER += ''
                
                # if the user press backspace
                elif pygame.key.name(e.key) == 'backspace':
                    
                    #this will check the USER list and only take 1 less than the total length of the string. therefore taking away the last entyered key
                    USER = USER[:(len(USER) - 1 )]
                    
                #if the user press tab
                elif pygame.key.name(e.key) == 'tab':
                    
                    #bring it to pass function
                    PASSWORD(PASS_POS_X,PASS_POS_Y,USER,PASS,WRONG)
                #if the user press return
                elif pygame.key.name(e.key) == 'return':
                    
                    #bring it to pass function
                    PASSWORD(PASS_POS_X,PASS_POS_Y,USER,PASS,WRONG)
                #other key imput will auto add to the list
                elif pygame.key.name(e.key).isalpha():
                    USER+=pygame.key.name(e.key)
                    
                else:
                    pass
                    
        #if WRONG is True
        if WRONG == True:
            
            #it will display the messgae 'invalid pass or id'
            SCREEN.blit(WORD.render('Pass or ID is wrong/invalid', 1, THECOLORS["red"]), (150,350))
            
            
        #this will display the USER textbox and then display the USER list(when the user entered) onto the screen
        SCREEN.blit(BACKGROUND,(USER_POS_X,USER_POS_Y))
        SCREEN.blit(myfont.render(USER, 1, THECOLORS["black"]), (USER_POS_X,USER_POS_Y))
        
        #update the display on the screen
        pygame.display.flip() 


#this is the same as USER, except what the user entered will store into the PASS string instead of USER
def PASSWORD(PASS_POS_X,PASS_POS_Y,USER,PASS,WRONG):
    while True:
        events = pygame.event.get( ) #This command will read everything that is user doing something (an event)
        for e in events:
            POS = pygame.mouse.get_pos()
            BUTT = pygame.mouse.get_pressed()
            X = POS[0]
            Y = POS[1]
            SCREEN.blit(ACCOUNT,(100,500))
            SCREEN.blit(GUEST,(400,500))
            #if the user click quit
            if e.type == QUIT:
                
                #import def and from def, it will exit pygame and sys
                Def.EXIT_GAME()
            if X < 600 and X > 300 and Y > 100 and Y < 135:
                if BUTT[0] == 1:
                    USERNAME(USER_POS_X,USER_POS_Y,USER,PASS)
            if X < 300 and X > 100 and Y < 600 and Y > 500:
                SCREEN.blit(ACCOUNT_ON,(100,500))
                if BUTT[0]==1:
                    Account_Creat.MAIN()
            elif X < 600 and X > 400 and Y < 600 and Y > 500:
                SCREEN.blit(GUEST_ON,(400,500))
                if BUTT[0] == 1:
                    GUEST_LOGIN()
            if e.type == KEYDOWN :
                if pygame.key.name(e.key) == 'return':
                    USER_CHECK(USER,PASS,USER_FILE,PASS_FILE,SCORE_FILE,WRONG)
                elif pygame.key.name(e.key) == 'enter':
                    USER_CHECK(USER,PASS,USER_FILE,PASS_FILE,SCORE_FILE,WRONG)
                elif pygame.key.name(e.key) == 'space':
                    PASS += ''
                elif pygame.key.name(e.key) == 'backspace':
                    PASS = PASS[:(len(PASS) - 1 )]
                elif pygame.key.name(e.key) == 'tab':
                    USERNAME(USER_POS_X,USER_POS_Y,USER,PASS,WRONG)
                elif pygame.key.name(e.key).isalpha():
                    PASS+=pygame.key.name(e.key)  
                #from here on,[9]-[0],this is if the user use numpad
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
                else:
                    pass
        if WRONG == True:
            SCREEN.blit(WORD.render('Pass or ID is wrong/invalid', 1, THECOLORS["red"]), (150,350))
        SCREEN.blit(BACKGROUND,(PASS_POS_X,PASS_POS_Y))
        SCREEN.blit(myfont.render(len(PASS)*'*', 1, THECOLORS["black"]), (PASS_POS_X,PASS_POS_Y))
        pygame.display.flip()

#start the page by using the USERNAME function
USERNAME(USER_POS_X,USER_POS_Y,USER,PASS,WRONG)