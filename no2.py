import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

"""
Visualisasikan untuk setiap asal geografis perkembangan waktu dari MPG dari tahun 1970 hingga 1982 menggunakan diagram garis. 
Setiap titik data akan sesuai dengan rata-rata tahunan MPG untuk Origin yang diberikan, dan setiap kurva akan terdiri dari 13 titik. 
Berikan warna yang berbeda untuk setiap kurva.
"""

df = pd.read_csv('old_cars.csv')

df = df[df['Model'].between(70, 82)]
df['Model'] = df['Model'] + 1900

group = df.groupby(['Origin', 'Model']).agg({'MPG': 'mean'}).reset_index()

sns.set_theme(style='darkgrid', palette='deep', font='sans-serif', font_scale=1.2)
sns.relplot(data=group, x='Model', y='MPG', hue='Origin', kind='line')
sns.scatterplot(data=group, x='Model', y='MPG', hue='Origin', legend=False)

plt.subplots_adjust(top=0.9)
plt.title('Perkembangan MPG dari 1970 hingga 1982', fontsize=16)
plt.xlabel('Tahun')
plt.ylabel('MPG')

plt.show()
