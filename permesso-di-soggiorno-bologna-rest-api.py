from flask import Flask, request
from flask_httpauth import HTTPBasicAuth
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

app = Flask(__name__)
auth = HTTPBasicAuth()

# Configura le credenziali (username e password)
users = {
    "username": "password"
}

@auth.verify_password
def verify_password(username, password):
    if username in users and password == users.get(username):
        return username

url = "https://www.questura.bologna.it/node/2"
codpratica = "23BO012345"
dng = "01"
dnm = "01"
dna = "2000"

# Imposta il percorso del driver del browser (chromedriver, geckodriver, ecc.)
driver = webdriver.Chrome(executable_path="/percorso/al/tuo/chromedriver")

@app.route("/check_permesso", methods=["GET"])
@auth.login_required
def check_permesso():
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
    
    response = {"result": result_text}
    
    return response

if __name__ == "__main__":
    app.run(debug=True)