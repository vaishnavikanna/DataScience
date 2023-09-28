import numpy as np
import matplotlib.pyplot as plt


# No of data points used
N = 20

# normal distribution
data = np.random.randn(N)

# sort the data in ascending order
x = np.sort(data)

# get the cdf values of y
y = np.arange(N) / float(N)

print(np.arange(N))
print(y)

# plotting
plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.title('CDF using sorting the data')

plt.plot(x, y, marker='o')
#plt.show()
