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

  def paddle_collide(self):
    if self.paddle.x + self.paddle.width>= self.ball.x >= self.paddle.x and \
      self.ball.y + self.ball.height >= self.paddle.y >= self.ball.y and \
      self.ball.y_speed > 0:
      self.ball.y_speed *= -1

      self.ball.x_speed *= 1.01 # increase difficulty
      self.ball.y_speed *= 1.01 # increase difficulty

  def brick_collide(self):
    for row in self.bricks:
      for brick in row:
        if brick.x <= self.ball.x <= brick.x + brick.width and \
          brick.y <= self.ball.y <= brick.y + brick.height:
          row.remove(brick)

          if self.ball.x <= brick.x + 2 or \
            self.ball.x >= brick.x + brick.width -2:
            self.ball.x_speed *= -1
          elif self.ball.y <= brick.y + 2 or \
            self.ball.y >= brick.y + brick.height -2:
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
          self.over = True
      self.screen.fill(BLACK)
      
      pressed = key.get_pressed()
      self.paddle.control(pressed, tick)
      self.ball.serve(pressed)
      self.paddle_collide()
      self.brick_collide()
      self.ball.move()

      for row in self.bricks:
        for brick in row:
          brick.draw()
      self.paddle.draw()

      self.ball.draw()


      display.update()
    
