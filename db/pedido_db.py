from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
import datetime

from db.db_connection import Base, engine

class PedidoDB(Base):
    __tablename__ = "pedido"

    id = Column(Integer, primary_key=True, autoincrement=True)    
    cc_cliente = Column(Integer, ForeignKey("cliente.cedula"))
    fecha = Column(DateTime, default=datetime.datetime.utcnow)
    valor = Column(Integer)
    forma_pago = Column(String, default="Efectivo")
    valor_pagado = Column(Integer)
    devuelta = Column(Integer)
    estado = Column(String)
    factura = Column(String)
    turno = Column(Integer)
    cc_usuario = Column(Integer, ForeignKey("usuario.cedula"))

Base.metadata.create_all(bind=engine)