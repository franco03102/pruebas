from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time, base64, smtplib, ssl
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

                anexo = WebDriverWait(init, 60).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[5]/div/div[1]/div/div[2]/table[2]/tbody/tr/td/div/table[2]/tbody/tr/td/div/a')))
                init.execute_script("arguments[0].scrollIntoView(true);", anexo)
                time.sleep(5)
                anexo.click()

                init.close()

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
            Prueba.envioEmail()

        if __name__ == "__main__":

            main()

        data = 1

    except:

        data = 2