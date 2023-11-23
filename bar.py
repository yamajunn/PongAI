def bar(bar_size, bar_position, display_array, width, height):
    for i in range(bar_size):
        display_array[width*(height-3)+i + bar_position] = "#"
        display_array[width*(height-2)+i + bar_position] = "#"
    return display_array