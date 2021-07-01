from pydantic import BaseModel

class CategoriaIn(BaseModel):
    nombre: str
    imagen: str

class CategoriaUpdate(BaseModel):
    id: int
    nombre: str
    imagen: str    