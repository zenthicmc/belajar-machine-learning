from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from pandas import DataFrame
import pandas as pd
import numpy as np

# Membaca file dataset
data = pd.read_csv('Apartemen_numerik.csv')

# Menampilkan data statistik deskriptif
print(data.describe())

# Mengganti pada lokasi tertentu
data.loc[2, 'Jum_kamar'] = 100
print(data)
print(data.shape)
print(data.Jum_kamar)

# Mencari min dan max
data_copy = data.copy()
features = data_copy[['Jum_kamar']]
kamar_minmax = MinMaxScaler().fit_transform(features.values)
print(kamar_minmax)

# Mengganti data pada kolom Jum_kamar
data_copy[['Jum_kamar']] = kamar_minmax
print(data_copy)