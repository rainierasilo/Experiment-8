import pandas as pd

df = pd.read_csv('cars.csv')
cars = df

#sub problem a
print(df.iloc[:5,[1,3,5,7,9,11]])

#sub problem b
print(df.loc[df.Model == 'Mazda RX4'])

#sub problem c
print(df.loc[df['Model'] == 'Camaro Z28', ['Model','cyl']])

#sub problem d
print(df.loc[df['Model'] == 'Camaro Z28', ['Model','cyl', 'gear']])
print(df.loc[df['Model'] == 'Ford Pantera L', ['Model','cyl', 'gear']])
print(df.loc[df['Model'] == 'Honda Civic', ['Model','cyl', 'gear']])

