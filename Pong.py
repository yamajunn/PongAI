import numpy as np
import os
import time
import readchar
from timeout_decorator import timeout, TimeoutError
import random
import matplotlib.pyplot as plt

from create_display import create_display
from bar import bar
# from bar_move import bar_move

TIMEOUT_SEC = 0.1
@timeout(TIMEOUT_SEC)
def input_with_timeout():
    return readchar.readchar()

width = 100
height = 30

try_count = 0

probability_list = [[10, 10] for i in range(4)]
choices_list = [-1,1]

line = "#"
back = " "

bar_size = 30
bar_position = width//2 - bar_size//2

break_bool = False

ball_position = [50, 1]
ball_direction = 0

display_array = create_display(width, height, line, back)  # create display

display_array = bar(bar_size, bar_position, display_array, width, height) # bar position

for i in range(height):  # print
    display_array[width*i+width-1] = "\n"
display_str = "".join(display_array)
print(display_str)
print(bar_position)

time_start = 0
time_end = 0

count = 0
count_list = []
while True:
    # if time_end - time_start > 0.14:
    #     time_start = time.time()
    display_array = create_display(width, height, line, back)  # create display

    # if time_end - time_start > 0.1:
    if ball_direction == 0 and ball_position[0] >= 2 and ball_position[1] >= 2:
        ball_position[0] -= 1
        ball_position[1] -= 1
    elif ball_direction == 0:
        if ball_position[0] <= 1:
            ball_direction = 1
        else:
            ball_direction = 2
    elif ball_direction == 1 and ball_position[0] <= width-6 and ball_position[1] >= 2:
        ball_position[0] += 1
        ball_position[1] -= 1
    elif ball_direction == 1:
        if ball_position[0] >= width -6:
            ball_direction = 0
        else:
            ball_direction = 3
    elif ball_direction == 2 and ball_position[0] >= 2 and ball_position[1] <= height-6:
        ball_position[0] -= 1
        ball_position[1] += 1
    elif ball_direction == 2:
        if ball_position[0] <= 1:
            ball_direction = 3
        elif bar_position-3  <= ball_position[0] <= bar_position+bar_size:
            ball_direction = 0
        else:
            # ball_position[0] -= 1
            # ball_position[1] += 1
            ball_position = [50, 15]
            ball_direction = random.randint(0,3)
            bar_position = width//2 - bar_size//2
            try_count += 1
            count_list.append(count)
            count = 0
    elif ball_direction == 3 and ball_position[0] <= width-6 and ball_position[1] <= height-6:
        ball_position[0] += 1
        ball_position[1] += 1
    elif ball_direction == 3:
        if ball_position[0] >= width-6:
            ball_direction = 2
        elif bar_position-3 <= ball_position[0] <= bar_position+bar_size:
            ball_direction = 1
        else:
            # ball_position[0] += 1
            # ball_position[1] += 1
            ball_position = [50, 15]
            ball_direction = random.randint(0,3)
            bar_position = width//2 - bar_size//2
            try_count += 1
            count_list.append(count)
            count = 0

    display_array[ball_position[1]*width+ball_position[0]] = "#"
    display_array[ball_position[1]*width+ball_position[0]+1] = "#"
    display_array[ball_position[1]*width+ball_position[0]+2] = "#"
    display_array[(ball_position[1]+1)*width+ball_position[0]] = "#"
    display_array[(ball_position[1]+1)*width+ball_position[0]+1] = "#"
    display_array[(ball_position[1]+1)*width+ball_position[0]+2] = "#"

    # bar_position, break_bool = bar_move(bar_position, width, bar_size, break_bool)  # bar move
    # if break_bool:
    #     break

    # if __name__ == '__main__':
    #     try:
    #         key = input_with_timeout()
    #         if key == "a" and bar_position >= 2:
    #             bar_position -= 1
    #         elif key == "d" and bar_position <= width - bar_size - 3:
    #             bar_position += 1
    #         elif key == "q":
    #             break_bool = True
    #     except TimeoutError:
    #         pass
    os.system("clear")
    # time_end = time.time()
    # bar_position = ball_position[0]-bar_size//2
    choice = random.choices(choices_list, weights = probability_list[ball_direction])[0]
    if 1 <= bar_position+choice and bar_position+choice+bar_size <= width-2:
        bar_position += choice
        # probability_list[ball_direction][choice+1] += (width-width//2) - abs(bar_position - ball_position[0]+bar_size//2)
    if bar_position <= ball_position[0] <= bar_position+bar_size:
        if choice == -1:
            probability_list[ball_direction][0] += 1
        else:
            probability_list[ball_direction][1] += 1
    # elif probability_list[ball_direction][choice+1] > 1:
    #     probability_list[ball_direction][choice+1] -= 1

    display_array = bar(bar_size, bar_position, display_array, width, height) # bar position

    for i in range(height):  # print
        display_array[width*i+width-1] = "\n"
    display_str = "".join(display_array)

    print(display_str,try_count)
    print(probability_list)

    # print(f"bar_position: {bar_position} ball_position: {ball_position} choice: {choice} ball_direction: {ball_direction} probability: {probability_list[ball_direction]}")
    
    time.sleep(0.001)
    count += 1
    # if len(count_list) == 1000:
    #     break

x_list = [i for i in range(len(count_list))]

# Figureの初期化
fig = plt.figure(figsize=(12, 8)) #...1

# Figure内にAxesを追加()
ax = fig.add_subplot(111) #...2
ax.plot(x_list, count_list, label="test") #...3

# 凡例の表示
plt.legend()    

# プロット表示(設定の反映)
plt.show()