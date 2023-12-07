from tkinter import Canvas, PhotoImage, Button, Entry, StringVar, ttk, Toplevel
from tkinter.ttk import Combobox
from tkinter import simpledialog
from pathlib import Path
import login, inventario, cliente, facturacion
import conexion


class MyPanel(Canvas):
    def __init__(self, master, agencia_id):
        super().__init__(
            master,
            bg="#252346",
            height=720,
            width=1080,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.agencia_id = agencia_id
        OUTPUT_PATH = Path(__file__).parent
        self.assets_path = OUTPUT_PATH / Path(r"C:\Users\favio\Downloads\prueba\build\assets\frame4")
        self.create_widgets()

    def create_widgets(self):
        self.load_images()

        self.create_image(540.0,40.0,self.image_1)
        self.create_image(50.0,400.0,self.image_2)
        self.create_image(265.0,40.0,self.image_3)
        self.create_image(128.0,40.0,self.image_4)
        self.create_button(5.0,630.0,90,90,self.button_image_1, self.button_1_click)
        self.create_button(5.0,95.0,90,90,self.button_image_2, self.button_2_click)
        self.create_button(5.0,221.0,90,90,self.button_image_3, self.button_3_click)
        self.create_button(5.0,337.0,90,90,self.button_image_4, self.button_4_click)
        self.create_button(5.0,463.0,90,90,self.button_image_5, self.button_5_click)
        self.create_entry()
        self.create_text()
        self.create_button(890.0,540.0,168,48,self.button_image_6, self.button_6_click)
        self.create_button(890.0,449.0,168,48,self.button_image_7, self.button_7_click)
        self.create_button(873.0,161.0,168,48,self.button_image_8, self.button_8_click)
        self.create_image(489.0,449.0,self.image_5)
        self.create_table()

    def load_images(self):
        self.image_1 = self.load_image("image_1.png")
        self.image_2 = self.load_image("image_2.png")
        self.image_3 = self.load_image("image_3.png")
        self.image_4 = self.load_image("image_4.png")
        self.image_5 = self.load_image("image_5.png")
        self.button_image_1 = self.load_image("button_1.png")
        self.button_image_2 = self.load_image("button_2.png")
        self.button_image_3 = self.load_image("button_3.png")
        self.button_image_4 = self.load_image("button_4.png")
        self.button_image_5 = self.load_image("button_5.png")
        self.button_image_6 = self.load_image("button_6.png")
        self.button_image_7 = self.load_image("button_7.png")
        self.button_image_8 = self.load_image("button_8.png")
        self.entry_1 = self.load_image("entry_1.png")
        self.entry_2 = self.load_image("entry_2.png")

    def create_button(self,x,y,width,height,image,command):
        return Button(
            self,
            image=image,
            borderwidth=0,
            highlightthickness=0,
            command= command,
            relief="flat"
        ).place(
            x=x,
            y=y,
            width=width,
            height=height
        )
    
    def create_entry(self):

        combobox_style = ttk.Style()
        combobox_style.configure('TCombobox', foreground='#000716', background='#D9D9D9', borderwidth=0, relief="flat")
        
        #combobox para la agencia
        conexion.cur.execute(("Select * from get_clientes_por_agencia("+str(self.agencia_id)+");"))
        self.options_cliente = [str(row[0]) for row in conexion.cur.fetchall()]
        self.cliente_var = StringVar()
        self.box_cliente = Combobox(self, values=self.options_cliente, textvariable=self.cliente_var, style='TCombobox')
        self.box_cliente.place(x=322.0, y=120.0, width=716.0, height=33.0)


        self.lista= ["cotizaciones", "facturas"]
        self.lista_var = StringVar()
        self.box_lista = Combobox(self, values=self.lista, textvariable=self.lista_var, style='TCombobox')
        self.box_lista.place(x=611.0, y=167.0, width=212.0, height=33.0)

        self.box_cliente.bind("<KeyRelease>", self.get_cliente)
        

    def create_text(self):
        super().create_text(
        129.0,
        115.0,
        anchor="nw",
        text="Cliente",
        fill="#FFFFFF",
        font=("Inter Bold", 40 * -1)
        )
    
    def create_table(self):
        self.productos = ttk.Treeview(self, columns=("cliente", "fecha","total"))
        
        # Define column headings
        self.productos.heading("#0", text="Codigo")
        self.productos.heading("#1", text="cliente")
        self.productos.heading("#2", text="fecha")
        self.productos.heading("#3", text="total")  

        # Configurar columnas
        self.productos.column("#0", width=100, anchor="center")
        self.productos.column("#1", width=150, anchor="center")
        self.productos.column("#2", width=200, anchor="center")
        self.productos.column("#3", width=100, anchor="center")

        self.productos.place(x=140.0, y=240.0, width=700, height=400)

    #Se definen las acciones de botones

    def button_1_click(self):
        self.destroy()
        panel = login.MyPanel(self.master)
        panel.pack(expand=True, fill="both")
    
    def button_2_click(self):
        self.destroy()
        panel = inventario.MyPanel(self.master, self.agencia_id)
        panel.pack(expand=True, fill="both")

    def button_3_click(self):
        self.destroy()
        panel = facturacion.MyPanel(self.master, self.agencia_id)
        panel.pack(expand=True, fill="both")

    def button_4_click(self):
        pass

    def button_5_click(self):
        self.destroy()
        panel = cliente.MyPanel(self.master, self.agencia_id)
        panel.pack(expand=True, fill="both")

    def button_6_click(self):
        print("button_6 clicked")

    def button_7_click(self):
        print("button_7 clicked")

    def button_8_click(self):
        self.get_factura_cotizacion()

    def load_image(self, filename):
        return PhotoImage(file=self.assets_path / filename)
    
    def create_image(self, x, y, image):
        return super().create_image(x, y, image=image)
    
    def get_cliente(self,event=None):
        conexion.cur.execute(("Select * from get_clientes_por_agencia("+str(self.agencia_id)+") where cliente_info iLIKE '%"+self.cliente_var.get()+"%';"))
        self.options_cliente = [str(row[0]) for row in conexion.cur.fetchall()]
        print(self.options_cliente)
        self.box_cliente["values"] = self.options_cliente


    def get_factura_cotizacion(self):
        self.cliente_id = int(self.box_cliente.get().split(" - ")[0])
        if self.box_lista.get() == "cotizaciones":
            conexion.cur.execute("SELECT * from obtener_cotizaciones("+str(self.cliente_id)+");")
            # Limpiar la tabla
            self.productos.delete(*self.productos.get_children())
            # Insertar datos
            for row in conexion.cur.fetchall():
                self.productos.insert("", "end", text=row[0], values=(row[1], row[2], row[3]))

        elif self.box_lista.get() == "facturas":
            conexion.cur.execute("SELECT * from obtener_facturas("+str(self.cliente_id)+");")
            # Limpiar la tabla
            self.productos.delete(*self.productos.get_children())
            # Insertar datos
            for row in conexion.cur.fetchall():
                self.productos.insert("", "end", text=row[0], values=(row[1], row[2], row[3]))        
        else: 
            pass