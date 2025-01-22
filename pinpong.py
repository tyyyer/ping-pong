
from pygame import *
from random import *
from time import time as timer


window = display.set_mode((700, 500))
display.set_caption('Пинпонг')
background = transform.scale(image.load('fon.jpg'), (700, 500))
 
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, filename, r, s, x, y, speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(filename), (r, s))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def bl1t(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 2:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 380:
            self.rect.y += self.speed

    def update2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 2:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 380:
            self.rect.y += self.speed
            

rocket1 = Player('rockk.png', 100, 120, 10, 200, 8)
rocket2 = Player('rockk.png', 100, 120, 600, 200, 8)
ball = GameSprite('ball.png', 100, 100, 280, 200, 8)

win = 0 
lost = 0

font.init()
font1 = font.SysFont('Arial', 36)
font2 = font.SysFont('Arial', 60)

run = True
finish = False

while run:
    for i in event.get():
        if i.type == QUIT:
            run = False
        
    window.blit(background, (0, 0))

    rocket1.bl1t()
    rocket1.update1()
    rocket2.bl1t()
    rocket2.update2()
    ball.bl1t()

    clock.tick(60)
    display.update()
     





