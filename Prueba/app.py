from selenium import webdriver
import time


#INICIO DEL NAVEGADOR CON SUS CONFIGURACIONES
init = webdriver.Chrome()
init.maximize_window()

#ACCEDER AL VÍNCULO DE INTERÉS
init.get('https://www.dane.gov.co/index.php/estadisticas-por-tema/precios-y-costos/precios-de-venta-alpublico-de-articulos-de-primera-necesidad-pvpapn')
time.sleep(10)
