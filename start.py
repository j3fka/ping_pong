from pygame import *
font.init()

class Telo(sprite.Sprite):
    def __init__(self, pic, h, w, x, y, speed):
        super().__init__()
        self.image = transform.scale(image.load(pic), (w, h))
        self.rect = self.image.get_rect()
        self.h = h
        self.w = w
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

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
    def __init__(self, pic, h, w, x, y, speed):
        super().__init__(pic, h, w, x, y, speed)
        self.speed_x = speed
        self.speed_y = speed
        self.count1 = 0
        self.count2 = 0

    def update(self):
        if self.rect.y >= 620:
            self.speed_y = self.speed_y * -1
        elif self.rect.y <= 0:
            self.speed_y = self.speed_y * -1
        if sprite.spritecollideany(ball, platform_g):
            self.speed_x = self.speed_x * -1
        
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.x < 0:
            self.count2 += 1
            self.rect.x = 615
            self.rect.y = 310
            
        elif self.rect.x > 1280:
            self.count1 += 1
            self.rect.x = 615
            self.rect.y = 310

        self.count1_i = font.SysFont('arial', 44).render(str(self.count1), True, (0, 0, 0))
        self.count2_i = font.SysFont('arial', 44).render(str(self.count2), True, (0, 0, 0))
        win.blit(self.count1_i, (50, 0))
        win.blit(self.count2_i, (1200, 0))



win = display.set_mode((1280, 720))
game = True
background = transform.scale(image.load('background.jpg'), (1280, 720))
platform1 = Platform('wall.jpg', 250, 50, 100, 390, 1, K_w, K_s)
platform2 = Platform('wall.jpg', 250, 50, 1180, 390, 1, K_o, K_l)
ball = Ball('ball.png', 100, 100, 615, 310, 1)

platform_g = sprite.Group()
platform_g.add(platform1)
platform_g.add(platform2)

while game:
    
    win.blit(background, (0, 0))

    platform_g.draw(win)
    platform_g.update()

    ball.reset()
    ball.update()

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()