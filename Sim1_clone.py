import random
from typing import Any
import pygame
import random
import numpy as np

class Neuron():

    def __init__(self, input_size, output_size) -> None:
        
        self.weights = np.random.rand(output_size,input_size)
        self.weights += np.random.random_sample((output_size, input_size))
        # np.random.rand(3,2)
    def __call__(self, state : np.ndarray)-> int:
        out = state@self.weights.T
        # print(out.shape)
        out = np.argmax(out,axis=-1).item()
        return out

def selection():
    selected = []
    non_selected = []
    for p in all_sprites.sprites():
        if abs(p.rect.x - 800) < 30 or abs(p.rect.x - 0) < 30:
            selected.append(p)

        else:
            non_selected.append(p)
    all_sprites.remove(non_selected)

    for p in selected:
        all_sprites.add(p)



pygame.init()


population_size = 50
mutation_rate=0.1
num_generations=100



# Define constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH)
        self.rect.y = random.randint(0, SCREEN_HEIGHT)
        self.neuron = Neuron(2, 4)

    def update(self):
        # Add AI and movement logic here
        l = [abs(SCREEN_WIDTH - self.rect.x), abs(SCREEN_WIDTH-0)]
        idx = l.index(min(l))
        state = np.zeros((1,2),dtype=np.float16)
        state[0][idx] =  1
        action = self.neuron(state)
        # print(action)  

        if self.rect.x != SCREEN_WIDTH and self.rect.x != 0 and self.rect.y != SCREEN_HEIGHT and self.rect.y != 0:

            if action == 0:
                self.rect.x += 1

            elif action == 1:
                self.rect.x -= 1
            
            elif action == 2:
                self.rect.y += 1

            elif action == 3:
                self.rect.y -= 1
        else:
            pass
        

# Set up the game display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Zelda-style Game")

# Create player and enemy groups
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()


# Create enemy instances
for _ in range(population_size):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            selection()
    # Update
    all_sprites.update()

    # Draw
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
