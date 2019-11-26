import pandas as pd

df = pd.read_csv('cars.csv')
cars = df

#first five rows of resulting cars
print(cars.head())

#last five rows of resulting cars
print(cars.tail())

