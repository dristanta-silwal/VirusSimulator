import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib.patches import Circle

# Set parameters
parameters = {
    'population_size': 100,
    'virus_size': 2,
    'antivirus_size': 10,
    'total_generation': 50,
    'dt': 0.5,
    'x_min': 0.50,
    'x_max': 9.80,
    'y_min': 0.50,
    'y_max': 9.80,
    'dv': 0.009,
    'virus_duration': 100  # Duration for which virus remains stationary
}
count_infected = 0
class Population:
    def __init__(self, parameters, name, ax):
        # global count_infected
        self.name = name
        self.ax = ax
        self.health = random.randint(4,5)
        self.x = random.uniform(parameters['x_min'], parameters['x_max'])
        self.y = random.uniform(parameters['y_min'], parameters['y_max'])
        self.health = random.randint(0, 5)
        self.color = 'grey'
        self.shape = Circle([self.x, self.y], 0.1, facecolor=self.color, edgecolor='none')
        self.angle = np.random.uniform(0, 2 * np.pi)  # Initial angle in radians
        self.speed = 0.05 # Linear speed
        self.is_infected = False
        self.is_recovered = False
        
    @staticmethod
    def create_population_instances(parameters, ax):
        pop_objs = []
        for i in range(parameters['population_size']):
            population_instance = Population(parameters, f"object {i}", ax)
            ax.add_artist(population_instance.shape)
            pop_objs.append(population_instance)
        return pop_objs

    def update_position(self, vir_obj_instance, antivirus_obj_instance):
        # Update position along the linear path
        self.x += self.speed * np.cos(self.angle)
        self.y += self.speed * np.sin(self.angle)
        
        # Apply a random change of angle
        self.angle += np.random.uniform(-np.pi/4, np.pi/4)

        # Check if new position is within bounds
        self.x = np.clip(self.x, parameters['x_min'], parameters['x_max'])
        self.y = np.clip(self.y, parameters['y_min'], parameters['y_max'])

        # Check for collision with virus
        collision_detected_virus= False
        for virus in vir_obj_instance:
            distance_virus = np.sqrt((self.x - virus.x)**2 + (self.y - virus.y)**2)
            if distance_virus < 0.3:  # Adjust this value according to your circle radius
                collision_detected_virus = True
                break

        if collision_detected_virus:
            self.color = 'red'  # Change color if collision occurs
            self.health = 0
            self.is_infected = True

        # Check for collision with virus
        collision_detected_antivirus= False
        if self.color == 'red':
            # collision_detected_antivirus= False
            for antivirus in antivirus_obj_instance:
                distance_antivirus = np.sqrt((self.x - antivirus.x)**2 + (self.y - antivirus.y)**2)
                if distance_antivirus < 0.5:  # Adjust this value according to your circle radius
                    collision_detected_antivirus = True
                    break
            if collision_detected_antivirus:
                self.color = 'skyblue'  # Change color if collision occurs
                self.health = random.randint(2,5)
                self.is_recovered = True
        self.shape.set_color(self.color)
        self.shape.set_center((self.x, self.y))
        self.color = self.shape.get_facecolor()  # Save the current color state


class Virus(Population):
    def __init__(self, parameters, name, ax):
        super().__init__(parameters, name, ax)
        self.transmission_rate = random.randint(1, 3)
        self.strength = random.randint(4, 7)
        self.color = 'purple'
        self.shape = Circle([self.x, self.y], 0.15, facecolor=self.color, edgecolor='none')
        self.hidden = False
        self.hidden_time = random.randint(10, 50)  # Random time to stay hidden
        self.time_hidden = 0

    @staticmethod
    def create_virus_instances(parameters, ax):
        virus_objs = []
        for i in range(parameters['virus_size']):
            virus_instance = Virus(parameters, f"object {i}", ax)
            ax.add_artist(virus_instance.shape)
            virus_objs.append(virus_instance)
        return virus_objs

    def virus_position(self):
        if self.hidden:
            plt.pause(0.05)
            super().update_position()
        else:
            self.time_hidden += 1
            if self.time_hidden >= self.hidden_time:
                self.hidden = False
                self.time_hidden = 0
                self.x = random.uniform(parameters['x_min'], parameters['x_max'])
                self.y = random.uniform(parameters['y_min'], parameters['y_max'])
                self.shape.set_center((self.x, self.y))
                self.deploy  = False

class Antivirus(Population):
    def __init__(self, parameters, name, ax):
        super().__init__(parameters, name, ax)
        self.vaccination_rate = random.uniform(1, 3)
        self.efficiency = random.uniform(4, 7)
        self.color = 'blue'
        self.shape = Circle([self.x, self.y], 0.1, facecolor=self.color, edgecolor='green')
        self.deploy = False
        
    @staticmethod
    def create_antivirus_instances(parameters, ax):
        antivirus_objs = []
        for i in range(parameters['antivirus_size']):
            antivirus_instance = Antivirus(parameters, f"object {i}", ax)
            ax.add_artist(antivirus_instance.shape)#.set_visible(False)
            antivirus_objs.append(antivirus_instance)
        return antivirus_objs

# Plot setup
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim([0, 10])
ax.set_ylim([0, 10])
ax.set_title('Corona Virus evolution model')

# Creating population, virus, and antivirus instances
pop_obj_instance = Population.create_population_instances(parameters, ax)
vir_obj_instance = Virus.create_virus_instances(parameters, ax)
# antivirus_obj_instance = Antivirus.create_antivirus_instances(parameters, ax)

# Initialize an empty list for antivirus instances
antivirus_obj_instance = []

# Deploying population and updating frame
for _ in range(500):
    # Update population positions and check for infections
    for pop in pop_obj_instance:
        pop.update_position(vir_obj_instance,antivirus_obj_instance)
        if pop.is_infected: 
            count_infected += 1
    # Update virus positions
    for vir in vir_obj_instance:
        vir.virus_position()

    # Calculate the percentage of infected population
    infected_percentage = (count_infected / parameters['population_size']) * 100
    
    # Deploy antivirus if the infected percentage is greater than 30%
    if infected_percentage > 15 and not antivirus_obj_instance:
        antivirus_obj_instance = Antivirus.create_antivirus_instances(parameters, ax)
    
    # Update antivirus positions if they have been deployed
    if antivirus_obj_instance:
        for antivir in antivirus_obj_instance:
            antivir.update_position(vir_obj_instance, antivirus_obj_instance)

    # for antivir in antivirus_obj_instance:
    #     antivir.update_position(vir_obj_instance)
    
    plt.pause(0.011)
    count_infected = 0 # Reset the count for the next iteration

for pop in pop_obj_instance:
    print(f"Population {pop.name}: Health = {pop.health}, Color = {pop.color}")
    if pop.is_infected == True:
      count_infected += 1
    print("infected number is: ", count_infected)
print("\n")


plt.show()