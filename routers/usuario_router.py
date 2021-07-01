from typing import List

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from db.db_connection import get_db

from db.usuario_db import UsuarioDB

from models.usuario_models import UsuarioIn


router = APIRouter()


@router.get("/usuarios")
async def get_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(UsuarioDB).all()
    return usuarios


@router.get("/usuario")
async def get_usuario(cc: int, db: Session = Depends(get_db)):
    mi_usuario = db.query(UsuarioDB).get(cc)
    if mi_usuario == None:
        raise HTTPException(status_code=404, detail="No se encontró el usuario.")
    return mi_usuario


@router.post("/usuario/nuevo")
async def new_usuario(usuario_in: UsuarioIn, db: Session = Depends(get_db)):
    new_usuario = UsuarioDB(**usuario_in.dict())

    db.add(new_usuario)
    db.commit()
    db.refresh(new_usuario)

    return {"mensaje": "Usuario creado exitosamente."} 


@router.put("/usuario/edit")
async def edit_usuario(usuario_in: UsuarioIn, db: Session = Depends(get_db)):
    usuario_in_db = db.query(UsuarioDB).get(usuario_in.id)
    usuario_in_db.cedula = usuario_in.cedula 
    usuario_in_db.password = usuario_in.password           
    usuario_in_db.nombre = usuario_in.nombre
    usuario_in_db.apellido = usuario_in.apellido
    usuario_in_db.telefono = usuario_in.telefono
             
    db.commit()
    db.refresh(usuario_in_db)

    return {"mensaje": "Usuario actualizado exitosamente."}  


@router.delete("/usuario/delete")
async def borrar_usuario(cc: int, db: Session = Depends(get_db)):
    db.query(UsuarioDB).filter(UsuarioDB.id==cc).delete()

    db.commit()

    return {"mensaje": "Usuario eliminado exitosamente."}  