import pandas as pd
import numpy as np

# Excel-filen
filnavn = 'support_uke_24.xlsx'
data = pd.read_excel(filnavn)

# tilfredshetsscore (kolonne 4)
score = data.iloc[:, 3]

# Fjerner mangler
score = score.dropna()

# tell positiv og neg
totalt = len(score)
negative = ((score >= 1) & (score <= 6)).sum()
noytrale = ((score == 7) | (score == 8)).sum()  
positive = ((score == 9) | (score == 10)).sum()

# Kalkuler NPS
prosent_negative = (negative / totalt) * 100
prosent_positive = (positive / totalt) * 100
nps = prosent_positive - prosent_negative

#  resultatet
print(" Net Promoter Score (NPS) for supportavdelingen:")
print(f"- Positive kunder: {prosent_positive:.1f}%")
print(f"- Negative kunder: {prosent_negative:.1f}%")
print(f" NPS: {nps:.1f}")
