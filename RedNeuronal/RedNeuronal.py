import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
import random
from sklearn.model_selection import train_test_split
import csv

#Cargar los datos
dataset = pd.read_csv("/home/axel/Escritorio/Covidmetro/Dataset.csv", delimiter=",")

#dividido en variables de entrada (x) y salida (y)
X = dataset[['sexo','entresi','edad','estaemba','mesesemb',
            'esindige','ocupacio','diassint','fiebre','tos',
            'odinogia','disnea','irritabi','diarrea','dotoraci',
            'calofrios','cefalea','mialgias','artral','ataedoge',
            'rinorrea','polipnea','vomito','dolabdo','conjun',
            'cianosis','inisubis','diabetes','epoc','asma',
            'inmusupr','hiperten','vih_sida','otracon','enfcardi',
            'obesidad','insrencr','tabaquis','conocaso','contaves',
            'concerdo','conanima','vacunado','puerperio',
            'diaspuerp','antipireticos']].values
Y = dataset[['resdefin','evoluci','intubado','uci']].values

#Crear un modelo
model = Sequential()
model.add(Dense(79, input_dim=46, activation='softsign'))
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