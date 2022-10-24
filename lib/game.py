from pygame import display, time, key
import pygame

from lib.colors import BLACK


class Game():
  def __init__(self, width=800, height=600):
    pygame.init()
    self.screen = display.set_mode((width, height))
    display.set_caption("Roman's Breakout Clone")

    self.over = False
    self.clock = time.Clock()

  def run(self, milliseconds=100):
    from lib.paddle import Paddle
    from lib.brick import Brick
    
    # self.paddle = Paddle()
    self.paddle = Paddle()
    self.bricks = Brick.load_bricks()
    # self.ball = Ball()
    while not self.over:
      tick = self.clock.tick(
        milliseconds)
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          game_over = True
      self.screen.fill(BLACK)
      
      pressed = key.get_pressed()
      self.paddle.control(pressed, tick)
      for row in self.bricks:
        for brick in row:
          brick.draw()
      self.paddle.draw()
      display.update()