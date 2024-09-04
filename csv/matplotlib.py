import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
file_name = "top 120 best-selling mobile phones.csv"
df = pd.read_csv(file_name)
print(df)
x = df['Year']
y = df["Units Sold (million )"]
z = df['Rank']
fig = plt.figure()
axis = plt.axes(projection = '3d')
axis.plot(x, y, z)
axis.set_title("datasets")
axis.set_xlabel('time')
axis.set_ylabel('Units sold (million )')
axis.set_zlabel('rank')

plt.show()