# Crea un DataFrame con:

# Edad (entre 15 y 70 años).

# Género (Hombre/Mujer, con distinta probabilidad).

# Tipo de alopecia (Androgenética, Areata, Fibrosante).

# Región (opcional: Madrid, Barcelona, etc.).

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


np.random.seed(120)
edad = np.random.randint(15,75,100)
genero = np.random.choice(["Hombre","Mujer"],size=100,p=[0.8,0.2])
tipo_de_alopecia = np.random.choice(["Androgenetica","Areata","Fibrosante"],size=100,p=[0.6,0.2,0.2])

data = {'Edad' : edad,
    'Genero' : genero,
    'Tipo_de_alopecia' : tipo_de_alopecia,
    }



df = pd.DataFrame(data)
df.value_counts();


grafica = sns.barplot(x='Tipo_de_alopecia', y='Edad', data=df, hue='Genero')
plt.title('Distribución de tipos de alopecia por edad y género', pad=20)  # Añade título con espacio (pad)
plt.xlabel('Tipos de alopecia')  # Eje X: qué se está comparando
plt.ylabel('Edad promedio')      # Eje Y: qué representa la altura de las barras
plt.show()


# import pandas as pd

# df = pd.DataFrame(
#     {
#         "Nombre": [
#             "xxx", "yyyy", "", "Luis", "Eduuss", "Juan2", "Juan",
#             "Jacobo", "Jorge.", "Santi", "sernior", "Prito", "Nico",
#             "Pablo", "Pedro.", "Alvaro"
#         ],
#         "Age": [
#             26, 25, 26, 25, 24, 25, 25, 25, 25, 26, 24, 24, 25, 26, 26,25
#         ],
#         "Sex": [
#             "male", "male", "male", "male", "male", "male", "male", "male",
#             "male", "male", "male", "male", "male", "male", "male", "male"
#         ]
#     }
# )

# # print(df)
# print (df.describe())
