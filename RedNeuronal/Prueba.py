from keras.models import Sequential
from keras.layers import Dense
import numpy
import csv

#Fijar las semillas aleatorias para la reproductibilidad
numpy.random.seed(7)

#carga los datos
#Nota: Quitar las cabeceras a los datos
dataset = numpy.loadtxt("/home/axel/Escritorio/RedNeuronal/Covidmetro/LimpiezaDato/entrenamiento.csv",delimiter=",")

#dividido en variables de entrada (x) y salida (y)
entrada = dataset[:,0:46]
salida = dataset[:,46:50]

#Crear el modelo
model = Sequential()
model.add(Dense(95,input_dim=46, activation='relu'))
model.add(Dense(4,activation='sigmoid'))

#Compila el modelo
model.compile(loss='mean_squared_error',optimizer='adam',metrics=['binary_accuracy'])

#Ajusta el modelo
model.fit(entrada,salida,epochs=25)

#carga los datos
dataset = numpy.loadtxt("/home/axel/Escritorio/RedNeuronal/Covidmetro/LimpiezaDato/prueba.csv",delimiter=",")

#dividido en variables de entrada (x) y salida (y)
entradaP = dataset[:,0:46]
salidaP = dataset[:,46:50]

score = model.evaluate(entradaP,salidaP)
print("\n%s: %.2f%%" % (model.metrics_names[1],score[1]*100))

predictions = model.predict(entradaP)
with open('predicciones.csv','w') as miArchivo:
    writer = csv.writer(miArchivo)
    writer.writerows(predictions)
