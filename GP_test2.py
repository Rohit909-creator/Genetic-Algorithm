import random
import pygame
import random


# Initialize Pygame
pygame.init()

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
        self.state = (self.rect.x, self.rect.y)
        self.action = None
    def update(self):
        # Add AI and movement logic here
        self.state = (self.rect.x, self.rect.y)
        self.action = random.choice([0,1,2,3])

        if self.action == 0:
            self.rect.x += 1

        elif self.action == 1:
            self.rect.x -= 1
        
        elif self.action == 2:
            self.rect.y += 1

        elif self.action == 3:
            self.rect.y -= 1
        

# Set up the game display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Zelda-style Game")

# Create player and enemy groups
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()


# Create enemy instances
for _ in range(50):
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
            xcor+=1
        

    # Update
    all_sprites.update()

    # Draw
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()



# population_size = 10
# mutation_rate=0.1
# num_generations=100

# def initialize():
#     return [random.uniform(-10,10) for _ in range(population_size)]

# def equation(x : int):
#     return x**2 - 4*x + 4

# def fitness(solution):
#     return abs(equation(solution))

# def mutate(solution):
#     if random.random() < mutation_rate:
#         solution+=random.uniform(-0.5,0.5)
#     return solution

# def crossover(parents):
#     return (parents[0]+parents[1])/2

# def select_parents(population):
#     return sorted(population, key=fitness)[:2]

# def genetic_algorithm():

#     population = initialize()

#     for generations in range(num_generations):

#         new_population = []

#         for _ in range(population_size//2):
            
#             parents = select_parents(population)
#             child = crossover(parents)
#             child = mutate(child)
#             new_population.extend([parents[0],parents[1], child])

#         population = new_population
    
#     best_solution = min(population, key=fitness)

#     return best_solution

# best_x = genetic_algorithm()
# best_fitness = fitness(best_x)

# print(f"best solution: {best_x} fitness_score: {best_fitness}")

