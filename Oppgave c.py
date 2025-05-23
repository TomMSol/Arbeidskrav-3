import pandas as pd
import numpy as np

# Excel-filen
filnavn = 'support_uke_24.xlsx'
data = pd.read_excel(filnavn)

# samtalens varighet
varighet = data.iloc[:, 2].to_numpy()

# Finner minste og lengste samtaletid
min_varighet = np.min(varighet)
max_varighet = np.max(varighet)

# printer ut res
print(f" Minste samtaletid i uke 24 var: {min_varighet} sekunder")
print(f" Lengste samtaletid i uke 24 var: {max_varighet} sekunder")
