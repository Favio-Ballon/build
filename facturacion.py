from tkinter import Canvas, PhotoImage, Button, Entry, StringVar, ttk
from tkinter.ttk import Combobox
from pathlib import Path
import login, inventario, cotizaciones, cliente


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
        self.assets_path = OUTPUT_PATH / Path(r"C:\Users\favio\Downloads\prueba\build\assets\frame2")
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
        self.create_text_1()
        self.create_button(890.0,202.0,168,48,self.button_image_6, self.button_6_click)
        self.create_button(890.0,621.0,168,48,self.button_image_7, self.button_7_click)
        self.create_button(890.0,548.0,168,48,self.button_image_8, self.button_8_click)
        self.create_image(489.0,449.0,self.image_5)
        self.create_image(974.0,393.0,self.image_6)
        self.create_text_2()
        self.create_table()

    def load_images(self):
        self.image_1 = self.load_image("image_1.png")
        self.image_2 = self.load_image("image_2.png")
        self.image_3 = self.load_image("image_3.png")
        self.image_4 = self.load_image("image_4.png")
        self.image_5 = self.load_image("image_5.png")
        self.image_6 = self.load_image("image_6.png")
        self.button_image_1 = self.load_image("button_1.png")
        self.button_image_2 = self.load_image("button_2.png")
        self.button_image_3 = self.load_image("button_3.png")
        self.button_image_4 = self.load_image("button_4.png")
        self.button_image_5 = self.load_image("button_5.png")
        self.button_image_6 = self.load_image("button_6.png")
        self.button_image_7 = self.load_image("button_7.png")
        self.button_image_8 = self.load_image("button_8.png")
        self.entry_image_1 = self.load_image("entry_1.png")
        self.entry_image_2 = self.load_image("entry_2.png")

    def load_image(self, filename):
        return PhotoImage(file=self.assets_path / filename)

    def create_image(self, x, y, image):
        return super().create_image(x, y, image=image)
    
    def create_text_1(self):
        self.create_text(
        129.0,
        115.0,
        anchor="nw",
        text="Cliente",
        fill="#FFFFFF",
        font=("Inter Bold", 40 * -1)
        )

        self.create_text(
            106.0,
            162.0,
            anchor="nw",
            text="Producto",
            fill="#FFFFFF",
            font=("Inter Bold", 40 * -1)
        )

    def create_text_2(self):
        self.create_text(
        906.0,
        285.0,
        anchor="nw",
        text="Total",
        fill="#FFFFFF",
        font=("Inter Bold", 40 * -1)
        )

        self.create_text(
        886.0,
        373.0,
        anchor="nw",
        text="1,000.25",
        fill="#FFFFFF",
        font=("Inter Bold", 30 * -1)
        )

    def create_button(self,x,y,width,height,image,command):
        return Button(
            self,
            image=image,
            borderwidth=0,
            highlightthickness=0,
            command=command,
            relief="flat"
        ).place(
            x=x,
            y=y,
            width=width,
            height=height
        )
    
    def create_entry(self): 
        self.entry_bg_1 = self.create_image(
            680.0,
            127.5,
            image=self.entry_image_1
        )
        entry_1 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        entry_1.place(
            x=322.0,
            y=110.0,
            width=716.0,
            height=33.0
        )
        self.entry_bg_2 = self.create_image(
            680.0,
            173.5,
            image=self.entry_image_2
        )
        entry_2 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        entry_2.place(
            x=322.0,
            y=156.0,
            width=716.0,
            height=33.0
        )

    def create_table(self):
        self.productos = ttk.Treeview(self, columns=("Nombre", "Descripcion", "precio","cantidad"))

        # Define column headings
        self.productos.heading("#0", text="Codigo")
        self.productos.heading("#1", text="Nombre")
        self.productos.heading("#2", text="Descripcion")
        self.productos.heading("#3", text="Precio")  
        self.productos.heading("#4", text="cantidad")  

        # Configurar columnas
        self.productos.column("#0", width=100, anchor="center")
        self.productos.column("#1", width=150, anchor="center")
        self.productos.column("#2", width=200, anchor="center")
        self.productos.column("#3", width=100, anchor="center")
        self.productos.column("#4", width=100, anchor="center")

        self.productos.place(x=140.0, y=240.0, width=700, height=400)

        # Insertar datos
        #self.insertar_datos(self.agencia_id)
    
    def button_1_click(self):
        self.destroy()
        panel = login.MyPanel(self.master)
        panel.pack(expand=True, fill="both")
    
    def button_2_click(self):
        self.destroy()
        panel = inventario.MyPanel(self.master,self.agencia_id)
        panel.pack(expand=True, fill="both")

    def button_3_click(self):
        pass

    def button_4_click(self):
        self.destroy()
        panel = cotizaciones.MyPanel(self.master)
        panel.pack(expand=True, fill="both")

    def button_5_click(self):
        self.destroy()
        panel = cliente.MyPanel(self.master)
        panel.pack(expand=True, fill="both")

    def button_6_click(self):
        print("button_6 clicked")

    def button_7_click(self):
        print("button_7 clicked")

    def button_8_click(self):
        print("button_8 clicked")