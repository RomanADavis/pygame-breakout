from pygame import image

from lib.setup import SCREEN

class Ball():
  def __init__(self, starting_position=(200, 200), speed=(3.0, 3.0)):
    self.image = image.load("images/football.png").convert_alpha()
    self.rect = self.image.get_rect()
    self.x, self.y = starting_position
    self.x_speed, self.y_speed = speed

  def draw(self):
    SCREEN.blit(self.image, (self.x, self.y))