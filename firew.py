import pygame
import pygame.sprite
import random
import pygame,math,sys,ball,fireballss,firew

class firework():
	def __init__(self,screen,x,y):
		self.screen=screen
		self.x=x
		self.y=y

		
	def arange(self,x,y,jump):
		while x<y:
			yield x 
			x+=jump
	def update(self,br):
		for angle in self.arange(0,math.pi*2,math.pi/30):
			
			
			xxx=math.cos(angle)*br
			yy=math.sin(angle)*br
			xxx=self.x+xxx
			yy=self.y+yy
			pygame.draw.circle(self.screen,(17,24,222),(int(xxx),int(yy)),1,0)


