# -*- coding: utf-8 -*-
"""datostratamiento

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14uXgnGHcUED2MhJ436yIg5NtREC4ArHE
"""

import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv("https://www.datos.gov.co/api/views/gt2j-8ykr/rows.csv?accessType=DOWNLOAD")

df.head(60)

df.tail(15)

df.groupby(by=['fecha reporte web','Sexo']).count()



df[(df['Edad'] > 19) & (df['Edad'] < 40)]

df_filtrar = df.fillna(0)

df_filtrar.head()

df["Fecha"]=pd.to_datetime(df['fecha reporte web'],dayfirst=True)

plt.figure()                                
x_values1 = df.Sexo.unique()
y_values1 = df.Sexo.value_counts().tolist()
ax = plt.subplot(1, 3, 1)                  
plt.bar(x_values1, y_values1)               
plt.title('Contagios')             
ax.set_xticks(x_values1)                    
ax.set_xticklabels(x_values1, rotation=60)  
ax.set_xlabel('nombres de departamento')            
ax.set_ylabel('numero de contagios')