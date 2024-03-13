#CRUD para los articulos 

from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
# import sqlite3


#python image library
from PIL import Image, ImageTk

class Articulo: 
    #db_name
    
    
    def __init__(self, ventana_articulo):
        self.window = ventana_articulo
        self.window.title('Articulos')
        self.window.geometry("800x670") 
        self.window.resizable(0,0)
        self.window.config(bg = "white")
        
        
        titulo = Label(ventana_articulo,text="Articulos",fg="black",font=("Comic Sans",17, "bold"),pady = 10 ).pack()
        
        #aqui agrego mi imagen que quiero mostrar
        frame_img_articulo = LabelFrame(ventana_articulo)
        frame_img_articulo.config(bd=0)
        frame_img_articulo.pack()
        
       
        imagen_articulo = Image.open("C:\\Users\\josuu\\OneDrive\\Documentos\\POO\\Merks_and_Spen\\imagenes\\articulo.jpeg")


        nueva_img = imagen_articulo.resize((60,60))
        render = ImageTk.PhotoImage(nueva_img)
        label_image = Label(frame_img_articulo, image=render)
        label_image.image = render
        label_image.grid(row=0, column=1, padx=15, pady=5)

        
        
        #frame marco 
        
        marco= LabelFrame(ventana_articulo,text="Informacion del articulo", font=("Comic Sans", 10, "bold"),pady=5)
        marco.config(bd=2)
        marco.pack()
        
        #formulario
        
        Label_codigo = Label(marco, text="Codigo del articulo:", font=("Comic Sans", 10, "bold"))
        Label_codigo.grid(row=0, column=0, sticky='e', padx=5, pady=8)
        self.codigo = Entry(marco, width=25)
        self.codigo.focus()
        self.codigo.grid(row=0, column=1, padx=5, pady=8)

        label_nombre = Label(marco, text="Nombre del articulo:", font=("Comic Sans", 10, "bold"))
        label_nombre.grid(row=1, column=0, sticky='e', padx=5, pady=8)
        self.nombre = Entry(marco, width=25)
        self.nombre.grid(row=1, column=1, padx=5, pady=8)

        label_categoria = Label(marco, text="Categoria:", font=("Comic Sans", 10, "bold"))
        label_categoria.grid(row=2, column=0, sticky='e', padx=5, pady=8)
        self.combo_categoria = ttk.Combobox(marco, values=["Categoria 1", "Categoria 2", "Categoria 3"], width=22)
        self.combo_categoria.current(0)
        self.combo_categoria.grid(row=2, column=1, padx=5, pady=8)

        label_cantidad = Label(marco, text="Cantidad:", font=("Comic Sans", 10, "bold"))
        label_cantidad.grid(row=0, column=2, sticky='e', padx=5, pady=8)
        self.cantidad = Entry(marco, width=25)
        self.cantidad.grid(row=0, column=3, padx=5, pady=8)

        label_precio = Label(marco, text="Precio:", font=("Comic Sans", 10, "bold"))
        label_precio.grid(row=1, column=2, sticky='e', padx=5, pady=8)
        self.precio = Entry(marco, width=25)
        self.precio.grid(row=1, column=3, padx=5, pady=8)

        label_descripcion = Label(marco, text="Descripcion:", font=("Comic Sans", 10, "bold"))
        label_descripcion.grid(row=2, column=2, sticky='e', padx=5, pady=8)
        self.descripcion = Text(marco, width=25, height=5)
        self.descripcion.grid(row=2, column=3, padx=10, pady=8)
        
        
        #frame botones
        
        frame_botones = Frame(ventana_articulo)
        frame_botones.pack()
        
        #botones
        
        boton_agregar =Button(frame_botones, text="Agregar", height=2, width=10,bg="green" ,fg="white",font=("Comic Sans", 10, "bold")).grid(row=0, column=0,padx=5,pady=8)
        boton_editar =Button(frame_botones, text="Editar", height=2, width=10,bg="gray" ,fg="white",font=("Comic Sans", 10, "bold")).grid(row=0, column=1,padx=5,pady=8)
        boton_eliminar =Button(frame_botones, text="Eliminar", height=2, width=10,bg="red" ,fg="white",font=("Comic Sans", 10, "bold")).grid(row=0, column=2,padx=5,pady=8)
        
        #tabla para ver los artuiculos 
        
        self.tree = ttk.Treeview(height=13, columns=("columna1","columna2","columna3","columna4","columna5"))
        self.tree.heading("#0", text="Codigo", anchor=CENTER)
        self.tree.column("#0",width=90,minwidth=75, stretch=NO)
        
        self.tree.heading("columna1", text="Nombre", anchor=CENTER)
        self.tree.column("columna1",width=150,minwidth=75, stretch=NO)
        
        self.tree.heading("columna2", text="Categoria", anchor=CENTER)
        self.tree.column("columna2",width=150,minwidth=75, stretch=NO)
        
        self.tree.heading("columna3", text="Cantidad", anchor=CENTER)
        self.tree.column("columna3",width=150,minwidth=60, stretch=NO)
        
        self.tree.heading("columna4", text="Precio", anchor=CENTER)
        self.tree.column("columna4",width=150,minwidth=60, stretch=NO)
        
        self.tree.heading("columna5", text="Descripcion", anchor=CENTER)
        
        self.tree.pack()
        
        
        # self.Obtener_articulos()
        
        ventana_articulo.mainloop()
        
if __name__ == "__main__":
    ventana_principal = Tk()
    aplicacion = Articulo(ventana_principal)     

