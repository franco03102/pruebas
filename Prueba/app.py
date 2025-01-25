from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time, base64, smtplib, ssl, os, glob
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#INICIO DE PROCESO
data = 2

while data != 1:

    try:

        class Prueba(object):

            def __init__(self):

                pass

            def descargaArchivo():

                #CONFIGURACIÓN DE DESCARGA EN EL NAVEGADOR
                settings = Options()
                settings.add_experimental_option(
                    "prefs", {"download.default_directory":"C:\\Users\\franc\\OneDrive\\Documentos\\GitHub\\pruebas\\Archivos\\Original"}
                )

                #INICIO DEL NAVEGADOR CON SUS CONFIGURACIONES
                init = webdriver.Chrome(options=settings)
                init.maximize_window()

                #ACCEDER AL VÍNCULO DE INTERÉS
                init.get("https://www.dane.gov.co/index.php/estadisticas-por-tema/precios-y-costos/precios-de-venta-al-publico-de-articulos-de-primera-necesidad-pvpapn")
                time.sleep(10)

                #BÚSQUEDA DEL ELEMENTO Y DESCARGA DE ARCHIVO
                anexo = WebDriverWait(init, 60).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[5]/div/div[1]/div/div[2]/table[2]/tbody/tr/td/div/table[2]/tbody/tr/td/div/a')))
                init.execute_script("arguments[0].scrollIntoView(true);", anexo)
                time.sleep(5)
                anexo.click()

                init.close()

            def generacionArchivo():

                rutas = []

                #LECTURA ARCHIVO ORIGINAL
                df = pd.read_excel('C:\\Users\\franc\\OneDrive\\Documentos\\GitHub\\pruebas\\Archivos\\Original\\pvpapn-2021-03-18-anexo-referencias-mas-vendidas.xlsx', sheet_name= "Cantidad_municipio 1203-1603", engine='openpyxl',header=None)

                #ELIMINAR DE ENCABEZADO
                row = 0
                while row < 7:

                    df.drop([row], inplace=True)
                    row+=1

                #GENERAR ARCHIVO BASE PARA MANIPULACIÓN DE DATOS
                df.to_excel('C:\\Users\\franc\\OneDrive\\Documentos\\GitHub\\pruebas\\Archivos\\Proceso\\base.xlsx', index=False, header=None, engine='openpyxl')
                rutas.append('C:\\Users\\franc\\OneDrive\\Documentos\\GitHub\\pruebas\\Archivos\\Proceso\\base.xlsx')

                #LECTURA ARCHIVO BASE
                df = pd.read_excel('C:\\Users\\franc\\OneDrive\\Documentos\\GitHub\\pruebas\\Archivos\\Proceso\\base.xlsx', engine='openpyxl')

                #ORDENAR DATAFRAME DE MAYOR A MENOR
                df_sorted = df.sort_values(by='Cantidades vendidas ', ascending=False)

                #GENERAR ARCHIVO ORDENADO
                df_sorted.to_excel('C:\\Users\\franc\\OneDrive\\Documentos\\GitHub\\pruebas\\Archivos\\Proceso\\ordenado.xlsx', index=False, engine='openpyxl')
                rutas.append('C:\\Users\\franc\\OneDrive\\Documentos\\GitHub\\pruebas\\Archivos\\Proceso\\ordenado.xlsx')


                #LECTURA ARCHIVO ORDENADO
                df = pd.read_excel('C:\\Users\\franc\\OneDrive\\Documentos\\GitHub\\pruebas\\Archivos\\Proceso\\ordenado.xlsx', engine='openpyxl')

                #ELIMINAR FILAS QUE NO CORRESPONDEN A LOS 10 PRIMEROS PRODUCTOS MAS VENDIDOS
                row = 10

                filas = len(df.index)
                while row < filas:

                    df.drop([row], inplace=True)
                    row+=1

                #GENERAR ARCHIVO PRODUCTOS MAS VENDIDOS
                df.to_excel('C:\\Users\\franc\\OneDrive\\Documentos\\GitHub\\pruebas\\Archivos\\Resultado\\mas_vendidos.xlsx', index=False, engine='openpyxl')
                rutas.append('C:\\Users\\franc\\OneDrive\\Documentos\\GitHub\\pruebas\\Archivos\\Resultado\\mas_vendidos.xlsx')

                #LECTURA ARCHIVO PRODUCTOS MAS VENDIDOS
                df = pd.read_excel('C:\\Users\\franc\\OneDrive\\Documentos\\GitHub\\pruebas\\Archivos\\Resultado\\mas_vendidos.xlsx', engine='openpyxl')

                #ELIMINAR COLUMNAS DIFERENTES A LAS SOLICITADAS
                columnas = df.columns.to_list()

                for columna in columnas:

                    if columna == "Nombre producto" or columna == "Marca" or columna == "Precio reportado ":
                        pass
                    else:

                        df.drop(columna, axis=1, inplace=True)

                #GENERAR ARCHIVO FINAL
                df.to_csv('C:\\Users\\franc\\OneDrive\\Documentos\\GitHub\\pruebas\\Archivos\\Resultado\\final.csv', index=False)

                #ELIMINAR ARCHIVOS NO RELEVANTES
                for ruta in rutas:
                    os.remove(ruta)

            
            def envioEmail():

                #ENCRIPTACIÓN DE CONTRASEÑA EN BASE64
                encode = b'ZnNyZCB0dmVuIGZhY3IgeWFicw=='
                data = base64.b64decode(encode)

                #TRANSOFMACIÓN DE INFORMACIÓN EN FORMATO UTF-8
                password = data.decode('utf-8')

                #CONFIGURACIÓN DEL SERVIDOR
                smtp_server = "smtp.gmail.com"
                smtp_port = 587
                smtp_username = 'francosecundaria@gmail.com'
                smtp_password = password

                #CONFIGURACIÓN DEL MENSAJE
                sender_email = 'francosecundaria@gmail.com'
                receiver_email = 'francomoncayo123@gmail.com'
                # subject = 'INTEGRACIÓN JOOR-DYNAMICS ' + str(file)
                subject = "prueba"
                body = "Hola"

                message = MIMEMultipart()
                message['From'] = sender_email
                message['To'] = receiver_email
                message['Subject'] = subject
                message.attach(MIMEText(body, 'plain'))

                context = ssl.create_default_context()

                #CONEXIÓN CON EL SERVIDOR
                server =  smtplib.SMTP(smtp_server, smtp_port)
                server.starttls(context=context)
                server.login(smtp_username, smtp_password)
                server.sendmail(sender_email, receiver_email, message.as_string())

                print("Correo electrónico enviado exitosamente.")

            

        def main():

            # Prueba.descargaArchivo()
            Prueba.generacionArchivo()
            # Prueba.envioEmail()

        if __name__ == "__main__":

            main()

        data = 1

    except:

        data = 2