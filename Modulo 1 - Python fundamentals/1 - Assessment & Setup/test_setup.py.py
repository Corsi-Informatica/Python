import sys
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf

print("=== VERIFICA AMBIENTE PYTHON FOR DATA & AI ===")
print(f"1. Versione Python: {sys.version.split()[0]}")
print(f"2. Versione Pandas: {pd.__version__}")
print(f"3. Versione TensorFlow: {tf.__version__}")

# Test grafico veloce
plt.figure(figsize=(4, 2))
plt.plot([1, 2, 3], [4, 5, 6], label="Test Line")
plt.title("Setup Confermato!")
plt.close()
print("\nSUCCESS: Tutti i pacchetti principali sono stati caricati con successo!")