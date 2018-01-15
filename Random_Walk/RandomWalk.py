import matplotlib.pyplot as plt
import numpy as np
np.random.seed(123)
all_walks = []

# Simulate random walk 250 times
for i in range(250) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
			# We use max Function to make sure step can't go below 0
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)

        # 0.01% chance of falling down
        if np.random.rand() <= 0.001 :
            step = 0

        random_walk.append(step)
    all_walks.append(random_walk)

#Plots
np_aw_t = np.transpose(np.array(all_walks))
plt.plot(np_aw_t)
plt.show()

ends = np_aw_t[-1]

#  histogram Plot of ends
plt.hist(ends)
plt.show()