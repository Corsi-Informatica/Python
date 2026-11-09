# --- FASE 1: ACQUISIZIONE DATI E CASTING ---

# Acquisiamo il nome come stringa (tipo predefinito di input())
nome = input("Inserisci il tuo nome: ")

# Acquisiamo l'età e la convertiamo in intero (int) per i confronti numerici
eta = int(input("Inserisci la tua età: "))

# Acquisiamo le ore previste e le convertiamo in numero decimale (float)
ore_utilizzo = float(input("Ore di utilizzo previste: "))

# Acquisiamo la scelta del piano
piano_scelto = input("Scegli piano (Basic/Premium): ")


# --- FASE 2: ALGEBRA BOOLEANA E REQUISITI DI ACCESSO ---

# Verifichiamo il requisito minimo assoluto (14 anni)
# La variabile accesso_approvato sarà un booleano (True o False)
accesso_approvato = eta >= 14


# --- FASE 3: LOGICA CONDIZIONALE ---
if not accesso_approvato:
    # Se il booleano è False, il programma termina il servizio per l'utente
    print(f"Spiacenti {nome}, non hai l'età minima (14 anni) per il servizio.")
else:
    # L'utente ha almeno 14 anni, procediamo con la logica del piano
    
    # Verifica restrizione per minorenni (tra 14 e 17 anni)
    if eta < 18 and piano_scelto == "Premium":
        print("AVVISO: I minori di 18 anni possono usare solo il piano Basic.")
        piano_scelto = "Basic" # Forza il cambio di piano

    # Determinazione del costo orario in base al piano finale
    if piano_scelto == "Premium":
        costo_orario = 5.0
    else:
        costo_orario = 2.5
    

   # --- FASE 4: OPERATORI E CALCOLI ---
    # Calcolo del costo base
    costo_totale = ore_utilizzo * costo_orario
    
    # Applicazione dello sconto (10% se ore > 50)
    if ore_utilizzo > 50:
        # Moltiplichiamo per 0.9 per applicare lo sconto del 10%
        costo_totale = costo_totale * 0.9
        nota_sconto = "(Sconto 10% applicato)"
    else:
        nota_sconto = ""


    # --- FASE 5: OUTPUT FINALE ---
    # Stampiamo il riepilogo formattato
    print("\n--- RIEPILOGO TARIFFARIO ---")
    print(f"Utente: {nome}")
    print(f"Piano Finale: {piano_scelto}")
    print(f"Ore Totali: {ore_utilizzo}")
    print(f"Costo Totale: {costo_totale:.2f} € {nota_sconto}")