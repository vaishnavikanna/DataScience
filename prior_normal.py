import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm, uniform, stats
import pandas as pd


y = [0.3120639, 0.5550930, 0.2493114, 0.9785842]

mu = np.arange(10)
sigma = np.arange(10)
priormu = uniform.rvs(mu)
priorsigma = uniform.rvs(sigma)

Likelihoods = []
def likelihoodcalc(mean, sd):
    return np.product(norm.pdf(y, mean, sd))

for i, j in zip(mu, sigma):
    Likelihoods.append(likelihoodcalc(i, j))


data= {'Priormu': priormu, 'Priorsigma': priorsigma, 'Likelihood': Likelihoods}
df = pd.DataFrame(data)
df['Posteriormu'] = df['Priormu'] * df['Likelihood']
df['Posteriorsigma'] = df['Priorsigma'] * df['Likelihood']
print(df)

plt.plot(df['Posteriormu'], label='Posterior for mu')
plt.plot(df['Posteriorsigma'], label='Posterior for sigma')
plt.legend()
plt.title('Posterior for parameters mu and sigma')
plt.show()
