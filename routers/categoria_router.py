from typing import List, Dict

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from db.db_connection import get_db

from db.categoria_db import CategoriaDB

#from models.categoria_models import CategoriaIn, CategoriaOut
from models.categoria_models import CategoriaIn, CategoriaUpdate

router = APIRouter()


@router.get("/categorias")
async def get_categorias(db: Session = Depends(get_db)):
    categorias = db.query(CategoriaDB).all()
    return categorias


@router.get("/categoria")
async def get_categoria(cat: int, db: Session = Depends(get_db)):
    mi_categoria = db.query(CategoriaDB).get(cat)
    if mi_categoria == None:
        raise HTTPException(status_code=404, detail="No se encontró la categoría.")
    return mi_categoria


@router.post("/categoria/nueva")
async def new_categoria(categoria_in: CategoriaIn, db: Session = Depends(get_db)):
    new_cat = CategoriaDB(**categoria_in.dict())

    db.add(new_cat)
    db.commit()
    db.refresh(new_cat)

    return {"mensaje": "Categoría creada exitosamente."}
    #return new_cat    


@router.put("/categoria/edit")
async def edit_categoria(categoria_in: CategoriaUpdate, db: Session = Depends(get_db)):
    categoria_in_db = db.query(CategoriaDB).get(categoria_in.id)
    #categoria_in_db = CategoriaDB(**categoria_in.dict())
    categoria_in_db.nombre = categoria_in.nombre
    categoria_in_db.imagen = categoria_in.imagen        

    db.commit()
    db.refresh(categoria_in_db)

    return {"mensaje": "Categoría actualizada exitosamente."}  
    #return categoria_in_db  


@router.delete("/categoria/delete")
async def borrar_categoria(cat: int, db: Session = Depends(get_db)):
    db.query(CategoriaDB).filter(CategoriaDB.id==cat).delete()

    db.commit()

    return {"mensaje": "Categoría eliminada exitosamente."}  
