#############################
####### END Game ############
#############################


#all the impots
import pygame, sys,os, time
from pygame.locals import * 
from pygame.color import THECOLORS
import Song_Selection
import Main_Menu
import Exit_Pygame
import platform, os
import Def

if platform.system() == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'

#initalize pygame
pygame.init() 

#set the window size and the screen
WINSIZE = pygame.display.set_mode((700, 700))
SCREEN = pygame.display.get_surface()


'''   this is the class for entering the highscore '''
#class Enter score
class ENTER_SCORE(object):
    
    #fuction check
    def CHECK(self,USER,NAME,PATH,SCORE):
        
        #get the path 
        PATH = os.path.join("HIGHSCORE",PATH,NAME)
        
        #open the file
        FILE = open(PATH,'r')
        
        #read the file and put it as a list
        FILE = FILE.readlines()
        
        #get the length of the file
        LENGTH = len(FILE)
        
        #this loop will go though all the item in the list
        for X in xrange(0,LENGTH):
            
            #replace the list's \n with nothing
            CHECK_SCORE = FILE[X].replace('\n','')
            
            #check the score by finding the space and find the number after the space
            CHECK_SCORE = int(CHECK_SCORE[CHECK_SCORE.find(' ')+1:])
            
            #if the score is higher than the highscore
            if SCORE > CHECK_SCORE:
                
                #it will make the score a string and add the \n at the end
                INSERT_SCORE = USER+' '+str(SCORE)+'\n'
                
                #this will inster the score
                FILE.insert(X,INSERT_SCORE)
                
                #this will open the file in write mode
                WRITE = open(PATH,'w')
                
                #this will add all the items into the file
                for Y in xrange(0,LENGTH+1):
                    
                    #write the file
                    WRITE.writelines(FILE[Y])
                    
                #close the file
                WRITE.close()
                
                #return the place where the score is inserted (to show player what place they got)
                return X+1
            
            #if the score is the same as another score
            elif SCORE == CHECK_SCORE:
                
                #this will add \n at the end of the score
                INSERT_SCORE = USER+' '+str(SCORE)+'\n'
                
                #insert the score
                FILE.insert(X+1,INSERT_SCORE)
                
                #open the file
                WRITE = open(PATH,'w')
                
                #write the score
                for Y in xrange(0,LENGTH+1):
                    
                    #write the score into the file
                    WRITE.writelines(FILE[Y])
                    
                #close the file
                WRITE.close()
                
                #return the place
                return X+1
        
        #anything else(lowest score)
        else:
            
            #add a \n at the end of the score
            INSERT_SCORE = USER+' '+str(SCORE)+'\n'
            
            #insert the score
            FILE.insert(LENGTH+1,INSERT_SCORE)
            
            #open file in write mode
            WRITE = open(PATH,'w')
            
            #write the file
            for Y in xrange(0,LENGTH+1):
                
                #write lines
                WRITE.writelines(FILE[Y])
                
            #close the file
            WRITE.close()
            
            #retrurn last
            return 'LAST'
            
        
        
'''     this is where to call up the class function '''

#function HIGHSCORE
def HIGHSCORE(SONG_INFO):
    
    #set the initalize of the class above
    ACCURACY = ENTER_SCORE()
    
    #all the infomation
    ACCURACY_PLACE = ACCURACY.CHECK(SONG_INFO[0],'ACCURACY.txt',SONG_INFO[9],SONG_INFO[16])
    COMBO_PLACE = ACCURACY.CHECK(SONG_INFO[0],'COMBO.txt',SONG_INFO[9],SONG_INFO[17])
    SCORE_PLACE = ACCURACY.CHECK(SONG_INFO[0],'SCORE.txt',SONG_INFO[9],SONG_INFO[18])
    
    #return the place of accuracy, combo and score
    return ACCURACY_PLACE,COMBO_PLACE,SCORE_PLACE


'''   this is to check if the player is in random mission mode and won the game '''
#check if the player won
def WIN_CHECK(SONG_INFO):
    
    #check if the mission
    #if the player wins
    if Def.WIN_MISSION_CHECK(SONG_INFO) == 'PASS':
        
        #next step
        WIN(SONG_INFO)
        
    #if player loses
    elif Def.WIN_MISSION_CHECK(SONG_INFO) == 'FAIL':
        
        #next step
        DEATH(SONG_INFO)
    
'''   if the player fail the game or random mission '''
#DEATH
def DEATH(SONG_INFO):
    
    #load the images font and blit all that onto the screem
    MENU = pygame.image.load('image/Game_End_Menu.png').convert_alpha()
    MENU_ON = pygame.image.load('image/Game_End_Menu_ON.png').convert_alpha()
    SONG = pygame.image.load('image/Game_End_Song.png').convert_alpha()
    SONG_ON = pygame.image.load('image/Game_End_Song_ON.png').convert_alpha()
    SCREEN.fill(THECOLORS["black"])
    WORD = pygame.font.SysFont("none", 100)
    SCREEN.blit(WORD.render('FAIL', 1, THECOLORS["red"]), (280,200))
    SCREEN.blit(MENU,(100,400))
    SCREEN.blit(SONG,(400,400))
    #delay
    pygame.time.delay(500)
    
    #update the screen
    pygame.display.update()
    
    #main loop
    while True:
        
        #blit the screen again
        SCREEN.blit(MENU,(100,400))
        SCREEN.blit(SONG,(400,400))
        
        #get the event of the keyborad and mouse
        events = pygame.event.get()
        
        #for loop
        for e in events:
            
            #if the user click quit
            if e.type == QUIT:
                
                #import def and from def, it will exit pygame and sys
                Exit_Pygame.EXIT()
            
            #get the position of the mouse
            POS = pygame.mouse.get_pos()
            
            #get the pressed button
            BUTT = pygame.mouse.get_pressed()
            
            #x,y
            X = POS[0]
            Y = POS[1]
            
            #if the mouse is within a certain range
            if X > 110 and X < 290 and Y > 413 and Y < 590:
                
                #blit this image ontop of the other image
                SCREEN.blit(MENU_ON,(100,400))
                
                #if the button id pressed
                if BUTT[0] == 1:
                    
                    #this will refresh the song lidt
                    NEW_SONG_INFO = []
                    
                    #only adding 
                    for X in xrange(0,2):
                        print "hi"
                        
                        #add the song info to the new list
                        NEW_SONG_INFO.append(SONG_INFO[X])
                        
                        
                    #song info will equal to the new list
                    SONG_INFO = NEW_SONG_INFO
                    
                    #goto main menu
                    Main_Menu.Main(SONG_INFO)
                        
            #everyhing here is the same as above, excepte the amount of item kept in the list is changed to 8 and it goes to another page
            elif X > 410 and X < 590 and Y > 413 and Y < 590:
                SCREEN.blit(SONG_ON,(400,400))
                if BUTT[0] == 1:
                    NEW_SONG_INFO = []
                    for X in xrange(0,8):
                        NEW_SONG_INFO.append(SONG_INFO[X])
                    SONG_INFO = NEW_SONG_INFO
                    Song_Selection.SONG_SELECTION(SONG_INFO) 
            pygame.display.update()

            
#this is when you win the game
def WIN(SONG_INFO):
    
    #all the imports and fonts
    print SONG_INFO
    MENU = pygame.image.load('image/Game_End_Menu.png').convert_alpha()
    MENU_ON = pygame.image.load('image/Game_End_Menu_ON.png').convert_alpha()
    SONG = pygame.image.load('image/Game_End_Song.png').convert_alpha()
    SONG_ON = pygame.image.load('image/Game_End_Song_ON.png').convert_alpha()
    SCREEN.fill(THECOLORS["black"])
    WORD = pygame.font.SysFont("none", 30)
    
    #blit the word onto the screen
    SCREEN.blit(WORD.render('Nice', 1, THECOLORS["red"]), (330,100))
    
    #if the conditionis true(white note,hardlevel) or (random mission)
    if (SONG_INFO[0] != 'GUEST' and SONG_INFO [7] == 25 and SONG_INFO[15] == 'white') or (SONG_INFO[2] != 'NONE'):
        
        #this will bring it to highscore
        SHOW_SCORE = HIGHSCORE(SONG_INFO)
        
        #calculate exp
        Def.EXP_CAL(SONG_INFO)
        
        #blit the words and the score the player got and the position he or she is in
        SCREEN.blit(WORD.render('Final Score: '+str(SONG_INFO[18])+', you are #'+str(SHOW_SCORE[2])+' On the score list', 1, THECOLORS["red"]), (50,200))
        SCREEN.blit(WORD.render('FINAL ACCURACY: '+str(SONG_INFO[16])+'%'+', you are #'+str(SHOW_SCORE[0])+' On the Accuracy list', 1, THECOLORS["red"]), (50,250))
        SCREEN.blit(WORD.render('Max Combo: '+str(SONG_INFO[17])+', you are #'+str(SHOW_SCORE[1])+' On the Combo list', 1, THECOLORS["red"]), (50,300))
        
        #if the player is a guest or didnt satisfy the highscore condition
    else:
        SCREEN.blit(WORD.render('Final Score: '+str(SONG_INFO[18]), 1, THECOLORS["red"]), (50,200))
        SCREEN.blit(WORD.render('FINAL ACCURACY: '+str(SONG_INFO[16])+'%', 1, THECOLORS["red"]), (50,250))
        SCREEN.blit(WORD.render('Max Combo: '+str(SONG_INFO[17]), 1, THECOLORS["red"]), (50,300))
        
    #update the screen
    pygame.display.flip()
    
    #main loop
    while True:
        
        #blit the images
        SCREEN.blit(MENU,(100,400))
        SCREEN.blit(SONG,(400,400))
        
        #get the event
        events = pygame.event.get()
        
        #for loop
        for e in events:
            if e.type == QUIT:
                
                #import def and from def, it will exit pygame and sys
                Exit_Pygame.EXIT()
            #get the pos of the mouse
            POS = pygame.mouse.get_pos()
            
            #get the press
            BUTT = pygame.mouse.get_pressed()
            
            #mouse X,Y
            X = POS[0]
            Y = POS[1]
            
            #if the mouse is within a certain range
            if X > 110 and X < 290 and Y > 413 and Y < 590:
                
                #blit the image ontop of the previous one
                SCREEN.blit(MENU_ON,(100,400))
                
                #if the player clicks (left mouse)
                if BUTT[0] == 1:
                    
                    #gives a new SONG_INFO
                    NEW_SONG_INFO = []
                    
                    #add the first 3 item onto the list
                    for X in xrange(0,2):
                        
                        #append to the list
                        NEW_SONG_INFO.append(SONG_INFO[X])
                        
                    #set the songinfo as the new info
                    SONG_INFO = NEW_SONG_INFO
                    
                    #goto the next page
                    Main_Menu.Main(SONG_INFO)
                    
            #this is the same process except the number are different and the images are different
            elif X > 410 and X < 590 and Y > 413 and Y < 590:
                SCREEN.blit(SONG_ON,(400,400))
                if BUTT[0] == 1:
                    NEW_SONG_INFO = []
                    for X in xrange(0,8):
                        NEW_SONG_INFO.append(SONG_INFO[X])
                    SONG_INFO = NEW_SONG_INFO
                    Song_Selection.SONG_SELECTION(SONG_INFO)
                    
            #update the screen
            pygame.display.flip()