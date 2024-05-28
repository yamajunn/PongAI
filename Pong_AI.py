import time
from Pong import pong
import random
import matplotlib.pyplot as plt

from create_display import create_display
from bar import bar

width = 100
height = 30
line = "#"
back = " "
display_array = create_display(width, height, line, back)  # create display

ball_position = [width//2, height//2]
ball_direction = random.randint(0,3)

bar_size = 30
bar_position = width//2 - bar_size//2
display_array = bar(bar_size, bar_position, display_array, width, height) # bar position

sleep = 0.001

try_count = 0
count = 0
count_list = []

probability_list = [[1, 1] for i in range(2)]
probability_list = [[180835, 5884], [30584, 104217]]
choices_list = [-1,1]

while True:
    bar_position, ball_position, ball_direction, try_count, count_list, count = pong(width, height, probability_list, bar_size, bar_position, ball_position, ball_direction, line, back, try_count, count, count_list, display_array, sleep)

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
    # print(count_list)
    
    if try_count == 10:
        break

print(probability_list)
x_list = [i for i in range(len(count_list))]
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)
ax.plot(x_list, count_list, label="test")
plt.legend()    
plt.show()