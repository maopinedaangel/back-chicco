from pydantic import BaseModel

class UsuarioIn(BaseModel):
    cedula: int
    password: str
    nombre: str
    apellido: str
    telefono: int
    perfil: str

#class CategoriaUpdate(BaseModel):
#    id: int
#    nombre: str
#    imagen: str   