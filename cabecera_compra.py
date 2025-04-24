from typing import List
from proveedor import Proveedor
from detalle_compra import DetalleCompra

class CabeceraCompra:
    def __init__(self, id: int, proveedor: "Proveedor", fecha_compra: str, numero_factura: str)-> None:
        self.id: int = id
        self.proveedor: Proveedor = proveedor
        self.fecha_compra: str = fecha_compra
        self.numero_factura: str = numero_factura
        self.detalles: List[DetalleCompra] = []
        self.subtotal: float = 0.0
        self.iva: float = 0.0
        self.total: float = 0.0
    def agregar_detalle(self, detalle: "DetalleCompra")-> None:
        self.detalles.append(detalle)
        self.calcular_total()
    def calcular_total(self)-> None:
        self.subtotal = sum(detalle.precio_unitario * detalle.cantidad for detalle in self.detalles)
        self.iva = self.subtotal * 0.15
        self.total = self.subtotal + self.iva