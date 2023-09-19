from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException

url = "https://www.questura.bologna.it/node/2"
codpratica = "23BO012345"
dng = "01"
dnm = "01"
dna = "2000"

# Initialize Chrome WebDriver without specifying executable_path
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

log_file = "log.txt"

driver.get(url)

codpratica_field = driver.find_element("id", "codpratica")
dng_field = driver.find_element("id", "dng")
dnm_field = driver.find_element("id", "dnm")
dna_field = driver.find_element("id", "dna")
prenota_button = driver.find_element("id", "prenota")

codpratica_field.send_keys(codpratica)
dng_field.send_keys(dng)
dnm_field.send_keys(dnm)
dna_field.send_keys(dna)
prenota_button.click()

time.sleep(5)  # Attendi qualche secondo per caricare la pagina successiva

try:
    result_message = driver.find_element("css selector", ".field-item.even")
    result_text = result_message.text.strip()
except NoSuchElementException:
    print("Element .field-item.even not found on the page. Check the page structure or selector.")

try:
    result_message = driver.find_element("css selector", ".view-header")
    result_text = result_message.text.strip()
except NoSuchElementException:
    print("Element .view-header not found on the page. Check the page structure or selector.")
  

now = datetime.now()
log_entry = f"{now} - {result_text}\n"

with open(log_file, "a") as log:
    log.write(log_entry)

if "Non è pronto alcun permesso di soggiorno" not in result_text:

    if "In base ai dati da te inseriti, il tuo permesso di soggiorno è pronto per il ritiro." in result_text:
        print("------- IL PERMESSO DI SOGGIORNO E' PRONTO !!!-----------")
        # Aggiungi qui il codice per avvisarti (ad esempio invio di una notifica)
    else:
        print("Risultato diverso:", result_text)

else:
    print("Non è pronto alcun permesso di soggiorno")

# Attendi un po' prima di effettuare la successiva iterazione
# time.sleep(3600)  # Attendi un'ora prima di controllare di nuovo

# Chiudi il browser alla fine
driver.quit()
