from microbit import *
import random
import time

comp = 0
counter = 0
run_once = 0
snake_len = 1
snake = [[0,2]]
compass = ['up', 'right', 'down', 'left']
cherry = [random.randint(0,4), random.randint(0,4)]

#if die
def die(snake_len):
    print("YOU LOST!")
    t = running_time()
    while running_time() < t+1400:
        display.show(Image.SAD)
        sleep(200)
        display.clear()
        sleep(200)
    (a,b) = (button_a.was_pressed(), button_b.was_pressed())
    while not (a or b):
        display.scroll(snake_len)
        (a,b) = (button_a.was_pressed(), button_b.was_pressed())
    display.clear()
#if cherry is eaten
def cherry_eaten():
    cherry = [random.randint(0,4), random.randint(0,4)]
    while cherry in snake:
        cherry = [random.randint(0,4), random.randint(0,4)]
    return cherry
#converts board to displayable image
def display_board(b):
    d = []
    c1 = 0
    c2 = 0
    while c1< 5:
        while c2<5:
            b[c1][c2] = str(b[c1][c2])
            c2+=1
        c2=0
        c1+=1
    for i in b:
        d.append("".join(i))
    c1 = 0
    while c1<4:
        d[c1] = d[c1]+":"
        c1+=1
    b = Image("".join(d))
    return b
#main
while True:#counter < 15:
    board = [[0,0,0,0,0], [0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    board2 = [[0,0,0,0,0], [0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

    if run_once == 0:
        for i in snake:
            board[4-i[0]][i[1]] = 9
        display.show(display_board(board))
        board = [[0,0,0,0,0], [0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        run_once = 1
        sleep(1000)
        display.clear()
#changing direction
    (a,b) = (button_a.was_pressed(), button_b.was_pressed())
    if a:
        comp -=1
    elif b:
        comp+=1
    if comp>=4:
        comp = 0
    elif comp<=-1:
        comp = 3
    direction = compass[comp]
#moving snake
    if direction == 'up':
        snake.insert(0, [snake[0][0]+1, snake[0][1]])
    elif direction == 'down':
        snake.insert(0, [snake[0][0]-1, snake[0][1]])
    elif direction == 'left':
        snake.insert(0, [snake[0][0], snake[0][1]-1])
    elif direction == 'right':
        snake.insert(0, [snake[0][0], snake[0][1]+1])
    else:
        print("Compass Error")
#cherry eaten detection
    if cherry in snake:
        snake_len += 1
        cherry = cherry_eaten()
#moving snake
    diff = len(snake)-snake_len
    for i in range(diff):
        snake.pop()
#win detection
    if snake_len == 25:
        print("YOU WON!")
        t = running_time()
        while running_time() < t+1800:
            display.show(Image.Happy)
            sleep(200)
            display.clear()
            sleep(200)
        display.clear()
#lose detection
    if snake[0][0] > 4 or snake[0][0] < 0 or snake[0][1] > 4 or snake[0][1] < 0:
        die(snake_len)
        break
    snake2 = []
    for i in snake:
        snake2.append(str(i))
    if len(snake) != len(set(snake2)):
        die(snake_len)
        break
#dispaying snake & cherry
    a = 1
    for i in snake:
        if a:
            board[4-i[0]][i[1]] = 8
            board2[4-i[0]][i[1]] = 8
            a = 0
        else:
            board[4-i[0]][i[1]] = 6
            board2[4-i[0]][i[1]] = 6
    board2[4-cherry[0]][cherry[1]] = 9
    to_display_board1 = display_board(board)
    to_display_board2 = display_board(board2)
    t = running_time()
    while running_time() < t+700:
        display.show(to_display_board1)
        sleep(100)
        display.show(to_display_board2)
        sleep(100)
    counter+=1
