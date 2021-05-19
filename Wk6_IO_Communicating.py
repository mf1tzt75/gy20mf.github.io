import matplotlib.pyplot
import matplotlib.animation
import agentframework
import csv
import random

# Set the random seed for reproducibility
random.seed(0)
#random.seed(1)

# Read in a file to initialise environment
f = open('in.txt', newline='') # with command to open text file.
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
environment = []  
for row in reader:
    rowlist = []
    environment.append(rowlist)
    for value in row:
        rowlist.append(value)
        #print(value) # Test the reading in of environment.
    #print(rowlist)
f.close()
#print(environment)

# Plot environment
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()

def distance_between(a, b):
    """
    Calculate the distance between a, b.

    Parameters
    ----------
    a : Agent
        This is a goat on a haystack.
    b : Agent
        This is a goat on a haystack.

    Returns
    -------
    Number
        Euclidean distance in a 2D space between a and b.
    """
    return (((a.x - b.x)**2) + ((a.y - b.y)**2))**0.5

# Initialise variables
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20

# Make the agents.
agents = []
for i in range(num_of_agents):
    agents.append(agentframework.Agent(i, random.randint(0, 99), 
                                       random.randint(0, 99), 
                                       environment, agents))
    #print(agents[i]) # Check the agents are created
print("Initial agents")
for i in range(num_of_agents):
    print(agents[i])
    
## Test the distance function
#d = distance_between(agentframework.Agent(0, 0, environment, agents),
#agentframework.Agent(3, 4, environment, agents))
#print(d)

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move() # uses the move method from class Agent.
        agents[i].eat() # uses the eat method in Agent class.
        agents[i].share_with_neighbours(neighbourhood) # uses the eat method in Agent class.
        
# Plot
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y) # as in line 7 and 8 pulls from Agent class.
matplotlib.pyplot.show()

# Calculate the distances between all the agents.
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
print(distance)
