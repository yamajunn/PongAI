import time
from Pong import pong
import random

from create_display import create_display
from bar import bar

width = 100
height = 30
probability_list = [[1, 1] for i in range(2)]
choices_list = [-1,1]
bar_size = 30
bar_position = width//2 - bar_size//2

ball_position = [width//2, height//2]
ball_direction = random.randint(0,3)

line = "#"
back = " "

try_count = 0
count = 0
count_list = []
display_array = create_display(width, height, line, back)  # create display
display_array = bar(bar_size, bar_position, display_array, width, height) # bar position

sleep = 0.001

while True:
    bar_position, ball_position, ball_direction, try_count = pong(width, height, probability_list, bar_size, bar_position, ball_position, ball_direction, line, back, try_count, count, count_list, display_array, sleep)

    if ball_position[0] <= bar_position+bar_size//2:
        num = 0
    else:
        num = 1
    choice = random.choices(choices_list, weights = probability_list[num])[0]
    if 1 <= bar_position+choice and bar_position+choice+bar_size <= width-2:
        bar_position += choice
    if bar_position <= ball_position[0] <= bar_position+bar_size:
        if choice == -1:
            probability_list[num][0] += 1
        else:
            probability_list[num][1] += 1