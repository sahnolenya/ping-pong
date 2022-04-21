from pygame import *
class GameSprite (sprite.Sprite):
    def __init__ (self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        #каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect() 
        self.rect.x = player_x
        self.rect.y = player_y
    def reset (self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < height - 50:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < height - 50:
            self.rect.y += self.speed

#окно 

width = 700
height = 500
window = display.set_mode((width, height))
display.set_caption("Пинг-понг")
background =(200, 255, 255)
window.fill(background)
count = 0
FPS = 60 
clock = time.Clock()
finish = False
game = True
font.init()
font1 = font.Font(None, 36)
lose1 = font1.render('Игрок 1 проиграл!', True, (255, 0, 0))
lose2 = font1.render('Игрок 2 проиграл!', True, (255, 0, 0))

racket1 = Player("racket.png", 30, 400, 25, 180, 10)
racket2 = Player("racket.png", 620, 200, 25, 180, 10)
ball = Player('ball.png', 200, 200, 75, 75, 50)

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            geme = False
        if finish != True:
            window.fill(background)
            racket1.update_l()
            racket2.update_r()
            ball.rect.x += speed_x
            ball.rect.y += speed_y
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
        if ball.rect.y > height - 50 or ball.rect.y < 0:
            speed_y *= -1
        
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
        
        if ball.rect.x > 625:
            finish = True
            window.blit(lose2, (200, 200))

        racket1.reset()
        racket2.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)
        