import numpy as np
import math

window_size = 800
frame_rate = 1000
dt = 1/frame_rate

class Particle:
    def __init__(self):
        # Static
        self.radius = 15
        self.mass = 10

        # Color
        self.color = (255,255,255)

        # Position
        self.px = 400
        self.py = 400

        # Velocity
        self.vx = 0
        self.vy = 0
        self.v = math.sqrt((self.vx ** 2) + (self.vy ** 2))

    def update(self):
        self.px = self.px + (self.vx * dt)
        self.py = self.py + (self.vy * dt)

# Particle 1
p1 = Particle()
p1.px = 125
p1.vx = -500
p1.vy = 100
p1.color = (100,0,100)
p1.mass = 20

# Particle 2
p2 = Particle()
p2.px = 375
p2.vx = 500
p2.vy = 300
p2.color = (0,200,200)
p2.mass = 40


import pygame
pygame.init()
screen = pygame.display.set_mode([window_size, window_size])
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    # Draw particle sprites
    pygame.draw.circle(screen, p1.color, (p1.px, p1.py), p1.radius)
    pygame.draw.circle(screen, p2.color, (p2.px, p2.py), p2.radius)

    # Wall collision
    if (p1.px - p1.radius <= 0) or (p1.px + p1.radius >= window_size):
        p1.vx = -p1.vx
    if (p1.py - p1.radius <= 0) or (p1.py + p1.radius >= window_size):
        p1.vy = -p1.vy
   
    # Wall collision
    if (p2.px - p2.radius <= 0) or (p2.px + p2.radius >= window_size):
        p2.vx = -p2.vx 
    if (p2.py - p2.radius <= 0) or (p2.py + p2.radius >= window_size):
        p2.vy = -p2.vy

    # Particle collision
    if abs(p2.px - p1.px) < p1.radius + p2.radius:
        ux1, ux2 = p1.vx, p2.vx
        p1.vx = (((p1.mass - p2.mass)/(p1.mass + p2.mass)) * ux1) + (((2 * p2.mass)/(p1.mass + p2.mass)) * ux2)
        p2.vx = (((2 * p1.mass)/(p1.mass + p2.mass)) * ux1) + (((p2.mass - p1.mass)/(p1.mass + p2.mass)) * ux2)
    
    if abs(p2.py - p1.py) < p1.radius + p2.radius:
        uy1, uy2 = p1.vy, p2.vy
        p1.vy = (((p1.mass - p2.mass)/(p1.mass + p2.mass)) * uy1) + (((2 * p2.mass)/(p1.mass + p2.mass)) * uy2)
        p2.vy = (((2 * p1.mass)/(p1.mass + p2.mass)) * uy1) + (((p2.mass - p1.mass)/(p1.mass + p2.mass)) * uy2)

    # Update display
    pygame.display.flip()
    p1.update()
    p2.update()

    # Limit frame rate
    clock.tick(frame_rate)

pygame.quit()