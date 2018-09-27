import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from random import randint

THROUGHPUT = 1000
NODE_NUM = 5

current_throughput = 0

fig, axs = plt.subplots(NODE_NUM, 1, sharex=True)

lines = []
for ax in axs:
  l, = ax.plot([], [], animated=True)
  lines.append(l)

def init():
  for ax in axs:
    ax.set_xlim((0, 2000))
    ax.set_ylim((0, THROUGHPUT))
  return lines

def next_data_func_gen(NODE_NUM):
  global current_throughput

  # init speed
  speed_list = [randint(0, THROUGHPUT // NODE_NUM) for _ in range(NODE_NUM)]
  speed_list[-1] = THROUGHPUT - sum(speed_list[:-1]) - 50
  current_throughput += sum(speed_list)
  def next_data_func():
    nonlocal speed_list
    global current_throughput

    next_data = []

    new_speed_list = []
    for speed in speed_list:
      delta = 1
      if current_throughput + delta > THROUGHPUT and speed == max(speed_list):
        delta = -speed // 2
      speed += delta
      current_throughput += delta
      new_speed_list.append(speed)
    speed_list = new_speed_list
    return speed_list
  return next_data_func
  
next_data_func = next_data_func_gen(NODE_NUM)

def update(frame):
  new_data = next_data_func()
  for l, datum in zip(lines, new_data):
    xdata, ydata = l.get_data()
    ydata = np.append(ydata, datum)
    xdata = range(0, len(ydata))
    l.set_data(xdata, ydata)
  return lines

ani = FuncAnimation(fig, update, interval=1, init_func=init, blit=True)
plt.show()
