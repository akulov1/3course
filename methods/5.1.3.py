import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

x_table = np.array([2, 3, 5, 7])
y_table = np.array([4, -2, 6, -3])

spline_table = CubicSpline(x_table, y_table)

x_plot_table = np.linspace(2, 7, 100)
f_spline_table = spline_table(x_plot_table)#peзультат интерполирования для построения графика

spline_at_nodes = spline_table(x_table)#вычислениe значений сплайна в узловых точках

print(spline_at_nodes)#сравнение значений
plt.figure(figsize=(10, 6))
plt.plot(x_plot_table, f_spline_table, 'b--', label='Кубический сплайн')
plt.scatter(x_table, y_table, color='red', marker='o', label='Узловые точки')
plt.title('Кубический сплайн для заданной таблицы')
plt.legend()
plt.grid(True)
plt.show()


