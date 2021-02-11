import pgzrun as pgz

WIDTH = 600
HEIGHT = 500

TITLE = 'Pong game'

WHITE = 255, 255, 255
BLUE = 0, 0, 255
BALL = Rect((WIDTH/2, HEIGHT/2), (10,10))
PADDLE_LENGTH = 100
PADDLE1 = Rect((20, 20),(10, PADDLE_LENGTH))
# PADDLE2 =

def update():
    if keyboard.down and PADDLE1.y + PADDLE_LENGTH < HEIGHT - 20:
        PADDLE1.y += 10
    elif keyboard.up and PADDLE1.y > 20:
        PADDLE1.y -= 10

def draw():
    screen.clear()
    screen.draw.filled_rect(BALL, WHITE)
    screen.draw.filled_rect(PADDLE1, BLUE)   



pgz.go()
