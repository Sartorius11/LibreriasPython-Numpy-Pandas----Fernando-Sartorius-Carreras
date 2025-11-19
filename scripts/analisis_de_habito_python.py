import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(1)

edad= np.random.randint(18,70,100)
genero= np.random.choice(["Hombres","Mujeres"],size=100,p=[0.6,0.4])
tipo_juego= np.random.choice(["LOL","CSGO","VALORANT"],size=100,p=[0.5,0.3,0.2])
horas_semanales= np.random.randint(1,10,100)

df = pd.DataFrame({
    "Edad" : edad,
    "Genero" : genero,
    "Tipo_Juego" : tipo_juego,
    "Horas semanales": horas_semanales})


plt.figure(figsize=(15, 5))  

plt.subplot(1, 2, 1) 
sns.countplot(data=df, x='Tipo_Juego', hue="Genero", palette="viridis")
plt.title("Frecuencia por tipo de juego")
plt.xticks(rotation=45) 


plt.subplot(1, 2, 2) 
sns.histplot(data=df, x='Edad', hue="Genero", kde=True, palette="magma")
plt.title("Distribución de edades")


plt.tight_layout()
plt.show()

