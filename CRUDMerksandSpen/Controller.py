import tkinter as tk
from MainMenuTkinter import MainMenuTkinter
from LoginTkinter import LoginTkinter
from crud_articulos import Articulo

class Controller:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sistema de Gestión de Artículos")
        self.root.geometry("800x600")

        self.crud = None

    def show_main_menu(self):
        self.main_menu = MainMenuTkinter(self.root)
        self.main_menu.root.mainloop()  # Mostrar el menú principal

    def show_login(self):
        self.login = LoginTkinter(self.root, self)
        self.login.root.mainloop()  # Mostrar la ventana de inicio de sesión

    def show_articulos(self):
        self.articulos = Articulo(self.root)
        self.login.root.destroy()  # Cerrar la ventana de inicio de sesión
        self.articulos.root.mainloop()  # Mostrar la interfaz de CRUD de artículos

    def validate_login(self, username, password):
        # Aquí deberías realizar la validación de las credenciales
        if username == "admin" and password == "admin":
            self.show_articulos()  # Mostrar la interfaz de CRUD de artículos
        else:
            tk.messagebox.showerror("Error", "Credenciales incorrectas")

if __name__ == "__main__":
    controller = Controller()
    controller.show_main_menu()  # Mostrar el menú principal al inicio
    controller.root.mainloop()
