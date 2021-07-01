from fastapi import Depends, FastAPI

from routers.categoria_router import router as router_categoria
from routers.cliente_router import router as router_cliente
from routers.usuario_router import router as router_usuario
from routers.producto_router import router as router_producto
from routers.pedido_router import router as router_pedido
from routers.compra_router import router as router_compra

from fastapi.middleware.cors import CORSMiddleware

api = FastAPI()

api.include_router(router_categoria)
api.include_router(router_cliente)
api.include_router(router_usuario)
api.include_router(router_producto)
api.include_router(router_pedido)
api.include_router(router_compra)


origins = [
    "http://localhost:8080",
]

api.add_middleware(
    CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)