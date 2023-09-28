import numpy as np
a1 = np.array((0, 0.77))
b1 = np.array((1, 1))

dist1 = np.sqrt(np.sum(np.square(a1-b1)))

a2 = np.array((0, 0.77))
b2 = np.array((0.25, 0.69))

dist2 = np.sqrt(np.sum(np.square(a2-b2)))

a3 = np.array((0, 0.77))
b3 = np.array((0.81, 0))

dist3 = np.sqrt(np.sum(np.square(a3-b3)))

a4 = np.array((0.62, 0))
b4 = np.array((0.70, 0.11))

dist4 = np.sqrt(np.sum(np.square(a4-b4)))

print(dist1)
print(dist2)
print(dist3)
print(dist4)