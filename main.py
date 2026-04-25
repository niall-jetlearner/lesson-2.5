import pygame
pygame.init()
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill((255,255,255))
blue = (0,0,255)
red = (255,0,0)
pygame.display.update()

class Circle:
    def __init__(self, color, pos, radius, width):
        self.circle_color = color
        self.circle_pos = pos
        self.circle_radius = radius
        self.circle_width = width
        self.circle_surface = screen

    def draw(self):
        pygame.draw.circle(self.circle_surface, self.circle_color, self.circle_pos, self.circle_radius, self.circle_width)

bcircle = Circle(blue, (100,250), 50, 5)

bcircle.draw()
position = (100,250)
radius  = 50
width = 5
pygame.draw.circle(screen, red, radius, position, width)

pygame.display.update()