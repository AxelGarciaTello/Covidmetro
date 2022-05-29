from random import shuffle
from keras.models import Sequential
from keras.layers import Dense
import numpy
import csv
import pandas as pd
from sklearn.model_selection import train_test_split
import random

#Fijar las semillas aleatorias para la reproductibilidad
numpy.random.seed(7)

#carga los datos
dataset = pd.read_csv("/home/axel/Escritorio/RedNeuronal/Covidmetro/LimpiezaDato/salida3.csv",delimiter=",")

#dividido en variables de entrada (x) y salida (y)
X = dataset[['sexo','entresi','edad','estaemba','mesesemb','esindige',
                        'ocupacio','diassint','fiebre','tos','odinogia','disnea',
                        'irritabi','diarrea','dotoraci','calofrios','cefalea',
                        'mialgias','artral','ataedoge','rinorrea','polipnea','vomito',
                        'dolabdo','conjun','cianosis','inisubis','diabetes','epoc',
                        'asma','inmusupr','hiperten','vih_sida','otracon','enfcardi',
                        'obesidad','insrencr','tabaquis','conocaso',
                        'contaves','concerdo','conanima','vacunado','puerperio',
                        'diaspuerp','antipireticos']].values
Y = dataset[['resdefin','evoluci',
                    'intubado','uci']].values

#Crear el modelo
model = Sequential()
model.add(Dense(95,input_dim=46, activation='relu'))
model.add(Dense(4,activation='sigmoid'))

#Compila el modelo
model.compile(loss='mean_squared_error',optimizer='adam',metrics=['binary_accuracy'])

#Elaboración de los conjuntos de entrenamiento y prueba
semilla = random.randint(0,100)
entrada, entradaP, salida, salidaP = train_test_split(X, Y, test_size=0.15, random_state=semilla, shuffle=True)

#Ajusta el modelo
model.fit(entrada,salida,epochs=25)

score = model.evaluate(entradaP,salidaP)
print("\n%s: %.2f%%" % (model.metrics_names[1],score[1]*100))
print("\n%s: %.2f%%" % (model.metrics_names[2],score[2]*100))

'''predictions = model.predict(entradaP)
with open('predicciones.csv','w') as miArchivo:
    writer = csv.writer(miArchivo)
    writer.writerows(predictions)'''
