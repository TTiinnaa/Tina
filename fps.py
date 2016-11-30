import pygame,math,sys,ball,fireballss,firew,bulletshoot,random

# Initialize Pygame.

def detect_clicked_direction(pos,screen):
	x,y=pos
	sxs=screen.get_rect().width/3*2
	sys=screen.get_rect().height/3*2
	sxf=screen.get_rect().width/3
	syf=screen.get_rect().height/3
	#import pdb;pdb.set_trace()
	if x<sxf:
		if y<syf:
			return (-1,-1)
		elif y<sys:
			return(-1,0)
		else:
			return(-1,1)
	elif x<sxs:
		if y<syf:
			return (0,-1)
		elif y<sys:
			return[]
		else:
			return(0,1)
	else:
		if y<syf:
			return (1,-1)
		elif y<sys:
			return(1,0)
		else:
			return(1,1)


def distance((x,y),(xx,yy)):

	return math.sqrt(math.pow(x-xx,2)+math.pow(y-yy,2))
	




def arange(x,y,jump):
	while x<y:
		yield x 
		x+=jump

def fireworks(r,screen):
	for angle in arange(0,math.pi*2,math.pi/30):
			
			rect=screen.get_rect()
			x=math.cos(angle)*r
			y=math.sin(angle)*r
			x=x+rect.width/2
			y=y+rect.height/2
			pygame.draw.circle(screen,(17,24,222),(int(x),int(y)),1,0)



def letsplay():
	pygame.init()
	screenlen=850
	screenwit=400
	# Set size of pygame window.
	screen=pygame.display.set_mode((screenlen,screenwit))
	# Create empty pygame surface.
	background = pygame.Surface(screen.get_size())
	# Fill the background white color.
	background.fill((255, 255, 255))
	# Convert Surface object to make blitting faster.
	background = background.convert()
	# Copy background to screen (position (0, 0) is upper left corner).
	vol=pygame.image.load("vol.jpg")
	screen.blit(vol, (0,0))
	# Create Pygame clock object.  
	clock = pygame.time.Clock()

	fireballsurf = pygame.display.set_mode((screenlen,screenwit))

	mainloop = True
	# Desired framerate in frames per second. Try out other values.              
	FPS = 30
	# How many seconds the "game" is played.
	playtime = 0.0

	fireball=pygame.image.load("fireball.png")
	canon=pygame.image.load("canon.png")

	#variables
	rect=screen.get_rect()
	score=0
	x=0
	y=0
	r=0
	speed=5
	xspeed=speed
	yspeed=speed
	mouse_pressed = False
	Alive=True
	bullets=[]
	balls=[]
	fire=[fireballss.Fireball(400,70,fireball,20,10),fireballss.Fireball(300,20,fireball,3,-2)]
	myfont = pygame.font.SysFont("monospace", 16)

	firewo2=firew.firework(screen,200,200)
	while mainloop:
	    # Do not go faster than this framerate.
	    milliseconds = clock.tick(FPS) 
	    playtime += milliseconds / 1000.0 
	    
	    for event in pygame.event.get():
	        # User presses QUIT-button.
	        if event.type == pygame.QUIT:
	            mainloop = False 
	        elif event.type == pygame.KEYDOWN:
	            # User presses ESCAPE-Key
	            if event.key == pygame.K_ESCAPE:
	                mainloop = False
	                
	    # Print framerate and playtime in titlebar.
	    text = "FPS: {0:.2f}   Playtime: {1:.2f}".format(clock.get_fps(), playtime) +"   your score is "+ str(score)
	    pygame.display.set_caption(text)
		


	    #pygame.display.set_icon(pygame.image.load("logo.png"))
	    screen.blit(vol, (0,0))
	    #fireball part this part is all about the fire ball

	    '''
	    if x>rect.width-fireball.get_rect().width:
	    	xspeed=-5
	    	
	    	pygame.transform.flip(fireball,False,True)
	    elif x<0:
	    	xspeed=5

	    if y>rect.height-fireball.get_rect().height:
	    	yspeed=-5
	    elif y<0:
	    	
	    	yspeed=5
	    x=x+xspeed
	    y=y+yspeed
	    screen.blit(fireball,(x,y))
'''

	    pos = pygame.mouse.get_pos()
	    

	    '''
	    #fireworks 
	    fireworks(r,screen)
	    r+=0.1

	    firewo2.update(r)

	    for f in fire:
	    	f.update(fireballsurf)
	    	f.draw(fireballsurf)

		'''
	    
	    angle = 360-math.atan2(pos[1]-200,pos[0]-425)*180/math.pi
	    rotimage = pygame.transform.rotate(canon,angle)
	    rects = rotimage.get_rect(center=(425,200))
	    screen.blit(rotimage,rects)
	    
	    #import pdb;pdb.set_trace()
	    pygame.event.get()

	    if len(fire)<1:
	    	fire.append(fireballss.Fireball(random.randrange(100,rect.width-100),random.randrange(100,rect.height-100),fireball,random.randrange(1,20),random.randrange(1,20)))
			

	    if pygame.mouse.get_pressed() ==(1,0,0) and mouse_pressed==False:
	    	print("pressed")
	    	mouse_pressed=True

	    	spd=detect_clicked_direction(pos,screen)
	   

	    	#import pdb;pdb.set_trace()
	    	'''
	    	if spd:
	    		spx,spy=spd
	    		balls.append(ball.Ball(pos,screen,spx,spy))
			'''
	    	bullets.append(bulletshoot.bulletshoots(screen,pos))

	    else:
	    	
	    	if  pygame.mouse.get_pressed() !=(1,0,0):
	    		 mouse_pressed=False
	    if bullets:
			for bu in bullets:
				bu.update(5)
	    if balls:
		    for bal in balls:
		    	bal.update(milliseconds)

		    for bal in balls:
		    	bal.draw()
	    if fire:
		    for f in fire:
		    	f.update(screen)

		    for f in fire:
		    	for bu in bullets:

		    		if distance((f.x+50,f.y+50),(bu.xxx,bu.yy))<50:
		    			print ("hahahah")
		    			score+=1
		    			if f in fire:
		    				fire.remove(f)
		    			if bu in bullets:
		    				bullets.remove(bu)
		    			Alive=False
		    		f.draw(screen,Alive)
		    		Alive=True

		    	
		
		


	    pygame.display.flip()







	# Finish Pygame.  
	pygame.quit()

	# At the very last:
	print("This game was played for {0:.2f} seconds".format(playtime))

letsplay()