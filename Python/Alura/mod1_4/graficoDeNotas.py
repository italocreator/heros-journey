# grafico de notas
import tkinter
import matplotlib.pyplot
from random import randrange
import matplotlib.pyplot as plt

notas_matematica = []

for notas in range(8):
    notas_matematica.append(randrange(0, 11))

x = list(range(1, 9))
y = notas_matematica
plt.plot(x, y, marker='o')
plt.title('Notas de matemática')
plt.xlabel('Provas')
plt.ylabel('Notas')
plt.show()
