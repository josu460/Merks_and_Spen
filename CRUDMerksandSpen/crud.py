class CRUD:
    def __init__(self):
        self.__usuarios = []

    def crear_usuario(self, nombre, contraseña):
       if self.obtener_contraseña(nombre) is None:
           self.__usuarios.append({"nombre": nombre, "contraseña": contraseña})
           print("Usuario creado:", nombre, contraseña)  # print para verificar
           return True
       else:
           return False

    def borrar_usuario(self, nombre):
        for usuario in self.__usuarios:
            if usuario["nombre"] == nombre:
                self.__usuarios.remove(usuario)
                return True
        return False

    def consultar_usuarios(self):
        return [usuario["nombre"] for usuario in self.__usuarios]

    def modificar_usuario(self, nombre, nuevo_nombre, nueva_contraseña):
        for usuario in self.__usuarios:
            if usuario["nombre"] == nombre:
                usuario["nombre"] = nuevo_nombre
                usuario["contraseña"] = nueva_contraseña
                return True
        return False

    def obtener_contraseña(self, nombre):
        for usuario in self.__usuarios:
            if usuario["nombre"] == nombre:
                return usuario["contraseña"]
        return None

    
# #instancia de CRUD
# crud = CRUD()

# # # nuevo usuario
# crud.crear_usuario("almacen", "1234")
# crud.crear_usuario("ventas", "456")
# # # Consultar la contraseña 
# print(crud.obtener_contraseña("almacen"))
# print(crud.obtener_contraseña("ventas"))

