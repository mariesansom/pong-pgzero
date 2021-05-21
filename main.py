import pgzrun as pgz
import random

WIDTH = 600
HEIGHT = 500

TITLE = 'Pong game'

WHITE = 255, 255, 255
BLUE = 0, 0, 255
RED = 255, 0, 0 

SPEED = 3
DY = -SPEED
DX = SPEED

class Game():
    def __init__(self):
        self.speed = SPEED
        self.score = 0

class Ball(Rect):
    def __init__(self, *args, dx, dy):
        ZRect.__init__(self, *args)
        self.active = False
        self.dx = dx * random.normalvariate(1, 0.2)
        self.dy = dy * random.normalvariate(0.0, 0.75)
        self.speed = SPEED

# music.play('seventies.mp3')
#music.set_volume(0.45)

game = Game()
ball = Ball((WIDTH/2, HEIGHT/2), (10, 10), dx=DX, dy=DY)
PADDLE_LENGTH = 100
PADDLE1 = Rect((20, 20),(10, PADDLE_LENGTH))
PADDLE2 = Rect((570, 20),(10, PADDLE_LENGTH))

def update():
    
    if keyboard.s and PADDLE1.y + PADDLE_LENGTH < HEIGHT - 20:
        PADDLE1.y += 10
    elif keyboard.w and PADDLE1.y > 20:
        PADDLE1.y -= 10
    
    if keyboard.down and PADDLE2.y + PADDLE_LENGTH < HEIGHT - 20:
         PADDLE2.y += 10
    elif keyboard.up and PADDLE2.y > 20:
        PADDLE2.y -= 10

    if not ball.active:
    # if ball.active == False:

        if keyboard.b:
            ball.active = True
            print(f'ball.active: {ball.active}')
           

    if ball.active:
        
        if keyboard.space:
            ball.active = False
            print(f'ball.active: {ball.active}')

        # # if ball.right >= WIDTH:
        #     ball.direction = -ball.dx, ball.dy

        # elif ball.left <= 0:
        #     ball.direction = ball.dx, -ball.dy

        ball.direction = ball.dx, ball.dy
        ball.speed = game.speed
        # ball.move_ip(ball.speed * 3, ball.speed * 3)
        ball.move_ip(ball.dx, ball.dy)

    if ball.colliderect(PADDLE1) or ball.colliderect(PADDLE2):
        print('COLLISION')
        ball.dx = -ball.dx



def draw():
    screen.clear()
    screen.draw.filled_rect(ball, WHITE)
    screen.draw.filled_rect(PADDLE1, BLUE)
    screen.draw.filled_rect(PADDLE2, RED)   



pgz.go()
