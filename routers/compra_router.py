from typing import List

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from db.db_connection import get_db

from db.compra_db import CompraDB
from db.pedido_db import PedidoDB
from db.producto_db import ProductoDB

from models.compra_models import CompraIn
#from models.pedido_models import PedidoIn, PedidoOut
#from models.producto_models import ProductoIn, ProductoOut

router = APIRouter()


@router.get("/compras")
async def get_compras(db: Session = Depends(get_db)):
    compras = db.query(CompraDB).all()
    return compras


@router.get("/ccompra")
async def get_compra(id: int, db: Session = Depends(get_db)):
    mi_compra = db.query(CompraDB).get(id)
    if mi_compra == None:
        raise HTTPException(status_code=404, detail="No se encontró la categoría.")
    return mi_compra


@router.post("/compra/nueva")
async def new_compra(compra_in: CompraIn, db: Session = Depends(get_db)):
    new_compra = CompraDB(**compra_in.dict())

    db.add(new_compra)
    db.commit()
    db.refresh(new_compra)

    return {"mensaje": "Compra creada exitosamente."}
    #return new_cat    


@router.delete("/compra/delete")
async def borrar_compra (id: int, db: Session = Depends(get_db)):
    db.query(CompraDB).filter(CompraDB.id==id).delete()

    db.commit()

    return {"mensaje": "Compra eliminada exitosamente."}