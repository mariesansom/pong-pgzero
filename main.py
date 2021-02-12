import pgzrun as pgz

WIDTH = 600
HEIGHT = 500

TITLE = 'Pong game'

WHITE = 255, 255, 255
BLUE = 0, 0, 255
RED = 255, 0, 0 
BALL = Rect((WIDTH/2, HEIGHT/2), (10,10))
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

def draw():
    screen.clear()
    screen.draw.filled_rect(BALL, WHITE)
    screen.draw.filled_rect(PADDLE1, BLUE)
    screen.draw.filled_rect(PADDLE2, RED)   



pgz.go()
