



#en saanut millään toimimaan

from matplotlib import pyplot as plt, patches
import numpy as np
from fractions import Fraction as fr

import matplotlib as mpl

fig = plt.figure()
ax = fig.subplots()

ymp = patches.Circle((0, 0), radius=1, fill=0)
ax.add_patch(ymp)

# Move left y-axis and bottom x-axis to centre, passing through (0,0)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Show ticks in the left and lower axes only
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.axis('equal')

plt.xticks([-1, 0, 1], minor=True)
plt.yticks([-1, 0, 1])

pii=np.pi
pist_xy=np.array([pii, pii, 3*pii, pii])
nim=np.array([1, 2, 4, 6])
varit=np.array(['red', 'green', 'blue', 'orange'])

text = [
    r'$\pi$', r'$\frac{\pi}{2}$', r'$\frac{3\pi}{4}$', r'$\frac{\pi}{6}$',
    r'$\frac{\pi}{3}$', r'$\frac{\pi}{4}$', r'$\frac{2\pi}{3}$', r'$\frac{3\pi}{2}$'
]

x = np.cos(pist_xy/nim)
y = np.sin(pist_xy/nim)

plt.scatter(x, y, color=varit, marker='X')

for i in range(len(pist_xy)):
    plt.annotate(text[i],
                 xy=(x[i], y[i]), xycoords='data',
                 xytext=(+20, +15), textcoords='offset points', fontsize=12,
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"))


plt.show()