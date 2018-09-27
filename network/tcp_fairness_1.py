import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

THROUGHPUT = 1000

fig, ax = plt.subplots()
ax.set_xlim(0, THROUGHPUT * 1.1)
ax.set_ylim(0, THROUGHPUT * 1.1)
ax.grid()

def plot_efficiency_line(ax):
  x = np.arange(0, THROUGHPUT, 50)
  y = THROUGHPUT - x
  ax.scatter(x, y, marker='.', c="grey")

def plot_fairness_line(ax):
  x = np.arange(0, THROUGHPUT, 50)
  y = x
  ax.scatter(x, y, marker='.', c="black")
# plot two nodes
point_xs = [int(np.random.rand() * THROUGHPUT)]
point_ys = [THROUGHPUT - point_xs[0]] 

splot = ax.scatter(point_xs, point_ys, marker='.')

def update(i):
  x, y = point_xs[-1], point_ys[-1]
  if x + y >= THROUGHPUT:
    x = x // 2
    y = y // 2
  else:
    x += 2
    y += 2
  point_xs.append(x)
  point_ys.append(y)
  splot.set_offsets(np.c_[point_xs, point_ys])

plot_efficiency_line(ax)
plot_fairness_line(ax)
ani = FuncAnimation(fig, update, repeat=True, interval=1)
plt.show()

