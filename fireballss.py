import pygame
import pygame.sprite
import random;
class Fireball():
	
	def __init__(self,xpos,ypos,firell,xspeed,yspeed):
		self.x=xpos
		self.y=ypos
		self.firell=firell
		self.yspeed=yspeed
		self.xspeed=xspeed
		if xspeed>0:
			xf=True
		else:
			xf=False
		if yspeed>0:
			yf=False
		else:
			yf=True
		self.flip=pygame.transform.flip(firell,xf,yf)
	def update(self,screen):

		rect=screen.get_rect()
		#import pdb;pdb.set_trace()
		
			
		if self.x <= -1:

			self.xspeed=-self.xspeed
			self.fliph()
		elif self.x>rect.width-self.firell.get_rect().width:

			self.xspeed=-self.xspeed
				
		    	self.fliph()
		   		#print "fliped"
		    
			
	  	if self.y>rect.height-self.firell.get_rect().height:
		   	self.yspeed=-self.yspeed
		   	self.flipv()
		if self.y <= 1:

			self.yspeed=-self.yspeed
			self.flipv()
		   	'''
		    if self.y > rect.height-self.fireball.get_rect().height:
		    	self.yspeed=-5

		   	'''

		self.x=self.x+self.xspeed
		self.y=self.y+self.yspeed
	def draw(self,screen,alive):
		if alive:
			screen.blit(self.flip,(self.x,self.y))

	def fliph(self):
		self.flip=pygame.transform.flip(self.flip,True,False)


	def flipv(self):
		self.flip=pygame.transform.flip(self.flip,False,True)

		
