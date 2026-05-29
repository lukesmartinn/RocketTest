import os

print("--- KONTROLA IZOLACE PROCESŮ ---")

try:
    # Vypíšeme všechna PID (čísla procesů) ve složce /proc
    pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]
    print(f"Vidím celkem {len(pids)} běžících procesů v systému.")
    
    if len(pids) > 10:
        print("!!! DIVNÉ: Vidím podezřele hodně procesů, to nevypadá jako izolovaný kontejner !!!")
        # Vypíšeme prvních pár, ať víme, co jsou zač
        for pid in pids[:10]:
            try:
                with open(f'/proc/{pid}/comm', 'r') as f:
                    print(f"PID {pid}: {f.read().strip()}")
            except:
                pass
    else:
        print(f"Vidím jen {len(pids)} procesy, to vypadá v pořádku.")
except Exception as e:
    print(f"Nemůžu číst /proc: {e}")

print("--- KONEC TESTU ---")