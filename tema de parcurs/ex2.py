import pandas as pd
import matplotlib.pyplot as plt

X = 16
Y = 6
fisier_csv = "data.csv"

# 1. Incarcarea si Curatarea Datelor

df = pd.read_csv(fisier_csv)

col_durata = 'Durata'
col_puls = 'Puls'
col_maxpuls = 'MaxPuls'
col_calorii = 'Calorii'

# Curatarea datelor: transforma valorile non-numerice in NaN
df[col_durata] = pd.to_numeric(df[col_durata], errors='coerce')
df[col_puls] = pd.to_numeric(df[col_puls], errors='coerce')
df[col_maxpuls] = pd.to_numeric(df[col_maxpuls], errors='coerce')
df[col_calorii] = pd.to_numeric(df[col_calorii], errors='coerce')

# Stergerea randurilor cu NaN in coloanele cheie
df_clean = df.dropna(subset=[col_durata, col_puls, col_maxpuls, col_calorii]).reset_index(drop=True)

# 2. Plotarea tuturor valorilor


plt.figure(figsize=(12, 6))
plt.plot(df_clean.index, df_clean[col_durata], label=f'{col_durata} (Toate Valorile)', marker='.', color='red')
plt.plot(df_clean.index, df_clean[col_puls], label=f'{col_puls} (Toate Valorile)', marker='.', color='blue')
plt.plot(df_clean.index, df_clean[col_maxpuls], label=f'{col_maxpuls} (Toate Valorile)', marker='v', color='green')
plt.plot(df_clean.index, df_clean[col_calorii], label=f'{col_calorii} (Toate Valorile)', marker='^', color='orange')
plt.title(f'1. Toate Valorile: {col_durata}, {col_puls}, {col_maxpuls} si {col_calorii}')
plt.xlabel('Index')
plt.ylabel('Valoare')
plt.legend()
plt.grid(True)
plt.show() # Afiseaza primul grafic

# 3. Plotarea primelor X=16 valori

df_x = df_clean.head(X)
plt.figure(figsize=(8, 5))
plt.plot(df_x.index, df_x[col_durata], label=f'{col_durata} (Primele {X})', marker='^', color='blue')
plt.plot(df_x.index, df_x[col_puls], label=f'{col_puls} (Primele {X})', marker='v', color='red')
plt.title(f'2. Primele {X} Valori: {col_durata} si {col_puls}')
plt.xlabel('Index')
plt.ylabel('Valoare')
plt.legend()
plt.grid(True)
plt.show() 

# 4. Plotarea ultimelor Y=6 valori

df_y = df_clean.tail(Y)
plt.figure(figsize=(8, 5))
plt.plot(df_y.index, df_y[col_durata], label=f'{col_durata} (Ultimele {Y})', marker='s')
plt.plot(df_y.index, df_y[col_puls], label=f'{col_puls} (Ultimele {Y})', marker='s')
plt.title(f'3. Ultimele {Y} Valori: {col_durata} si {col_puls}')
plt.xlabel('Index')
plt.ylabel('Valoare')
plt.legend()
plt.grid(True)
plt.show() # Afiseaza al treilea grafic
