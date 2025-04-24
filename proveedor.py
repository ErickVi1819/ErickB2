class Proveedor:
    def __init__(self, id: int, nombre: str, ruc: str, direccion:str, telefono:str, correo: str, activo: bool = True)-> None:
        self.id: int = id
        self.nombre: str = nombre
        self.ruc: str = ruc
        self.direccion: str = direccion
        self.telefono: str = telefono
        self.correo: str = correo
        self.activo: bool = activo