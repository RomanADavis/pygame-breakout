from pygame import image

class Ball():
  def __init__(self):
    self.image = image.load("images/football.png").convert_alpha()
    self.rect = self.image.get_rect()