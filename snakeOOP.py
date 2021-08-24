import pygame
from pygame.locals import *
import random
class Colors:
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)


class Snake:
    def __init__(self, x, y, size, speed):
        self.body = []
        self.length = 1
        self.size = size
        self.speed = speed
        self.x = x
        self.y = y
        self.x_speed = 0
        self.y_speed = 0

class Target:
    def __init__(self,x,y):
        self.x = x
        self.y = y


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = 640, 400
        self.clock = pygame.time.Clock()
        self.snake = Snake(self.width/2, self.height/2, 10, 15)
        self.target = Target(x = round(random.randrange(0,self.width-self.snake.size) / 10.0) * 10,y = round(random.randrange(0, self.height-self.snake.size) / 10.0) * 10
)

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.score_font = pygame.font.SysFont('ubuntu', 25)
        self._running = True

    def on_event(self, event):
        
        if event.type == pygame.QUIT:
            self._running = False
        #Define keypresses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.snake.x_speed = -self.snake.size
                self.snake.y_speed = 0
            elif event.key == pygame.K_RIGHT:
                self.snake.x_speed = self.snake.size
                self.snake.y_speed = 0
            elif event.key == pygame.K_UP:
                self.snake.x_speed = 0
                self.snake.y_speed = -self.snake.size
            elif event.key == pygame.K_DOWN:
                self.snake.x_speed = 0
                self.snake.y_speed = self.snake.size


    def on_loop(self):
       
        if self.snake.x >= self.width or self.snake.x < 0 or self.snake.y >= self.height or self.snake.y < 0:
            self._running = False

        self.snake.x += self.snake.x_speed
        self.snake.y += self.snake.y_speed

        self.snake.body.append([self.snake.x,self.snake.y])

        if len(self.snake.body) > self.snake.length:
            del self.snake.body[0]

        for pixel in self.snake.body[:-1]:
            if pixel == [self.snake.x,self.snake.y]:
                self._running = False

        if self.snake.x == self.target.x and self.snake.y == self.target.y:
            self.target.x = round(random.randrange(0,self.width-self.snake.size) / 10.0) * 10
            self.target.y = round(random.randrange(0, self.height-self.snake.size) / 10.0) * 10
            self.snake.length += 1

        self.clock.tick(self.snake.speed)

    def on_render(self):
        text = self.score_font.render("Score: " + str(self.snake.length-1), True, Colors.white)
        self._display_surf.fill(Colors.black)
        self._display_surf.blit(text, [0,0])
        for pixel in self.snake.body:
             pygame.draw.rect(self._display_surf, Colors.green, [pixel[0], pixel[1], self.snake.size, self.snake.size])
        pygame.draw.rect(self._display_surf, Colors.red, [self.target.x, self.target.y, self.snake.size, self.snake.size])
        pygame.display.flip()
        
    
    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()