from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime

url = "https://www.questura.bologna.it/node/2"
codpratica = "23BO012345"
dng = "01"
dnm = "01"
dna = "2000"

# Imposta il percorso del driver del browser (chromedriver, geckodriver, ecc.)
driver = webdriver.Chrome(executable_path="/percorso/al/tuo/chromedriver")

log_file = "log.txt"

while True:
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
    
    result_message = driver.find_element("css selector", ".field-item.even")
    result_text = result_message.text.strip()
    
    now = datetime.now()
    log_entry = f"{now} - {result_text}\n"
    
    with open(log_file, "a") as log:
        log.write(log_entry)
    
    if "Non è pronto alcun permesso di soggiorno" not in result_text:
        print("Risultato diverso:", result_text)
        # Aggiungi qui il codice per avvisarti (ad esempio invio di una notifica)
    else:
        print("Non è pronto alcun permesso di soggiorno")
    
    # Attendi un po' prima di effettuare la successiva iterazione
    # time.sleep(3600)  # Attendi un'ora prima di controllare di nuovo

# Chiudi il browser alla fine
driver.quit()
