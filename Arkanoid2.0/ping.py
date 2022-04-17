from pygame import *
mixer.init()
mixer.music.load('geometri-dash-2chast--1-uroven.mp3')
mixer.music.play()
img_player1 = 'player.jpg'
img_player2 = 'player.jpg'
img_back = 'back.jpg'
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       sprite.Sprite.__init__(self)
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
    def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update1(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
back = 200,255,255
win_width = 700
win_height = 500
display.set_caption("Arkanoid2.0")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))
player1 = Player(img_player1,30,200,40,50,150)
player2 = Player(img_player2, 620,200,40,50,150)
ball = GameSprite('tennis_PNG10405.png', 200,200,40,50,50)
font.init()
font = font.Font(None,35)
lose1 = font.render('PLAYER 1 LOSE!',True,(180,0,0))
lose2 = font.render('PLAYER 2 LOSE!',True,(180,0,0))
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
    if finish != True:
        window.fill(back)
        player1.update1()
        player2.update2()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            speed_x *= -1
            speed_y *= 1
        if ball.rect.y > win_height-50 or ball.rect.y <0:
            speed_y *= -1
        if ball.rect.x <0:
            finish = True
            window.blit(lose1, (200,200))
            game_over = True
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200,200))
            game_over = True
        player1.reset()
        player2.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)