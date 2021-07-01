from sqlalchemy import Column, Integer, String, BigInteger
from db.db_connection import Base, engine

class UsuarioDB(Base):
    __tablename__ = "usuario"

    cedula = Column(BigInteger, primary_key=True)   
    password = Column(String)     
    nombre = Column(String)
    apellido = Column(String)
    telefono = Column(BigInteger)
    perfil = Column(String)

Base.metadata.create_all(bind=engine)