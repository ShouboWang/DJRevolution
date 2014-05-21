############################
##########   DEF   #########
############################




#all the imports
import pygame
import sys
import os
import random
import Note_Selection
import Level
from pygame.color import THECOLORS


#initalize pygame + get the screen
pygame.init()
SCREEN = pygame.display.get_surface()


#function to exit pygame
def EXIT_GAME():
    pygame.quit()
    sys.exit()
    
#function to calculate exp    
def EXP_CAL(SONG_INFO):
    print SONG_INFO
    USER_1 = open('DATA/ACCOUNTS.txt','r')  #read form the scrore file
    USER = USER_1.readlines() #read the file and put it as a list
    USER_1.close() #close the file
    EXP_1 = open('DATA/SCORE.txt','r') #open the exp file
    EXP = EXP_1.readlines()  #read the file and put it as a list
    EXP_1.close() #close the file
    LENGTH = len(USER) #length of the userfile
    
    
    
    for X in xrange(0,LENGTH):
        
        #by username, check for the location of the username
        if SONG_INFO[0]+'\n' == USER[X]:
            
            #get the exp 
            NEW_EXP = str(EXP[X])
            
            #get the exp and add the exp up
            NEW_EXP = int(int(NEW_EXP.replace('\n',''))+300+(SONG_INFO[6]*1.5))
            
            #insert the exp into the list
            EXP.insert(X,str(NEW_EXP)+'\n')
            
            #take out the old exp
            EXP.pop(X+1)
            
    #open the file in write mode
    EXP_1 = open('DATA/SCORE.txt','w')
    
    
    #write the new list into the file
    for X in EXP:
        
        #write the file
        EXP_1.writelines(X)
        
    #close the file
    EXP_1.close()

    

# Creta random mission
def RANDOM_MISSION(SONG_INFO):
    
    
    #depending on random number, different mission will be created
    MISSION = random.randint(0,4)
    
    #random choice for the song
    SONG = random.choice(['CANON','VIRUS'])
    
    #different exp is available
    EXP = [100,200,300,400,500]
    
    #if the mission is 0
    if MISSION == 0:
        
        #this is the goal the user have to reach
        ITEM = [75,80,85,90,95]
        
        #set the goal by randomly choose an number in the item list
        GOAL = random.choice(ITEM)
        
        #add the corresponding exp
        EXP = EXP[ITEM.index(GOAL)]
        
        #add the name accuracy to the mission 
        NAME = 'ACCURACY'
        
        #add the numbers
        #accuracy
        ACC = GOAL
        
        #score
        SCORE = 0
        
        #combo
        COMBO = 0
        
        #delay
        DELAY = 25
        
    #this one is the same as the one ontop, only the mission changed
    elif MISSION == 1:
        ITEM = [23,20,16,12,7]
        GOAL = random.choice(ITEM)
        EXP = EXP[ITEM.index(GOAL)]
        NAME = 'SURVIVAL'
        ACC = 0
        SCORE = 0
        COMBO = 0
        DELAY = GOAL
        
        
        
    #these mission require notes    
    elif MISSION > 1 and MISSION < 5:
        
        #join the path to the keyfile
        PATH = os.path.join("KEY",SONG,"KEY_1_PRESS.txt")
        PATH2 = os.path.join("KEY",SONG,"KEY_2_PRESS.txt")
        PATH3 = os.path.join("KEY",SONG,"KEY_3_PRESS.txt")
        PATH4 = os.path.join("KEY",SONG,"KEY_4_PRESS.txt")
        
        #read the file
        FILE = open(PATH,'r')
        
        #put it as a list
        NOTE = FILE.readlines()
        
        #close the file
        FILE.close()
        
        #these are the same
        FILE2 = open(PATH,'r')
        NOTE2 = FILE2.readlines()
        FILE2.close()
        FILE3 = open(PATH,'r')
        NOTE3 = FILE3.readlines()
        FILE3.close()
        FILE4 = open(PATH,'r')
        NOTE4 = FILE4.readlines()
        FILE4.close()
        
        
        #add up all the length on the file to get the total amount of notes
        LENGTH = len(NOTE)+len(NOTE2)+len(NOTE3)+len(NOTE4)
        
        
        #if the mission is 2
        if MISSION == 2:
            
            #name will be score
            NAME = 'SCORE'
            
            #these are the goals
            ITEM = [5000,65000,7000,75000,8000]
            
            #randomly choose a item from the list
            CHOICE = random.choice(ITEM)
            
            #goal is the length of the total note and the amount of score each note has
            GOAL = LENGTH * CHOICE
            
            #get the coresponding exp
            EXP = EXP[ITEM.index(CHOICE)]
            
            #Acc
            ACC = 0
            
            #score
            SCORE = GOAL
            
            #combo
            COMBO = 0
            
            #delay
            DELAY = 25
            
        
        #these on wards are the same
        elif MISSION == 3:
            NAME = 'COMBO'
            ITEM = [1.25,1.5,2,2.25,3]
            CHOICE = random.choice(ITEM)
            GOAL = LENGTH * CHOICE
            EXP = EXP[ITEM.index(CHOICE)]
            ACC = 0
            SCORE = 0
            COMBO = GOAL
            DELAY = 25
            
            
            
        elif MISSION == 4:
            NAME = 'HELL'
            ITEM = [60,65,70,75,85]
            ITEM2 = [24,22,20,18,15]
            ITEM3 = [1000,1300,1600,1900,2100]
            ITEM4 = [1.1,1.25,1.5,1.75,2]
            EXP = [800,900,1000,1100,1200]
            ACC = random.choice(ITEM)
            DELAY = random.choice(ITEM2)
            SCORE1 = random.choice(ITEM3)
            SCORE = SCORE1 * LENGTH
            COMBO1 = random.choice(ITEM4)
            COMBO = COMBO1 * LENGTH
            EXP = EXP[int((ITEM.index(ACC) + ITEM2.index(DELAY) + ITEM3.index(SCORE1) + ITEM4.index(COMBO1)) / 4 + 0.5)]
            
    #append the soong info to the list
    #name
    SONG_INFO.append(NAME)
    
    #accuracy
    SONG_INFO.append(ACC)
    
    #score
    SONG_INFO.append(SCORE)
    
    #combo
    SONG_INFO.append(int(COMBO))
    
    #exp
    SONG_INFO.append(EXP)
    
    #delay
    SONG_INFO.append(DELAY)
    
    #gives the other song info
    if SONG == 'VIRUS':
        
        #add the file name of the song
        SONG_NAME = 'VIRUS.ogg'
        
        #the time of the song
        SONG_LENGTH = 22000
    if SONG == 'CANON':
        SONG_NAME = 'CANON.ogg'
        SONG_LENGTH = 32000
        
    #add the song name
    SONG_INFO.append(SONG_NAME)
    
    #add the song
    SONG_INFO.append(SONG)
    
    #add the song length
    SONG_INFO.append(SONG_LENGTH)
    
    #goes to the next page 
    Note_Selection.NOTE_SELECTION(SONG_INFO)
    
    
    
    
'''   if the user didnt select random mission '''

#function for normal selection
def NORMAL(SONG_INFO):
    
    #add the name as NONE
    SONG_INFO.append('NONE')
    
    #add everything as 0
    SONG_INFO.append(0)
    SONG_INFO.append(0)
    SONG_INFO.append(0)
    SONG_INFO.append(0)
    
    #go to the next page
    Level.LEVEL(SONG_INFO)
    
    
'''  this is for the display on the note selection page, it tells you the mission goal '''

#function check
def CHECK_MISSION_NOTE(SONG_INFO):
    
    #set the word type
    WORD = pygame.font.SysFont("none", 30)
    
    #the name is defalt to nothing
    NAME = ''
    
    #if the 3rd item in the list is ACCURACY
    if SONG_INFO[2] == 'ACCURACY':
        
        #it will give the ACCURACY mission and the goal's value to variable NAME
        NAME = 'ACCURACY: '+str(SONG_INFO[3])
        
    #after this, everything is the same
    elif SONG_INFO[2] == 'SCORE':
        NAME = 'SCORE: '+str(SONG_INFO[4])
    elif SONG_INFO[2] == 'COMBO':
        NAME = 'COMBO: '+str(SONG_INFO[5])
    elif SONG_INFO[2] == 'SURVIVAL':
        NAME = 'SURVIVE: '+str(SONG_INFO[7]) + 'Delay'
        
    elif SONG_INFO[2] == 'HELL':
        ACC = 'ACCURACY: '+str(SONG_INFO[3])
        SCORE = 'SCORE: '+str(SONG_INFO[4])
        COMBO = 'COMBO: '+str(SONG_INFO[5])
        SURIVE = 'SURVIVE: '+str(SONG_INFO[7])
        
        
        #bilt the words onto the screen
        SCREEN.blit(WORD.render(ACC, 1, THECOLORS["red"]), (10,50))
        SCREEN.blit(WORD.render(COMBO, 1, THECOLORS["red"]), (10,80))
        SCREEN.blit(WORD.render(SCORE, 1, THECOLORS["red"]), (10,110))
        SCREEN.blit(WORD.render(SURIVE, 1, THECOLORS["red"]), (10,140))
    else:
        #if the words are not the ones shown above
        pass
    
    #blit the info(SONG NAME)
    SCREEN.blit(WORD.render('SONG: '+SONG_INFO[9], 1, THECOLORS["red"]), (10,20))
    
    #blit song info
    SCREEN.blit(WORD.render(NAME, 1, THECOLORS["green"]), (10,50))

        
    
    
    
''' this is to shown mission requirement on the game page '''

#everything is the same as above except the font of the word and the opsition of the word is the same
def CHECK_MISSION_GAME(SONG_INFO):
    WORD = pygame.font.SysFont("none", 25)
    NAME = ''
    
    if SONG_INFO[2] == 'ACCURACY':
        NAME = 'ACCURACY: '+str(SONG_INFO[3])
    elif SONG_INFO[2] == 'SCORE':
        NAME = 'SCORE: '+str(SONG_INFO[4])
    elif SONG_INFO[2] == 'COMBO':
        NAME = 'COMBO: '+str(SONG_INFO[5])
    elif SONG_INFO[2] == 'SURVIVAL':
        NAME = 'SURVIVE: '+str(SONG_INFO[7]) + 'Delay'
        
    elif SONG_INFO[2] == 'HELL':
        ACC = 'ACCURACY: '+str(SONG_INFO[3])
        SCORE = 'SCORE: '+str(SONG_INFO[4])
        COMBO = 'COMBO: '+str(SONG_INFO[5])
        SURIVE = 'SURVIVE: '+str(SONG_INFO[7])
        SCREEN.blit(WORD.render(ACC, 1, THECOLORS["red"]), (10,280))
        SCREEN.blit(WORD.render(COMBO, 1, THECOLORS["red"]), (10,305))
        SCREEN.blit(WORD.render(SCORE, 1, THECOLORS["red"]), (10,330))
        SCREEN.blit(WORD.render(SURIVE, 1, THECOLORS["red"]), (10,355))
    else:
        pass
    SCREEN.blit(WORD.render(NAME, 1, THECOLORS["red"]), (10,280))
    
    
    
    
'''   this is to check if the player has beat the game '''

#function check the game
def WIN_MISSION_CHECK(SONG_INFO):
    # if the mission requiremnt is higher than the player's score, then its a fail
    if SONG_INFO[3] > SONG_INFO[16]:
        END = 'FAIL'
    elif SONG_INFO[4] > SONG_INFO[18]:
        END = 'FAIL'
    elif SONG_INFO[5] > SONG_INFO[17]:
        END = 'FAIL'
        
    #if the player's score is the same or higher then the requirement is a pass
    else:
        END = 'PASS'
        
    #reture the value of END
    return END