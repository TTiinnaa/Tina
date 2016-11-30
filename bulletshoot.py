import pygame
import pygame.sprite
import random
import pygame,math,sys,ball,fireballss,firew

class bulletshoots():
	def __init__(self,screen,(x,y)):
		self.rect=screen.get_rect()
		self.screen=screen
		self.x=x-self.rect.width/2
		self.y=(self.rect.height/2)-y
		self.angle=math.atan2(self.x,self.y)-math.pi/2
		self.br=80
		self.colors=random.randrange(255),random.randrange(255),random.randrange(255)
		self.xxx=self.x
		self.yy=self.y
		#import pdb;pdb.set_trace()
		
	def update(self,bulletspeed):
		
			
		
		self.xxx=math.cos(self.angle)*self.br
		self.yy=math.sin(self.angle)*self.br
		self.xxx=self.rect.width/2+self.xxx
		self.yy=self.rect.height/2+self.yy
		self.bullet=pygame.draw.circle(self.screen,(self.colors),(int(self.xxx),int(self.yy)),10,0)
		self.br=self.br+bulletspeed
		#import pdb;pdb.set_trace()
	def returnn(self):
		return self.bullet