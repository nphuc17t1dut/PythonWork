import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

carSale = pd.read_csv("Car_sales.csv")
#Hien thi du lieu
print(carSale.head(20))
#Tong Sales_in_thousands cua tung Manufacturer
print(carSale.groupby("Manufacturer")["Sales_in_thousands"].agg(np.sum))
# plot
chervroletData=carSale[carSale['Manufacturer'] == 'Chevrolet']
plt.bar(chervroletData["Model"],chervroletData["Horsepower"])
plt.title("Chevrolet Models")
plt.xlabel("Model")
plt.ylabel("Horse Power")
plt.show()