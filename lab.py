import pygame
import random
from pygame.locals import * 
from constant import *
from position import*
pygame.init()

fichier = "lab.txt"

#ouverture de la fenetre pygame
nombre_sprite_cote = 15
taille_sprite = 20
cote = nombre_sprite_cote * taille_sprite
fenetre = pygame.display.set_mode((cote, cote))
#élément graphique
fond = pygame.image.load("background.jpg").convert()
fenetre.blit(fond, (0, 10))
wall = pygame.image.load("wall.png").convert()
arrive = pygame.image.load("guard.png").convert()
fenetre.blit(wall,(0, 40))
niveau = Niveau(fichier, fenetre)
niveau.generer()
niveau.display(fenetre)


#objet
c_ether = "ether.png"
ether = Items("E", c_ether, niveau)
ether.display(fenetre)
c_tube = "tube.png"
tube = Items("T", c_tube, niveau)
tube.display(fenetre)
c_needle ="needle.png"
needle = Items("N", c_needle, niveau)
needle.display(fenetre)


#titre
pygame.display.set_caption("EscapeMacGyver")
taille_perso = taille_sprite * taille_sprite


pygame.display.flip()
pygame.key.set_repeat(400,30)


continuer_jeu = 1

TubeNotPicked = True
EtherNotPicked = True
NeedleNotPicked = True

GAME_WON = False
GAME_LOOSE = False

guard = pygame.image.load("guard.png").convert_alpha()
mac = Perso("macgyver.png", niveau)
fenetre.blit(mac.sprite, (mac.x, mac.y))


while continuer_jeu:
	pygame.display.flip()
	pygame.time.Clock().tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			continuer_jeu = 0
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_DOWN:
				mac.deplacer("bas")
			if event.key == pygame.K_UP:
				mac.deplacer("haut")
			if event.key == pygame.K_LEFT:
				mac.deplacer("gauche")
			if event.key == pygame.K_RIGHT:
				mac.deplacer("droite")

	
	fenetre.blit(fond, (0, 0))
	niveau.display(fenetre)
	fenetre.blit(mac.sprite, (mac.x, mac.y))

	
	if TubeNotPicked:
		fenetre.blit(tube.sprite, (tube.x, tube.y))
	if (mac.x, mac.y) == (tube.x, tube.y):
		TubeNotPicked = False
	if TubeNotPicked == False:
		tube.x, tube.y = 10, 0
		fenetre.blit(tube.sprite, (10, 0))

		
	if NeedleNotPicked:
		fenetre.blit(needle.sprite, (needle.x, needle.y))
	if (mac.x, mac.y) == (needle.x, needle.y):
		NeedleNotPicked = False
	if NeedleNotPicked == False:
		needle.x, needle.y = 30, 0
		fenetre.blit(needle.sprite, (30, 0))

		
	if EtherNotPicked:
		fenetre.blit(ether.sprite, (ether.x, ether.y))
	if (mac.x, mac.y) == (ether.x, ether.y):
		EtherNotPicked = False
	if EtherNotPicked == False:
		ether.x, ether.y = 50, 0
		fenetre.blit(ether.sprite, (50, 0))
	

	#Endgame condition
	if niveau.structure[mac.case_y][mac.case_x] == 'G': 
		if TubeNotPicked is False and NeedleNotPicked is False and EtherNotPicked is False:
			GAME_WON = True
		else:
			GAME_LOOSE = True
		
		
	if GAME_WON is True:
		fenetre.blit(fond, (0, 0))
		font = pygame.font.Font(None, 25)
		text = font.render("You won! you escaped from these walls !", 1, (255, 255, 255))
		textrect = text.get_rect()
		textrect.centerx, textrect.centery = cote / 2, cote / 2
		fenetre.blit(text, textrect)

	
	if GAME_LOOSE is True:
		fenetre.blit(fond, (0, 0))
		font = pygame.font.Font(None, 25)
		text = font.render("You died.", 1, (255 , 255, 255))
		textrect = text.get_rect()
		textrect.centerx, textrect.centery = cote / 2, cote / 2
		fenetre.blit(text, textrect)