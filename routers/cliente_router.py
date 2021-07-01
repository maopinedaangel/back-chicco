from typing import List

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from db.db_connection import get_db

from db.cliente_db import ClienteDB

from models.cliente_models import ClienteIn


router = APIRouter()


@router.get("/clientes")
async def get_clientes(db: Session = Depends(get_db)):
    clientes = db.query(ClienteDB).all()
    return clientes


@router.get("/cliente")
async def get_cliente(cc: int, db: Session = Depends(get_db)):
    mi_cliente = db.query(ClienteDB).get(cc)
    if mi_cliente == None:
        raise HTTPException(status_code=404, detail="No se encontró el cliente.")
    return mi_cliente


@router.post("/cliente/nuevo")
async def new_cliente(cliente_in: ClienteIn, db: Session = Depends(get_db)):
    new_cliente = ClienteDB(**cliente_in.dict())

    db.add(new_cliente)
    db.commit()
    db.refresh(new_cliente)

    return {"mensaje": "Cliente creado exitosamente."}
    #return new_cat    


@router.put("/cliente/edit")
async def edit_cliente(cliente_in: ClienteIn, db: Session = Depends(get_db)):
    cliente_in_db = db.query(ClienteDB).get(cliente_in.id)
    cliente_in_db.cedula = cliente_in.cedula       
    cliente_in_db.nombre = cliente_in.nombre
    cliente_in_db.apellido = cliente_in.apellido
    cliente_in_db.telefono = cliente_in.telefono
    cliente_in_db.puntos = cliente_in.puntos
             
    db.commit()
    db.refresh(cliente_in_db)

    return {"mensaje": "Cliente actualizado exitosamente."}  


@router.delete("/cliente/delete")
async def borrar_cliente(cc: int, db: Session = Depends(get_db)):
    db.query(ClienteDB).filter(ClienteDB.id==cc).delete()

    db.commit()

    return {"mensaje": "Cliente eliminado exitosamente."}  