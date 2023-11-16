# intranetTrabajadores


Sistema Intranet Trabajadores 
--NO TOCAR SETTINGS--

para activar el entorno virtual en Terminal PowerShell.

*Realizar estos pasos para crear el Entorno virtual*
-pip install virtualenv
-python -m venv venv
*Realizar estos pasos para crear el Entorno virtual*

1. estar en la carpeta madre del proyecto
2. entrar a la carpeta "VENV"
3. una vez dentro procedemos a escribir en la terminal el siguiente comando = Scripts\Activate.ps1
4. Agregar el .gitignore y agregar el comando venv/
5. Instalar las librerias que estan a continuacion.
   

Librerias para instalar en la carpeta de manage.py *DEBES TENER EL ENTORNO VIRTUAL ENCENDIDO*.
1. DJANGO
2. DJANGORESTFRAMEWORK
3. COREAPI
4. DJANGO-CORS-HEADERS


LIBRERIAS PARA INSTALAR EN LA CARPETA DEL FRONT CLIENT *DEBES TENER EL ENTORNO VIRTUAL ENCENDIDO* 
1. react-router-dom
2. react-hot-toast
3. axios
4. react-hook-form


Para prender el servidor de django
1. entramos a la carpeta madre del proyecto
2. python manage.py runserver

Para prender el servidor del cliente FRONT 
1. entramos a la carpeta "clienteFront"
2. una vez dentro, en la terminal pondremos el siguiente codigo = npm run dev

Funciona en base a REACT - DJANGO REST FRAMEWORK 

En caso de problemas, revisar urls, codeheaders, settings o las vistas.
