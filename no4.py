import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

"""
Visualisasikan MPG, weight, horsepower, dan displacement dalam sebuah matriks diagram pencar. Kode warna titik data individu berdasarkan Origin.
"""

df = pd.read_csv('old_cars.csv')

sns.set_theme(style='darkgrid', palette='deep', font='sans-serif', font_scale=1.2)
sns.pairplot(data=df, vars=["MPG", "Weight", "Horsepower", "Displacement"], hue="Origin", diag_kind="hist")

plt.subplots_adjust(top=0.9)
plt.suptitle('Scatter Plot Matrix', fontsize=16)

plt.show()