# Importo la libreria para trabajar con objetos json
# Con jsonify podemos pasar de un diccionario a un objeto json
# Las APIs generalmente trabajan con objetos json
# COn request me permite hacer los POST-GET
from flask import Flask, jsonify, redirect, url_for, render_template
from flask import request
from flask import session

import flask_excel as excel

import openpyxl
from openpyxl import Workbook
from openpyxl import load_workbook
import datetime


import pandas as pd
import json
import csv
# Esto lo importo para interactuar con la base de datos y sus metodos
# Menciono el directorio, el fichero y la clase dentro del fichero
from models.user_model import User
from  models.db import Database
from models.new_user import Model_new_user
from models.validation import Validation

# Este es el modelo que cree para realizar las predicciones
from models.classifier import Classifier as cls

#-------------------------------
#       APLICACION
#-------------------------------

# Creo una instancia de Flask
# Esto es importante porque a traves de esto la aplicacion
# sabe donde buscar los archivos :html,statiics ,ect
# Necesita saber si la plaicacion va a ser ejecutada desde el archivo pricipal o desde otro archivo
app = Flask(__name__)

# his session has a default time limit of some number of minutes or hours or days after which it will expire
app.config["SESSION_PERMANENT"] = False
# It will store in the hard drive
#  it is an alternative to using a Database or something else like that.
app.config["SESSION_TYPE"] = "filesystem"

app.secret_key = 'ItShouldBeAnythingButSecret'

excel.init_excel(app) # required since version 0.0.7
                #-------------------------------
                #       CREAR RUTAS
                #-------------------------------
#---------------
#    INDEX
#----------------
# Esto es un decorador que me ayudar a genera rutas
# Lo utiliza Flask para saber a que  URL acceder
# Paso como argumento la ruta de la URL en este caso Root
# Esta ruta lleva ligada una funcionindex
@app.route('/')
# Ahora defino una funcion home que esta envuelta en el decorador app.route
# Aqui se define lo que hay que ejecutar si el ‘endpoint’ de la URL
#definida es solicitado por un usuario. Su valor de retorno determina lo que el
#usuario verá cuando cargue la página
def index():
    # Utilizo la funcion del modelo user_model para obtener lso usuarios de
    # la base de datos
    users = User.get_users()
    # Paso la variable a la vista para mostrar los usuarios
    return render_template('index.html', users = users)
#---------------.-----
#    Entitlement report
#----------------------
@app.route('/entitlement/', methods = ['GET','POST'])
def entitlement():
    if request.method == 'POST':

        f = request.files['file']
        # Leo el archivo queme llega por request
        df1 = pd.read_excel(f,'Journals')
        df2 = pd.read_excel(f,'Perpetual Access')
        df3 = pd.read_excel(f,'Databases')
        df4 = pd.read_excel(f,'DB Jumpstarts')

        # Convertimos Excel
        dfex1 = df1.to_excel("portfolio1.xlsx", index=False)
        dfex2 = df2.to_excel("portfolio2.xlsx", index=False)
        dfex3 = df3.to_excel("portfolio3.xlsx", index=False)
        dfex4 = df4.to_excel("portfolio4.xlsx", index=False)

        count = int(len(df1))
        return render_template('entitlementData.html',df1 = df1, count = count)

    #df = pd.read_csv("iris.csv")
    # axos='columns' to count with respect to row
    #count = int(len(df))
    # Paso el count de los elementos dentro del data y el dataset completo
    #return render_template('irisData.html',df = df, count = count)
    return render_template('entitlement.html')


@app.route("/export/", methods=['GET'])
def export_records():
    return excel.make_response_from_array([[1,2], [3, 4]], "xls",
                                          file_name="export_data")
#---------------
#    GET DATA
#----------------
@app.route('/iris/', methods = ['GET'])
def irisData():
    df = pd.read_csv("iris.csv")
    # axos='columns' to count with respect to row
    count = int(len(df))
    # Paso el count de los elementos dentro del data y el dataset completo
    return render_template('irisData.html',df = df, count = count)


#---------------
#    INSERT
#----------------
@app.route('/iris/insertData/', methods = ['POST'])
def insertData():

    if request.method == 'POST':
        # Obtengo la variables que me llegan por POST
        # Aún no puedo utilizar el jsonfy bien :P
        sw = request.form['sepal_width']
        sl = request.form['sepal_lenght']
        pw = request.form['petal_width']
        pl = request.form['petal_lenght']
        sp = request.form['species']
        # Obtengo la variables que me llegan por POST
        # Aún no puedo utilizar el jsonfy bien :P
        # Recojemos los datos que vienen por la peticion


        # Abro el fichero para insertar DATOS
        # Append ---> "a"
        # newline ----> Me busca la primera linea vacia para meter los datos
        with open("iris.csv", "a", newline = "")as csvfile:
            fieldnames = ["sepal_lenght","sepal_width","petal_width","petal_lenght","species"]

            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
            writer.writerow({"sepal_lenght": sl,
                            "sepal_width": sw,
                            "petal_width": pw,
                            "petal_lenght": pl,
                            "species": sp})

    df = pd.read_csv("iris.csv")
    # No lo convierto a josn para poder interactuar con el en el URL con KEY, VALUE
    # SI lo convierto no puedo recorrer el diccionario asi
    result = df.iloc[-1]
    print(result)
    return render_template('insertData.html',result = result)

#---------------
#    Update
#----------------
@app.route('/iris/<int:i>/update/', methods = ['POST'])
# Auiq lo que hago es recibir la info que me viene de la pagina principal
# Cuando el usuario hace click en el boton de update me trae aqui
# Me traigo la informacion de ID que el mi variable i
def updateData(i):
    df = pd.read_csv("iris.csv")
    id = i
    # Le paso al HTML la info del ID y del objeto del data frame con ese
    return render_template('updateData.html',id = id, df = df)

#---------------
#    Updated
#----------------

# Ahora creo otra pagina para que me de la infromacion ya actualizada
# con lo datos que recibo del formulario
@app.route('/iris/<int:id>/updated/', methods = ['POST'])
def updatedData(id):
    if request.method == 'POST':
        # Obtengo la variables que me llegan por POST
        # Aún no puedo utilizar el jsonfy bien :P
        sw = request.form['sepal_width']
        sl = request.form['sepal_length']
        pw = request.form['petal_width']
        pl = request.form['petal_length']
        sp = request.form['species']

        df = pd.read_csv("iris.csv")

        # Como ya tengo mi dato seleccionado por ID procedo a ubucar cada columna
        df.loc[df.index[id], 'sepal_length'] = sw
        df.loc[df.index[id], 'sepal_width'] = sl
        df.loc[df.index[id], 'petal_length'] = pl
        df.loc[df.index[id], 'petal_width'] = pw
        df.loc[df.index[id], 'species'] = sp

        df.to_csv('iris.csv', index=False)

        result = df.iloc[id].to_json(orient="index")

        # Si actualizo el registro envio en siguiente mensaje a la URL
        info = " El registro ha sido actualizado correctamente"
        return render_template('updatedData.html',id = id, df = df)
#---------------
#    DELETE
#----------------
@app.route('/iris/<int:i>/delete/', methods = ['POST'])
def deleteData(i):
    # Para elinimar un dato primero llamamos el archivo
    df = pd.read_csv("iris.csv")
    id = i
    result = df.iloc[i]
    return render_template('deleteData.html',result = result, id = id)


#---------------
#    DELETED
#----------------
@app.route('/iris/<int:id>/removed/',methods = ['POST'])
def deletedData(id):
    # Para elinimar un dato primero llamamos el archivo
    df = pd.read_csv("iris.csv")
    # Con drop podemos eleiminar una filename# Le pasamos el indice que se desea borra
    df.drop(df.index[id],inplace=True)
    # Lo pasamos a csv para que actualice
    df.to_csv("iris.csv")

    result = df.iloc[id]
    return render_template('deletedData.html',result = result)
#---------------
#    LOGIN
#----------------
# Necesito grabar cuando el usuario evía el formulario
@app.route('/login', methods = ['GET', 'POST'])
def login():

    if request.method == 'POST':
        # Obtengo la variables que me llegan por POST
        # Aún no puedo utilizar el jsonfy bien :P
        email = request.form['email']
        password = request.form['password']
        # Utilizo mi modelo de new user y le paso por parametro mis variables
        user = Validation.login(email, password)
        #------------------
        #    VALIDATION
        #------------------
        # Comparo las variables que me llegan del form con la info de la BD
        # Si la información existe dentro del fetchone que obtuve de la base de DATOS
        # Entonces significa que si existe ese usuario
        if email in user and password in user:
            # Obtengo el nombre de la persona para usarlo con id de session
            id_session = user[1]
            # Asigno la variable al id de session
            session['user'] = id_session
            # Si el usuario existe lo redirijo a la página dashboard
            # Invboco al metodo dashboard y le paso el ID de session actual para validarlo
            return redirect('/dashboard')
    else:
        return "<h1>Ha ocurrido un error de authenticación.</h1>"    #if the username or password does not matches

#---------------
#    LOGOUT
#----------------
@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('user', None)
   return redirect('/')

#---------------
#    REGISTER
#----------------
# Necesitamos saber de donde vienen los datos
# Utilizamos el GET POST para obtener los datos del usuario
@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        #---- EXTRAIGO LA INFO------
        # Variable para almacenar la info del formulario
        #user_details = request.get_json()
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        #-------------------
        #    OBJETO USUARIO
        #-------------------
        # Aqui creo un objeto de Usuario
        # Le paso por parámetro los datos del formulario
        user = Model_new_user(name,email,password)
        # Obtengo los atributo del objeto y los paso como parametro
        # Esto es para realizar la consulta en la BD
        #------------------------
        #    INSERTO DATOS EN BD
        #------------------------
        User.insert_user(user.name,user.email,user.password)

        return redirect('/')
    else:
        #return jsonify(object_user)
        return redirect('/')

#---------------
#    DASHBOARD
#----------------
@app.route('/dashboard', methods = ['GET'])
# Recibo como parámetro el id_session
def dashboard():
    # Si es igual al session ID grabado en el sistema...
    if session['user']:
        # ENvio un ejemplo de infromacion a la paina principal del USUARIO
        # Lo envio en forma de diccionario
        sampleData = {'sepal_length': 5.1, 'sepal_width': 3.5,
                    'petal_length': 1.4, 'petal_width': 0.2,
                    'class': "Iris Setosa"}
        # Envio los parametros para que pueda renderizarlos en la URL

        df = pd.read_csv("iris.csv")
        # No lo convierto a josn para poder interactuar con el en el URL con KEY, VALUE
        # SI lo convierto no puedo recorrer el diccionario asi
        result = df.iloc[-1]

        return render_template('home.html', sampleData = sampleData, result = result)

    return '<h1>You are not logged in.</h1>'

#---------------
#    PREDICT
#----------------
@app.route('/predictData', methods = ['POST','GET'])
# Recibo como parámetro el id_session
def predictData():
    info = " los datos de la prediccion son los siguientes:"
    # Obtengo la variables que me llegan por POST
    #---- EXTRAIGO LA INFO------
    # Variable para almacenar la info del formulario
    #user_details = request.get_json()
    sw = request.form['sepal_width']
    sl = request.form['sepal_length']
    pw = request.form['petal_width']
    pl = request.form['petal_length']
    #--------------------------·
    #-- INYECTO datos
    #--------------------------·
    # convierto los datos en una lista para inyectarlo en la funcion
    # como un X_test una vez que el modelo esta entrenado
    testData = [[sl, sw, pl, pw]]

    # Llamo a mi metodo de desicionclassifier en el modelo de classifier
    # Obtengo las valieables para entrenar mi MODELO
    # Llamo directamente porque setup, trainig  los  llamo dentro del metodo
    X, Y = pred.setUp()

    X_train, X_test, y_train, y_test = pred.training(X,Y)
    print(Y)
    #--------------------------·
    #-- CAMBIO lo datos por el INPUT que recibo del usuario
    #--------------------------·
    # Entonces voy a inyectar estos datos con todos los demas dentro del algoritmo.
    X_test = testData

    # Guardo la prediccion en una variable
    prediccion = pred.desicionClassifier(X_train, X_test, y_train, y_test)

    # Como tengo el eje Y  convertido en numeros lo debo de pasar a string
    # COn un bucle if analizo el retorno de la funcion
    if prediccion == 0:
        result = 'Setosa'
    elif prediccion == 1:
        result = 'Versicolor'
    else:
        result = 'Virginica'

    print(testData)
    # Ahora regreso lo argumento que deseo mostrar en pantalla
    return render_template('predictedData.html',testData = testData, result = result)

@app.route('/users', methods = ['GET'])
def show_users():
    users = User.get_users()
    return jsonify(users)

# Esto es para saber si el script se ejecuta directo desde aqui y no
# Esta siendo importado
if __name__ == "__main__":

    Database.create_table()
    # Aqui activo el debuger en la aplicacion para poder ver los cambios en vivo cuando los hago
    # Esto es produccion ya no es recomendable
    # Aqui le indico el puerto 8080
    app.run(debug=True)
