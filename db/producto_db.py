from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String, Boolean
from db.db_connection import Base, engine
from typing import Dict
from pydantic import BaseModel

'''
class ProductoDB(BaseModel):
    id: int
    nombre: str
    unidad: str
    precio: int
    imagen: str
    descripcion: str
    stock: bool
    categoria: str
'''
class ProductoDB(Base):
    __tablename__ = "producto"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    unidad = Column(String)
    precio = Column(Integer)
    imagen = Column(String)
    descripcion = Column(String)
    stock = Column(Boolean, default=True)
    id_categoria = Column(Integer, ForeignKey("categoria.id"))

'''
database_producto = Dict[int, CategoriaDB]

database_producto = {
    1: ProductoDB(**{"id":1, "nombre":"Croissant", "unidad":"un", "precio": 3000, "imagen":"img-croissant.jpeg", "descripcion":"Croissant de queso.", "stock":True, "categoria":"Alimentos" }),
    2: ProductoDB(**{"id":2, "nombre":"Torta de chocolate", "unidad":"un", "precio": 5000, "imagen":"img-torta-de-chocolate.jpeg", "descripcion":"Porción de torta de chocolate.", "stock":True, "categoria":"Alimentos" }),
    3: ProductoDB(**{"id":3, "nombre":"Gaseosa", "unidad":"un", "precio": 3000, "imagen":"img-gaseosa.jpeg", "descripcion":"Gaseosa 350 ml.", "stock":True, "categoria":"Bebidas" }),
    4: ProductoDB(**{"id":4, "nombre":"Agua", "unidad":"un", "precio": 3000, "imagen":"img-agua.jpeg", "descripcion":"Botella de agua sin gas 350 ml.", "stock":True, "categoria":"Bebidas" }),
    5: ProductoDB(**{"id":5, "nombre":"Cerveza artesanal", "unidad":"un", "precio": 6000, "imagen":"img-cerveza-artesanal.jpeg", "descripcion":"Cerveza artesanal Apostol 300 ml.", "stock":True, "categoria":"Bebidas" }),
    6: ProductoDB(**{"id":6, "nombre":"Americano", "unidad":"un", "precio": 3000, "imagen":"img-americano.jpeg", "descripcion":"Café americano 4 oz", "stock":True, "categoria":"Café" }),
    7: ProductoDB(**{"id":7, "nombre":"Cappuccino", "unidad":"un", "precio": 4000, "imagen":"img-cappuccino.jpeg", "descripcion":"Café cappuccino sin licor 150 ml.", "stock":True, "categoria":"Café" }),
    8: ProductoDB(**{"id":8, "nombre":"Capuccino con licor", "unidad":"un", "precio": 6000, "imagen":"img-cappuccino-con-licor.jpeg", "descripcion":"Café cappuccino con Amaretto o Baileys 180 ml.", "stock":True, "categoria":"Café" }),
    9: ProductoDB(**{"id":9, "nombre":"Margarita", "unidad":"un", "precio": 14000, "imagen":"img-margarita.jpeg", "descripcion":"Coctel Margarita tradicional 6 oz.", "stock":True, "categoria":"Licores" }),
    10: ProductoDB(**{"id":10, "nombre":"Mojito", "unidad":"un", "precio": 12000, "imagen":"img-mojito.jpeg", "descripcion":"Coctel Mojito cubano 6 oz.", "stock":True, "categoria":"Licores" }),                                
}     
'''

Base.metadata.create_all(bind=engine)