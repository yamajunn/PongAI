import numpy as np

def create_display(width, height, line, back):
    display_array = np.array([back for i in range((width)*height)])

    for i in range(width):
        display_array[i] = line
        display_array[width*(height-1)+i] = line

    for i in range(height):
        display_array[i*width] = line
        display_array[i*width+width-2] = line
    return display_array