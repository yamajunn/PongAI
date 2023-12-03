import numpy as np
import os
import time
import readchar
from timeout_decorator import timeout, TimeoutError
import random

from create_display import create_display
from bar import bar
# from bar_move import bar_move

TIMEOUT_SEC = 0.1
@timeout(TIMEOUT_SEC)
def input_with_timeout():
    return readchar.readchar()

width = 100
height = 30

probability_list = [[10, 10, 10] for i in range(width*height*4)]
choices_list = [-1,0,1]

line = "#"
back = " "

bar_size = 30
bar_position = width//2 - bar_size//2

break_bool = False

ball_position = [50, 15]
ball_direction = 3

display_array = create_display(width, height, line, back)  # create display

display_array = bar(bar_size, bar_position, display_array, width, height) # bar position

for i in range(height):  # print
    display_array[width*i+width-1] = "\n"
display_str = "".join(display_array)
print(display_str)
print(bar_position)

time_start = 0
time_end = 0
while True:
    if time_end - time_start > 0.14:
        time_start = time.time()
    display_array = create_display(width, height, line, back)  # create display

    if time_end - time_start > 0.1:
        if ball_direction == 1 and ball_position[0] >= 2 and ball_position[1] >= 2:
            ball_position[0] -= 1
            ball_position[1] -= 1
        elif ball_direction == 1:
            if ball_position[0] <= 1:
                ball_direction = 2
            else:
                ball_direction = 3
        elif ball_direction == 2 and ball_position[0] <= width-6 and ball_position[1] >= 2:
            ball_position[0] += 1
            ball_position[1] -= 1
        elif ball_direction == 2:
            if ball_position[0] >= width -6:
                ball_direction = 1
            else:
                ball_direction = 4
        elif ball_direction == 3 and ball_position[0] >= 2 and ball_position[1] <= height-6:
            ball_position[0] -= 1
            ball_position[1] += 1
        elif ball_direction == 3:
            if ball_position[0] <= 1:
                ball_direction = 4
            elif bar_position-3  <= ball_position[0] <= bar_position+bar_size:
                ball_direction = 1
            else:
                # ball_position[0] -= 1
                # ball_position[1] += 1
                ball_position = [50, 15]
                ball_direction = 3
                bar_position = width//2 - bar_size//2
        elif ball_direction == 4 and ball_position[0] <= width-6 and ball_position[1] <= height-6:
            ball_position[0] += 1
            ball_position[1] += 1
        elif ball_direction == 4:
            if ball_position[0] >= width-6:
                ball_direction = 3
            elif bar_position-3 <= ball_position[0] <= bar_position+bar_size:
                ball_direction = 2
            else:
                # ball_position[0] += 1
                # ball_position[1] += 1
                ball_position = [50, 15]
                ball_direction = 3
                bar_position = width//2 - bar_size//2

    display_array[ball_position[1]*width+ball_position[0]] = "#"
    display_array[ball_position[1]*width+ball_position[0]+1] = "#"
    display_array[ball_position[1]*width+ball_position[0]+2] = "#"
    display_array[(ball_position[1]+1)*width+ball_position[0]] = "#"
    display_array[(ball_position[1]+1)*width+ball_position[0]+1] = "#"
    display_array[(ball_position[1]+1)*width+ball_position[0]+2] = "#"

    # bar_position, break_bool = bar_move(bar_position, width, bar_size, break_bool)  # bar move
    # if break_bool:
    #     break
    if __name__ == '__main__':
        try:
            key = input_with_timeout()
            if key == "a" and bar_position >= 2:
                bar_position -= 1
            elif key == "d" and bar_position <= width - bar_size - 3:
                bar_position += 1
            elif key == "q":
                break_bool = True
        except TimeoutError:
            pass
    os.system("clear")
    time_end = time.time()
    # bar_position = ball_position[0]-bar_size//2
    choice = random.choices(choices_list, weights = probability_list[ball_position[0]*ball_position[1]*ball_direction])[0]
    if 1 <= bar_position+choice <= width-2:
        bar_position += choice
    probability_list[ball_position[0]*ball_position[1]*ball_direction][choice+1] += (width-width//2) - abs(bar_position - ball_position[0]+bar_size//2)

    display_array = bar(bar_size, bar_position, display_array, width, height) # bar position

    for i in range(height):  # print
        display_array[width*i+width-1] = "\n"
    display_str = "".join(display_array)
    print(display_str)
    print(f"bar_position: {bar_position} ball_position: {ball_position} ball_direction: {ball_direction} choice: {choice} probability: {probability_list[ball_position[0]*ball_position[1]*ball_direction]}")