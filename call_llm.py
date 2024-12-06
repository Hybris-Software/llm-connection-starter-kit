import requests


def call_lm_studio(prompt, model="default-model", temperature=0.7, max_tokens=100):
    """
    Effettua una chiamata API a LM Studio per ottenere una risposta a un prompt.

    :param prompt: Testo di input da inviare al modello.
    :param model: Nome del modello da utilizzare (opzionale).
    :param temperature: Parametro di temperatura per controllare la creatività (opzionale).
    :param max_tokens: Numero massimo di token nella risposta (opzionale).
    :return: Risposta generata dal modello.
    """
    url = "http://localhost:1234/v1/completions"  # URL dell'API di LM Studio
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": model,
        "prompt": prompt,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Solleva eccezioni per errori HTTP
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Errore nella chiamata API: {e}")
        return None


# Esempio di utilizzo
if __name__ == "__main__":
    prompt = "Scrivi una breve poesia su un tramonto."
    response = call_lm_studio(prompt)
    if response:
        print("Risposta dal modello:")
        print(response.get("choices", [{}])[0].get("text", ""))
