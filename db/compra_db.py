from sqlalchemy import Column, Integer, String, ForeignKey
from db.db_connection import Base, engine

class CompraDB(Base):
    __tablename__ = "compra"

    id = Column(Integer, primary_key=True, autoincrement=True)    
    id_pedido = Column(Integer, ForeignKey("pedido.id"))
    id_producto = Column(Integer, ForeignKey("producto.id"))
    cantidad = Column(Integer)
    comentario = Column(String)


Base.metadata.create_all(bind=engine)