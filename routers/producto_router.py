from typing import List

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from db.db_connection import get_db

from db.categoria_db import CategoriaDB
from db.producto_db import ProductoDB

from models.categoria_models import CategoriaIn, CategoriaUpdate
from models.producto_models import ProductoIn, ProductoUpdate

router = APIRouter()


@router.get("/productos")
async def get_productos(db: Session = Depends(get_db)):
    productos = db.query(ProductoDB).all()
    return productos


@router.get("/producto")
async def get_producto(prod: int, db: Session = Depends(get_db)):
    mi_producto = db.query(ProductoDB).get(prod)
    if mi_producto == None:
        raise HTTPException(status_code=404, detail="No se encontró el producto.")
    return mi_producto


@router.get("/cat/productos")
async def filtrar_producto(cat: int, db: Session = Depends(get_db)):
    filtro_productos = db.query(ProductoDB).filter(ProductoDB.id_categoria==cat).all()
    if filtro_productos == None:
        raise HTTPException(status_code=404, detail="No se encontraron resultados.")
    return filtro_productos

@router.post("/producto/nuevo")
async def new_producto(producto_in: ProductoIn, db: Session = Depends(get_db)):
    new_prod = ProductoDB(**producto_in.dict())

    db.add(new_prod)
    db.commit()
    db.refresh(new_prod)

    return {"mensaje": "Producto creado exitosamente."}
    #return new_cat    


@router.put("/producto/edit")
async def edit_producto(producto_in: ProductoUpdate, db: Session = Depends(get_db)):
    producto_in_db = db.query(ProductoDB).get(producto_in.id)
    producto_in_db.nombre = producto_in.nombre
    producto_in_db.unidad = producto_in.unidad
    producto_in_db.precio = producto_in.precio        
    producto_in_db.imagen = producto_in.imagen
    producto_in_db.descripcion = producto_in.descripcion
    producto_in_db.stock = producto_in.stock
    producto_in_db.id_categoria = producto_in.id_categoria                    

    db.commit()
    db.refresh(producto_in_db)

    return {"mensaje": "Producto actualizado exitosamente."}  
    #return categoria_in_db  


@router.delete("/producto/delete")
async def borrar_producto(prod: int, db: Session = Depends(get_db)):
    db.query(ProductoDB).filter(ProductoDB.id==prod).delete()

    db.commit()

    return {"mensaje": "Producto eliminado exitosamente."}  