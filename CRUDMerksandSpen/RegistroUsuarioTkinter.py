import tkinter as tk
from tkinter import messagebox
from crud import CRUD

class RegistroUsuarioTkinter:
    def __init__(self, root, crud):
        self.root = root
        self.root.title("Registro de Usuario")
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

        self.button_registrar = tk.Button(root, text="Registrar", command=self.registrar_usuario)
        self.button_registrar.pack()

    def registrar_usuario(self):
        nombre = self.entry_nombre.get()
        contraseña = self.entry_contraseña.get()
        
        if nombre and contraseña:
            if self.crud.crear_usuario(nombre, contraseña):
                messagebox.showinfo("Usuario Registrado", "Usuario registrado exitosamente")
                print("Usuario registrado:", nombre) #print verificar
            else:
                messagebox.showerror("Error", "El usuario ya existe")
        else:
            messagebox.showerror("Error", "Debe completar todos los campos")

if __name__ == "__main__":
    root = tk.Tk()
    crud = CRUD()
    app = RegistroUsuarioTkinter(root, crud)
    root.mainloop()
