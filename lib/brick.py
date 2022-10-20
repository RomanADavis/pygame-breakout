from pygame import image

class Brick():
  def __init__(self):
    self.image = image.load("images/brick.png").convert_alpha()
    self.rect = self.image.get_rect()