import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

# First set up the figure, the axis, and the plot element we want to animate
fig, ax = plt.subplots(subplot_kw=dict(projection='polar', frameon=True), figsize=(15, 15))

# initialization function: plot the background of each frame
def init():
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    return ax


# animation function.  This is called sequentially
def animate(i):
    fig1, ax1, cax1 = vis.plot_polar_contour(cop_proc[i], cmap='spring', levels=200)
    cax = cax1
    return cax


# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=30, interval=2000, blit=True)
anim.save('test.html')