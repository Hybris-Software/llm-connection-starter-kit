# **Progetto API LM Studio**

Questo progetto utilizza Python per effettuare chiamate API a un server LM Studio locale. Il codice invia un prompt al modello configurato su LM Studio e restituisce una risposta generata dal modello.

---

## **Prerequisiti**

1. **LM Studio**:

   - Assicurati di aver scaricato e installato LM Studio.
   - Configura LM Studio per esporre un'API locale. Solitamente l'API è accessibile su `http://localhost:1234`.

2. **Python**:

   - Versione Python >= 3.7.
   - Installato il gestore dei pacchetti `pip`.

3. **Libreria `requests`**:
   - Per installarla, esegui il comando:
     ```bash
     pip install requests
     ```
     o in alternativa:
     ```
     pip install -r requirements.txt
     ```


---

## **Istruzioni per avviare il progetto**

1. **Clona il progetto**:
   Clona il repository o copia il codice Python nel tuo ambiente locale.

2. **Verifica che LM Studio sia in esecuzione**:

   - Avvia LM Studio e assicurati che l'API sia disponibile all'indirizzo `http://localhost:1234`.
   - Se l'API è esposta su una porta diversa, modifica la riga:
     ```python
     url = "http://localhost:1234/v1/completions"
     ```
     Sostituendo `1234` con il numero di porta corretto.

3. **Esegui lo script Python**:

   - Usa il terminale o un editor di testo con un ambiente Python integrato.
   - Esegui il comando:
     ```bash
     python nome_del_file.py
     ```
     Sostituendo `nome_del_file.py` con il nome del file in cui hai salvato lo script.

4. **Fornisci un prompt**:

   - Lo script invia un prompt predefinito:
     ```python
     prompt = "Scrivi una breve poesia su un tramonto."
     ```
     Modifica questa riga per inviare il testo desiderato.

5. **Visualizza il risultato**:
   - Se la chiamata API è corretta, vedrai la risposta generata dal modello stampata nel terminale.
   - Un esempio di output potrebbe essere:
     ```
     Risposta dal modello:
     Un tramonto dipinto nel cielo,
     colori che svaniscono piano,
     il giorno si spegne con grazia,
     la notte sorge come un piano.
     ```

---

## **Modifiche personalizzabili**

- **Modello predefinito**:
  Cambia il parametro `model` nella funzione `call_lm_studio` con il nome del modello che desideri utilizzare.

- **Creatività**:
  Modifica il parametro `temperature` per aumentare o diminuire la creatività della risposta:

  - Valori più bassi (es. 0.1) producono risposte più prevedibili.
  - Valori più alti (es. 0.9) aumentano la variabilità.

- **Lunghezza massima della risposta**:
  Cambia il parametro `max_tokens` per definire il numero massimo di token nella risposta.

---

## **Gestione degli errori**

Se qualcosa va storto, lo script mostrerà un messaggio di errore. Possibili cause:

1. **LM Studio non in esecuzione**: Assicurati che il server sia avviato.
2. **URL API errato**: Controlla che l'indirizzo e la porta siano corretti.
3. **Parametri non validi**: Verifica che il payload contenga valori accettabili.

Per ulteriori informazioni o supporto, consulta la documentazione ufficiale di LM Studio.

---

## **Licenza**

Questo progetto è distribuito sotto una licenza open-source. Sentiti libero di modificarlo e migliorarlo secondo le tue esigenze.
