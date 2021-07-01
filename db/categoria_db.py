from sqlalchemy import Column, Integer, String
from db.db_connection import Base, engine
#from typing import Dict
#from pydantic import BaseModel

'''
class CategoriaDB(BaseModel):
    id: int
    nombre: str
    imagen: str
'''

class CategoriaDB(Base):
    __tablename__ = "categoria"

    #id = Column(Integer, primary_key=True, unique=True)
    id = Column(Integer, primary_key=True, autoincrement=True)    
    nombre = Column(String)
    imagen = Column(String)

'''
database_cat = Dict[int, CategoriaDB]

database_cat = {
    1: CategoriaDB(**{"id":1, "nombre":"Alimentos", "imagen":"img-alimentos.jpeg"}),
    2: CategoriaDB(**{"id":2, "nombre":"Bebidas", "imagen":"img-bebidas.jpeg"}), 
    3: CategoriaDB(**{"id":3, "nombre":"Café", "imagen":"img-cafe.jpeg"}),
    4: CategoriaDB(**{"id":4, "nombre":"Licores", "imagen":"img-licores.jpeg"})
}     
'''

Base.metadata.create_all(bind=engine)

'''
def get_categorias():
    return database_cat

def update_categoria(cat_in_db: CategoriaDB):
    database_cat[cat_in_db.id] = cat_in_db
    return cat_in_db
'''