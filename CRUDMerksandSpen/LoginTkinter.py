import tkinter as tk
from tkinter import messagebox
from crud import CRUD

class LoginTkinter:
    def __init__(self, root, crud):
        self.root = root
        self.root.title("Login")
        self.root.geometry("300x150")

        self.crud = crud

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
        nombre = self.entry_nombre.get()
        contraseña = self.entry_contraseña.get()

        stored_password = self.crud.obtener_contraseña(nombre)
        if stored_password is not None and stored_password == contraseña:
            messagebox.showinfo("Bienvenido", f"Bienvenido Administrador de: {nombre}")
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")

if __name__ == "__main__":
    root = tk.Tk()
    crud = CRUD()
    app = LoginTkinter(root, crud)
    root.mainloop()
