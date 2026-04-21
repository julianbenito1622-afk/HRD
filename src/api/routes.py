from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.core.config import SessionLocal
from src.database.models import Cliente
from src.core.auth import obtener_usuario_actual
from src.core.mikrotik import MikroTik
from src.core.monitor import estado_red
from pydantic import BaseModel
from typing import Optional, List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class ClienteSchema(BaseModel):
    nombre: str
    telefono: Optional[str] = None
    direccion: Optional[str] = None
    ip: Optional[str] = None
    plan: Optional[str] = None
    precio: Optional[float] = None

class MikroTikConfig(BaseModel):
    host: str
    user: str
    password: str

@router.post("/clientes")
def crear_cliente(cliente: ClienteSchema, db: Session = Depends(get_db), usuario: str = Depends(obtener_usuario_actual)):
    nuevo = Cliente(**cliente.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.get("/clientes")
def listar_clientes(db: Session = Depends(get_db), usuario: str = Depends(obtener_usuario_actual)):
    return db.query(Cliente).all()

@router.get("/clientes/{id}")
def obtener_cliente(id: int, db: Session = Depends(get_db), usuario: str = Depends(obtener_usuario_actual)):
    cliente = db.query(Cliente).filter(Cliente.id == id).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente

@router.delete("/clientes/{id}")
def eliminar_cliente(id: int, db: Session = Depends(get_db), usuario: str = Depends(obtener_usuario_actual)):
    cliente = db.query(Cliente).filter(Cliente.id == id).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    db.delete(cliente)
    db.commit()
    return {"mensaje": "Cliente eliminado"}

@router.post("/mikrotik/cortar/{ip}")
def cortar_cliente(ip: str, config: MikroTikConfig, usuario: str = Depends(obtener_usuario_actual)):
    mk = MikroTik(config.host, config.user, config.password)
    return mk.cortar_cliente(ip)

@router.post("/mikrotik/activar/{ip}")
def activar_cliente(ip: str, config: MikroTikConfig, usuario: str = Depends(obtener_usuario_actual)):
    mk = MikroTik(config.host, config.user, config.password)
    return mk.activar_cliente(ip)

@router.get("/mikrotik/conectados")
def ver_conectados(host: str, user: str, password: str, usuario: str = Depends(obtener_usuario_actual)):
    mk = MikroTik(host, user, password)
    return mk.listar_conectados()

@router.post("/monitor/ping")
def monitorear_red(hosts: List[str], usuario: str = Depends(obtener_usuario_actual)):
    return estado_red(hosts)