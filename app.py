import socket

def check_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((ip, port))
    s.close()
    return result == 0

print(f"--- RUNTIME NETWORK CHECK ---")
print(f"Je OTEL port 44725 dostupný i teď? {'ANO' if check_port('127.0.0.1', 44725) else 'NE'}")