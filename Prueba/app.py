from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

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
                    "prefs", {"download.default_directory":"C:\\Users\\franc\\OneDrive\\Documentos\\GitHub\\pruebas"}
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

        def main():

            Prueba.descargaArchivo()

        if __name__ == "__main__":

            main()

        data = 1

    except:

        data = 2