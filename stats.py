import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generating example data for time taken, total clicks, and total misclicks
np.random.seed(42)  # Setting seed for reproducibility

participants = ['Participant {}'.format(i) for i in range(1, 6)]
tasks = ['Task {}'.format(i) for i in range(1, 4)]

data = [
	{ 'Participant': 'hunter', 'Task': 'route', 'TimeTaken': 3.7, 'TotalClicks': 1, 'TotalMisclicks': 0, },
	{ 'Participant': 'hunter', 'Task': 'waypoint', 'TimeTaken': 4.6, 'TotalClicks': 2, 'TotalMisclicks': 0, },
	{ 'Participant': 'hunter', 'Task': 'Map Layers', 'TimeTaken': 8.4, 'TotalClicks': 5, 'TotalMisclicks': 1, },

	{ 'Participant': 'Ice-Climber', 'Task': 'route', 'TimeTaken': 4.2, 'TotalClicks': 2, 'TotalMisclicks': 1, },
	{ 'Participant': 'Ice-Climber', 'Task': 'waypoint', 'TimeTaken': 3.6, 'TotalClicks': 2, 'TotalMisclicks': 0, },
	{ 'Participant': 'Ice-Climber', 'Task': 'Map Layers', 'TimeTaken': 9.1, 'TotalClicks': 4, 'TotalMisclicks': 0, },

	{ 'Participant': 'Mountaineer', 'Task': 'route', 'TimeTaken': 2.7, 'TotalClicks': 1, 'TotalMisclicks': 0, },
	{ 'Participant': 'Mountaineer', 'Task': 'waypoint', 'TimeTaken': 3, 'TotalClicks': 2, 'TotalMisclicks': 0, },
	{ 'Participant': 'Mountaineer', 'Task': 'Map Layers', 'TimeTaken': 9.8, 'TotalClicks': 4, 'TotalMisclicks': 0, },

	{ 'Participant': 'Backpacker', 'Task': 'route', 'TimeTaken': 3, 'TotalClicks': 1, 'TotalMisclicks': 0, },
	{ 'Participant': 'Backpacker', 'Task': 'waypoint', 'TimeTaken': 4, 'TotalClicks': 2, 'TotalMisclicks': 0, },
	{ 'Participant': 'Backpacker', 'Task': 'Map Layers', 'TimeTaken': 10.1, 'TotalClicks': 6, 'TotalMisclicks': 2, },

	{ 'Participant': 'Rock-Climber', 'Task': 'route', 'TimeTaken': 3.6, 'TotalClicks': 1, 'TotalMisclicks': 0, },
	{ 'Participant': 'Rock-Climber', 'Task': 'waypoint', 'TimeTaken': 5.1, 'TotalClicks': 2, 'TotalMisclicks': 0, },
	{ 'Participant': 'Rock-Climber', 'Task': 'Map Layers', 'TimeTaken': 11.3, 'TotalClicks': 5, 'TotalMisclicks': 1, },
]

df = pd.DataFrame(data)
print(df)
 
df_numeric = df.drop(columns=['Participant'])
means = df_numeric.groupby('Task').mean().reset_index()
std_devs = df_numeric.groupby('Task').std().reset_index()

print('\nMeans:')
print(means)

print('\nStandard Deviations:')
print(std_devs)

# Creating boxplots for time taken for each task
plt.figure(figsize=(8, 6))
plt.title('Time Taken for Each Task')
plt.xlabel('Task')
plt.ylabel('Time Taken (seconds)')
boxplot = df.boxplot(column='TimeTaken', by='Task', grid=False)
plt.xticks(rotation=45)
plt.show()