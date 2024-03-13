import tkinter as tk
from tkinter import messagebox
from crud_articulos import Articulo  # Importa la clase Articulo desde el archivo crud_articulos

class LoginTkinter:
    def __init__(self, root, crud):
        self.root = root
        self.crud = crud

        self.root.title("Login")
        self.root.geometry("300x150")

        self.label_nombre = tk.Label(root, text="Nombre del departamento:")
        self.label_nombre.pack()

        self.entry_nombre = tk.Entry(root)
        self.entry_nombre.pack()

        self.label_contraseña = tk.Label(root, text="Contraseña:")
        self.label_contraseña.pack()

        self.entry_contraseña = tk.Entry(root, show="*")
        self.entry_contraseña.pack()

        self.button_login = tk.Button(root, text="Login", command=self.validar_login)
        self.button_login.pack()

    def validar_login(self):
        username = self.entry_nombre.get()
        password = self.entry_contraseña.get()

        if username == "admin" and password == "admin":
            messagebox.showinfo("Bienvenido", f"Bienvenido Administrador de: {username}")
            self.abrir_crud_articulos()  # Llama a la función para abrir el CRUD de artículos
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")

    def abrir_crud_articulos(self):
        crud_root = tk.Toplevel(self.root)  # Crea una nueva ventana para el CRUD de artículos
        app = Articulo(crud_root)  # Inicia la aplicación del CRUD de artículos

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginTkinter(root, None)
    root.mainloop()
