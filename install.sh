#!/bin/bash

echo "================================================"
echo "  HRD - Home Router Daemon"
echo "  ISP Management System"
echo "  by r00t @ github.com/julianbenito1622-afk"
echo "================================================"

# Verificar que es Debian
if ! command -v apt &> /dev/null; then
    echo "ERROR: HRD solo funciona en Debian/Ubuntu"
    exit 1
fi

echo "[1/5] Actualizando sistema..."
sudo apt update -y

echo "[2/5] Instalando dependencias..."
sudo apt install -y python3 python3-pip postgresql postgresql-client git

echo "[3/5] Clonando HRD..."
git clone https://github.com/julianbenito1622-afk/HRD.git
cd HRD

echo "[4/5] Instalando librerías Python..."
pip install fastapi uvicorn sqlalchemy psycopg2-binary librouteros --break-system-packages

echo "[5/5] Configurando base de datos..."
sudo systemctl start postgresql
sudo -u postgres psql -c "CREATE DATABASE hrd;" 2>/dev/null
sudo -u postgres psql -c "CREATE USER hrd_user WITH PASSWORD 'hrd2024';" 2>/dev/null
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE hrd TO hrd_user;" 2>/dev/null
sudo -u postgres psql -c "GRANT ALL ON SCHEMA public TO hrd_user;" 2>/dev/null

echo ""
echo "✅ HRD instalado exitosamente"
echo "👉 Inicia con: cd HRD && python3 -m uvicorn main:app --host 0.0.0.0 --port 8000"
echo "👉 Panel: http://TU-IP:8000/docs"