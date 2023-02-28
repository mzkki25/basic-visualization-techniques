import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

"""
Visualisasikan dengan diagram batang berkelompok (lihat di atas) distribusi MPG dari semua model berdasarkan Origin. 
Dengan kata lain, Anda akan membuat diagram di mana setiap nilai MPG dikaitkan dengan 3 batang (satu untuk setiap origin: AS, Eropa, Jepang) 
dan menunjukkan bagaimana distribusi MPG dibandingkan di seluruh wilayah. Untuk itu, Anda akan mendiskretisasi rentang nilai MPG yang mungkin 
dalam kenaikan 2 MPG.
"""

df = pd.read_csv('old_cars.csv')

df['MPG'] = ((df['MPG'] // 2) * 2).astype(int)

sns.set_theme(style='darkgrid', palette='deep', font='sans-serif', font_scale=1.2)
sns.countplot(data=df, x='MPG', hue='Origin')

plt.title('Distribusi MPG')
plt.xlabel('MPG (discrete)')
plt.ylabel('Jumlah')

plt.show()
