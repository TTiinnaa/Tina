print "hello world"
import pygame
import pygame.sprite
import random;
class Ball():
	
	def __init__(self,(mxpos,mypos),screen,speedx,speedy):
		self.mxpos=mxpos
		self.mypos=mypos
		self.screen=screen
		self.rect=screen.get_rect()
		self.xpos = self.rect.width/2
		self.ypos = self.rect.height/2
		self.shooted = False
		self.k=0
		self.b=0
		self.speed=0.2
		self.alive=True
		self.speedx=speedx
		self.speedy=speedy
		self.color=random.choice([pygame.Color("BLUE"),pygame.Color("azure3")])
		self.colors=random.randrange(255),random.randrange(255),random.randrange(255)
	def update(self,time_passed):
		if self.alive:
			self.xpos = int(self.xpos+self.speedx*time_passed*self.speed)
			self.ypos = int(self.ypos+self.speedy*time_passed*self.speed)
		if self.xpos>self.rect.width:
			self.alive=False
		if self.xpos<0:
			self.alive=False
		if self.ypos>self.rect.height:
			self.alive=False
		if self.ypos<0:
			self.alive=False
	def draw(self):
		if self.alive:
			
			pygame.draw.circle(self.screen,self.colors,(self.xpos,self.ypos),5,0)

	

