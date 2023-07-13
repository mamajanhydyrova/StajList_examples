import pandas as pd
import numpy as np


data = r"C:/Users/Lenovo/PycharmProjects/pythonProject1/odev3/Iris.csv"
df = pd.read_csv(data)

# Son sütunu çıkararak diğer sütunları alıyoruz
columns_to_normalize = df.columns[:-1]

# Normalleştirme işlemi için asv listesini oluşturma
asv = np.array(df[columns_to_normalize])

# Normalleştirme işlemi
normalized_data = []
for column in range(asv.shape[1]):
    column_data = asv[:, column]
    normalized_column = (column_data - np.min(column_data)) / (np.max(column_data) - np.min(column_data))
    normalized_data.append(normalized_column)

# Normalleştirilmiş veri setini DataFrame olarak oluşturma
normalized_df = pd.DataFrame(np.transpose(normalized_data), columns=columns_to_normalize)

print("Normalleştirilmiş Iris veri seti:")
print(normalized_df)