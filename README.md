# Proyecto automatización prueba técnica

## Métodos

- crearCarpetas(): genera de forma automática las carpetas necesarias para guardar los archivos durante el proceso de ejecución
- descargarArchivo(): ingresa al URL proporcionado, interactua con la plataforma y descarga el archivo necesario para el proceso
- generarArchivo(): realiza el proceso de manipulación de datos, generación del archivo final con la información solicitada y los cálculos necesarios
- envioEmail(): envia el correo hacia el usuario deseado

## Instalación

Sigue estos pasos para instalar y ejecutar este proyecto en tu máquina local.

### 1. Clona este repositorio:


git clone https://github.com/franco03102/pruebas.git


### 2. Instala las dependencias:

pip install selenium@4.28.1
pip install pandas@2.2.3

### 3. Modifica las variables:

{{ruta}}: Ruta completa donde se ubique la carpeta del proyecto, ya que de este depende la correcta descarga del archivo y los procesos siguientes

"contrasena": Contraseña del remitente (Actualmente es necesario configurar el gmail con 2FA y agregar una contraseña de aplicación menos segura para el correcto funcionamiento del envío de correos automatizados).

Adicionalmente, esta contraseña debe ser encriptada en base 64, se puede realizar en el URL: https://www.base64encode.org/es/

{{usuario}}: Dominio (gmail) del remitente

{{receptor}}: Dominio del receptor