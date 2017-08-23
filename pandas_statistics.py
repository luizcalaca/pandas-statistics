import matplotlib.pyplot as plt
import pandas as pd

iris = pd.read_csv('iris.csv')
plt.scatter(iris['sepal.length'], iris['sepal.width'], sizes=50 * iris['petal.length'],
           c=iris['petal.width'], cmap='viridis', alpha=0.4)

plt.show()

print(iris['sepal.length'].mean()) #Média
print(iris['sepal.length'].median()) #Mediana
print(iris['sepal.length'].quantile(q=0.25)) #Quantil
print(iris['sepal.length'].mode()) #Moda
print(iris['sepal.length'].max() - iris['sepal.length'].min()) #Amplitude
print(iris['sepal.length'].var()) #Variância
print(iris['sepal.length'].std()) #Desvio padrão
print(iris['sepal.length'].mad()) #Desvio absoluto
print(iris.corr()) #Correlação
print(iris.cov()) #Covariância




