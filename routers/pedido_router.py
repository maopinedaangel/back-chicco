from typing import List
import math

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from db.db_connection import get_db

from db.pedido_db import PedidoDB
from db.cliente_db import ClienteDB
from db.usuario_db import UsuarioDB

from models.pedido_models import PedidoIn, VentaIn
from models.cliente_models import ClienteIn
#from models.compra_models import CompraIn
#from models.usuario_models import UsuarioIn, UsuarioOut

router = APIRouter()


@router.get("/pedidos")
async def get_pedidos(db: Session = Depends(get_db)):
    pedidos = db.query(PedidoDB).all()
    return pedidos


@router.post("/pedido/nuevo")
async def new_pedido(venta_in: VentaIn, db: Session = Depends(get_db)):

    new_pedido = PedidoDB(**venta_in.pedido_in.dict())
    new_pedido.devuelta = new_pedido.valor_pagado - new_pedido.valor

    db.add(new_pedido)
    db.commit()
    db.refresh(new_pedido)

    mi_cliente = db.query(ClienteDB).get(new_pedido.cc_cliente)


    lista_compras = ""
    for item in venta_in.compras:
        linea = str(item.id_producto) + " - " + item.nombre + " - " + str(item.cantidad) + " - " + str(item.valor*item.cantidad) + "\n"
        lista_compras += linea


    recibo = ""
    puntos_compra = math.floor(new_pedido.valor/1000)
    #puntos = mi_cliente.puntos
    recibo += "Tabaqueria\n"
    recibo += "NIT: XXXXXXXXXX-X\n\n"
    recibo += "Cliente: " + str(mi_cliente.cedula) + "\n\n"
    recibo += lista_compras + "\n" 
    recibo += "TOTAL: " + str(new_pedido.valor) + "\n" 
    recibo += "EFECTIVO: " + str(new_pedido.valor_pagado) + "\n" 
    recibo += "CAMBIO: " + str(new_pedido.devuelta) + "\n\n" 
    recibo += "GRACIAS POR SU COMPRA\n\n"     
    recibo += "PUNTOS:\n"   
    recibo += "SALDO ANTERIOR: " + str(mi_cliente.puntos) + "\n"
    recibo += "EN ESTA COMPRA: " + str(puntos_compra) + "\n"
    mi_cliente.puntos += puntos_compra
    recibo += "NUEVO SALDO: " + str(mi_cliente.puntos) + "\n\n"
    recibo += "FACTURA NO.: " + str(new_pedido.id) + "\n\n"               

    new_pedido.factura = recibo

    db.commit()
    db.refresh(new_pedido)
    db.refresh(mi_cliente)

    #return {"mensaje": "Pedido creado exitosamente."}
    return new_pedido


@router.delete("/pedido/delete")
async def borrar_pedido(id: int, db: Session = Depends(get_db)):
    db.query(PedidoDB).filter(PedidoDB.id==id).delete()

    db.commit()

    return {"mensaje": "Pedido eliminado exitosamente."}  
