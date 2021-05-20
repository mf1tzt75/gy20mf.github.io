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

# Animated Plot # Defines figure size and axes.
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


#ax.set_autoscale_on(False)

# Plot environment
#matplotlib.pyplot.imshow(environment)
#matplotlib.pyplot.show()

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
num_of_agents = input("How many agents? ")
num_of_iterations = input("How many iterations? ")
neighbourhood = input("Distance between agents before they share? ")

num_of_agents = int(num_of_agents)
num_of_iterations = int(num_of_iterations)
neighbourhood = int(neighbourhood)

# Make the agents.
agents = []
print("Initial agents")
for i in range(num_of_agents):
    agents.append(agentframework.Agent(i, random.randint(0, 99), 
                                               random.randint(0, 99), 
                                               environment, agents))

carry_on = True
# This function does the move, eat and share functions from Class and animates them.
def update(frame_number):
        
    fig.clear() 
    global carry_on

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

def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1


#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=10)
animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)



matplotlib.pyplot.show()


# Calculate the distances between all the agents.
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
print(distance)
