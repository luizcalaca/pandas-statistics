import matplotlib.pyplot as plt
import pandas as pd

iris = pd.read_csv('iris.csv')
plt.scatter(iris['sepal.length'], iris['sepal.width'], sizes=50 * iris['petal.length'])




