from pygame import image, K_SPACE

from lib.setup import SCREEN

class Ball():
  def __init__(self, starting_position=(200, 200), speed=(3.0, 3.0)):
    self.image = image.load("images/football.png").convert_alpha()
    self.rect = self.image.get_rect()
    self.width = self.image.get_width()
    self.height = self.image.get_height()

    self.starting_position = starting_position
    self.default_speed = speed

    self.limits = {
      "top": 0,
      "bottom": SCREEN.get_height() - self.image.get_height(),
      "left": 0,
      "right": SCREEN.get_width() - self.image.get_width()
    }

    self.set_up()

  def set_up(self):
    self.x, self.y = self.starting_position
    self.x_speed, self.y_speed = self.default_speed

    self.is_moving = False

  def draw(self):
    SCREEN.blit(self.image, (self.x, self.y))

  def move(self):
    if self.is_moving:
      self.bounce()
      self.x += self.x_speed
      self.y += self.y_speed

  def bounce(self):
    if self.x < self.limits["left"]:
      self.x_speed *= -1
    if self.x > self.limits["right"]:
      self.x_speed *= -1
    if self.y < self.limits["top"]:
      self.y_speed *= -1
    if self.y > self.limits["bottom"]:
      self.set_up()

  def serve(self, pressed):
    if pressed[K_SPACE]:
      self.is_moving = True