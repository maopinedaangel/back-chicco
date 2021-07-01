from pydantic import BaseModel

class ClienteIn(BaseModel):
    cedula: int
    nombre: str
    apellido: str
    telefono: int
    puntos: int

#class CategoriaUpdate(BaseModel):
#    id: int
#    nombre: str
#    imagen: str    