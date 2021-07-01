from pydantic import BaseModel
from typing import List
from models.cliente_models import ClienteIn
from models.compra_models import CompraIn

class PedidoIn(BaseModel):
    cc_cliente: int
    valor: int
    forma_pago: str
    valor_pagado: int
    estado: str
    turno: int
    cc_usuario: int


class ItemCompra(BaseModel):
    id_producto: int
    nombre: str
    cantidad: int
    valor: int
    comentario: str


class VentaIn(BaseModel):
    #cliente_in: ClienteIn
    pedido_in: PedidoIn
    compras: List[ItemCompra]