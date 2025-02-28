import pygame
import random
import sys

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.SysFont('Pixelify Sans Regular', 35)
font_game_over = pygame.font.SysFont('Pixelify Sans Regular', 60)

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 768
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Targetz Shooter")

# Classe do Botão
class Button:
    def __init__(self, x, y, image_path):
        self.image = pygame.image.load(image_path)  
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, (0, 200, 0), self.rect, 5)
        screen.blit(self.image, self.rect)

# Classe do Alvo
class Target(pygame.sprite.Sprite):
    def __init__(self, x, y, is_bomb=False):
        super().__init__()
        self.is_bomb = is_bomb
        if self.is_bomb:
            self.image = pygame.image.load('bomba.png')
        else:
            self.image = pygame.image.load('alvo.png')
        
        self.image = pygame.transform.scale(self.image, (90, 90))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

# Classe do Jogo
class Game:

# Função que exibe a tela de Game Over
def game_over():


# Função que exibe a tela de créditos
def credits_screen():


# Função que exibe a tela de dificuldade
def difficulty_screen():


# Função que exibe o menu
def main_menu():


def main():