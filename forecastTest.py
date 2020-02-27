import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

calcY = lambda x : regression.slope * x + regression.intercept # function to return the Y value for a given X value (y = mx + c)

dataFrame = pd.read_excel('testData.xlsx', names = ['x', 'y'], header = None) # Creates a dataframe from an excel spreadsheet

print(dataFrame)

plt.scatter(dataFrame['x'], dataFrame['y']) # Prints a scatter graph of the points from the spreadsheet

regression = stats.linregress(dataFrame['x'], dataFrame['y']) # returns many objects and assigns them to regression

myModel = list(map(calcY, dataFrame['x'])) # Makes a list of Y Values for the line

plt.plot(dataFrame['x'], myModel) # Plots X against Y

print(f'next water day: {0 - regression.intercept/regression.slope}')

plt.show()
