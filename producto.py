class Producto:
    def __init__(self, id: int, nombre: str, descripcion: str, precio_unitario: float, stock_actual: int, activo: bool = True)-> None:
        self.id: int = id
        self.nombre: str = nombre
        self.descripcion: str = descripcion
        self.precio_unitario: float = precio_unitario
        self.stock_actual: int = stock_actual
        self.activo: bool = activo
        