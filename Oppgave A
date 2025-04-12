import pandas as pd
import numpy as np

#excel fil
filnavn = 'support_uke_24.xlsx'
data = pd.read_excel(filnavn)

#  data bank
u_dag = data.iloc[:, 0].to_numpy()      
kl_slett = data.iloc[:, 1].to_numpy()    
varighet = data.iloc[:, 2].to_numpy()    
score = data.iloc[:, 3].to_numpy()       

# Printer ut 
print("Ukedag (u_dag):", u_dag[:5])
print("Klokkeslett (kl_slett):", kl_slett[:5])
print("Varighet:", varighet[:5])
print("Score:", score[:5])
