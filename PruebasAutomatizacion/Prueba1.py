from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

# Inicializa el WebDriver de Chrome
d = webdriver.Chrome()

try:
    # Abre la URL
    d.get("https://www.stanford.edu/")

    search_box = WebDriverWait(d, 100).until(
        EC.presence_of_element_located((By.ID, "search-input-field"))
    )

    # Busca el término 'quantum'
    search_box.send_keys("quantum")
    search_box.submit()

    time.sleep(2)  # Pausa de 2 segundos

    link = d.find_element_by_link_text("Quantum Entanglement and Information")

    link.click()


except TimeoutException:
    print("Tiempo de espera agotado. No se encontró el elemento buscado.")
except NoSuchElementException:
    print("No se encontró el elemento específico en la página.")
except Exception as e:
    print(f"Error desconocido: {e}")

finally:
    d.quit()