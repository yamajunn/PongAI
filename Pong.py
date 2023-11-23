import numpy as np

from create_display import create_display
from bar import bar
from bar_move import bar_move

width = 100
height = 30
line = "="
back = " "

bar_size = 30
bar_position = width//2 - bar_size//2

break_bool = False

display_array = create_display(width, height, line, back)  # create display

display_array = bar(bar_size, bar_position, display_array, width, height) # bar position

for i in range(height):  # print
    display_array[width*i+width-1] = "\n"
display_str = "".join(display_array)
print(display_str)
print(bar_position)


while True:
    display_array = create_display(width, height, line, back)  # create display

    bar_position, break_bool = bar_move(bar_position, width, bar_size, break_bool)  # bar move
    if break_bool:
        break

    display_array = bar(bar_size, bar_position, display_array, width, height) # bar position

    for i in range(height):  # print
        display_array[width*i+width-1] = "\n"
    display_str = "".join(display_array)
    print(display_str)
    print(bar_position)