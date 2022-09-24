import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
import random
from sklearn.model_selection import train_test_split
import csv

#Cargar los datos
dataset = pd.read_csv("/home/axel/Escritorio/Covidmetro/Dataset.csv", delimiter=",")

#dividido en variables de entrada (x) y salida (y)
X = dataset[['diassint','tos','mialgias','edad',
             'odinogia','disnea','fiebre',
             'antipireticos','esindige',
             'hiperten','inisubis','dolabdo','ocupacio',
             'diarrea','mesesemb','estaemba',
             'vomito']].values
Y = dataset[['resdefin','evoluci','intubado','uci']].values

#Crear un modelo
model = Sequential()
model.add(Dense(79, input_dim=17, activation='softsign'))
model.add(Dense(27, activation='sigmoid'))
model.add(Dense(30, activation='softsign'))
model.add(Dense(4, activation='sigmoid'))

#Compilar el modelo
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['binary_accuracy'])

#Elaboración de los conjuntos de entramiento y prueba
semilla = random.randint(0,100)
entrada, entradaP, salida, salidaP = train_test_split(X, Y, test_size=0.2, random_state=semilla, shuffle=True)

#Ajustar el modelo
model.fit(entrada, salida, epochs=15)

#Evaluar el modelo
score = model.evaluate(entradaP, salidaP)

print("\n%s: %.2f%%" % (model.metrics_names[1],score[1]*100))
print("\n%s: %.2f%%" % (model.metrics_names[0],score[0]*100))