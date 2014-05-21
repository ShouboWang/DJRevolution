#   00000     000000000
#   00  000        000
#   00   000       000
#   00   000  00   000
#   00  000   00000000
#   00000       0000
# 
#   000000   000000000 000   000 0000000 00      000   000 000000000 000000000 0000000 00   00
#   00   00  000       000   000 0000000 00      000   000 000000000 000000000 0000000 00   00
#   00    00 000       000   000 00   00 00      000   000    000       000    00   00 0000 00
#   0000000  00000000  000   000 00   00 00      000   000    000       000    00   00 0000000
#   00  00   000        000 000  00   00 00      000   000    000       000    00   00 00 0000
#   00   00  000          000    0000000 0000000  0000000     000    000000000 0000000 00   00
#   00   00  00000000      0     0000000 0000000   00000      000    000000000 0000000 00   00





# Jack Wang
# Lat updated may 28,2010




#This will import all the necessary item
import pygame, sys,os, time
from pygame.locals import * 
from pygame.color import THECOLORS
import random
import time
import Exit_Pygame
import Def
import End_Game
import platform, os



#Solve the window problem
if platform.system() == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'


#initalize pygame and music
pygame.init() 
pygame.mixer.init()

#WINDOW SIZE + SCREEN
WINSIZE = pygame.display.set_mode((700, 700))
SCREEN = pygame.display.get_surface()



'''  this is when the player presses a key and this class will respond to the press'''
#class
class KEY_PRESSED_VAL(object):
    
    #intialize all the vlaue
    def __init__(self,NAME):
        self.NAME = NAME
    
    #this is for the accuracy of the key thats been pressed
    def KEY_ACC(self,NOTE_TIME,PRESS_TIME,KEY_SPICAL_ACC,DELAY):
        
        #the balance for the key
        BALANCER = 100 / DELAY
        
        #the key sccuracy for the key
        self.KEY_ACCURACY = (int(NOTE_TIME) - int(PRESS_TIME)) * BALANCER
        
        #if the key accuracy is a negative number
        if self.KEY_ACCURACY < 0:
            
            #this will convert the negative into positive
            self.KEY_ACCURACY = self.KEY_ACCURACY * -1
        
        #if the key have spical ability
        self.KEY_ACCURACY = int(100 - self.KEY_ACCURACY) + KEY_SPICAL_ACC
        
        #this gives a general value to the accuracy
        if self.KEY_ACCURACY > 95:
            self.KEY_ACCURACY = 100
        elif self.KEY_ACCURACY > 85 and self.KEY_ACCURACY < 95:
            self.KEY_ACCURACY = 90
        elif self.KEY_ACCURACY > 80 and self.KEY_ACCURACY < 85:
            self.KEY_ACCURACY = 85
        elif self.KEY_ACCURACY > 70 and self.KEY_ACCURACY < 80:
            self.KEY_ACCURACY = 80
        elif self.KEY_ACCURACY > 60 and self.KEY_ACCURACY < 70:
            self.KEY_ACCURACY = 70
        elif self.KEY_ACCURACY > 50 and self.KEY_ACCURACY < 60:
            self.KEY_ACCURACY = 60
        elif self.KEY_ACCURACY > 40 and self.KEY_ACCURACY < 50:
            self.KEY_ACCURACY = 50
        elif self.KEY_ACCURACY > 20 and self.KEY_ACCURACY < 40:
            self.KEY_ACCURACY = 30
        if self.KEY_ACCURACY < 20:
            self.KEY_ACCURACY = 10
            
        #return the accuracy
        return self.KEY_ACCURACY
    
    #to calculate combo
    def COMBO_CAL(self,MULTIPLIER):
        COMBO = MULTIPLIER * 1
        
        #return combo
        return COMBO
    
    #calculate score
    def SCORE_CAL(self,KEY_ACCURACY,COMBO,MULTIPLIER,KEY_SPICAL_SCORE,SPEED):
        SCORE = int(((KEY_ACCURACY * MULTIPLIER * (1 + COMBO / 10.0)) + KEY_SPICAL_SCORE)*SPEED/3)
        #return score
        return SCORE
    
    #calculate damgae
    def DMG_CAL(self,LIFE_GAIN,KEY_ACCURACY,KEY_SPICAL_HEAL):
        DMG = KEY_ACCURACY * LIFE_GAIN / 10 + KEY_SPICAL_HEAL
        #return the damage
        return DMG
    
    #calculate burst
    def BURST_CAL(self,KEY_ACCURACY,BURST_GAIN,KEY_SPICAL_BURST):
        BURST = KEY_ACCURACY * BURST_GAIN + KEY_SPICAL_BURST
        #return burst
        return BURST
    
    
#creat the notes for the game
class NOTE_CRATE(object):
    
    #initalize the class
    def __init__(self,FILE,TIMER_FOR_KEY,SPEED,NOTE_COLOR,X_POS):
        
        #start of the note
        self.START = 0 - 556 * (SPEED - 1)
        
        #length of the file
        self.LENGTH = len(FILE)
        
        #the note will equal to the file
        self.NOTE = FILE
        
        #get the time 
        self.TIMER = TIMER_FOR_KEY
        
        #the speed of the key
        self.SPEED = SPEED
        
        #the color of the key
        self.COLOR = NOTE_COLOR
        
        #the x_pos of the key
        self.X_POS = X_POS
        
    #to show the note    
    def NOTE_SHOW(self):
        
        #for loop
        for X in xrange(0,self.LENGTH):
            
            #get the timer and check if the note is within a certain time
            if int(self.NOTE[X]) - self.TIMER < 100:
                
                #if the note is, then the start will be set
                Y_POS = self.START
                
                #get the y_pos of the note
                Y_POS += int(556*self.SPEED-(int(self.NOTE[X]) - self.TIMER) * 5.56 * self.SPEED)
                
                #draw the circle
                pygame.draw.circle(SCREEN, THECOLORS[self.COLOR], (self.X_POS,int(Y_POS)), 20)
                
                #if y is greater than 556 pixel
                if Y_POS > 556:
                    
                    #this will remove the note off the list
                    self.NOTE.pop(0)
                    
                    #return the new note
                    return self.NOTE
                
            #if the note is not within the range
            else:
                
                #return the untouched note
                return self.NOTE
            
            
            
            
# to open the file            
def OPEN_FILE(PATH):
    
    #to read the file
    OPEN=open(PATH,'r')
    
    #read the lines
    FILE_1 = OPEN.readlines()
    
    #close the file
    OPEN.close()
    
    #open the file
    OPEN=open(PATH,'r')
    
    #ead the file and put iot as a list
    FILE_2 = OPEN.readlines()
    
    #close the file
    OPEN.close()
    
    #return the file
    return FILE_1,FILE_2

#to get the color of the key accuracy(random)
def KEY_COLOR():
    
    #set a list containing all the colors and randomly choose a color
    COLOR = random.choice(['blue','yellow','green','white','brown','red','orange','purple','pink','steelblue','greenyellow'])
    
    #return the color
    return COLOR

#check the speed of the key
def CHECK_SPEED(SPEED):
    
    #if the speed is above 5
    if SPEED > 5:
        
        #speed will equal to 5
        SPEED = 5
        
        #if the speed is less than 1
    elif SPEED < 1:
        
        #speed will be 1
        SPEED = 1
        
        #else, speed will stay as it is
    else:
        SPEED = SPEED
        
        #return the speed
    return SPEED



# check the state 
def CHECK_STAT(ACCURACY,TOTAL_KEY):
    
    #depending on the sccuracy level, it will give a general stat
    if ACCURACY/TOTAL_KEY > 90:
        STAT = 'Awesome'
        return STAT
    elif ACCURACY/TOTAL_KEY > 80 and ACCURACY/TOTAL_KEY <= 90:
        STAT = 'Very Good'
        return STAT
    elif ACCURACY/TOTAL_KEY > 70 and ACCURACY/TOTAL_KEY <= 80:
        STAT = 'Good'
        return STAT
    elif ACCURACY/TOTAL_KEY > 60 and ACCURACY/TOTAL_KEY <= 70:
        STAT = 'Nice'
        return STAT
    elif ACCURACY/TOTAL_KEY > 50 and ACCURACY/TOTAL_KEY <= 60:
        STAT = 'Bad'
        return STAT
    elif ACCURACY/TOTAL_KEY <= 50:
        STAT = 'Horrible'
        return STAT
    
#the main game
def Main(SONG_INFO):
    
    
    #set up all the variables
    DELAY = SONG_INFO[7]    
    SONG = SONG_INFO[8]
    NOTE_FILE  = SONG_INFO[9]
    SONG_LENGTH = SONG_INFO[10]
    KEY_SPICAL_ACC = SONG_INFO[11]
    KEY_SPICAL_SCORE = SONG_INFO[12]
    KEY_SPICAL_HEAL = SONG_INFO[13]
    KEY_SPICAL_BURST = SONG_INFO[14]
    NOTE_COLOR = SONG_INFO[15]
    
    
    #set the backgrounds
    BACKGROUND = pygame.image.load('image/combo_100.jpg').convert() #the background when combo is below 100
    BACKGROUND_2 = pygame.image.load('image/combo_300.jpg').convert() #the background when combo is between 100 and 300
    BACKGROUND_3 = pygame.image.load('image/combo_500.jpg').convert() #the background when combo is above 500
    KEY_PRESS_1 = pygame.image.load('image/note1.jpg').convert() # when key "a" is pressed
    KEY_PRESS_2 = pygame.image.load('image/note2.jpg').convert() # when key "s" is pressed
    KEY_PRESS_3 = pygame.image.load('image/note3.jpg').convert() # when key "k" is pressed
    KEY_PRESS_4 = pygame.image.load('image/note4.jpg').convert() # when key "l" is pressed 
    LIFE_BAR = pygame.image.load('image/life_bar.jpg').convert() # image for the life bar
    LIFE_BAR_COVER = pygame.image.load('image/life_bar_cover.jpg').convert() #
    BURST_BAR = pygame.image.load('image/brust.jpg').convert() #
    BURST_BAR_COVER = pygame.image.load('image/brust_cover.jpg').convert() #
    BAR = pygame.image.load('image/pressed_up.jpg').convert()
    BURST_DISPLAY_1 = pygame.image.load('image/BURST_1.png').convert_alpha()#
    BURST_DISPLAY_1_FLIP = pygame.transform.flip(BURST_DISPLAY_1, True, False )
    BURST_DISPLAY_2 = pygame.image.load('image/BURST_2.png').convert_alpha()#
    BURST_DISPLAY_2_FLIP = pygame.transform.flip(BURST_DISPLAY_2, True, False )
    BURST_DISPLAY_3 = pygame.image.load('image/BURST_3.png').convert_alpha()#
    BURST_DISPLAY_3_FLIP = pygame.transform.flip(BURST_DISPLAY_3, True, False )
    BURST_DISPLAY_4 = pygame.image.load('image/BURST_4.png').convert_alpha()#
    BURST_DISPLAY_4_FLIP = pygame.transform.flip(BURST_DISPLAY_4, True, False )
    BURST_DISPLAY_5 = pygame.image.load('image/BURST_5.png').convert_alpha()#
    BURST_DISPLAY_5_FLIP = pygame.transform.flip(BURST_DISPLAY_5, True, False )
    
    
    
    #Get the clock and all the variables for the clock
    CLOCK = pygame.time.Clock()
    CLOCK_FONT = pygame.font.SysFont("Times New Roman", 25)
    
    
    #find the files and open it
    KEY_1_PATH = os.path.join("KEY",NOTE_FILE,"KEY_1_PRESS.txt")
    KEY_2_PATH = os.path.join("KEY",NOTE_FILE,"KEY_2_PRESS.txt")
    KEY_3_PATH = os.path.join("KEY",NOTE_FILE,"KEY_3_PRESS.txt")
    KEY_4_PATH = os.path.join("KEY",NOTE_FILE,"KEY_4_PRESS.txt")
    KEY_1_PRESS = OPEN_FILE(KEY_1_PATH)[0]
    KEY_FOR_NOTE1 = OPEN_FILE(KEY_1_PATH)[1]
    KEY_2_PRESS = OPEN_FILE(KEY_2_PATH)[0]
    KEY_FOR_NOTE2 = OPEN_FILE(KEY_2_PATH)[1]
    KEY_3_PRESS = OPEN_FILE(KEY_3_PATH)[0]
    KEY_FOR_NOTE3 = OPEN_FILE(KEY_3_PATH)[1]
    KEY_4_PRESS = OPEN_FILE(KEY_4_PATH)[0]
    KEY_FOR_NOTE4 = OPEN_FILE(KEY_4_PATH)[1]
    
    #Make a class for the keys that were pressed
    
    BURST_SOUND = pygame.mixer.Sound('SOUND/BURST.ogg')

    #blit the first background
    SCREEN.blit(BACKGROUND,(0,0))
       
    
    
    
    ############################################################################
    ############################################################################
    #########################   all the varibles ###############################
    ############################################################################
    ############################################################################
    
    
    #combo is set to 0
    COMBO = 0
    
    #score is set to 0
    SCORE = 0
    
    #multiplier is set to 1
    MULTIPLIER = 1
    
    #first accuracy is set to 100
    ACCURACY = 100
    
    #next note is set to 1
    NEXT_NOTE = 1
    
    #total key is set to 1
    TOTAL_KEY = 1
    
    #life lose is set to 0
    LIFE_LOSE = 0
    
    #break is set to false
    BREAK = False
    
    #miss is set to false
    MISS = False
    
    #timer is 0
    TIMER = 0
    
    #note, which note the key is on from 1-4
    NOTE_1_FIRST = 0
    NOTE_2_FIRST = 0
    NOTE_3_FIRST = 0
    NOTE_4_FIRST = 0
       
    #the position of the key is on
    KEY_1_TURN = 0
    KEY_2_TURN = 0
    KEY_3_TURN = 0
    KEY_4_TURN = 0
    
    #key accuracy is already set to 100
    KEY_ACCURACY = 100
    
    #BRUST BAR LOCATION
    BURST_X = 62
    BURST_Y = 421
    
    #hoe much burst player gains if they hit the key
    BURST_GAIN = 0.074#0.074
    
    #how much burst they have
    BURST = 0
    
    #burst allow is set to false at the start
    BRUST_ALLOW = False
    
    #the timer is set to a high number
    BURST_TIMER = 999999
    
    #BRUST BAR COVER
    BURST_COVER_X = 62
    BURST_COVER_Y = 421
    
    #LIFE BAR LOCATION
    LIFE_X = 535
    LIFE_Y = 360
    
    #hoe much life a player can gain if he or she hits the key
    LIFE_GAIN = 0.082
    
    
    
    
    #how much life they lose if they miss a key
    ######################   CHANGE THE VALUE OF LIFE_LOSE TO 0 TO NOT DIE ##########################
    LIFE_LOSE = 32.8 #change is to 0 and you wont die                          #normal :32.8
    ###########################################################################################

    
    
    
#how much damage the player took
    DMG = 0
    
    #how much life they have
    LIFE = 328
    
    #LIFE BAR COVER
    LIFE_COVER_X = 535
    LIFE_COVER_Y = 360
    
    #list for the 
    #LIST_NOTE_1 = []
    #LIST_NOTE_2 = []
    #LIST_NOTE_3 = []
    #LIST_NOTE_4 = []
    #make the list just for the note
    
    #this is used to contain all the note to creat new song(not used 4 now)
    #list_1_test = []
    #list_2_test = []
    #list_3_test = []
    #list_4_test = []
    
    #set the speed of the note to 1
    SPEED = 1
    
    #start point of the note
    #START_POINT = 0 - 556 * (SPEED - 1)
    
    #join the path of music
    MUSIC = pygame.mixer.music.load(os.path.join("MUSIC",SONG))
    
    #play the music
    pygame.mixer.music.play()
    
    #the max combo the player has
    MAX_COMBO = 0
    
    #get the color of the first key accuracy
    ACC_COLOR = KEY_COLOR()
    
    #main loo[
    while True:
        
        #This is the start point for the notes
        START_POINT = 0 - 556 * (SPEED - 1)
        
        # if the combo is below 100, the background will the frist 
        if COMBO < 100:
            SCREEN.blit(BACKGROUND,(0,0))
            
        #if the combo is above 100 and below 200
        elif COMBO >=100 and COMBO< 200:
            SCREEN.blit(BACKGROUND_2,(0,0))
            
        #if the combo is above 200
        elif COMBO >=200:
            SCREEN.blit(BACKGROUND_3,(0,0))   
        
        
        #TIMER (Youtube/thenewboston)
        MILLISEC = CLOCK.tick() #Gets the time in milliseconds
        SECONDS = MILLISEC / 1000.0 #this will change millisec into seconds
        TIMER_FOR_KEY = int(TIMER/10) #THis will get time in 10milliseconds
        TIMER += SECONDS*1000 #this will add milliseconds into the timer
        ROUGH_SEC = int(TIMER/1000) + 0.0 #This will get time in seconds and in float form
        CLOCK_MIN = int(ROUGH_SEC /60) #this is the display on the clock for minutes
        CLOCK_SEC = int((ROUGH_SEC / 60 - CLOCK_MIN) * 60) #this is seconds
        FINAL_CLOCK = str(CLOCK_MIN)+':'+str(CLOCK_SEC) #this will display time on the screen
        text=CLOCK_FONT.render(FINAL_CLOCK, True, THECOLORS["black"]) #Display on the screen
        
        
        #this is where it call up the class to creat the note
        NOTE_1 = NOTE_CRATE(KEY_FOR_NOTE1,TIMER_FOR_KEY,SPEED,NOTE_COLOR,220)
        NOTE_FOR_CRATE_1 = NOTE_1.NOTE_SHOW()
        NOTE_2 = NOTE_CRATE(KEY_FOR_NOTE2,TIMER_FOR_KEY,SPEED,NOTE_COLOR,300)
        NOTE_FOR_CRATE_2 = NOTE_2.NOTE_SHOW()
        NOTE_3 = NOTE_CRATE(KEY_FOR_NOTE3,TIMER_FOR_KEY,SPEED,NOTE_COLOR,390)
        NOTE_FOR_CRATE_3 = NOTE_3.NOTE_SHOW()
        NOTE_4 = NOTE_CRATE(KEY_FOR_NOTE4,TIMER_FOR_KEY,SPEED,NOTE_COLOR,480)
        NOTE_FOR_CRATE_4 = NOTE_4.NOTE_SHOW()
        
        
        
        #if the player didnt break
        if BREAK == False:
            
            #MAKE SURE THAT THE KEY ACCURACY ID NOT IN NEGATIVE
            if KEY_ACCURACY < 0:
                KEY_ACCURACY = KEY_ACCURACY * -1
            
            #SHOWS ACCURACY OF THE KEY PRESSED
            SCREEN.blit(CLOCK_FONT.render(str(KEY_ACCURACY)+"%", 1, THECOLORS[ACC_COLOR]), (310,500))
        
        #if the player breaks
        if BREAK == True:

            #blit the word saying that the playerhas break
            SCREEN.blit(CLOCK_FONT.render("BREAK", 1, THECOLORS['red']), (310,500))
            
        #get the press of the key (keypress gives all the state of the keys on the keyboard and in list form, it will serch though the list and find if any key is pressed)   
        KEY_PRESSED = pygame.key.get_pressed()  #code from(pygame.org)
        
        #this is for the light at the bottom when the player press on the key
        if KEY_PRESSED[K_a]:
            
            #blit the screen
            SCREEN.blit(KEY_PRESS_1,(169,630))
            SCREEN.blit(BAR,(174,562))
        if KEY_PRESSED[K_s]:
            SCREEN.blit(KEY_PRESS_2,(259,630))
            SCREEN.blit(BAR,(264,562))
        if KEY_PRESSED[K_k]:
            SCREEN.blit(KEY_PRESS_3,(349,630))
            SCREEN.blit(BAR,(354,562))
        if KEY_PRESSED[K_l]:
            SCREEN.blit(KEY_PRESS_4,(439,630))
            SCREEN.blit(BAR,(444,562))
            
        #get the event of the keyboard
        for event in pygame.event.get():
            #if the user click quit
            if event.type == QUIT:
                
                #import def and from def, it will exit pygame and sys
                Exit_Pygame.EXIT()
                
                
                
                
                
                
            if event.type == KEYDOWN:
                #############this is used to creat the note for songs#############
                # used to creat  new keys(not used)
           #     if event.key == K_z:
           #         list_1_test.append(TIMER_FOR_KEY)
           #     if event.key == K_x:
           #         list_2_test.append(TIMER_FOR_KEY)
           #     if event.key == K_n:
           #         list_3_test.append(TIMER_FOR_KEY)
           #     if event.key == K_m:
           #         list_4_test.append(TIMER_FOR_KEY)
           #     if event.key == K_q:
           #         print "Key 1"
           #         for x in list_1_test:
           #             print x
           #         print "Key 2"
           #         for x in list_2_test:
           #             print x
           #         print "Key 3"
           #         for x in list_3_test:
           #             print x
           #         print "Key 4"
           #         for x in list_4_test:
           #             print x        
            
                        
                        
###############################################################################
###############################################################################
########################   if a key is pressed ################################
###############################################################################
###############################################################################
                        
                        
                        
                        
                #if the key pressed is a
                if event.key == K_a:
                    
                    #if the key is pressed within a certain range
                    if int(KEY_1_PRESS[KEY_1_TURN]) + DELAY > TIMER_FOR_KEY and int(KEY_1_PRESS[KEY_1_TURN]) - DELAY < TIMER_FOR_KEY:
                        
                        #randomly creat a color for the note
                        ACC_COLOR = KEY_COLOR()
                        
                        #call up the class
                        KEY_PRESSED_A = KEY_PRESSED_VAL('KEY_PRESSED_A')
                        
                        #getthe note time
                        NOTE_TIME = KEY_1_PRESS[KEY_1_TURN]
                        
                        #get the press time
                        PRESS_TIME = TIMER_FOR_KEY
                        
                        #get the key accuracy
                        KEY_ACCURACY = KEY_PRESSED_A.KEY_ACC(NOTE_TIME,PRESS_TIME,KEY_SPICAL_ACC,DELAY)
                        
                        #get the overall accuracy
                        ACCURACY += KEY_ACCURACY
                        
                        #get the combo
                        COMBO += KEY_PRESSED_A.COMBO_CAL(MULTIPLIER)
                        
                        #get the score
                        SCORE += KEY_PRESSED_A.SCORE_CAL(KEY_ACCURACY,COMBO,MULTIPLIER,KEY_SPICAL_SCORE,SPEED)
                        
                        #get the dmage
                        DMG -= KEY_PRESSED_A.DMG_CAL(LIFE_GAIN,KEY_ACCURACY,KEY_SPICAL_HEAL)
                        
                        #get the burst
                        BURST += KEY_PRESSED_A.BURST_CAL(KEY_ACCURACY,BURST_GAIN,KEY_SPICAL_BURST)
                        
                        #break will be false
                        BREAK = False
                        
                        #total key will add one
                        TOTAL_KEY += 1
                        
                        #NOTE_1_FIRST += 1 
                        KEY_1_TURN += NEXT_NOTE
                  
                    
                #these on wards are the same as above, the only different is the turn and the key press time
                if event.key == K_s:
                    if int(KEY_2_PRESS[KEY_2_TURN]) + DELAY > TIMER_FOR_KEY and int(KEY_2_PRESS[KEY_2_TURN]) - DELAY < TIMER_FOR_KEY:
                        ACC_COLOR = KEY_COLOR()
                        KEY_PRESSED_A = KEY_PRESSED_VAL('KEY_PRESSED_K')
                        NOTE_TIME = KEY_2_PRESS[KEY_2_TURN]
                        PRESS_TIME = TIMER_FOR_KEY
                        KEY_ACCURACY = KEY_PRESSED_A.KEY_ACC(NOTE_TIME,PRESS_TIME,KEY_SPICAL_ACC,DELAY)
                        ACCURACY += KEY_ACCURACY
                        COMBO += KEY_PRESSED_A.COMBO_CAL(MULTIPLIER)
                        SCORE += KEY_PRESSED_A.SCORE_CAL(KEY_ACCURACY,COMBO,MULTIPLIER,KEY_SPICAL_SCORE,SPEED)
                        DMG -= KEY_PRESSED_A.DMG_CAL(LIFE_GAIN,KEY_ACCURACY,KEY_SPICAL_HEAL)
                        BURST += KEY_PRESSED_A.BURST_CAL(KEY_ACCURACY,BURST_GAIN,KEY_SPICAL_BURST)
                        BREAK = False
                        TOTAL_KEY += 1
                        KEY_2_TURN += NEXT_NOTE                    
                    
                    
                if event.key ==K_k:
                    if int(KEY_3_PRESS[KEY_3_TURN]) + DELAY > TIMER_FOR_KEY and int(KEY_3_PRESS[KEY_3_TURN]) - DELAY < TIMER_FOR_KEY:
                        ACC_COLOR = KEY_COLOR()
                        KEY_PRESSED_A = KEY_PRESSED_VAL('KEY_PRESSED_K')
                        NOTE_TIME = KEY_3_PRESS[KEY_3_TURN]
                        PRESS_TIME = TIMER_FOR_KEY
                        KEY_ACCURACY = KEY_PRESSED_A.KEY_ACC(NOTE_TIME,PRESS_TIME,KEY_SPICAL_ACC,DELAY)
                        ACCURACY += KEY_ACCURACY
                        COMBO += KEY_PRESSED_A.COMBO_CAL(MULTIPLIER)
                        SCORE += KEY_PRESSED_A.SCORE_CAL(KEY_ACCURACY,COMBO,MULTIPLIER,KEY_SPICAL_SCORE,SPEED)
                        DMG -= KEY_PRESSED_A.DMG_CAL(LIFE_GAIN,KEY_ACCURACY,KEY_SPICAL_HEAL)
                        BURST += KEY_PRESSED_A.BURST_CAL(KEY_ACCURACY,BURST_GAIN,KEY_SPICAL_BURST)
                        BREAK = False
                        TOTAL_KEY += 1
                        KEY_3_TURN += NEXT_NOTE
                    
                    
                    
                if event.key == K_l:
                    if int(KEY_4_PRESS[KEY_4_TURN]) + DELAY > TIMER_FOR_KEY and int(KEY_4_PRESS[KEY_4_TURN]) - DELAY < TIMER_FOR_KEY:
                        ACC_COLOR = KEY_COLOR()
                        KEY_PRESSED_A = KEY_PRESSED_VAL('KEY_PRESSED_L')
                        NOTE_TIME = KEY_4_PRESS[KEY_4_TURN]
                        PRESS_TIME = TIMER_FOR_KEY
                        KEY_ACCURACY = KEY_PRESSED_A.KEY_ACC(NOTE_TIME,PRESS_TIME,KEY_SPICAL_ACC,DELAY)
                        ACCURACY += KEY_ACCURACY
                        COMBO += KEY_PRESSED_A.COMBO_CAL(MULTIPLIER)
                        SCORE += KEY_PRESSED_A.SCORE_CAL(KEY_ACCURACY,COMBO,MULTIPLIER,KEY_SPICAL_SCORE,SPEED)
                        DMG -= KEY_PRESSED_A.DMG_CAL(LIFE_GAIN,KEY_ACCURACY,KEY_SPICAL_HEAL)
                        BURST += KEY_PRESSED_A.BURST_CAL(KEY_ACCURACY,BURST_GAIN,KEY_SPICAL_BURST)
                        BREAK = False
                        TOTAL_KEY += 1
                        KEY_4_TURN += NEXT_NOTE
                        
                        
                        
                #if the player press q or p to increase or decrease the speed
                if event.key == K_p:
                    SPEED += 0.2
                if event.key == K_q:
                    SPEED -= 0.2
                    
        #check the speed
        SPEED = CHECK_SPEED(SPEED)
        
        
####################################################################################
########################    miss   #################################################
####################################################################################

        #if the no key is press within this time frame
        if int(KEY_1_PRESS[KEY_1_TURN]) + DELAY < TIMER_FOR_KEY:
            #the key will equal to the next key
            KEY_1_TURN += 1
            #miss will equal to true
            MISS = True   
        #these onwards are the same as above
        if int(KEY_4_PRESS[KEY_4_TURN]) + DELAY < TIMER_FOR_KEY:
            KEY_4_TURN += 1
            MISS = True
        if int(KEY_2_PRESS[KEY_2_TURN]) + DELAY < TIMER_FOR_KEY:
            KEY_2_TURN += 1
            MISS = True        
        if int(KEY_3_PRESS[KEY_3_TURN]) + DELAY < TIMER_FOR_KEY:
            KEY_3_TURN += 1
            MISS = True           
            
            
            
        #if a key is missed
        if MISS == True:
            
            #combo will be set to zero
            COMBO = 0
            
            #accuracy will add 0
            ACCURACY = ACCURACY + 0
            
            #total key will add 0
            TOTAL_KEY +=1
            
            #damage will add life lose
            DMG += LIFE_LOSE
            
            #break will be true
            BREAK = True
            
            #miss will be false
            MISS = False  
        
            
        #blit all the things onto the screen    
        SCREEN.blit(BURST_BAR,(BURST_X,BURST_Y))  #burst bar
        SCREEN.blit(LIFE_BAR,(LIFE_X,LIFE_Y))  #life bar
        SCREEN.blit(CLOCK_FONT.render('speed:'+str(SPEED), 1, THECOLORS['red']), (320,50))  #speed
        SCREEN.blit(CLOCK_FONT.render(str(int(SCORE)), 1, THECOLORS['white']), (25,88))  #score
        SCREEN.blit(CLOCK_FONT.render(str(ACCURACY/TOTAL_KEY)+'%', 1, THECOLORS['white']), (590,88))  #accuracy
        SCREEN.blit(CLOCK_FONT.render(str(int(COMBO)), 1, THECOLORS['white']), (25,230))  #combo
        SCREEN.blit(CLOCK_FONT.render(FINAL_CLOCK, 1, THECOLORS['white']), (350,0))  #final clock
        
        #this is to check if the random mission is on
        Def.CHECK_MISSION_GAME(SONG_INFO)  
        
        #if the damage is less than 0
        if DMG < 0:
            
            #damage will be 0
            DMG = 0
            
        #CHANGE THE LENGTH OF THE LIFE BAR
        LIFE_BAR_LEN = 1 + int(DMG)
        
        #if the damage is greater than 328
        if DMG > 328:
            
            #stop the music
            pygame.mixer.music.stop()
            
            #goto death page
            End_Game.DEATH(SONG_INFO)
            
            
        #this will transform the life bar
        LIFE_BAR_COVER = pygame.transform.scale(LIFE_BAR_COVER,( 38, LIFE_BAR_LEN ))
        
        #blit the life bar onto the screen
        SCREEN.blit(LIFE_BAR_COVER,(LIFE_COVER_X,LIFE_COVER_Y))
        
        #BURST BAR LENGTH
        BURST_BAR_COVER_Y = 185 - BURST
        
        #MAKE SURE THAT THE BAR IS NOT IN NEGATIVE
        if BURST_BAR_COVER_Y < 1:
            BURST_BAR_COVER_Y = 1

        #TRANSFORM THE BAR
        BURST_BAR_COVER = pygame.transform.scale(BURST_BAR_COVER,( 39, int(BURST_BAR_COVER_Y )))

        #DISPLAY THE BAR ON THE SCREEN
        SCREEN.blit(BURST_BAR_COVER,(BURST_COVER_X,BURST_COVER_Y))
        
        #if burst is greater than 186
        if BURST > 186:
            
            #burst will be 186
            BURST = 186
            
        #if burst is greater than 185
        if BURST > 185:
            
            #IF PLAYER PRESS KEY TO RELEASE BURST
            if KEY_PRESSED[K_d]:
                
                #this will play the burst sound
                BURST_SOUND.play()
                
                #this will set the burst timer
                BURST_TIMER = TIMER_FOR_KEY
                
                #ADD ONE TO MULTIPLIER
                MULTIPLIER += 1
                
                #RESET BURST + BURST BAR COVER
                BURST = 0
                
                #this will change the burst bar cover back
                BURST_BAR_COVER_Y = 185
                
                
        #if the multiplier is greater than 5
        if MULTIPLIER > 5:
            
            #multiplier will equal to 5
            MULTIPLIER = 5
            
        #this is the burst display
        #if the multiplier is 2
        if MULTIPLIER == 2:
            
            #this will blit the image onto the screen
            SCREEN.blit(BURST_DISPLAY_2,(180,0))
            
            #this will blit it onto the other side
            SCREEN.blit(BURST_DISPLAY_2_FLIP,(480,0))
            
        #these are the same after wards, the only different is the image
        elif MULTIPLIER == 3:
            SCREEN.blit(BURST_DISPLAY_3,(180,0))
            SCREEN.blit(BURST_DISPLAY_3_FLIP,(480,0))
        elif MULTIPLIER == 4:
            SCREEN.blit(BURST_DISPLAY_4,(180,0))
            SCREEN.blit(BURST_DISPLAY_4_FLIP,(480,0))
        elif MULTIPLIER == 5:
            SCREEN.blit(BURST_DISPLAY_5,(180,0))
            SCREEN.blit(BURST_DISPLAY_5_FLIP,(480,0))

        #if the burst time is over
        if BURST_TIMER + 1000 < TIMER_FOR_KEY:

            #multiplier will be back to 1
            MULTIPLIER = 1
            
            #burst time will be back to the high number
            BURST_TIMER = 999999
        
        #if the max combo is smaller then the combo
        if MAX_COMBO < COMBO:
            
            #combo will be max combo
            MAX_COMBO = COMBO
            
        #if the timner is greater than the song length
        if TIMER_FOR_KEY > SONG_LENGTH:
            
            #it will stop the music
            pygame.mixer.music.stop()
            
            #this will add all the song info
            #accuracy
            SONG_INFO.append(ACCURACY/TOTAL_KEY)
            
            #max combo
            SONG_INFO.append(MAX_COMBO)
            
            #score
            SONG_INFO.append(SCORE)
            
            #brings the player to the next page
            End_Game.WIN_CHECK(SONG_INFO)
        
        #the stat will be checked by the function
        STAT = CHECK_STAT(ACCURACY,TOTAL_KEY)
        
        #this will blit the stat
        SCREEN.blit(CLOCK_FONT.render(STAT, 1, THECOLORS['white']), (565,225))
        
        #this will update the screen
        pygame.display.flip()    
    
