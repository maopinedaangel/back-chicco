from pydantic import BaseModel

class CompraIn(BaseModel):
    id_pedido: int               #Se requiere el id_pedido para almacenar la compra
    id_producto: int
    cantidad: int
    comentario: str
  