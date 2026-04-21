import subprocess
import socket
from datetime import datetime

def ping(host):
    resultado = subprocess.run(
        ["ping", "-c", "1", "-W", "2", host],
        capture_output=True
    )
    return resultado.returncode == 0

def check_puerto(host, puerto, timeout=3):
    try:
        sock = socket.socket()
        sock.settimeout(timeout)
        sock.connect((host, puerto))
        sock.close()
        return True
    except:
        return False

def estado_red(hosts: list):
    resultado = []
    for host in hosts:
        activo = ping(host)
        resultado.append({
            "host": host,
            "activo": activo,
            "timestamp": datetime.utcnow().isoformat()
        })
    return resultado