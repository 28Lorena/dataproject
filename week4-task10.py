import pandas as pd

import matplotlib.pyplot as plt

holiday = {"Destination": ["CountryA", "CountryB", "CountryC", "CountryD", "CountryE", "CountryF", "CountryG", "CountryH", "CountryI", "CountryJ", "CountryK", "CountryL", "CountryM", "CountryN", "CountryO"],
           "Star Rating": [4.5, 3.0, 3.8, 4.4, 4.0, 4.7, 4.1, 4.0, 4.2, 3.3 , 4.0, 4.3, 4.6, 4.5, 3.9]}
           
           
df = pd.DataFrame (holiday, columns= ["Destination", "Star Rating"])

print (df [["Destination", "Star Rating"]])

df.plot (x="Destination", y="Star Rating", kind = "line")

plt.show()















