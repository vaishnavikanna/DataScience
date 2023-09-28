import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.pyplot import pie, axis, show, figure

df = pd.read_csv('data1.csv')

fig = plt.figure(figsize=(10, 12))

y = df.groupby(df['religion']).size()
percent = 100.*y/y.sum()

x = df['religion']

colours = ['blue', 'green', 'red', 'pink', 'purple', 'yellow', 'orange', 'black', 'lightblue', 'gray', 'maroon', 'brown']

patches, texts = plt.pie(df.groupby('religion').size(), colors=colours, startangle=90, radius=1.2)
labelnames = df['religion'].astype('category').cat.categories.tolist()



labels = [f'{l}, {s:0.1f}%' for l, s in zip(labelnames, percent)]


plt.legend(patches, labels, loc='upper left',bbox_to_anchor=(-0.1, 1.), fontsize=8)


# df.groupby('religion').size().plot(kind='pie', autopct='%1.1f%%')


plt.title("Religions in Germany")
axis('equal')
plt.savefig('piechart.pdf')
show()


