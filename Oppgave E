import pandas as pd
import matplotlib.pyplot as plt

# Excel-filen
filnavn = 'support_uke_24.xlsx'
data = pd.read_excel(filnavn)

# klokkeslett
kl_slett = pd.to_datetime(data.iloc[:, 1])
timer = kl_slett.dt.hour

# tidsrom
tid_08_10 = ((timer >= 8) & (timer < 10)).sum()
tid_10_12 = ((timer >= 10) & (timer < 12)).sum()
tid_12_14 = ((timer >= 12) & (timer < 14)).sum()
tid_14_16 = ((timer >= 14) & (timer < 16)).sum()

# sektordiagram
labels = ['08–10', '10–12', '12–14', '14–16']
verdier = [tid_08_10, tid_10_12, tid_12_14, tid_14_16]

plt.figure(figsize=(7, 7))
plt.pie(verdier, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Henvendelser per tid')
plt.axis('equal') 
plt.show()
