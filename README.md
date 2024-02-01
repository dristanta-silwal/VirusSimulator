# Simulating Corona-Virus and its Antivirus
Evolving corona virus and its antivirus using a genetic algorithm and deep learning from scratch with python.

![alt text](image.png)

This open source project simulates the behavior of a population of organisms and a virus within a confined space using Python and Matplotlib. The organisms move randomly within the space, while the virus appears at random positions and affects the organisms it comes into contact with.

## Project Description

- **Population Simulation**: The project creates a population of organisms represented by circles moving randomly within a defined space.

- **Virus Spread Simulation**: A virus, represented by a red circle, appears randomly in the space and remains in one position for a certain duration. It affects organisms it comes into contact with.

- **Visualization**: Matplotlib is used to visualize the simulation in real-time, showing the movement of organisms and the spread of the virus.

## Code Overview

- The code initializes the parameters for the population, including their positions, velocities, and radii, as well as parameters for the virus.

- It defines functions to plot organisms and the virus using Matplotlib's Circle patches.

- The `update` function is called in each frame of the animation to update the positions of the organisms and the virus, as well as to visualize them.

- The animation is created using Matplotlib's `FuncAnimation` class, which updates the plot in each frame.

## Usage

- Ensure you have Matplotlib installed (`pip install matplotlib`).

- Run the Python script to start the simulation. Adjust the parameters and the number of frames as needed.

## Future Improvements

- Incorporate more complex behaviors for the organisms, such as interactions between individuals.

- Implement a more realistic virus spread model, considering factors like transmission rate and immunity.

- Enhance the visualization to provide more insights into the simulation.

- Implement antivirus in the most affected areas and population finding nearest anitvirus, making each generation more efficient in fighting against virus.

- Also, evolving virus is a plan.