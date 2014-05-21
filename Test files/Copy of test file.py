import End_Game
import MUSIC_GAME_FINAL
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

#Joystick.init()
'''while True:

    #print guitar.get_numbuttons()
    print guitar.get_numbuttons()
    print guitar.get_button(0)
    print guitar.get_button(1)
    print guitar.get_button(2)
    print guitar.get_button(3)
    print guitar.get_button(4)
    print guitar.get_button(5)
    print guitar.get_button(6)
    print guitar.get_button(7)
    print guitar.get_button(8)
    print guitar.get_button(9)
    system('cls')

if e.type == KEYDOWN:
    if e.key == K_a:
            music.play()
    if e.key == K_s:
            music1.play()
music = pygame.mixer.Sound('skill_explo_113.ogg')
music1 = pygame.mixer.Sound('skill_explo_114.ogg')


import pygame, pygame.joystick

pygame.init()
pygame.joystick.init()

if pygame.joystick.get_init():
  count = pygame.joystick.get_count()
  for i in range(0,count):
    joystick = pygame.joystick.Joystick(i)
    joystick.init()
    if joystick.get_init():
      while True:
          print guitar.get_button(0)'''

#import pygame
#from pygame import locals


#pygame.init()


#pygame.joystick.init() # main joystick device system


#try:
#	j = pygame.joystick.Joystick(0) # create a joystick instance
#	j.init() # init instance
#	print 'Enabled joystick: ' + j.get_name()
#except pygame.error:
#	print 'no joystick found.'
#

while True:
	for e in pygame.event.get():
		
		print guitar.get_button(0),'1'
		print guitar.get_button(1),'2'
		print guitar.get_button(2),'3'
		print guitar.get_button(3),'4'
		print guitar.get_button(4),'5'
		print guitar.get_button(5),'6'
		print guitar.get_button(6),'7'
		print guitar.get_button(7),'8'
		print guitar.get_button(8),'9'
		print guitar.get_button(9),'0'
#print 'hi'# iterate over event stack
		#print 'event : ' + str(e.type)
		#if e.type == pygame.locals.JOYAXISMOTION: # 7
			#x , y = j.get_axis(0), j.get_axis(1)
			#print 'x and y : ' + str(x) +' , '+ str(y)
		#if e.type == pygame.locals.JOYBALLMOTION: # 8
		#	print 'ball motion'
		if e.type == pygame.locals.JOYHATMOTION: # 9
			print 'hat motion'
		#elif e.type == pygame.locals.JOYBUTTONDOWN: # 10
		#	if guitar.get_button(0) == 1:
		#		print 'hi'
		#	print guitar.get_button(1)
		#	print guitar.get_button(2)
		#	print guitar.get_button(3)
		#	print guitar.get_button(4)
		#	print guitar.get_button(5)
		#	print guitar.get_button(6)
		#	print guitar.get_button(7)
		#	print guitar.get_button(8)
		#	print guitar.get_button(9)
		#	print 'button down'
		#elif e.type == pygame.locals.JOYBUTTONUP: # 11
		#	print 'button up'


      