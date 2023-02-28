import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

"""
visualisasikan hubungan antara horsepower dan MPG dalam diagram pencar. Sumbu horizontal harus sesuai dengan horsepower, 
sumbu vertikal dengan MPG, dan setiap titik data dengan mobil tertentu. Terapkan pada diagram pencar pengkodean warna yang menunjukkan tahun.
"""

df = pd.read_csv('old_cars.csv')
df["Model"] = df["Model"] + 1900

# membuat scatter plot
sns.set_theme(style='darkgrid', palette='deep', font='sans-serif', font_scale=1.2)
sns.scatterplot(data=df ,x="Horsepower", y="MPG", hue="Model")

plt.subplots_adjust(top=0.9)
plt.xlabel("Horsepower")
plt.ylabel("MPG")
plt.title('Scatter Plot Horsepower dan MPG', fontsize=16)

plt.show()