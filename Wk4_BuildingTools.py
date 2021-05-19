import random
# import time
import operator
import matplotlib.pyplot

# start = time.clock() - start timer for running the code
# Function to calculate distance between agents
def distance_between(agents_row_a, agents_row_b):
    #  return agents_row_a[0] - needed to be replaced with the pythag equation
    return (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5
    
        
num_of_agents = 5
num_of_iterations = 10
agents = []

# Make the agents.
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):

        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100

        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100

# compares the agents locations
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between (agents_row_a, agents_row_b)
    

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show()

# for loop to compare each agent
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
print(distance)


# end = time.clock() - stops timer of the code.

# print("time = " + str(end - start)) - prints the difference between start and end times.
