import numpy as np


# Creating a Function.
def normal_dist(x, mean, sd):
    prob_density = 1 / (sd * np.sqrt(2 * np.pi)) * np.exp(- (x - mean) ** 2 / (2 * sd ** 2))
    return prob_density


x = [157434, 261952, 144657, 118777, 147511, 163025, 120131, 162745, 155569]

dist1 = []
dist2 = []
dist3 = []

for val in range(len(x)):
    mean = 188014.34
    sd = 52541.39
    # Apply function to the data.
    pdf = normal_dist(float(x[val]), float(mean), float(sd))
    dist1.append(pdf)
    print(pdf)

for val in range(len(x)):
    mean = 143104.34
    sd = 18330.95
    # Apply function to the data.
    pdf = normal_dist(float(x[val]), float(mean), float(sd))
    dist2.append(pdf)
    print(pdf)

for val in range(len(x)):
    mean = 146148.34
    sd = 18628.83
    # Apply function to the data.
    pdf = normal_dist(float(x[val]), float(mean), float(sd))
    dist3.append(pdf)
    print(pdf)

z1 = []
z2 = []
z3 = []

print("z1")
for i in range(len(x)):
    z = dist1[i] / (dist1[i] + dist2[i] + dist3[i])
    z1.append(z)
    print(z)

print("z2")
for i in range(len(x)):
    z = dist2[i] / (dist1[i] + dist2[i] + dist3[i])
    z2.append(z)
    print(z)

print("z3")
for i in range(len(x)):
    z = dist3[i] / (dist1[i] + dist2[i] + dist3[i])
    z3.append(z)
    print(z)

mean1 = np.average(x, weights = z1)
mean2 = np.average(x, weights = z2)
mean3 = np.average(x, weights = z3)

print("Mean values: ")
print(mean1)
print(mean2)
print(mean3)

variance1 = np.average((x-mean1)**2, weights=z1)
variance2 = np.average((x-mean2)**2, weights=z2)
variance3 = np.average((x-mean3)**2, weights=z3)

print(variance1)

sd1 = np.sqrt(variance1)
sd2 = np.sqrt(variance2)
sd3 = np.sqrt(variance3)

print("SD values: ")

print(sd1)
print(sd2)
print(sd3)



