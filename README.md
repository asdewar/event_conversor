# Conversor de archivos generados por cámaras de eventos

_En este proyecto se ha desarrollado un conversor de archivos generados por cámaras de eventos. Esta aplicación soporta los ficheros de formato bag, mat, txt, bin y AEDAT y está programada en Python3._

## Introducción al programa
Este programa se centra en la conversión de archivos que almacenan _eventos_. Estos _eventos_ son producidos por las [cámaras de eventos](https://en.wikipedia.org/wiki/Event_camera) y se almacenan con diferentes formatos. El programa desarrollado puede leer los eventos almacenados en un archivo y escribirlos en otro archivo con diferente formato. Este programa solo transforma los eventos almacenados, el resto de la información que pueda contener el archivo (la calibración de la cámara por ejemplo) se perderá en la conversión.

## Pre-requisitos
Se debe tener instalado [Python 3](https://www.python.org/downloads/). Se ha programado el código con la versión 3.9.2, por lo que se recomienda utilizar esta versión por posibles errores.

También se debe tener instalado una versión de [ROS](https://www.ros.org/) para poder acceder a las cabeceras compatibles con los archivos bag. Se recomienda instalar la versión [Noetic](http://wiki.ros.org/noetic) ya que es la usada en el desarrollo. En este [link](http://wiki.ros.org/noetic/Installation) se ofrece un tutorial para su instalación.

## Dependencias
En esta aplicación se han utilizado las siguientes librerías de Python:
- [aedat](https://pypi.org/project/aedat/)
- [genpy](https://pypi.org/project/genpy/)
- [NumPy](https://www.numpy.org)
- [PySimpleGUI](https://pysimplegui.readthedocs.io/en/latest/)
- [rosbag](http://wiki.ros.org/rosbag/Cookbook)
- [rospy](http://wiki.ros.org/rospy)
- [rospkg](http://wiki.ros.org/rospkg)
- [gnupg](https://gnupg.org/)
- [pycryptodomex](https://pypi.org/project/pycryptodomex/)
- [PyYAML](https://pypi.org/project/PyYAML/)
- [scipy](https://www.scipy.org/)

## Instalación
Se deben instalar todas las dependencias antes de ejecutar el programa. Para instalar estos paquetes, se debe ejecutar el siguiente comando:

```
pip3 install aedat genpy numpy pysimplegui rosbag rospy rospkg gnupg pycryptodomex PyYAML scipy
```

## Ejecución y parámetros
Para iniciar la aplicación, se debe ejecutar el archivo **main.py** del repositorio. Se debe ejecutar con python y tiene dos tipos de argumentos:

- Posicionales, deben seguir un orden específico, hay dos:
    - **input_file**: Debe ir en primer lugar, path del fichero de entrada.
    - **output_file**: Debe ir en segundo lugar, path del fichero de salida.
- No posicionales, no deben seguir un orden, hay seis:
    - **--input_type**: Debe acompañarlo una cadena de texto indicando el tipo de entrada.
    - **--output_type**: Debe acompañarlo una cadena de texto indicando el tipo de salida.
    - **--config_path**: Debe acompañarlo una cadena de texto que indique el path al fichero de configuración.
    - **--use_config**: El uso de este flag indica al programa la utilización del archivo de configuración.
    - **--use_graphic_UI**: El uso de este flag indica la utilización de la interfaz gráfica.
    - **--use_terminal_UI**: El uso de este flag indica la utilización de la interfaz basada en la terminal.

Si no se usa ni la flag **--use_graphic_UI** ni la flag **--use_terminal_UI**, no se mostrará nada de información al usuario. Además, en este modo se deben usar los argumentos **input_file**, **--output_type** y **--use_config**.

Si se usa la opción **--use_terminal_UI**, se deberá introducir los parámetros **input_file** y **--output_type**.

Introducir el comando **--help** para mostrar ayuda adicional de los argumentos.

A continuación, se muestra un ejemplo de ejecución utilizando la interfaz gráfica, con fichero de entrada "_input.bag_", tipo de salida "_bag_", path del fichero de configuración "_config.json_" y usando el fichero de configuración.
```
python3 main.py input.bag --output_type bag --use_config --config_path config.json --use_graphic_UI
```

## Archivo de configuración
En este programa se añade un fichero de configuración para automatizar las conversiones. Algunos formatos requieren datos extra, por ejemplo, el tipo _mat_ requiere el nombre de las variables a almacenar. Para automatizar este proceso, se ha implementado un fichero de configuración que guarda estos valores.

El fichero usado por la aplicación por defecto se encuentra en la ruta _src/config/config.json_. En este fichero se puede observar el formato que debe tener un fichero de configuración, así como cada variable explicada para que el usuario pueda implementar un fichero de configuración por sí mismo.

## Formatos aceptados
En esta aplicación se aceptan cinco formatos diferentes:
- Archivos _bag_, utilizados por [ROS](https://www.ros.org/). El formato es el mencionado en la siguiente [web](http://rpg.ifi.uzh.ch/davis_data.html).
- Archivos _txt_, que contienen texto plano. El formato es el mencionado en la siguiente [web](http://rpg.ifi.uzh.ch/davis_data.html).
- Archivos _mat_, utilizados por [MATLAB](https://es.mathworks.com/products/matlab.html). Se aceptan tres estructuras diferentes:
    - Se almacenan cuatro variables dentro de una estructura. Cada variable contiene un array de datos.
    - Se almacenan cuatro variables directamente. Cada variable contiene un array de datos.
    - Se utiliza para almacenar una matriz 4 x N, siendo N el número de eventos.
- Archivos _bin_, que contienen los datos codificados en binario.
- Archivos _AEDAT_, que siguen el formato especificado en esta [web](https://inivation.github.io/inivation-docs/Software%20user%20guides/AEDAT_file_formats.html). Se aceptan las siguientes versiones:
    - Versión **2.0**, escritura y lectura implementadas.
    - Versión **3.1**, escritura y lectura implementadas.
    - Versión **4.0**, solo lectura implementada.

## Archivos de ejemplo
Junto al programa desarrollado, se ha añadido una carpeta de nombre _data-examples_ con archivos de ejemplos para cada tipo de archivo. Cada archivo contiene 200 eventos almacenados, para que el usuario pueda empezar a probar el programa con estos ficheros.

## Autoría
Este programa se ha desarrollado como Trabajo de Fin de Grado de la Escuela Politécnica Superior ([EPS](https://www.uam.es/ss/Satellite/EscuelaPolitecnica/es/home.htm)) de la  Universidad Autónoma de Madrid ([UAM](https://www.uam.es/uam/inicio)) en el grado de Ingeniería Informática.

```
Autor: Andrés Calderón Ayuso

Tutor: Erik Velasco Salido

Ponente: José María Martínez Sánchez
```