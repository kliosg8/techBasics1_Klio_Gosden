import random
import math
import os
import pygame

pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Assignment 8")
clock = pygame.time.Clock()
original_image = pygame.image.load(r"assignments\week8\Marge.png").convert_alpha()
background = pygame.image.load(r"assignments\week8\har.jpg").convert()
background = pygame.transform.scale(background, (width, height))

class Sprite:
    def __init__(self):
     
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)

        self.speed_x = random.uniform(1, 5)

        self.size = random.randint(40, 100)

        self.image = pygame.transform.scale(
            original_image,
            (self.size, self.size)
        )

      
        self.base_y = self.y
        self.amplitude = random.randint(20, 80)
        self.frequency = random.uniform(0.01, 0.05)
        self.angle = random.uniform(0, math.pi * 2)

    def update(self):
       
        self.x += self.speed_x
        self.angle += self.frequency
        self.y = self.base_y + math.sin(self.angle) * self.amplitude

        if self.x > width:
            self.x = -self.size

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

sprites = []

for i in range(10):
    sprites.append(Sprite())

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0, 0))

    for sprite in sprites:
        sprite.update()
        sprite.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()