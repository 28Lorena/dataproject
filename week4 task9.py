import pandas as pd

holiday = {"Destination": ["CountryA", "CountryB", "CountryC", "CountryD", "CountryE", "CountryF", "CountryG", "CountryH", "CountryI", "CountryJ", "CountryK", "CountryL", "CountryM", "CountryN", "CountryO"],
           "Feedback": [5, 2, 6, 8, 8, 8, 7, 6, 6, 2, 7, 8, 6, 8, 7],
          "Star_Rating": [4.5, 3.0, 3.8, 4.4, 4.0, 4.7, 4.1, 4.0, 4.2, 3.3 , 4.0, 4.3, 4.6, 4.5, 3.9],
           "Inc_Hotels": [5, 7, 15, 12, 10, 12, 8, 15, 15, 6, 20, 20, 9, 10, 12],
           "Most_Visited": ["City1", "City2", "City3", "City4", "City5", "City6", "City7", "City8", "City9", "City10", "City11", "City12", "City13", "City14", "City15"]}


print (holiday)

destinations = pd.DataFrame (holiday)

destinations = pd.read_csv("Hypothetical Tours.csv")

print (destinations [["Inc Hotels" , "Star Rating"]])

print (destinations["Inc Hotels"].corr (destinations [ "Star Rating"]))

#finished
    


