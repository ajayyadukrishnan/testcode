import numpy as np
import matplotlib.pyplot as plt

# Create 1000 samples from a normal distribution
rng = np.random.default_rng()
vals = rng.standard_normal(1000)

#And make a histogram
plt.hist(vals)
plt.ylabel('counts')
plt.title('1000 random numbers generated from a standard normal distribution')
plt.savefig('standard normal historgram.png')
