# %%
# import numpy as np

# from matplotlib import pyplot as plt

# # %%
# X = np.linspace(-(np.pi), (np.pi), 256)
# C, S = np.cos(X), np.sin(X)
# plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="coseno")
# plt.plot(X, S, color="red",  linewidth=2.5, linestyle="-", label="seno")
# plt.legend(loc='upper left')
# # plt.grid()
# # plt.ylabel("Seno y Coseno")
# # plt.xlabel("angulo")
# plt.title("Grafico Posta")

# ax = plt.gca()  # gca es 'get current axis' ó 'tomar eje actual'
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# ax.xaxis.set_ticks_position('bottom')
# ax.spines['bottom'].set_position(('data',0))
# ax.yaxis.set_ticks_position('left')
# ax.spines['left'].set_position(('data',0))

# t = 2 * np.pi / 3
# plt.plot([t, t], [0, np.cos(t)], color='blue', linewidth=2.5, linestyle="--")
# plt.scatter([t, ], [np.cos(t), ], 50, color='blue')

# plt.annotate(r'$cos(\frac{2\pi}{3})=-\frac{1}{2}$',
#             xy=(t, np.cos(t)), xycoords='data',
#             xytext=(-90, -50), textcoords='offset points', fontsize=16,
#             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

# plt.plot([t, t],[0, np.sin(t)], color='red', linewidth=2.5, linestyle="--")
# plt.scatter([t, ],[np.sin(t), ], 50, color='red')

# plt.annotate(r'$sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
#             xy=(t, np.sin(t)), xycoords='data',
#             xytext=(+10, +30), textcoords='offset points', fontsize=16,
#             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

# plt.show()

# %%
import matplotlib.pyplot as plt

fig = plt.figure()
plt.subplot(2, 1, 1) # define la figura de arriba
plt.plot([0,1,2],[0,1,0]) # dibuja la curva
plt.xticks([]), plt.yticks([]) # saca las marcas

plt.subplot(2, 3, 4) # define la primera de abajo, que sería la tercera si fuera una grilla regular de 2x2
plt.plot([0,1],[0,1])
plt.xticks([]), plt.yticks([])

plt.subplot(2, 3, 5) # define la segunda de abajo, que sería la cuarta figura si fuera una grilla regular de 2x2
plt.plot([0, 1], [1, 1])
plt.xticks([]), plt.yticks([])

plt.subplot(2, 3, 6) # define la segunda de abajo, que sería la cuarta figura si fuera una grilla regular de 2x2
plt.plot([0,1],[1,0])
plt.xticks([]), plt.yticks([])

plt.show()