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
    def __init__(self, difficulty):
        self.score = 0
        self.lives = 3
        self.targets = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        self.difficulty = difficulty
        
        self.spawn_rate = 0.06  # Taxa de spawn de alvos
        self.bomb_chance = 0.2  # Chance de bomba

        if difficulty == 'Hard':
            self.bomb_chance = 0.5  
            self.time_limit = 45
        else:
            self.time_limit = 60
        
        self.time_left = self.time_limit  
        self.spawn_rate = 0.06

        self.heart_image = pygame.image.load('heart.png')
        self.heart_image = pygame.transform.scale(self.heart_image, (40, 40)) 

    def spawn_target(self):
        x = random.randint(50, 1230)
        y = random.randint(50, 718)
        
        is_bomb = random.random() < self.bomb_chance
        target = Target(x, y, is_bomb)
        self.targets.add(target)
        self.all_sprites.add(target)

    def run(self):
        running = True 
        while running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    for target in self.targets:
                        if target.rect.collidepoint(mouse_pos):
                            if target.is_bomb:
                                self.lives -= 1
                            else:
                                self.score += 10
                            target.kill()

            if random.random() < self.spawn_rate:
                self.spawn_target()

            self.all_sprites.update()
            screen.fill((41, 41, 41)) 
            self.all_sprites.draw(screen)

            # Mostrar a pontuação
            score_text = font.render(f"{self.score}", True, WHITE)
            screen.blit(score_text, (10, 10))

            # Exibir os corações restantes com base nas vidas
            for i in range(self.lives):
                screen.blit(self.heart_image, (SCREEN_WIDTH - 50 * (i + 1), 10))

            # Exibir o temporizador
            time_rounded = round(self.time_left, 1)  # Limita o temporizador a 1 casa decimal
            timer_text = font.render(f"Tempo: {time_rounded}", True, WHITE)
            screen.blit(timer_text, (SCREEN_WIDTH // 2 - timer_text.get_width() // 2, 10))  # Exibe o tempo no centro superior

            pygame.display.flip()

            self.time_left -= 1 / 60  # Diminui o tempo a cada quadro (1/60 segundos)

            # Verifica se o tempo acabou
            if self.time_left <= 0:
                self.game_over()  # Chama a função para exibir a tela de Game Over
                return False  # Retorna para o menu quando o tempo acabar

            if self.lives <= 0:
                self.game_over()  # Chama a função para exibir a tela de Game Over
                return False  # Retorna para o menu quando as vidas acabarem

        pygame.quit()

# Função que exibe a tela de Game Over
def game_over():


# Função que exibe a tela de créditos
def credits_screen():


# Função que exibe a tela de dificuldade
def difficulty_screen():


# Função que exibe o menu
def main_menu():


def main():
