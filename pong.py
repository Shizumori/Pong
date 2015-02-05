#!/usr/bin/env python3
import pygame
from random import randint
from pygame.locals import QUIT


class Ball(pygame.sprite.Sprite):
	
	def __init__(self,w, h, color):
		super().__init__()
		self.x_max, self.y_max = w, h
		self.x_speed = 1
		self.y_speed = 1
		self.width = 20
		self.height = 20
		self.x = randint(0, w-self.width)
		self.y = randint(0, h-self.height)
		
		self.image = pygame.Surface([self.width, self.height])
		self.image.fill(color)
		self.rect = self.image.get_rect()
		
		self.move_right = True
		self.move_down = True
	
	def bounce(self):
		self.move_right = not self.move_right
		
	def update(self):
	# Bounce on walls
		if self.x <= 0 or self.x + self.width >= self.x_max:
			self.move_right = not self.move_right
		if self.y <= 0 or self.y + self.height >= self.y_max:
			self.move_down = not self.move_down
 
		if self.move_right:
			self.x += self.x_speed
		else:
			self.x -= self.x_speed
		if self.move_down:
			self.y += self.y_speed
		else:
			self.y -= self.y_speed
 
		self.rect.x = self.x
		self.rect.y = self.y
		
class Latte(pygame.sprite.Sprite):
	
	def __init__(self,w, h, color):
		super().__init__()
		self.x_max, self.y_max = w, h
		self.width = 30
		self.height = 200
		self.x = 200
		self.y = 300
		
		self.image = pygame.Surface([self.width, self.height])
		self.image.fill(color)
		self.rect = self.image.get_rect()

	def update(self):
 
		self.rect.x = self.x
		self.rect.y = self.y		
 
if __name__ == '__main__':
	pygame.init()
	width = 1500
	height = 800
	window = pygame.display.set_mode((width, height))
	backg = (50, 60, 90)
	white = (255, 255, 255)
	clock = pygame.time.Clock()
 
	ball = Ball(width, height, white)
	latte1 = Latte(width,height, white)
	all_sprites_list = pygame.sprite.Group()
	all_sprites_list.add(ball)
	all_sprites_list.add(latte1)
	background = pygame.Surface(window.get_size())
 
	while True:
		for i in pygame.event.get():
			if i.type == QUIT:
				exit()
 
		window.fill(backg)
 
		all_sprites_list.update()
 
		if pygame.sprite.collide_rect(ball, latte1):
			ball.bounce()
			
		
		all_sprites_list.draw(window)
		clock.tick(120)
		pygame.display.flip() 
#du wells dass de 2 Latten geigeniwer hues mat nemmen enger Class
