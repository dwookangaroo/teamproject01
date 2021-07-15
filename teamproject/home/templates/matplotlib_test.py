import numpy as np
from pandas.io.parsers import read_csv
import matplotlib.pyplot as plt
from matplotlib import font_manager


df = read_csv('성인재범률.csv', encoding='CP949')
df2 = read_csv('소년범죄자 재범률.csv', encoding='CP949')
plt.rc('font', family='Malgun Gothic', size=7)

plot = df.plot(kind='bar', x='시점')
plot.set_title("성인의 재범률", fontsize=20)
plot.set_xlabel("연도")
plot.set_ylabel("재범률")

plot = df2.plot(kind='bar', x='시점')
plot.set_title("소년범의 재범률", fontsize=20)
plot.set_xlabel("연도")
plot.set_ylabel("재범률")



plt.show()




