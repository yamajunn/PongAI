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

def pong(width, height, probability_list, bar_size, bar_position, ball_position, ball_direction, line, back, try_count, count, count_list, display_array, sleep):

    #  1012
    # [[28530, 9987], [7156, 33990]]

    # 2625
    # [[180835, 5884], [30584, 104217]]

    display_array = create_display(width, height, line, back)  # create display

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
            ball_position = [width//2, height//2]
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
            ball_position = [width//2, height//2]
            ball_direction = random.randint(0,3)
            bar_position = width//2 - bar_size//2
            try_count += 1
            count_list.append(count)
            count = 0

    for i in range(3):
        display_array[ball_position[1]*width+ball_position[0]+i] = "#"
        display_array[(ball_position[1]+1)*width+ball_position[0]+i] = "#"

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
    # bar_position, break_bool = bar_move(bar_position, width, bar_size, break_bool)  # bar move
    # if break_bool:
    #     break

    # os.system("clear")

    display_array = bar(bar_size, bar_position, display_array, width, height) # bar position

    # for i in range(height):  # print
    #     display_array[width*i+width-1] = "\n"
    # display_str = "".join(display_array)
    # print(display_str)
    # print(try_count)
    # print(probability_list)

    # time.sleep(sleep)
    count += 1
    return [bar_position, ball_position, ball_direction, try_count, count_list, count]