# Python Samples
Shows different frameworks to work with Python.

## First Steps

To create a virtual environment we can do it with Anaconda. However, it is more advisable to do it manually by activating VirtuaEnv. In this way we can manually install the packages that we need and avoid conflicting with any library. It is better to install them manually so that when generating the requirements file it only contains the libraries that we have been installing throughout the project.

- Create virtual environment

  virtualenv <name>

  - [x] For Linux and Windows it´s the same comman

- Activate  virtual environment

  ###### Windows

    We position ourselves in the project folder

      .\env\Scripts\activate

    - [x] Another way is to browse the folders and activate

      cd /env/Script/activate

  ###### Linux

    source env/bin/activate  

- Now we need to do a pip list to see the libraries we have installed. Only a few should appear by default. If we do it with Anaconda many appear.

   pip list

- Install:

    Flask

   	  pip install flask

    Pandas

      pip install pandas

    Numpy

      pip install Numpy

- Vuelvo a hacer pip list y deberia de aparecer Djando installado con algunas dependencias

- Ahora necesito declarar las variables de entorno para correr mi aplicacion

  ###### Windows

       set FLASK_APP = <nombre del archivo de arranque> (en este caso: main)
       set FLASK_ENV = development

  ###### Linux

       export FLASK_APP=<nombre del archivo de arranque>

- Ahora extraemos esta información para que cualquier usuario pueda utilizarla.
Esto se guarda en el archivo de requirements.

     pip freeze > requirements.txt

- Si se tiene un proyecto ya comenzado y se quiere instalar las librerias del archivo:

      pip install -r requirements.txt  (o el nombre del archivo)



## Links

 - [Repo](https://github.com/mcespedesWK/PythonSamples)

 ## Projects

 - [Basic Python](/BasicProgrammingExercises/)

 - [Create Libraries](/CreateLibraries/)

 - [Django](/Django/)

 - [Samples](/examples/)

 - [Flask](/Flask/)

 - [Modules](/ModulesPackages/)

 - [Web Devs](/my_projectWeb/)

 - [Sockets](/Sockets/)

 - [Threats](/Threats/)

 - [Tkinter](/Tkinter/)


 ## Built With

 - Python
 - HTML
 - CSS

 ## Future Updates

 - [ ] Reliable Storage

 ## Author

 **Mauro Céspedes Araya**

 - [Profile](https://github.com/rohit19060 "Rohit jain")
 - [Email](mailto:mauro.cespedesaraya@wolterskluwer.com?subject=Hi "Hi!")
 - [Website](https://maurocespedes.notion.site/Mauro-C-spedes-Araya-dd59fd760a8b4060ae1423ad78b1e2f3)

 ## 🤝 Support

 Contributions, issues, and feature requests are welcome!

 Give a ⭐️ if you like this project!



----------------------------------------------------
