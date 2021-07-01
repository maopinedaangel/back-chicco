from sqlalchemy import Column, Integer, String, BigInteger
from db.db_connection import Base, engine

class ClienteDB(Base):
    __tablename__ = "cliente"

    cedula = Column(BigInteger, primary_key=True)    
    nombre = Column(String)
    apellido = Column(String)
    telefono = Column(BigInteger)
    puntos = Column(Integer, default=0)

Base.metadata.create_all(bind=engine)
