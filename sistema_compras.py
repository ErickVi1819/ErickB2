from typing import List
from proveedor import Proveedor
from producto import Producto
from detalle_compra import DetalleCompra
from cabecera_compra import CabeceraCompra
from typing import Optional
class SistemaCompras:
    def __init__(self)-> None:
        self.proveedores: List[Proveedor] = []
        self.productos: List[Producto] = []
        self.compras: List[CabeceraCompra] = []
        #CRUD PARA PROVEEDORES
    def registrar_proveedor(self, id: int, nombre: str, ruc: str, direccion: str, telefono: str, correo: str)-> Proveedor:
        proveedor = Proveedor(id, nombre, ruc, direccion, telefono, correo)
        self.proveedores.append(proveedor)
        return proveedor
    def obtener_proveedor(self, id: int)-> Optional[Proveedor]:
        for proveedor in self.proveedores:
            if proveedor.id == id and proveedor.activo:
                return proveedor
        return None
    #CRUD PARA PRODUCTOS
    def registrar_productos(self, id: int, nombre: str, descripcion: str, precio_unitario: float, stock_actual: int)-> Producto:
        producto = Producto(id, nombre, descripcion, precio_unitario, stock_actual)
        self.productos.append(producto)
        return producto
    def obtener_producto(self, id: int)-> Optional[Producto]:
        for producto in self.productos:
            if producto.id == id and producto.activo:
                return producto
        return None
    #REGISTRAR UNA NUEVA COMPRA
    def registrar_compra(self, id: int, proveedor_id: int, fecha_compra: str, numero_factura: str)-> CabeceraCompra:
        proveedor = self.obtener_proveedor(proveedor_id)
        if not proveedor:
            raise ValueError("El proveedor no existe o está inactivo")
        compra = CabeceraCompra(id, proveedor, fecha_compra, numero_factura)
        self.compras.append(compra)
        return compra
    #AGREGAR DETALLE A UNA COMPRA
    def agregar_detalle_compra(self, compra_id: int, producto_id: int, cantidad: int, precio_unitario: float)-> None:
        compra = None
        for c in self.compras:
            if c.id == compra_id:
                compra = c
                break
        if not compra:
            raise ValueError("La compra no existe")
        
        producto = self.obtener_producto(producto_id)
        if not producto:
            raise ValueError("El producto no existe o está inactivo")
        
        detalle_id = len(compra.detalles) + 1
        detalle = DetalleCompra(detalle_id, producto, cantidad, precio_unitario)
        compra.agregar_detalle(detalle)
    #MOSTRAR COMPRAS
    def mostrar_compras(self)-> None:
        for compra in self.compras:
            print(f"Compra ID: {compra.id}")
            print(f"Proveedor: {compra.proveedor.nombre}")
            print(f"Fecha de Compra: {compra.fecha_compra}")
            print("Detalles:")
            for detalle in compra.detalles:
                print(f"Producto: {detalle.producto.nombre}")
                print(f"Cantidad: {detalle.cantidad}")
                print(f"Precio Unitario: {detalle.precio_unitario}")
            print(f"Subtotal: {compra.subtotal}, IVA: {compra.iva}, Total: {compra.total}")