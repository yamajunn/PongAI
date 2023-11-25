import readchar
import os
from timeout_decorator import timeout, TimeoutError

def bar_move(bar_position, width, bar_size, break_bool):
    TIMEOUT_SEC = 0.1
    @timeout(TIMEOUT_SEC)
    def input_with_timeout():
        return readchar.readchar()
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
    return [bar_position, break_bool]