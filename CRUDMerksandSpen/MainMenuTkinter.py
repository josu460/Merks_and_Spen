import tkinter as tk
from tkinter import messagebox
from RegistroUsuarioTkinter import RegistroUsuarioTkinter
from ModificacionUsuarioTkinter import ModificacionUsuarioTkinter
from LoginTkinter import LoginTkinter
from crud import CRUD

class MainMenuTkinter:
    def __init__(self, root):
        self.root = root
        self.root.title("Menú Principal")
        self.root.geometry("300x300")

        self.crud = CRUD()

        self.button_registro = tk.Button(root, text="Registrar Usuario", command=self.abrir_registro_usuario)
        self.button_registro.pack()

        self.button_modificacion = tk.Button(root, text="Modificar Usuario", command=self.abrir_modificacion_usuario)
        self.button_modificacion.pack()

        self.button_login = tk.Button(root, text="Login", command=self.abrir_login)
        self.button_login.pack()

        self.button_visualizar = tk.Button(root, text="Visualizar Departamentos", command=self.visualizar_departamentos)
        self.button_visualizar.pack()

        self.button_borrar = tk.Button(root, text="Borrar Usuario", command=self.borrar_usuario)
        self.button_borrar.pack()

    def abrir_registro_usuario(self):
        registro_root = tk.Toplevel(self.root)
        app = RegistroUsuarioTkinter(registro_root, self.crud)

    def abrir_modificacion_usuario(self):
        modificacion_root = tk.Toplevel(self.root)
        app = ModificacionUsuarioTkinter(modificacion_root, self.crud)

    def abrir_login(self):
        login_root = tk.Toplevel(self.root)
        app = LoginTkinter(login_root, self.crud)

    def visualizar_departamentos(self):
        departamentos = self.crud.consultar_usuarios()
        departamentos_str = "\n".join(departamentos)
        messagebox.showinfo("Departamentos Registrados", f"Departamentos Registrados:\n{departamentos_str}")

    def borrar_usuario(self):
        nombre = tk.simpledialog.askstring("Borrar Usuario", "Ingrese el nombre del departamento a borrar:")
        if nombre is not None:
            if self.crud.borrar_usuario(nombre):
                messagebox.showinfo("Usuario Borrado", f"El usuario '{nombre}' ha sido borrado exitosamente.")
            else:
                messagebox.showerror("Error", f"No se encontró el usuario '{nombre}'.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MainMenuTkinter(root)
    root.mainloop()
