import json
import ollama
#from pydantic import BaseModel, Field
from typing import List, Optional
import pdfplumber

# Estrazione Dati Grezzi da referto_lab_a.pdf
file_path = "referto_lab_a.pdf"

def estrai_da_pdf(file_pdf_path):
    try:
        with pdfplumber.open(file_path) as pdf:
            page = pdf.pages[0]
            testo_grezzo = page.extract_text()
            tabelle = page.extract_tables()
            
            return testo_grezzo
            
    except FileNotFoundError:
        print(f"Errore: Il file '{file_path}' non è stato trovato. Verifica il percorso.")
    except Exception as e:
        print(f"Si è verificato un errore inatteso: {e}")

def elabora_testo(testo):
    prompt_system = f"""
    Sei un assistente AI specializzato nell'estrazione dati di referti chimici.
    Analizza il testo seguente e restituisci un JSON contenente una chiave 'risultati' con una lista di oggetti.
    Ogni oggetto deve corrispondere ai parametri analizzati e contenere: 'Parametro', 'Valore' (come numero se possibile), 'Unita', 'Limite min' , 'Limite max'.
    Se un dato non è presente metti null.
    
    Testo da analizzare:
    {testo}
    """
    
    try:
        # Chiamata al modello con json_mode
        response = ollama.chat(
            model='llama3.2', 
            messages=[{'role': 'user', 'content': prompt_system}],
            format='json'
        )
        
        # Trasformazione
        risultato_dizionario = json.loads(response['message']['content'])
        return risultato_dizionario
        
    except Exception as e:
        print(f"Errore nell'estrazione: {e}")
        return None

# Test in live
file_path = 'referto_lab_a.pdf'
testo_grezzo = estrai_da_pdf(file_path)
print(testo_grezzo)
dati = elabora_testo(testo_grezzo)
print(dati)
print(json.dumps(dati, indent=4, ensure_ascii=False))