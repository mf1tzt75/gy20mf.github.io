import operator
import random
import matplotlib.pyplot

# y0 = random.randint(0,99)
# x0 = random.randint(0,99)  This creates variables that can be linked too!
num_of_agents = 5
num_of_iterations = 10

agents = []
n = 0
for i in range(num_of_agents): # Creates the Agent(s)
    agents.append([random.randint(0, 100), random.randint(0, 100)])

for j in range(num_of_iterations): # Moves the agent by set iterations
    for i in range(num_of_agents): # code compression from wk2 
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100 # torus effect to solve the edge issue.
        else:
            agents[i][0] = (agents[i][0] - 1) % 100

        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100

print(agents)

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0]) # Wk3 code shrinking.
# matplotlib.pyplot.scatter(agents[1][1],agents[1][0]) # removed as previous is in the for loop.
matplotlib.pyplot.show()