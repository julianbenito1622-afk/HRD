from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Cliente(Base):
    __tablename__ = "clientes"

    id          = Column(Integer, primary_key=True)
    nombre      = Column(String, nullable=False)
    telefono    = Column(String)
    direccion   = Column(String)
    ip          = Column(String, unique=True)
    plan        = Column(String)
    precio      = Column(Float)
    activo      = Column(Boolean, default=True)
    creado_en   = Column(DateTime, default=datetime.utcnow)

class Pago(Base):
    __tablename__ = "pagos"

    id          = Column(Integer, primary_key=True)
    cliente_id  = Column(Integer, nullable=False)
    monto       = Column(Float)
    fecha       = Column(DateTime, default=datetime.utcnow)
    mes         = Column(String)