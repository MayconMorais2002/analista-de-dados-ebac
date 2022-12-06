import pandas as pl
import matplotlib.pyplot as plt

gasolina = pl.read_csv('/content/Atividade-Ebac/gasolina.csv')

plt.figure(figsize=(8, 6))
plt.plot(gasolina['dia'], gasolina['venda'])
plt.xlabel('Dias')
plt.ylabel('Preço')
plt.title('Preço da Gasolina')
plt.savefig('gasolina.png')

plt.close()
