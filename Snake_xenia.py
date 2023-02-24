import pygame
import random

pygame.init()

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
purple=(160,32,240)

FPS=15

display_width=800
display_height=600

gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Mr. Snake")

snake_size=10

clock=pygame.time.Clock()

font=pygame.font.SysFont(None,25)
medfont=pygame.font.SysFont(None,50)
largefont=pygame.font.SysFont(None,75)

def pause_game():
	pause=True
	while pause:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					pygame.quit()
					quit()
				elif event.key == pygame.K_c:
					pause=False
		gameDisplay.fill(red)
		message_on_screen("Game Paused",white,(display_width/2)-175,display_height/2)
		message_on_screen("Press C to continue or Q to quit",white,(display_width/2)-175,display_height/2+40)
		pygame.display.update()
		clock.tick(5)


def snake(snake_size,snakelist):
	for ele in snakelist:
		pygame.draw.rect(gameDisplay,black,[ele[0],ele[1],snake_size,snake_size])

def message_on_screen_medium(msg,color,x_message,y_message):
	screen_text=medfont.render(msg,True,color)
	gameDisplay.blit(screen_text,[x_message,y_message])

def message_on_screen_large(msg,color,x_message,y_message):
	screen_text=largefont.render(msg,True,color)
	gameDisplay.blit(screen_text,[x_message,y_message])

def message_on_screen(msg,color,x_message,y_message):
	screen_text=font.render(msg,True,color)
	gameDisplay.blit(screen_text,[x_message,y_message])

def loading_screen():
	load = True
	while load:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_c:
					load=False
				elif event.key==pygame.K_q:
					pygame.quit()
					quit()
		gameDisplay.fill(red)
		message_on_screen_large("Mr. Snake",green,(display_width/2)-250,display_height/2-100)
		message_on_screen("Welcome to Our game Mr. Snake",purple,(display_width/2)-250,display_height/2-10)
		message_on_screen("Objective of the game is to eat the white dot",purple,(display_width/2)-250,display_height/2+20)
		message_on_screen("Instructions:- Press C to play, Q to quit or P to pause the game",purple,(display_width/2)-250,display_height/2+50)
		pygame.display.update()
		clock.tick(5)

def gameloop():

	gameExit=False
	gameOver=False

	start_x=display_width/2
	start_y=display_height/2

	x_change=0
	y_change=0

	snakelist=[]
	snakelength=1

	rand_dot_x=round(random.randrange(0,display_width-snake_size)/10.0)*10.0
	rand_dot_y=round(random.randrange(0,display_height-snake_size)/10.0)*10.0

	prev=None

	while not gameExit:

		while gameOver==True:
			myfile=open('score.txt','r')
			score_text=myfile.readline()
			score_text=int(score_text)
			myfile.close()

			if snakelength-1 > score_text:
				f=open('score.txt','w')
				score=snakelength-1
				score=str(score)
				f.write(score)
				f.close()

			ff=open('score.txt','r')
			best_score=ff.readline()
			best_score=int(best_score)
			ff.close()

			gameDisplay.fill(red)
			message_on_screen("Hahaha You lose",white,(display_width/2)-175,display_height/2)
			message_on_screen("Press Q to quit or press C to play again",white,(display_width/2)-175,display_height/2+30)
			message_on_screen("Your score is : "+str(snakelength-1),white,(display_width/2)-175,display_height/2+60)
			message_on_screen("Best score till now is: "+str(best_score),white,(display_width/2)-175,display_height/2+90)
			pygame.display.update()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					gameExit=True
					gameOver=False
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						gameExit=True
						gameOver=False
					if event.key == pygame.K_c:
						gameloop()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit=True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_p:
					pause_game()
				elif event.key == pygame.K_LEFT and prev!=pygame.K_RIGHT:
					prev=pygame.K_LEFT
					x_change=-snake_size
					y_change=0
				elif event.key == pygame.K_RIGHT and prev!=pygame.K_LEFT:
					prev=pygame.K_RIGHT
					x_change=snake_size
					y_change=0
				elif event.key == pygame.K_UP and prev!=pygame.K_DOWN:
					prev=pygame.K_UP
					y_change=-snake_size
					x_change=0
				elif event.key == pygame.K_DOWN and prev!=pygame.K_UP:
					prev=pygame.K_DOWN
					y_change=snake_size
					x_change=0

		if start_x<0 or start_y<0 or start_x>=display_width or start_y>=display_height:
			gameOver=True

		start_x+=x_change
		start_y+=y_change
		gameDisplay.fill(red)
		pygame.draw.rect(gameDisplay,white,[rand_dot_x,rand_dot_y,snake_size,snake_size])

		snakehead=[]
		snakehead.append(start_x)
		snakehead.append(start_y)
		snakelist.append(snakehead)

		if len(snakelist) > snakelength:
			del(snakelist[0])

		for eachsegment in snakelist[:-1]:
			if eachsegment == snakehead:
				gameOver=True

		snake(snake_size,snakelist)
		message_on_screen(""+str(snakelength-1),black,display_width-100,20)
		pygame.display.update()



		if start_x==rand_dot_x and start_y==rand_dot_y:
			rand_dot_x=round(random.randrange(0,display_width-snake_size)/10.0)*10.0
			rand_dot_y=round(random.randrange(0,display_height-snake_size)/10.0)*10.0
			snakelength+=1

		clock.tick(FPS)

	pygame.quit()
	quit()

loading_screen()
gameloop()
