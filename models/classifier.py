import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Lo primer es desidir si estamos antes un problema de:

    # 1- Regresión
    # 2- Clasificacion
    # 3- Clustering
#--------------------------------------#
# ---     1- DesicionClasifier     -----
#--------------------------------------#
# Para saber que libreria utilizar es necesario saber ante que problema nos enfrenteamos
# En este caso utilizamos un algoritmo de      ----> Clasificacion Multivariable <-------
# En donde la salida es de 0,1,2
from sklearn.tree import DecisionTreeClassifier
#--------------------------------------#
# ---   2- RandomForestClassifier  -----
#--------------------------------------#
from sklearn.ensemble import RandomForestClassifier

# Ahora importo la libreria de sklearn para crear mis SETs de Training y TEST
from sklearn.model_selection import train_test_split

# Ahora EVALUO EL MODELO
# Uso accuracy_Score pero hay otras

from sklearn.metrics import accuracy_score

class Classifier():

    def setUp():
        df = pd.read_csv("iris.csv")
        # Usamos map para transformar el texto en numeros
        # Existen más formas de hacerlo
        # En Pandas para nombrar una columna concreta se escribe : nombre_dataframe.nombre_columna
        # Entonces lo que estamos haciendo es cambiar los valores por otros
        # De esta forma es mas facil clasificarlo en el dataset
        df.species = df.species.map({'setosa':0,'versicolor':1, 'virginica':2})
        #------------ COnfigurar eje Y --------------
        # El eje Y va a estar definido por la columna Species
        # Entonces asignamos la column a a la variable Y
        Y = df["species"]
        # Hacemos lo mismo con la Y
        Y = Y.values
        #-------- Configurar eje X ---------------
        # Ahora elimino las columnas de ID y Species
        # Como es un dataframa axis=1 con las columnas y axis=0 las filas
        # Utilizo el metodo drop para borrar las columnas para configurar el eje X (Horizontal)
        # Indico el nombre de las columnas que deseo eliminar
        X = df.drop(["species"],axis=1)
        # Ha veces es necesario hacer esto para que no devuelva errores posteriormente
        X = X.values
        return X, Y

    def training(X,Y):
        #--------- TRAIN and TEST Models ------------

        # Creo variables para guardar los resultados de la division de mis datos
        # Se divide en 75% training y 25% testing
        # Esta funcion la importo desde la libreria de SCIKIT_LEARN
        # El random_state igual a 0 significa que no habran valores al azar
        X_train, X_test, y_train, y_test = train_test_split(X,Y,random_state= 0)

        return X_train, X_test, y_train, y_test

    # Recibo los datos que ingresa el usuario
    def desicionClassifier(X_train, X_test, y_train, y_test):
        #--------------------------------------#
        # ---     1- DesicionClasifier     -----
        #--------------------------------------#
        # Para saber que libreria utilizar es necesario saber ante que problema nos enfrenteamos
        # En este caso utilizamos un algoritmo de      ----> Clasificacion Multivariable <-------
        # En donde la salida es de 0,1,2
        # 1- Tipo de clasificador
        # Primero creo el objeto
        clf = DecisionTreeClassifier()

        # Le inyecto los datos de entrenamiento
        #2- Entreno con los datos que indico entre parentesis
        clf.fit(X_train,y_train)

        # Aqui es donde tengo que cambiar y enlugar de inyectarle
        #los datos de X_test le inyecto los datos del usuario
        #3- Realizo la prediccion
        # Recordar que el X_test es el valor que el usuario ingresa por pantalla
        y_pred = clf.predict(X_test)

        # Imprimo esa prediccion
        return y_pred

    def randomForest():
        X_train, X_test, y_train, y_test = training()
        # Primero creo el objeto
        # 1- Tipo de clasificador
        clf = RandomForestClassifier()

        # Le inyecto los datos de entrenamiento
        # Entreno con los datos que indico entre parentesis
        clf.fit(X_train, y_train)

        # Realizo la prediccion
        y_pred = clf.predict(X_test)

        y_pred

        # Esto lo que nos dice es el nivel de acierto
        # El porcentaje de datos que han sido predecidos correctamente
        acc = accuracy_score(y_test, y_pred)
