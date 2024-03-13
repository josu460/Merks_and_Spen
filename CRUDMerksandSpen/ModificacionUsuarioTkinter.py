import tkinter as tk
from tkinter import messagebox, simpledialog
from crud import CRUD

class ModificacionUsuarioTkinter:
    def __init__(self, root, crud):
        self.root = root
        self.root.title("Modificación de Usuario")
        self.root.geometry("300x250")

        self.crud = crud

        self.label_nombre = tk.Label(root, text="Nombre del departamento:")
        self.label_nombre.pack()

        self.entry_nombre = tk.Entry(root)
        self.entry_nombre.pack()

        self.label_contraseña = tk.Label(root, text="Contraseña:")
        self.label_contraseña.pack()

        self.entry_contraseña = tk.Entry(root, show="*")
        self.entry_contraseña.pack()

        self.button_validar = tk.Button(root, text="Validar", command=self.validar_usuario)
        self.button_validar.pack()

    def validar_usuario(self):
        nombre = self.entry_nombre.get()
        contraseña = self.entry_contraseña.get()

        stored_password = self.crud.obtener_contraseña(nombre)
        if stored_password is not None and stored_password == contraseña:
            self.mostrar_modificaciones()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")

    def mostrar_modificaciones(self):
        self.label_modificar = tk.Label(self.root, text="Seleccione qué desea modificar:")
        self.label_modificar.pack()

        self.var_modificar_nombre = tk.IntVar()
        self.check_modificar_nombre = tk.Checkbutton(self.root, text="Modificar Nombre", variable=self.var_modificar_nombre)
        self.check_modificar_nombre.pack()

        self.var_modificar_contraseña = tk.IntVar()
        self.check_modificar_contraseña = tk.Checkbutton(self.root, text="Modificar Contraseña", variable=self.var_modificar_contraseña)
        self.check_modificar_contraseña.pack()

        self.button_modificar = tk.Button(self.root, text="Modificar", command=self.realizar_modificacion)
        self.button_modificar.pack()

    def realizar_modificacion(self):
        nombre = self.entry_nombre.get()
        antiguo_nombre = nombre
        contraseña = self.entry_contraseña.get()
        nueva_nombre = ""
        nueva_contraseña = ""

        if self.var_modificar_nombre.get() == 1:
            nueva_nombre = simpledialog.askstring("Modificar Nombre", "Ingrese el nuevo nombre:")
            if nueva_nombre is None:
                return
            self.crud.modificar_usuario(nombre, nueva_nombre, contraseña)
            messagebox.showinfo("Usuario Modificado", f"Nombre de usuario '{antiguo_nombre}' modificado exitosamente\n"
                                                       f"Nombre anterior: {antiguo_nombre}\n"
                                                       f"Nuevo nombre: {nueva_nombre}")
        elif self.var_modificar_contraseña.get() == 1:
            nueva_contraseña = simpledialog.askstring("Modificar Contraseña", "Ingrese la nueva contraseña:")
            if nueva_contraseña is None:
                return
            self.crud.modificar_usuario(nombre, nombre, nueva_contraseña)
            messagebox.showinfo("Contraseña Modificada", f"Contraseña de usuario '{antiguo_nombre}' modificada exitosamente\n"
                                                          f"Contraseña anterior: {contraseña}\n"
                                                          f"Nueva contraseña: {nueva_contraseña}")
        else:
            messagebox.showerror("Error", "Seleccione qué desea modificar")

if __name__ == "__main__":
    root = tk.Tk()
    crud = CRUD()
    app = ModificacionUsuarioTkinter(root, crud)
    root.mainloop()