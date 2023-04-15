from pygame import *


speed = 5


win_height = 800
win_width = 1000

window = display.set_mode((win_width, win_height))
display.set_caption("ping-pong")




class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_heigh, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(player_width, player_heigh))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.direction = 'left'
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))



font.init()

lost = 0

font1 = font.SysFont('Arial', 69)

win = font1.render('Player 1wssssss wins the game',True, (0,180,0))

lose = font1.render('Player 2 wins the game', True, (225,0,0))




class Player(GameSprite):
    def update_platform1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 100:
            self.rect.y += self.speed
    def update_platform2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 100:
            self.rect.y += self.speed



ball = GameSprite('ball.png', 300, 300, 50, 50, 3) #создаем шар
platform1 = Player('platform.png', 940, 100, 80, 100, speed)
platform2 = Player('platform.png', -20, 250, 80, 100  ,speed)

speed_x = 3
speed_y = 3


game = True
finish = False
clock = time.Clock()

FPS = 60



while game:
    for e in event.get():
        if e.type == QUIT:
            game = False




    if ball.rect.y > win_height-50 or ball.rect.y < 0:
        speed_y *= -1


    if sprite.collide_rect(platform1, ball) or sprite.collide_rect(platform2, ball):
        speed_x *= -1


    if ball.rect.x < 0:
        finish = True
        window.blit(lose, (300, 500))

    if ball.rect.x > win_width-50:
        finish = True
        window.blit(win, (300,500))

    if not finish:  
        window.fill((0,110,110))
        platform1.update_platform1()
        platform2.update_platform2()
        ball.rect.x += speed_x
        ball.rect.y += speed_y


        platform1.reset()
        platform2.reset()
        ball.reset()
        



    clock.tick(FPS)
    display.update()