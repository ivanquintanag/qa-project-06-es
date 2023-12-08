# Proyecto 6.
Breve descripción: Trabajo de proyecto 6 ejecutando técnicas adquiridas en bootcamp para casos de prueba web y móviles.

# Lenguaje utilizado.
Python es un lenguaje de programación ampliamente utilizado en las aplicaciones web, el desarrollo de software, la ciencia de datos y el machine learning (ML).
Una de las ventajas de éste lenguaje es que es eficiente y fácil de aprender, además de que se puede ejecutar en muchas plataformas diferentes.

# Instrucciones e instalación de intérprete de Python.
Primero, se requeire instalar un intérprete de Python. Este es un programa para iniciar y ejecutar el código Python en un dispositivo. Descarga su última versión desde el sitio web oficial: https://www.python.org/downloads/. Instala el programa siguiendo las instrucciones.

Configuración del Entorno:
Antes de ejecutar las pruebas, se debe asegurar de tener Python y pytest instalados en tu entorno de desarrollo. Aquí hay algunos pasos para verificar e instalar.

Verificar la Instalación de Python:
Abre una terminal y ejecuta el siguiente comando para verificar si Python está instalado:

python --version

Si Python está instalado, se deberá corroborar la versión. Si no lo está, sigue las instrucciones de descarga para re instalar Python.

Instalar pytest:
Después de instalar Python, verifica si pytest está instalado. Ejecuta el siguiente comando:

pytest --version

Si pytest está instalado, deberías ver la versión. Si no lo está, instálalo ejecutando:

pip install pytest

Ejecución de pruebas:
Una vez que Python y pytest estén instalados, puedes ejecutar las pruebas con el siguiente comando:

pytest

Este comando buscará automáticamente archivos con nombres que coincidan con el patrón test_*.py en el directorio actual y ejecutará las pruebas. Si se tiene archivos con nombres diferentes o en ubicaciones específicas, se puede ajustar el comando de acuerdo a tu estructura de directorios.

Ejemplo: Abre una terminal y navega al directorio de tu proyecto. Ejecuta el siguiente comando para ejecutar todas las pruebas en el directorio actual y sus subdirectorios: pytest
Si deseas ejecutar pruebas de un archivo específico, puedes proporcionar el nombre del archivo después del comando pytest: pytest nombre_del_archivo.py

Después de ejecutar las pruebas, pytest mostrará los resultados en la terminal. Se conocerá si todas las pruebas han pasado correctamente o si hay algún fallo. Además, pytest proporciona información detallada sobre las pruebas individuales.

¡Listo! Ahora está listo para ejecutar tus pruebas con pytest.

# Plataforma de caso de prueba.
Se trabaja para realización de pruebas de aplicación Urban Grocers por códigos Python.

# Pasos para obtención de datos:
- Se generan los archivos necesarios para llamar a funciones y respuestas solicitadas.
- Se ingresan datos a los archivos de configuración con la información desde URL, APIS y DOC
- Se generan 9 casos de pruebas entre positivas y negativas según lista de comprobación.
- Se utiliza además, token de autorización para las mismos casos de prueba.
- Se realiza y se corre prueba en Pycharm con conexión a GITHUB.
