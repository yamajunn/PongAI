import numpy as np
import readchar
import os

from create_display import create_display
from bar import bar

width = 100
height = 30
line = "="
back = " "
display_array = create_display(width, height, line, back)  # create display

bar_size = 20
bar_position = width//2 - bar_size//2 - 1

while True:
    display_array = create_display(width, height, line, back)  # create display
    
    key = readchar.readchar()
    os.system('cls')
    if key == "a" and bar_position >= 2:
        bar_position -= 1
    elif key == "d" and bar_position <= width - bar_size - 3:
        bar_position += 1
    elif key == "q":
        break

    display_array = bar(bar_size, bar_position, display_array, width, height) # bar position

    for i in range(height):
        display_array[width*i+width-1] = "\n"

    display_str = "".join(display_array)
    print(display_str)
    print(bar_position)