from pygame import init, display, time

from lib.colors import BLACK


class Game():
  def __init__(self, width=800, height=600):
    init()
    self.screen = display.set_mode((width, height))
    display.set_caption("Roman's Breakout Clone")

    from lib.paddle import Paddle
    from lib.brick import Brick
    
    # self.paddle = Paddle()
    self.bricks = Brick.load_bricks()
    # self.ball = Ball()

    self.over = False
    self.clock = time.Clock()

  def run(self, milliseconds=100):
    print(self.bricks)
    while not self.over:
      tick = self.clock.tick(milliseconds)
      self.screen.fill(BLACK)
      
      for row in self.bricks:
        for brick in row:
          brick.draw()

      display.update()