import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.externals.six import StringIO
import pydotplus
import matplotlib.image as mpimg
from sklearn import tree
import matplotlib.pyplot as plt
import csv

#Carga datos
dataset = pd.read_csv("/home/axel/Escritorio/RedNeuronal/Covidmetro/LimpiezaDato/entrenamiento.csv",delimiter=",")

#Separar los datos
x_trainset = dataset[['sexo','entresi','edad','estaemba','mesesemb','esindige',
                        'ocupacio','diassint','fiebre','tos','odinogia','disnea',
                        'irritabi','diarrea','dotoraci','calofrios','cefalea',
                        'mialgias','artral','ataedoge','rinorrea','polipnea','vomito',
                        'dolabdo','conjun','cianosis','inisubis','diabetes','epoc',
                        'asma','inmusupr','hiperten','vih_sida','otracon','enfcardi',
                        'obesidad','insrencr','tabaquis','conocaso',
                        'contaves','concerdo','conanima','vacunado','puerperio',
                        'diaspuerp','antipireticos']].values
y_trainset = dataset[['resdefin','evoluci',
                    'intubado','uci']].values

#carga los datos
dataset = pd.read_csv("/home/axel/Escritorio/RedNeuronal/Covidmetro/LimpiezaDato/prueba.csv",delimiter=",")

#dividido en variables de entrada (x) y salida (y)
x_testset = dataset[['sexo','entresi','edad','estaemba','mesesemb','esindige',
                        'ocupacio','diassint','fiebre','tos','odinogia','disnea',
                        'irritabi','diarrea','dotoraci','calofrios','cefalea',
                        'mialgias','artral','ataedoge','rinorrea','polipnea','vomito',
                        'dolabdo','conjun','cianosis','inisubis','diabetes','epoc',
                        'asma','inmusupr','hiperten','vih_sida','otracon','enfcardi',
                        'obesidad','insrencr','tabaquis','conocaso',
                        'contaves','concerdo','conanima','vacunado','puerperio',
                        'diaspuerp','antipireticos']].values
y_testset = dataset[['resdefin','evoluci',
                    'intubado','uci']].values

#Creación del árbol de decisión
drugTree = DecisionTreeClassifier(criterion="entropy",max_depth=8,min_samples_split=7,min_samples_leaf=2,random_state=20)

#Entrenamiento
drugTree.fit(x_trainset, y_trainset)

#Predicción
predTree = drugTree.predict(x_testset)

#Evaluar el árbol
print("Precisión del Árbol de decisión: ",metrics.accuracy_score(y_testset,predTree))

#Exportación de una imagen del árbol
"""dot_data = StringIO()
filename = "covid.png"
featureNames = dataset.columns[0:46]
targetNames = dataset.columns[46:50]
out=tree.export_graphviz(drugTree,feature_names=featureNames, out_file=dot_data, class_names= np.unique(y_trainset), filled=True,  special_characters=True,rotate=False)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png(filename)
img = mpimg.imread(filename)
plt.figure(figsize=(100, 200))
plt.imshow(img,interpolation='nearest')"""

#Exportar resultados
with open('predicciones.csv','w') as miArchivo:
    writer = csv.writer(miArchivo)
    writer.writerows(predTree)