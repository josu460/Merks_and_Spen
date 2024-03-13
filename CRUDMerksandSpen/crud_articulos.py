from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
from tkinter import filedialog

# para poder mostrar imagenes en la interfaz
from PIL import Image, ImageTk
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os

class Articulo:
    def __init__(self, ventana_articulo):
        self.articulos = []  # Lista para almacenar los artículos

        self.window = ventana_articulo
        self.window.title('Articulos')
        self.window.geometry("800x670") 
        self.window.resizable(0,0)
        self.window.config(bg="white")
        
        titulo = Label(ventana_articulo,text="Articulos",fg="black",font=("Comic Sans",17, "bold"),pady=10)
        titulo.pack()

        # Carga de imagen
        imagen_articulo = Image.open("C:\\Users\\josuu\\OneDrive\\Documentos\\POO\\Merks_and_Spen\\CRUDMerksandSpen\\imagenes\\online-shopping-mexico-800-3423d44e0.png")


        nueva_img = imagen_articulo.resize((60,60))
        render = ImageTk.PhotoImage(nueva_img)
        label_image = Label(ventana_articulo, image=render)
        label_image.image = render
        label_image.pack(pady=10)

        # Formulario
        marco = LabelFrame(ventana_articulo,text="Informacion del articulo", font=("Comic Sans", 10, "bold"),pady=5)
        marco.config(bd=2)
        marco.pack()

        Label(marco, text="Codigo del articulo:", font=("Comic Sans", 10, "bold")).grid(row=0, column=0, sticky='e', padx=5, pady=8)
        self.codigo = Entry(marco, width=25)
        self.codigo.focus()
        self.codigo.grid(row=0, column=1, padx=5, pady=8)

        Label(marco, text="Nombre del articulo:", font=("Comic Sans", 10, "bold")).grid(row=1, column=0, sticky='e', padx=5, pady=8)
        self.nombre = Entry(marco, width=25)
        self.nombre.grid(row=1, column=1, padx=5, pady=8)

        Label(marco, text="Departamento:", font=("Comic Sans", 10, "bold")).grid(row=2, column=0, sticky='e', padx=5, pady=8)
        self.combo_categoria = ttk.Combobox(marco, values=["Almacen", "Recursos Humanos", "Departamento 3"], width=22)
        self.combo_categoria.current(0)
        self.combo_categoria.grid(row=2, column=1, padx=5, pady=8)

        Label(marco, text="Cantidad:", font=("Comic Sans", 10, "bold")).grid(row=0, column=2, sticky='e', padx=5, pady=8)
        self.cantidad = Entry(marco, width=25)
        self.cantidad.grid(row=0, column=3, padx=5, pady=8)

        Label(marco, text="Precio:", font=("Comic Sans", 10, "bold")).grid(row=1, column=2, sticky='e', padx=5, pady=8)
        self.precio = Entry(marco, width=25)
        self.precio.grid(row=1, column=3, padx=5, pady=8)

        Label(marco, text="Descripcion:", font=("Comic Sans", 10, "bold")).grid(row=2, column=2, sticky='e', padx=5, pady=8)
        self.descripcion = Text(marco, width=25, height=5)
        self.descripcion.grid(row=2, column=3, padx=10, pady=8)

        # Botones
        frame_botones = Frame(ventana_articulo)
        frame_botones.pack()

        Button(frame_botones, text="Agregar", height=2, width=10, bg="green", fg="white", font=("Comic Sans", 10, "bold"), command=self.agregar_articulo).grid(row=0, column=0, padx=5, pady=8)
        Button(frame_botones, text="Editar", height=2, width=10, bg="gray", fg="white", font=("Comic Sans", 10, "bold"), command=self.editar_articulo).grid(row=0, column=1, padx=5, pady=8)
        Button(frame_botones, text="Eliminar", height=2, width=10, bg="red", fg="white", font=("Comic Sans", 10, "bold"), command=self.eliminar_articulo).grid(row=0, column=2, padx=5, pady=8)
        Button(frame_botones, text="Generar Ticket", height=2, width=15, bg="blue", fg="white", font=("Comic Sans", 10, "bold"), command=self.generar_ticket).grid(row=0, column=3, padx=5, pady=8)

        # Tabla para ver los artículos
        self.tree = ttk.Treeview(height=13, columns=("columna1", "columna2", "columna3", "columna4", "columna5"))
        self.tree.heading("#0", text="Codigo", anchor=CENTER)
        self.tree.column("#0", width=90, minwidth=75, stretch=NO)

        self.tree.heading("columna1", text="Nombre", anchor=CENTER)
        self.tree.column("columna1", width=150, minwidth=75, stretch=NO)

        self.tree.heading("columna2", text="Categoria", anchor=CENTER)
        self.tree.column("columna2", width=150, minwidth=75, stretch=NO)

        self.tree.heading("columna3", text="Cantidad", anchor=CENTER)
        self.tree.column("columna3", width=150, minwidth=60, stretch=NO)

        self.tree.heading("columna4", text="Precio", anchor=CENTER)
        self.tree.column("columna4", width=150, minwidth=60, stretch=NO)

        self.tree.heading("columna5", text="Descripcion", anchor=CENTER)

        self.tree.pack()

    def agregar_articulo(self):
        articulo = {
            "nombre": self.nombre.get(),
            "categoria": self.combo_categoria.get(),
            "cantidad": self.cantidad.get(),
            "precio": self.precio.get(),
            "descripcion": self.descripcion.get("1.0", END)
        }
        self.articulos.append(articulo)
        self.actualizar_tabla()

    def editar_articulo(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showerror("Error", "Por favor selecciona un artículo para editar.")
            return

        item_id = seleccion[0]
        articulo = self.tree.item(item_id)

        ventana_editar = Toplevel(self.window)
        ventana_editar.title("Editar Artículo")

        Label(ventana_editar, text="Nombre:", font=("Comic Sans", 10, "bold")).grid(row=0, column=0, sticky="e", padx=5, pady=5)
        nombre_edit = Entry(ventana_editar)
        nombre_edit.insert(END, articulo["values"][0])  # Nombre del artículo
        nombre_edit.grid(row=0, column=1, padx=5, pady=5)

        Label(ventana_editar, text="Departamento:", font=("Comic Sans", 10, "bold")).grid(row=1, column=0, sticky="e", padx=5, pady=5)
        categoria_edit = Entry(ventana_editar)
        categoria_edit.insert(END, articulo["values"][1])  # Categoria del artículo
        categoria_edit.grid(row=1, column=1, padx=5, pady=5)
        
        Label(ventana_editar, text="Cantidad:", font=("Comic Sans", 10, "bold")).grid(row=2, column=0, sticky="e", padx=5, pady=5)
        cantidad_edit = Entry(ventana_editar)
        cantidad_edit.insert(END, articulo["values"][2])  # Categoria cantidad
        cantidad_edit.grid(row=2, column=1, padx=5, pady=5)
        
        Label(ventana_editar, text="Precio:", font=("Comic Sans", 10, "bold")).grid(row=3, column=0, sticky="e", padx=5, pady=5)
        precio_edit = Entry(ventana_editar)
        precio_edit.insert(END, articulo["values"][3])  # Categoria precio
        precio_edit.grid(row=3, column=1, padx=5, pady=5)
        
        Label(ventana_editar, text="Descripcion:", font=("Comic Sans", 10, "bold")).grid(row=4, column=0, sticky="e", padx=5, pady=5)
        descripcion_edit = Text(ventana_editar, width=40, height=10)
        descripcion_edit.insert(END, articulo["values"][4])  # Descripcion del artículo
        descripcion_edit.grid(row=4, column=1, padx=5, pady=5)

        def guardar_cambios():
            self.tree.item(item_id, values=(nombre_edit.get(), categoria_edit.get(), cantidad_edit.get(), precio_edit.get(), descripcion_edit.get("1.0", END)))
            ventana_editar.destroy()

        Button(ventana_editar, text="Guardar Cambios", command=guardar_cambios).grid(row=5, column=0, columnspan=2, pady=10)


    def eliminar_articulo(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showerror("ERROR", "Por favor selecciona un artículo para eliminar.")
            return

        item_id = seleccion[0]
        nombre = self.tree.item(item_id)['values'][0]
        respuesta = messagebox.askquestion("ADVERTENCIA", f"¿Seguro que desea eliminar el artículo: {nombre}?")
        if respuesta == 'yes':
            self.tree.delete(item_id)
            messagebox.showinfo('EXITO', f'Artículo eliminado: {nombre}')
        else:
            messagebox.showerror('ERROR', f'Error al eliminar el artículo: {nombre}')


    def generar_ticket(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showerror("Error", "Por favor selecciona al menos un artículo para generar el ticket.")
            return

        # Crear el documento PDF
        c = canvas.Canvas("ticket.pdf", pagesize=letter)
        
        # Escribir el contenido del ticket
        c.drawString(100, 750, "Ticket de Compra")
        c.drawString(100, 730, "--------------------------")
        y = 700
        for i, item_id in enumerate(seleccion):
            articulo = self.tree.item(item_id)['values']
            c.drawString(100, y, f"Artículo {i + 1}: {articulo[0]} - ${articulo[3]} - Cantidad: {articulo[2]} - Categoria: {articulo[1]} ")
            y -= 20
        
       
        c.save()
        messagebox.showinfo("Ticket generado", "Se ha generado el ticket correctamente como 'ticket.pdf'")
        self.abrir_pdf()

    def abrir_pdf(self):
        filepath = os.path.abspath("ticket.pdf")
        os.system(f'start {filepath}')

    def actualizar_tabla(self):
        self.tree.delete(*self.tree.get_children())
        for i, articulo in enumerate(self.articulos):
            self.tree.insert("", END, text=str(i), values=(articulo["nombre"], articulo["categoria"], articulo["cantidad"], articulo["precio"], articulo["descripcion"]))

if __name__ == "__main__":
    ventana_principal = Tk()
    aplicacion = Articulo(ventana_principal)
    ventana_principal.mainloop()
