from pygame import *

class Telo(sprite.Sprite):
    def __init__(self, pic, h, w, x, y, speed):
        super().__init__()
        self.img = transform.scale(image.load(pic), (w, h))
        self.rect = self.img.get_rect()
        self.h = h
        self.w = w
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self):
        win.blit(self.img, (self.rect.x, self.rect.y))

class Platform(Telo):
    def __init__(self, pic, h, w, x, y, speed, key_up, key_down):
        super().__init__(pic, h, w, x, y, speed)
        self.k_up = key_up
        self.k_down = key_down
    def update(self):
        k_pressed = key.get_pressed()
        if k_pressed[self.k_up] and self.rect.y > 0:
            self.rect.y -= self.speed
        if k_pressed[self.k_down] and self.rect.y < 720 - self.h:
            self.rect.y += self.speed

class Ball(Telo):
    def update(self):
        pass


win = display.set_mode((1280, 720))
game = True
background = transform.scale(image.load('background.jpg'), (1280, 720))
platform = Platform('wall.jpg', 250, 50, 100, 390, 1, K_w, K_s)

while game:
    
    win.blit(background, (0, 0))

    platform.reset()
    platform.update()

    for e in event.get():
        if e.type == QUIT:
            game = False

    
    display.update()