from pygame import image, K_LEFT, K_RIGHT
from lib.setup import SCREEN

class Paddle():
  def __init__(self, x=0):
    self.image = image.load("images/paddle.png").convert_alpha()
    self.rect = self.image.get_rect()
    self.width = self.image.get_width()
    self.height = self.image.get_height()
    self.x = 0
    self.y = SCREEN.get_height() - 100
    self.speed = 1
    self.limits = {
      "left": 0,
      "right": SCREEN.get_width() - self.width
    }
  
  def draw(self):
    SCREEN.blit(self.image, (self.x, self.y, self.width, self.height))

  def control(self, pressed, tick):
    if pressed[K_LEFT]:
      self.x -= self.speed * tick
    if pressed[K_RIGHT]:
      self.x += self.speed * tick
    if self.x > self.limits["right"]:
      self.x = self.limits["right"]
    if self.x < self.limits["left"]:
      self.x = self.limits["left"]