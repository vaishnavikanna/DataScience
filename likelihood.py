import numpy as np


def normal_dist(x, mean, sd):
    prob_density = 1 / (sd * np.sqrt(2 * np.pi)) * np.exp(- (x - mean) ** 2 / (2 * sd ** 2))
    return prob_density

# male
x = 57
male = [57,65,76]
mean = np.average(male)
variance = np.average((x-mean)**2)
sd = np.sqrt(variance)

likelihood = normal_dist(x, mean, sd)
print(likelihood)

# female
y = 23
female = [20,42,27]
meanf = np.average(female)
variancef = np.average((y-mean)**2)
sdf = np.sqrt(variance)
female_likelihood = normal_dist(y, meanf, sdf)
print(female_likelihood)

