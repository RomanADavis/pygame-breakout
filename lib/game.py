from pygame import init, display

from lib.colors import BLACK

from lib.paddle import Paddle

class Game():
  def __init__(self, width=800, height=600):
    init()
    self.screen = display.set_mode((width, height))
    display.set_caption("Roman's Breakout Clone")

    self.paddle = Paddle()
    self.brick = Brick()
    self.ball = Ball()

    self.over = False
    self.clock = pygame.time.Clock()

  def run(self, milliseconds=100):
    while not self.over:
      tick = clock.tick(milliseconds)
      screen.fill(BLACK)