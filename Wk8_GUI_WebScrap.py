import matplotlib
import matplotlib.pyplot
import matplotlib.animation
import agentframework
import csv
import tkinter
import random
import requests
import bs4

matplotlib.use('TkAgg')

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

page = requests.get("https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html")
content = page.text
#print(content)
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs)


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
print("Initial agents")
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
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

def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()

# creates the tkinter display box
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

# creates the menu bar and the model button to press to run the model.
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run) 
model_menu.add_command(label="Exit", command=model_menu.quit)

# Calculate the distances between all the agents.
for agents_row_a in agents:
   for agents_row_b in agents:
      distance = distance_between(agents_row_a, agents_row_b)

tkinter.mainloop()