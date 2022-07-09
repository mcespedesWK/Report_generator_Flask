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

- Run pip list again  and it should show Djando dependencies already installed

- We muus declare tha ENV VARS to be able to run the enviroment in Flask

    pip install pyexcel-xls
    pip install pyexcel-xlsx
    pip install pyexcel-ods

  - And please make sure that you have pyexcel-xls and pyexcel-handsontable installed:

    pip install pyexcel-xls, pyexcel-handsontable

  ###### Windows

       set FLASK_APP = <main filename>
       set FLASK_ENV = development

  ###### Linux

       export FLASK_APP=<main filename>

- Now we extract this information so that any user can use it.
This is saved in the requirements file.

     pip freeze > requirements.txt

- If you have a project already started and you want to install the libraries from the file:

      pip install -r requirements.txt



## Links

 - [Repo](https://github.com/mcespedesWK/PythonSamples)


 ## Built With

 - Python
 - HTML
 - CSS
 - Flask

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
