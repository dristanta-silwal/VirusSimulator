import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib.patches import Circle
from matplotlib.animation import FuncAnimation

# Set random seed for reproducibility
np.random.seed(random.randint(1, 100))

# Define the number of organisms
num_organisms = 100

# Initial positions, velocities, and radii of the organisms
x = np.random.uniform(0, 3, num_organisms)
y = np.random.uniform(0, 3, num_organisms)
vx = np.random.normal(0, 0.01, num_organisms)  # Initial x velocity
vy = np.random.normal(0, 0.01, num_organisms)  # Initial y velocity
radii = np.random.uniform(0.03, 0.07, num_organisms)

# Initialize virus parameters
virus_x = np.random.uniform(0, 3)
virus_y = np.random.uniform(0, 3)
virus_radius = np.random.uniform(0.05, 0.1)
virus_duration = 50  # Duration for which virus remains at one position
virus_counter = 0  # Counter to track virus duration

def plot_organism(x, y, r, ax):
    circle = Circle([x, y], r, edgecolor='g', facecolor='lightgreen', zorder=8)
    ax.add_artist(circle)

def plot_virus(x, y, r, ax):
    circle = Circle([x, y], r, edgecolor='darkred', facecolor='red', zorder=8)
    ax.add_artist(circle)

def update(frame):
    global virus_x, virus_y, virus_radius, virus_counter
    
    ax.clear()
    ax.set_aspect('equal')
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 3)
    ax.axes.get_xaxis().set_ticks([])
    ax.axes.get_yaxis().set_ticks([])
    
    # Update the positions of the organisms with random movements
    for i in range(num_organisms):
        # Update position based on velocity
        x[i] = max(0, min(3, x[i] + vx[i]))
        y[i] = max(0, min(3, y[i] + vy[i]))
        
        # Check boundaries and adjust velocity if necessary
        if x[i] <= 0 or x[i] >= 3:
            vx[i] *= -1  # Reverse x velocity
        if y[i] <= 0 or y[i] >= 3:
            vy[i] *= -1  # Reverse y velocity
        
        # Update velocity with random Gaussian noise
        vx[i] += np.random.normal(0, 0.001)
        vy[i] += np.random.normal(0, 0.001)
        
        plot_organism(x[i], y[i], radii[i], ax)
    
    # Update the virus position and duration
    if virus_counter == 0:
        # Reset virus position and radius
        virus_x = np.random.uniform(0, 3)
        virus_y = np.random.uniform(0, 3)
        virus_radius = np.random.uniform(0, 0.1)
        virus_counter = virus_duration
    else:
        plot_virus(virus_x, virus_y, virus_radius, ax)
        virus_counter -= 1

fig, ax = plt.subplots() 
ani = FuncAnimation(fig, update, frames=range(1000), repeat=False, interval=8)  # Decrease the interval
plt.show()
