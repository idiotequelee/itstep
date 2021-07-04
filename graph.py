
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

#  Данные, которые хотим отобразить:
x1 = [1,2,3,4,5]    #  координаты 'x'
y1 = [2,2,5,5,4]    #  координаты 'y'

ax.scatter(x1, y1)    #  метод, отображающий данные в виде точек
                      #  на плоскости

ax.set(title='Случайные точки')    #  метод, размещающий заголовок
                                       #  над "Axes"
    
plt.show()