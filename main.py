import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

penguins = sns.load_dataset('penguins')

print(penguins.head())
# 1. Аналіз розподілу ваги та висоти птахів:
sns.set_theme(style="whitegrid")
plt.figure(figsize=(8, 6))
sns.scatterplot(data=penguins, x='flipper_length_mm', y='body_mass_g', hue='species', style='species')
plt.title('Розподіл ваги та довжини ласт пінгвінів')
plt.xlabel('Довжина ласт (мм)')
plt.ylabel('Маса тіла (г)')
plt.legend(title='Вид пінгвіна')
plt.show()

# 2. Вивчення впливу виду птаха на розміри крил:
plt.figure(figsize=(8, 6))
sns.boxplot(data=penguins, hue='species',  legend = False, x='species', y='flipper_length_mm', palette='Set2')
plt.title('Розмір крил у залежності від виду пінгвіна')
plt.xlabel('Вид пінгвіна')
plt.ylabel('Довжина ласт (мм)')
plt.show()

# 3. Кореляція між різними ознаками:
corr_matrix = penguins.corr(numeric_only=True)
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Кореляція між числовими ознаками')
plt.show()





