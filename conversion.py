import pandas as pd

dataframe = pd.read_csv("stars.csv")
stars_list = dataframe.values.tolist()

data = []
for i in stars_list:
    star = {
        "name": i[1],
        "distance": i[2],
        "mass": i[6],
        "radius": i[7],
        "luminosity": i[5],
        "magnitude": i[8]
    }
    
    data.append(star)

