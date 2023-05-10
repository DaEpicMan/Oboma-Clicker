import pygame
from pygame import *
pygame.init()

screensize = (800, 600)
screen = pygame.display.set_mode(screensize)
pygame.display.set_caption("Oboma Clicker")

play = True
clock = pygame.time.Clock()

class Oboma:
  def __init__()


while play:
  clock.tick(60)
  screen.fill((0, 0, 0))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      play = False
      
      
