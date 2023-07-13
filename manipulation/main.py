import pandas as pd

data = pd.read_csv(r"C:/Users/Lenovo/PycharmProjects/pythonProject1/odev2/Iris.csv")

data.loc[data['species'] == 'Iris-setosa', 'species'] = 'menekse'
data.loc[data['species'] == 'Iris-versicolor', 'species'] = 'manolya'
data.loc[data['species'] == 'Iris-virginica', 'species'] = 'papatya'

data.to_excel(r"C:/Users/Lenovo/PycharmProjects/pythonProject3/manipulation/Dataset.xlsx")