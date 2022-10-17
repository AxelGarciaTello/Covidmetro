import pandas as pd
import random
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

#Cargar los datos
dataset = pd.read_csv("/home/axel/Escritorio/CovidmetroModelos/Dataset.csv",delimiter=",")

#dividido en variables de entrada (x) y salida (y)
X = dataset[['diassint','mialgias','artral','edad',
             'disnea','fiebre','ataedoge',
             'rinorrea','antipireticos','calofrios','dotoraci','esindige',
             'hiperten','dolabdo','diabetes','ocupacio']].values
Y = dataset[['resdefin','evoluci','intubado','uci']].values

#Elaboración de los conjuntos de entramiento y prueba
semilla = random.randint(0,100)
entrada, entradaP, salida, salidaP = train_test_split(X, Y, test_size=0.15, random_state=semilla, shuffle=True)

#Creación del árbol de decisión
arbol = DecisionTreeClassifier(criterion="entropy", splitter="best", max_depth=6, min_samples_split=2, min_samples_leaf=5, min_weight_fraction_leaf=0.0, max_features=42, max_leaf_nodes=180, min_impurity_decrease=0.0, class_weight=None, ccp_alpha=0.0)

#Entrenamiento
arbol.fit(entrada,salida)

#Predicción
resultados = arbol.predict(entradaP)

#Aplanado de los datos
resultados_aplanados = [item for sublist in resultados for item in sublist]
verdaderos_aplanados = [item for sublist in salidaP for item in sublist]

#Evaluar al árbol
print("Precisión del Árbol de decisión",(metrics.accuracy_score(verdaderos_aplanados,resultados_aplanados))*100)
