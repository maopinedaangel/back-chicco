from pydantic import BaseModel

class ProductoIn(BaseModel):
    nombre: str
    unidad: str
    precio: int
    imagen: str
    descripcion: str
    stock: bool
    id_categoria: int

class ProductoUpdate(BaseModel):
    id: int
    nombre: str
    unidad: str
    precio: int
    imagen: int
    descripcion: str
    stock: bool
    id_categoria: int