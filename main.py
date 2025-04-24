# main.py
from sistema_compras import SistemaCompras

# Crear una instancia del sistema de compras
sistema = SistemaCompras()

# Registrar un proveedor
proveedor = sistema.registrar_proveedor(1, "Proveedor A", "123456789", "Dirección 1", "0991234567", "proveedor@correo.com")

# Registrar productos
producto1 = sistema.registrar_productos(1, "Producto 1", "Descripción 1", 10.0, 100)
producto2 = sistema.registrar_productos(2, "Producto 2", "Descripción 2", 20.0, 50)

# Registrar una compra
compra = sistema.registrar_compra(1, 1, "2025-04-24", "FACT001")

# Agregar detalles a la compra
sistema.agregar_detalle_compra(1, 1, 5, 10.0)  # 5 unidades del Producto 1
sistema.agregar_detalle_compra(1, 2, 3, 20.0)  # 3 unidades del Producto 2

# Mostrar las compras
sistema.mostrar_compras()