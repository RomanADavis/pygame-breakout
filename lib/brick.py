from pygame import image


class Brick():
  image = image.load("images/brick.png").convert_alpha()
  rect = image.get_rect()
  
  def __init__(self, x, y):
    self.x = x * self.rect[2]
    self.y = y * self.rect[3]

  def draw(self):
    from lib.setup import SCREEN
    SCREEN.blit(self.image, (self.x, self.y))
    

  @classmethod
  def load_bricks(cls, columns=3, rows=5):
    return [[cls(x, y) for x in range(columns)] for y in range(rows)]
    