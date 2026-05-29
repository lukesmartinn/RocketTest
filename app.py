import time
import os
import sys

def log_bomb():
    print("--- STARTING LOG BOMB TEST ---")
    data = []
    counter = 0
    
    while True:
        counter += 1
        # Generujeme agresivní logy
        log_line = f"[{counter}] SEVERE_DEBUG_LOG: Payload structure flooding... " + ("X" * 100)
        print(log_line)
        
        # Každých 1000 řádků alokujeme trochu paměti pro simulaci memory leaku
        if counter % 1000 == 0:
            data.append(" " * (1024 * 1024)) # +1 MB
            print(f">>> Memory leak simulation: Allocated total approx {len(data)} MB", file=sys.stderr)
            
        # Žádný sleep nebo jen velmi krátký pro maximální tlak
        # time.sleep(0.001) 

if __name__ == "__main__":
    log_bomb()