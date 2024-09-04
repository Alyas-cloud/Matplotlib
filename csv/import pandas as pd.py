import pandas as pd
import matplotlib.pyplot as plt

# Create some example data
data = {
    'X': ['samsung', 'iphone', 'vivo', 'oppo', 'nokia'],
    'Y': [10, 20, 30, 40, 50]
}

# Convert categorical 'X' values to numerical values
df = pd.DataFrame(data)

# Plotting in 2D (Bar Graph)
plt.figure()

# Bar plot
plt.bar(df['X'], df['Y'], color='r')

# Set labels
plt.xlabel('X Label')
plt.ylabel('Y Label')

# Display the plot
plt.show()
