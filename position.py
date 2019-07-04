import pygame
import random
from pygame.locals import *
from constant import *



class Niveau:
    """Classe permettant de créer un niveau"""
    def __init__(self, fichier, fenetre):
        self.fichier = fichier
        self.structure = 0
        self.taille_sprite = 20
        self.fenetre = fenetre
        
        
        
    def generer(self):

        with open(self.fichier, "r") as fichier:
            structure_niveau = []
            for ligne in fichier:
                ligne_niveau = []
                
                for sprite in ligne:
                        #pass \n
                    if sprite != '\n':
                        ligne_niveau.append(sprite)
                structure_niveau.append(ligne_niveau)
            self.structure = structure_niveau
            
        
        
    def display(self, fenetre):
        wall = pygame.image.load("wall.png").convert()
        arrive = pygame.image.load("guard.png").convert()
        
        #lecture liste 
        num_ligne = 0
        for ligne in self.structure:
            num_case=0
            for sprite in ligne:
            #calcul position to pixels
                x = num_case * self.taille_sprite
                y = num_ligne * self.taille_sprite
                if sprite == "#":
                    self.fenetre.blit(wall, (x,y))
                    
                
                elif sprite == "G":
                    self.fenetre.blit(arrive, (x,y))
                num_case += 1
            num_ligne  += 1        
                
    
    def map(self):
        niveau = Niveau(fichier, fenetre)
        niveau.map.generer()
        niveau.display(fenetre)
            

class Perso:
	#Classe permettant de créer un personnage
	def __init__(self, path, niveau):
		#Sprites du personnage
		self.droite = "macgyver.png"
		#Position du personnage en cases et en pixels
		self.case_x = 0
		self.case_y = 0
		self.items = 0
		self.x = 0
		self.y = 0
		#Direction par défaut
		self.direction = self.droite
		#Niveau dans lequel le personnage se trouve 
		self.niveau = niveau
		self.sprite= pygame.image.load(path).convert_alpha()

	def chgsprite(self, path):
		self.sprite = pygame.image.load(path).convert_alpha()
	
	
	def deplacer(self, direction):
		"""Methode permettant de déplacer le personnage"""
		#nombre_sprite_cote = 15
		#taille_sprite = 20
		#Déplacement vers la droite
		if direction == 'droite':
			#Pour ne pas dépasser l'écran
			if self.case_x < (nombre_sprite_cote - 1):
				#On vérifie que la case de destination n'est pas un mur
				if self.niveau.structure[self.case_y][self.case_x+1] != '#':
					#Déplacement d'une case
					self.case_x += 1
					#Calcul de la position "réelle" en pixel
					self.x = self.case_x * taille_sprite
			
		
		#Déplacement vers la gauche
		if direction == 'gauche':
			if self.case_x > 0:
				if self.niveau.structure[self.case_y][self.case_x-1] != '#':
					self.case_x -= 1
					self.x = self.case_x * taille_sprite
			
		
		#Déplacement vers le haut
		if direction == 'haut':
			if self.case_y > 0:
				if self.niveau.structure[self.case_y-1][self.case_x] != '#':
					self.case_y -= 1
					self.y = self.case_y * taille_sprite
					
		#Déplacement vers le bas
		if direction == 'bas':
			if self.case_y < (nombre_sprite_cote - 1):
				if self.niveau.structure[self.case_y+1][self.case_x] != '#':
					self.case_y += 1
					self.y = self.case_y * taille_sprite
		
class Items:
	def __init__(self, name,  path, niveau):
		self.id = name
		self.niveau = niveau
		rand_x, rand_y = self.randpos()
		self.x = rand_x * taille_sprite
		self.y = rand_y * taille_sprite
		self.sprite = pygame.image.load(path).convert_alpha()
		

	def randpos(self):
		while True:
			rand_x = random.randrange(0, 14)
			rand_y = random.randrange(0, 14)
			if self.niveau.structure[rand_y][rand_x] == '.':
				self.niveau.structure[rand_y][rand_x] = self.id
				break

		return rand_x, rand_y

	def display(self, fenetre):
			print(self.x, self.y)
			fenetre.blit(self.sprite, (self.x, self.y))