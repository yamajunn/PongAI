import readchar
import os

def bar_move(bar_position, width, bar_size, break_bool):
    key = readchar.readchar()
    os.system('cls')
    if key == "a" and bar_position >= 2:
        bar_position -= 1
    elif key == "d" and bar_position <= width - bar_size - 3:
        bar_position += 1
    elif key == "q":
        break_bool = True
    return [bar_position, break_bool]