from pygame import image

class Paddle():
  def __init__(self):
    self.image = image.load("images/paddle.png").convert_alpha()
    self.rect = self.image.get_rect()
