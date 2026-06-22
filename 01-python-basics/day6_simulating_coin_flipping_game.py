import numpy as np

simulation = np.zeros((10000, 100))

for i in range(10000):
    flips = np.random.choice([-1, 1], size = 100)
    simulation[i] = np.cumsum(flips)

totals = simulation[:, -1]

simulation_mean = np.mean(totals)
simulation_std = round(np.std(totals), 4)
simulation_max = np.max(totals)
simulation_min = np.min(totals)
profit_probability = np.mean(totals>0)

print(f' The simulations gave a mean of {simulation_mean} and a standard deviation' 
      f'  of {simulation_std}. The \'best\' simulation'
      f' ended on {simulation_max} and the \'worst\' on {simulation_min}.'
      f' The probability of making profit on any given simluation is {profit_probability}')
