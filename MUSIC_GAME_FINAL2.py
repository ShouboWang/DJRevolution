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
# 
# 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#This will import all the necessary item
import pygame, sys,os, time
from pygame.locals import * 
from pygame.color import THECOLORS
import random
import time
import Def
import End_Game
import platform, os

import End_Game
import SCORE_DISPLAY
import Def
import Control
import pygame, sys,os, time
from os import system
from pygame.locals import * 
from pygame.color import THECOLORS
import platform, os 
SONG_INFO = ['GUEST', 1700, 25, 'VIRUS.ogg', 'VIRUS', 22000, 1, 1, 5, 50, 'white',99999999,8,51010]
#MUSIC_GAME_FINAL.Main(SONG_INFO) 
pygame.init() 
guitar = pygame.joystick.Joystick(0)
guitar.init()

#Solve the window problem
if platform.system() == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'


#initalize pygame and music
pygame.init() 
pygame.mixer.init()


#WINDOW SIZE + SCREEN
WINSIZE = pygame.display.set_mode((700, 700))
SCREEN = pygame.display.get_surface()

class KEY_PRESSED_VAL(object):
    def __init__(self,NAME):
        self.NAME = NAME
        
    def KEY_ACC(self,NOTE_TIME,PRESS_TIME,KEY_SPICAL_ACC,DELAY):
        BALANCER = 100 / DELAY
        self.KEY_ACCURACY = (int(NOTE_TIME) - int(PRESS_TIME)) * BALANCER
        if self.KEY_ACCURACY < 0:
            self.KEY_ACCURACY = self.KEY_ACCURACY * -1
        self.KEY_ACCURACY = int(100 - self.KEY_ACCURACY) + KEY_SPICAL_ACC 
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
        return self.KEY_ACCURACY
    
    def COMBO_CAL(self,MULTIPLIER):
        COMBO = MULTIPLIER * 1
        return COMBO
    
    def SCORE_CAL(self,KEY_ACCURACY,COMBO,MULTIPLIER,KEY_SPICAL_SCORE,SPEED):
        SCORE = int(((KEY_ACCURACY * MULTIPLIER * (1 + COMBO / 50.0)*10) + KEY_SPICAL_SCORE)*SPEED/2)
        return SCORE
    
    def DMG_CAL(self,LIFE_GAIN,KEY_ACCURACY,KEY_SPICAL_HEAL):
        DMG = KEY_ACCURACY * LIFE_GAIN / 10 + KEY_SPICAL_HEAL
        return DMG
    def BURST_CAL(self,KEY_ACCURACY,BURST_GAIN,KEY_SPICAL_BURST):
        BURST = KEY_ACCURACY * BURST_GAIN + KEY_SPICAL_BURST
        return BURST
    
class NOTE_CRATE(object):
    def __init__(self,FILE,TIMER_FOR_KEY,SPEED,NOTE_COLOR,X_POS):
        self.START = 0 - 556 * (SPEED - 1)
        self.LENGTH = len(FILE)
        self.NOTE = FILE
        self.TIMER = TIMER_FOR_KEY
        self.SPEED = SPEED
        self.COLOR = NOTE_COLOR
        self.X_POS = X_POS
    def NOTE_SHOW(self):
        for X in xrange(0,self.LENGTH):
            if int(self.NOTE[X]) - self.TIMER < 100:
                Y_POS = self.START
                Y_POS += int(556*self.SPEED-(int(self.NOTE[X]) - self.TIMER) * 5.56 * self.SPEED)
                pygame.draw.circle(SCREEN, THECOLORS[self.COLOR], (self.X_POS,int(Y_POS)), 20)
                if Y_POS > 556:
                    self.NOTE.pop(0)
                    return self.NOTE
            else:
                return self.NOTE
            
            
            
            
            
def OPEN_FILE(PATH):
    OPEN=open(PATH,'r')
    FILE_1 = OPEN.readlines()
    OPEN.close()
    OPEN=open(PATH,'r')
    FILE_2 = OPEN.readlines()
    OPEN.close()
    return FILE_1,FILE_2


def KEY_COLOR():
    COLOR = random.choice(['blue','yellow','green','white','brown','red','orange','purple','pink','steelblue','greenyellow'])
    return COLOR

def CHECK_SPEED(SPEED):
    if SPEED > 5:
        SPEED = 5
    elif SPEED < 1:
        SPEED = 1
    else:
        SPEED = SPEED
    return SPEED




def CHECK_STAT(ACCURACY,TOTAL_KEY):
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
    elif ACCURACY/TOTAL_KEY <= 40:
        STAT = 'Horrible'
        return STAT
def Main(SONG_INFO):
    print SONG_INFO
    #set up all the variables
    DELAY = SONG_INFO[6]    
    SONG = SONG_INFO[8]
    NOTE_FILE  = SONG_INFO[9]
    SONG_LENGTH = SONG_INFO[10]
    KEY_SPICAL_ACC = SONG_INFO[11]
    KEY_SPICAL_SCORE = SONG_INFO[12]
    KEY_SPICAL_HEAL = SONG_INFO[13]
    KEY_SPICAL_BURST = SONG_INFO[14]
    NOTE_COLOR = SONG_INFO[15]
    
    
    
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


    SCREEN.blit(BACKGROUND,(0,0))
       
    
    
    
    COMBO = 0
    DMG = 2
    SCORE = 0
    BURST = 0
    MULTIPLIER = 1
    ACCURACY = 100
    NEXT_NOTE = 1
    TOTAL_KEY = 1
    LIFE_LOSE = 0
    BREAK = False
    MISS = False
    TIMER = 0
    
    
    
    #list 
    NOTE_1_FIRST = 0
    NOTE_2_FIRST = 0
    NOTE_3_FIRST = 0
    NOTE_4_FIRST = 0
    
    
    
    
    
    
    
    #NOTE
    KEY_1_TURN = 0
    KEY_2_TURN = 0
    KEY_3_TURN = 0
    KEY_4_TURN = 0
    KEY_ACCURACY = 100
    #BRUST BAR LOCATION
    BURST_X = 62
    BURST_Y = 421
    BURST_GAIN = 0.074#0.074
    BURST = 0
    BRUST_ALLOW = False
    BURST_TIMER = 999999
    
    #BRUST BAR COVER
    BURST_COVER_X = 62
    BURST_COVER_Y = 421
    
    #LIFE BAR LOCATION
    LIFE_X = 535
    LIFE_Y = 360
    LIFE_GAIN = 0.082
    LIFE_LOSE = 32.8
    DMG = 0
    LIFE = 328
    
    #LIFE BAR COVER
    LIFE_COVER_X = 535
    LIFE_COVER_Y = 360
    
    #list 
    
    LIST_NOTE_1 = []
    LIST_NOTE_2 = []
    LIST_NOTE_3 = []
    LIST_NOTE_4 = []
    #make the list just for the note
    
    
    list_1_test = []
    list_2_test = []
    list_3_test = []
    list_4_test = []
    
    SPEED = 1
    START_POINT = 0 - 556 * (SPEED - 1)
    
    
    MUSIC = pygame.mixer.music.load(os.path.join("MUSIC",SONG))
    pygame.mixer.music.play()
    
    
    MAX_COMBO = 0
    ACC_COLOR = KEY_COLOR()
    while True:
        
        #This is the start point for the notes
        START_POINT = 0 - 556 * (SPEED - 1)
        if COMBO < 100:
            SCREEN.blit(BACKGROUND,(0,0))
        elif COMBO >=100 and COMBO< 200:
            SCREEN.blit(BACKGROUND_2,(0,0))
        elif COMBO >=200:
            SCREEN.blit(BACKGROUND_3,(0,0))   
        
        
        #TIMER 
        MILLISEC = CLOCK.tick() #Gets the time in milliseconds
        SECONDS = MILLISEC / 1000.0 #this will change millisec into seconds
        TIMER_FOR_KEY = int(TIMER/10) #THis will get time in 10milliseconds
        TIMER += SECONDS*1000 #this will add milliseconds into the timer
        ROUGH_SEC = int(TIMER/1000) + 0.0 #This will get time in seconds and in float form
        CLOCK_MIN = int(ROUGH_SEC /60) #this is the display on the clock for minutes
        CLOCK_SEC = int((ROUGH_SEC / 60 - CLOCK_MIN) * 60) #this is seconds
        FINAL_CLOCK = str(CLOCK_MIN)+':'+str(CLOCK_SEC) #this will display time on the screen
        text=CLOCK_FONT.render(FINAL_CLOCK, True, THECOLORS["black"]) #Display on the screen
        
        
        
        NOTE_1 = NOTE_CRATE(KEY_FOR_NOTE1,TIMER_FOR_KEY,SPEED,NOTE_COLOR,220)
        NOTE_FOR_CRATE_1 = NOTE_1.NOTE_SHOW()
        NOTE_2 = NOTE_CRATE(KEY_FOR_NOTE2,TIMER_FOR_KEY,SPEED,NOTE_COLOR,300)
        NOTE_FOR_CRATE_2 = NOTE_2.NOTE_SHOW()
        NOTE_3 = NOTE_CRATE(KEY_FOR_NOTE3,TIMER_FOR_KEY,SPEED,NOTE_COLOR,390)
        NOTE_FOR_CRATE_3 = NOTE_3.NOTE_SHOW()
        NOTE_4 = NOTE_CRATE(KEY_FOR_NOTE4,TIMER_FOR_KEY,SPEED,NOTE_COLOR,480)
        NOTE_FOR_CRATE_4 = NOTE_4.NOTE_SHOW()
    
        if BREAK == False:
            #MAKE SURE THAT THE KEY ACCURACY ID NOT IN NEGATIVE
            if KEY_ACCURACY < 0:
                KEY_ACCURACY = KEY_ACCURACY * -1
            #SHOWS ACCURACY OF THE KEY PRESSED
            SCREEN.blit(CLOCK_FONT.render(str(KEY_ACCURACY)+"%", 1, THECOLORS[ACC_COLOR]), (310,500))
        
        if BREAK == True:
            SCREEN.blit(CLOCK_FONT.render("BREAK", 1, THECOLORS['red']), (310,500))
            
            
        KEY_PRESSED = pygame.key.get_pressed()
        if KEY_PRESSED[K_a]:
            SCREEN.blit(KEY_PRESS_1,(169,630))
            SCREEN.blit(BAR,(174,562))
        if KEY_PRESSED[K_s]:
            SCREEN.blit(KEY_PRESS_2,(259,630))
            SCREEN.blit(BAR,(264,562))
        if KEY_PRESSED[K_k]:
            SCREEN.blit(KEY_PRESS_3,(349,630))
            SCREEN.blit(BAR,(354,562))
   #     for event in pygame.event.get():    
   #         if event.type == KEYDOWN:
   #             if event.key == K_z:
   #                 list_1_test.append(TIMER_FOR_KEY)
   #             if event.key == K_x:
   #                 list_2_test.append(TIMER_FOR_KEY)
   #             if event.key == K_n:
   #                 list_3_test.append(TIMER_FOR_KEY)
   #             if event.key == K_m:
   #                 list_4_test.append(TIMER_FOR_KEY)
   #             if event.key == K_q:
   #                 print "Key 1"
   #                 for x in list_1_test:
   #                     print x
   #                 print "Key 2"
   #                 for x in list_2_test:
   #                     print x
   #                 print "Key 3"
   #                 for x in list_3_test:
   #                     print x
   #                 print "Key 4"
   #                 for x in list_4_test:
   #                     print x        
        for event in pygame.event.get():
            if guitar.get_button(0) == 1:
                if int(KEY_1_PRESS[KEY_1_TURN]) + DELAY > TIMER_FOR_KEY and int(KEY_1_PRESS[KEY_1_TURN]) - DELAY < TIMER_FOR_KEY and event.type == pygame.locals.JOYHATMOTION:
                    ACC_COLOR = KEY_COLOR()
                    KEY_PRESSED_A = KEY_PRESSED_VAL('KEY_PRESSED_A')
                    NOTE_TIME = KEY_1_PRESS[KEY_1_TURN]
                    PRESS_TIME = TIMER_FOR_KEY
                    KEY_ACCURACY = KEY_PRESSED_A.KEY_ACC(NOTE_TIME,PRESS_TIME,KEY_SPICAL_ACC,DELAY)
                    ACCURACY += KEY_ACCURACY
                    COMBO += KEY_PRESSED_A.COMBO_CAL(MULTIPLIER)
                    SCORE += KEY_PRESSED_A.SCORE_CAL(KEY_ACCURACY,COMBO,MULTIPLIER,KEY_SPICAL_SCORE,SPEED)
                    DMG -= KEY_PRESSED_A.DMG_CAL(LIFE_GAIN,KEY_ACCURACY,KEY_SPICAL_HEAL)
                    BURST += KEY_PRESSED_A.BURST_CAL(KEY_ACCURACY,BURST_GAIN,KEY_SPICAL_BURST)
                    BREAK = False
                    TOTAL_KEY += 1
                    #NOTE_1_FIRST += 1 
                    KEY_1_TURN += NEXT_NOTE
                    #print KEY_1_TURN,BURST,TOTAL_KEY,DMG,COMBO,KEY_ACCURACY,SCORE
                
                
                
            if guitar.get_button(1) == 1:
                print 'hi2'
                if int(KEY_2_PRESS[KEY_2_TURN]) + DELAY > TIMER_FOR_KEY and int(KEY_2_PRESS[KEY_2_TURN]) - DELAY < TIMER_FOR_KEY and event.type == pygame.locals.JOYHATMOTION:
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
                    #NOTE_2_FIRST += 1 
                    KEY_2_TURN += NEXT_NOTE
                    #print KEY_1_TURN,BURST,TOTAL_KEY,DMG,COMBO,KEY_ACCURACY,SCORE
                
                
                
            if guitar.get_button(3) == 1:
                if int(KEY_3_PRESS[KEY_3_TURN]) + DELAY > TIMER_FOR_KEY and int(KEY_3_PRESS[KEY_3_TURN]) - DELAY < TIMER_FOR_KEY and event.type == pygame.locals.JOYHATMOTION:
                    SCREEN.blit(KEY_PRESS_4,(439,630))
                    SCREEN.blit(BAR,(444,562))
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
                    #NOTE_3_FIRST += 1 
                    KEY_3_TURN += NEXT_NOTE
                    #print KEY_1_TURN,BURST,TOTAL_KEY,DMG,COMBO,KEY_ACCURACY,SCORE
                
                
                
            if guitar.get_button(2) == 1:
                print 'hi4'
                if int(KEY_4_PRESS[KEY_4_TURN]) + DELAY > TIMER_FOR_KEY and int(KEY_4_PRESS[KEY_4_TURN]) - DELAY < TIMER_FOR_KEY and event.type == pygame.locals.JOYHATMOTION:
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
                    #NOTE_4_FIRST += 1 
                    KEY_4_TURN += NEXT_NOTE
                    #print KEY_1_TURN,BURST,TOTAL_KEY,DMG,COMBO,KEY_ACCURACY,SCORE
            if BURST > 185:
                #IF PLAYER PRESS KEY TO RELEASE BURST
                if guitar.get_button(4) == 1:
                    BURST_SOUND.play()
                    BURST_TIMER = TIMER_FOR_KEY
                    #ADD ONE TO MULTIPLIER
                    MULTIPLIER += 1
                    #RESET BURST + BURST BAR COVER
                    BURST = 0
                    BURST_BAR_COVER_Y = 185
            if guitar.get_button(6) == 1:
                SPEED += 0.2
            if guitar.get_button(7) == 1:
                SPEED -= 0.2
                    
        
        SPEED = CHECK_SPEED(SPEED)
            
        #print len(KEY_1_PRESS)
                
        if int(KEY_1_PRESS[KEY_1_TURN]) + DELAY < TIMER_FOR_KEY:
            KEY_1_TURN += 1
            MISS = True   
        if int(KEY_4_PRESS[KEY_4_TURN]) + DELAY < TIMER_FOR_KEY:
            KEY_4_TURN += 1
            MISS = True
        if int(KEY_2_PRESS[KEY_2_TURN]) + DELAY < TIMER_FOR_KEY:
            KEY_2_TURN += 1
            MISS = True        
        if int(KEY_3_PRESS[KEY_3_TURN]) + DELAY < TIMER_FOR_KEY:
            KEY_3_TURN += 1
            MISS = True            
            
            
            
            
        if MISS == True:
            COMBO = 0
            ACCURACY = ACCURACY + 0
            TOTAL_KEY +=1
            DMG += LIFE_LOSE
            BREAK = True
            MISS = False  
        
            
            
        SCREEN.blit(BURST_BAR,(BURST_X,BURST_Y))
        SCREEN.blit(LIFE_BAR,(LIFE_X,LIFE_Y))
        SCREEN.blit(CLOCK_FONT.render('speed:'+str(SPEED), 1, THECOLORS['red']), (320,50))
        SCREEN.blit(CLOCK_FONT.render(str(int(SCORE)), 1, THECOLORS['white']), (25,88))
        SCREEN.blit(CLOCK_FONT.render(str(ACCURACY/TOTAL_KEY)+'%', 1, THECOLORS['white']), (590,88))
        SCREEN.blit(CLOCK_FONT.render(str(int(COMBO)), 1, THECOLORS['white']), (25,230))
        SCREEN.blit(CLOCK_FONT.render(FINAL_CLOCK, 1, THECOLORS['white']), (350,0))
        Def.CHECK_MISSION_GAME(SONG_INFO)
        if DMG < 0:
            DMG = 0
        #CHANGE THE LENGTH OF THE LIFE BAR
        LIFE_BAR_LEN = 1 + int(DMG)
        
        
        
        if DMG > 328:
            pygame.mixer.music.stop()
            End_Game.DEATH(SONG_INFO)
        #THIS WILL TRANDFORM THE LIFE BAR
        #print DMG
        LIFE_BAR_COVER = pygame.transform.scale(LIFE_BAR_COVER,( 38, LIFE_BAR_LEN ))
        #PRINTS IT ON THE SCREEN
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
        if BURST > 186:
            BURST = 186
                
                
                
        if MULTIPLIER > 5:
            MULTIPLIER = 5
        if MULTIPLIER == 2:
            SCREEN.blit(BURST_DISPLAY_2,(180,0))
            SCREEN.blit(BURST_DISPLAY_2_FLIP,(480,0))
        elif MULTIPLIER == 3:
            SCREEN.blit(BURST_DISPLAY_3,(180,0))
            SCREEN.blit(BURST_DISPLAY_3_FLIP,(480,0))
        elif MULTIPLIER == 4:
            SCREEN.blit(BURST_DISPLAY_4,(180,0))
            SCREEN.blit(BURST_DISPLAY_4_FLIP,(480,0))
        elif MULTIPLIER == 5:
            SCREEN.blit(BURST_DISPLAY_5,(180,0))
            SCREEN.blit(BURST_DISPLAY_5_FLIP,(480,0))

            
        if BURST_TIMER + 1000 < TIMER_FOR_KEY:
            MULTIPLIER = 1
            BURST_TIMER = 999999
        if MAX_COMBO < COMBO:
            MAX_COMBO = COMBO
        if TIMER_FOR_KEY > SONG_LENGTH:
            pygame.mixer.music.stop()
            SONG_INFO.append(ACCURACY/TOTAL_KEY)
            SONG_INFO.append(MAX_COMBO)
            SONG_INFO.append(SCORE)
            End_Game.WIN(SONG_INFO)
        #print BURST
        
        STAT = CHECK_STAT(ACCURACY,TOTAL_KEY)
        SCREEN.blit(CLOCK_FONT.render(STAT, 1, THECOLORS['white']), (565,225))
        pygame.display.flip()    
    
