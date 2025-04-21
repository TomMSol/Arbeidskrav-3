import pandas as pd
import numpy as np

# Excel-filen
filnavn = 'support_uke_24.xlsx'
data = pd.read_excel(filnavn)

# samtalens varighet
varighet = data.iloc[:, 2].to_numpy()

# gjennomsnittlig varighet
gjennomsnitt = np.mean(varighet)

# print resultatet
print(f" Gjennomsnittlig samtaletid i uke 24 var: {gjennomsnitt:.2f} sekunder ")
