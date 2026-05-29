import socket

def check_redis(ip):
    print(f"Zkouším Redis na {ip}...")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((ip, 6379))
        # Zkusíme poslat příkaz PING (standardní Redis test)
        s.send(b"PING\r\n")
        response = s.recv(1024)
        print(f"!!! REDIS ODPOVĚDĚL NA {ip}: {response.decode().strip()} !!!")
        
        # Zkusíme INFO (vysype to hromadu informací o serveru)
        s.send(b"INFO\r\n")
        info = s.recv(1024)
        print(f"INFO výstřižek: {info.decode()[:200]}...")
    except Exception as e:
        print(f"Redis na {ip} nedostupný: {e}")
    finally:
        s.close()

print("--- REDIS SCAN ---")

# 1. Zkusíme localhost (jestli neběží v podu)
check_redis("127.0.0.1")

# 2. Zkusíme vnitřní Kubernetes službu (pokud ji nabízejí jako "redis")
try:
    redis_ip = socket.gethostbyname("redis")
    check_redis(redis_ip)
except:
    print("Služba s názvem 'redis' nebyla nalezena přes DNS.")

# 3. Zkusíme "bránu" (často tam bývají sdílené služby)
check_redis("10.96.0.1")

print("--- KONEC SCANU ---")