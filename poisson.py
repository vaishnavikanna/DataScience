import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson, uniform
import itertools
#from scipy.interpolate import make_interp_splines
import pandas as pd

y = [0, 0, 1, 2, 0, 2, 2, 1, 1]


prior = np.linspace(0, 4, 100)

print(prior)
Likelihoods = []
def likelihoodcalc(priorcalc):
    return np.product(poisson.pmf(y,priorcalc))

for i in prior:
    Likelihoods.append(likelihoodcalc(i))

data= {'Priors': prior, 'Likelihood': Likelihoods}
lmda= list(itertools.repeat(4, 100))
#df= pd.DataFrame(data)
#df['Posterior'] = df['Priors'] * df['Likelihood']
Posteriors = [ lmda * likelihood for lmda, likelihood in zip(Likelihoods,lmda) ]
plt.plot(lmda, Posteriors, label = 'Posterior for lambda')
plt.legend()
plt.title('Posterior for parameter lambda')
plt.show()