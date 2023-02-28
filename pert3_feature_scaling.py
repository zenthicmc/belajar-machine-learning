from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from pandas import DataFrame
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
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

fig, ax = plt.subplots()

# convert to array
kodeApt = data.KodeApt.values.astype(str)
Jum_kamar = data.Jum_kamar.values.astype(int)

# convert to list
kodeApt = kodeApt.tolist()
Jum_kamar = Jum_kamar.tolist()

print(kodeApt)
print(Jum_kamar)

labels = kodeApt
counts = Jum_kamar
bar_labels = ['red', 'blue', '_red', 'orange']
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

ax.bar(labels, counts, label=bar_labels, color=bar_colors)

ax.set_ylabel('Jumlah Kamar')
ax.set_title('Jumlah kamar berdasarkan kode apartemen')
ax.legend(title='Kamar color')

plt.show()

# # Mencari min dan max
# data_copy = data.copy()
# features = data_copy[['Jum_kamar']]
# kamar_minmax = MinMaxScaler().fit_transform(features.values)
# print(kamar_minmax)

# # Mengganti data pada kolom Jum_kamar
# data_copy[['Jum_kamar']] = kamar_minmax
# print(data_copy)

# data.to_csv('Apartemen_minmax.csv', header=True, index=False)