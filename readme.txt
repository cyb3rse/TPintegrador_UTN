Este proyecto es una aplicación desarrollada en Python utilizando el framework Flask.
Su objetivo es permitir que el usuario pueda buscar información de diferentes países a partir de un archivo CSV que contiene datos como el nombre,
la población, la superficie y el continente al que pertenecen. 
La aplicación muestra los resultados de forma ordenada en una página web simple y clara.
Para poder usar el proyecto, primero es necesario tener instalado Python 3.10 o superior, ya que el código está hecho en esa versión o una más reciente. 
También se recomienda tener Git, aunque no es obligatorio, 
solo en caso de que se quiera clonar el repositorio directamente desde GitHub.

El siguiente paso es crear un entorno virtual, lo cual es importante para mantener las dependencias del proyecto separadas del sistema. Esto se hace con el siguiente comando:

python -m venv venv

Después de crear el entorno, hay que activarlo. En Windows, si estás usando PowerShell, el comando es:

.\venv\Scripts\Activate.ps1


Si usás la consola clásica de Windows (CMD), el comando es:

venv\Scripts\activate.bat


Y si estás en Linux o macOS, se activa con:

source venv/bin/activate


Cuando el entorno virtual esté activo, vas a notar que aparece la palabra (venv) al inicio de la línea en la terminal. Esto significa que todo lo que ejecutes o instales se va a guardar dentro de ese entorno.

Luego hay que instalar las dependencias necesarias. En este caso solo se utiliza Flask, así que alcanza con escribir:

pip install flask


Con eso ya está todo listo para ejecutar la aplicación. Para hacerlo, primero hay que entrar en la carpeta donde está el archivo principal del programa, llamada datos, usando el comando:

cd datos


Una vez dentro, se ejecuta el archivo app.py con el siguiente comando:

python app.py
