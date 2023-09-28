import pystan
from numpy import *
import matplotlib.pyplot as plt

obs = 20
x_sample = random.binomial(1, 0.5, obs)
y_sample = random.binomial(1, 0.5, obs)
alpha_sample = 0.3
beta_x_sample = 0.3
beta_y_sample = 0.2
sigma = 0.7
z_sample = alpha_sample+beta_x_sample*x_sample+beta_y_sample*y_sample
sim_data = random.normal(z_sample,sigma,obs)
print(sim_data) #simulated data

model = """
data {
   int<lower=4> N; // Number of data points
   real x[N];      // the 1st predictor
   real y[N];      // the 2nd predictor
   real z[N];      // the outcome
}
parameters {
   real alpha;     // intercept
   real betax;     // x-slope
   real betay;     // y-slope
   real<lower=0> sigma;       // dispersion
}
model {
   for (i in 1:N)
      z[i] ~ normal(alpha + betax * x[i] + betay * y[i], sigma);
}"""

data = {'N':obs, 'x':x_sample, 'y':y_sample, 'z':z_sample}

sm = pystan.StanModel(model_code=model)
fit= sm.sampling(data=data)
summary = fit.summary()

print(summary)