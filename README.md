# Permesso di Soggiorno Bologna Checker

Questo progetto è stato creato per automatizzare il controllo periodico dello stato di ritiro del Permesso di Soggiorno presso la Questura di Bologna. L'obiettivo è verificare se il permesso di soggiorno è pronto per il ritiro o meno, e ricevere notifiche in caso di risultato diverso.

## Funzionalità

- Automatizza il processo di controllo periodico dello stato di ritiro del Permesso di Soggiorno.
- Verifica se il Permesso di Soggiorno è pronto per il ritiro tramite un'apposita pagina web.
- Invia notifiche in caso di risultato diverso dal messaggio standard.

## Come funziona

1. Lo script utilizza il browser per accedere alla pagina di controllo dello stato di ritiro presso la Questura di Bologna.
2. Inserisce i dati richiesti (codice pratica, data di nascita) e fa clic sul pulsante "prenota il ritiro".
3. Controlla il risultato ottenuto dalla pagina: se è diverso dal messaggio "Non è pronto alcun permesso di soggiorno", invia una notifica (puoi personalizzare come ricevere la notifica).

## Istruzioni per l'uso

1. Assicurati di avere Python installato sul tuo sistema.
2. Installa le librerie necessarie eseguendo `pip install -r requirements.txt`  e  `pip install selenium` (come amministratore).
3. Scarica il driver del browser corrispondente (es. chromedriver per Chrome) e inserisci il percorso nel codice.
4. Modifica le informazioni necessarie nel codice, come il codice pratica, la data di nascita, il percorso del driver, ecc.
5. Esegui lo script con il comando `python permesso-di-soggiorno-bologna.py`.

## Personalizzazioni

Puoi personalizzare lo script per adattarlo alle tue esigenze. Ad esempio, puoi modificare il periodo di controllo, il tipo di notifica, ecc.

## Attenzione

L'automazione di interazioni con siti web può essere soggetta a restrizioni o politiche del sito. Assicurati di rispettare i termini d'uso e le normative.

---
Autore: @thun88  (Sun Wen-Long)

Licenza MIT
