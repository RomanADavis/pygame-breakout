from pygame import image

from lib.setup import SCREEN

class Brick():
  image = image.load("images/brick.png").convert_alpha()
  rect = image.get_rect()
  
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def draw(self):
    from lib.setup import SCREEN
    SCREEN.blit(self.image, (self.x, self.y))
    
  @classmethod
  def load_bricks(cls, rows=5):
    gap = 10
    columns = SCREEN.get_width() // (cls.rect[2] + gap)
    margin = (SCREEN.get_width() - (cls.rect[2] + gap) * columns + gap) // 2
    
    bricks = []
    for y in range(rows):
      row = []
      for x in range(columns):
        brick = cls(x * (cls.rect[2] + gap) + margin, y * (cls.rect[3] + gap))
        row.append(brick)
      bricks.append(row)

    return bricks
    