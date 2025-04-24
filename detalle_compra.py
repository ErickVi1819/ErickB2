from producto import Producto
class DetalleCompra:
    def __init__(self, id: int, producto: 'Producto', cantidad: int, precio_unitario: float)-> None:
        self.id: int = id
        self.producto: Producto = producto
        self.cantidad: int = cantidad
        self.precio_unitario: float = precio_unitario