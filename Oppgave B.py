import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# informasjon fra excel
filnavn = 'support_uke_24.xlsx'
data = pd.read_excel(filnavn)

# Hent ut ukedag
u_dag = data.iloc[:, 0].to_numpy()

# henvendelser per ukedag
ukedager, antall = np.unique(u_dag, return_counts=True)

# søylediagram
plt.figure(figsize=(8, 5))
plt.bar(ukedager, antall)
plt.xlabel('Ukedag')
plt.ylabel('Antall henvendelser')
plt.title('Antall supporthenvendelser per ukedag 🐇')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

