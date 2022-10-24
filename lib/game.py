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

  def collide(self):
    if self.paddle.x + self.paddle.width>= self.ball.x >= self.paddle.x and \
      self.ball.y + self.ball.height >= self.paddle.y >= self.ball.y and \
      self.ball.y_speed > 0:
      self.ball.y_speed *= -1

  def run(self, milliseconds=100):
    from lib.paddle import Paddle
    from lib.brick import Brick
    from lib.ball import Ball

    self.paddle = Paddle()
    self.bricks = Brick.load_bricks()
    self.ball = Ball()
    
    while not self.over:
      tick = self.clock.tick(
        milliseconds)
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          game_over = True
      self.screen.fill(BLACK)
      
      pressed = key.get_pressed()
      self.paddle.control(pressed, tick)
      self.ball.serve(pressed)
      self.collide()
      self.ball.move()

      for row in self.bricks:
        for brick in row:
          brick.draw()
      self.paddle.draw()

      self.ball.draw()


      display.update()