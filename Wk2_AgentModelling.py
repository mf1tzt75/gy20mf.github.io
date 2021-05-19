import random

y0 = 50
x0 = 50

if random.random() < 0.5: # random number between 0 and 1
    y0 += 1
else:
    y0 -= 1

if random.random() < 0.5:
    x0 += 1
else:
    x0 -= 1

print(y0, x0)


y1 = 50
x1 = 50

if random.random() < 0.5:
    y1 += 1
else:
    y1 -= 1

if random.random() < 0.5:
    x1 += 1
else:
    x1 -= 1

print(y1, x1)

answer = (((y0 - y1)**2) + ((x0 - x1)**2))**0.5 # works out the distance moved.
print(answer)