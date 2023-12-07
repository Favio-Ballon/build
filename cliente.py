from tkinter import Canvas, PhotoImage, Button, Entry
from pathlib import Path
import login, facturacion, inventario,  cotizaciones


class MyPanel(Canvas):
    def __init__(self, master):
        super().__init__(
            master,
            bg="#252346",
            height=720,
            width=1080,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        OUTPUT_PATH = Path(__file__).parent
        self.assets_path = OUTPUT_PATH / Path(r"C:\Users\favio\Downloads\prueba\build\assets\frame3")
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
        self.create_button(880.0,400.0,168,48,self.button_image_6, self.button_6_click)
        self.create_button(638.0,400.0,199,48,self.button_image_7, self.button_7_click)
        self.create_image(589.0,584.0,self.image_5)

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
        self.entry_1 = self.load_image("entry_1.png")
        self.entry_2 = self.load_image("entry_2.png")
        self.entry_3 = self.load_image("entry_3.png")
        self.entry_4 = self.load_image("entry_4.png")
        self.entry_5 = self.load_image("entry_5.png")

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

        self.entry_bg_1 = self.create_image(
        680.0,
        127.5,
        image= self.entry_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=322.0,
            y=110.0,
            width=716.0,
            height=33.0
        )

        self.entry_bg_2 = self.create_image(
            680.0,
            178.5,
            image=self.entry_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2.place(
            x=322.0,
            y=161.0,
            width=716.0,
            height=33.0
        )

        self.entry_bg_3 = self.create_image(
            680.0,
            240.5,
            image=self.entry_3
        )
        self.entry_3 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_3.place(
            x=322.0,
            y=223.0,
            width=716.0,
            height=33.0
        )

        self.entry_bg_4 = self.create_image(
            680.0,
            302.5,
            image=self.entry_4
        )
        self.entry_4 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_4.place(
            x=322.0,
            y=285.0,
            width=716.0,
            height=33.0
        )
        self.entry_bg_5 = self.create_image(
            680.0,
            364.5,
            image=self.entry_5
        )
        self.entry_5 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_5.place(
            x=322.0,
            y=347.0,
            width=716.0,
            height=33.0
        )

    def create_text_1(self):

        self.create_text(
        129.0,
        104.0,
        anchor="nw",
        text="CI / NIT",
        fill="#FFFFFF",
        font=("Inter Bold", 40 * -1)
        )

        self.create_text(
        106.0,
        167.0,
        anchor="nw",
        text="Nombre",
        fill="#FFFFFF",
        font=("Inter Bold", 40 * -1)
        )

        self.create_text(
            106.0,
            229.0,
            anchor="nw",
            text="Apellido",
            fill="#FFFFFF",
            font=("Inter Bold", 40 * -1)
        )

        self.create_text(
            106.0,
            291.0,
            anchor="nw",
            text="Correo",
            fill="#FFFFFF",
            font=("Inter Bold", 40 * -1)
        )

        self.create_text(
            106.0,
            353.0,
            anchor="nw",
            text="Telefono",
            fill="#FFFFFF",
            font=("Inter Bold", 40 * -1)
        )


    def button_1_click(self):
        self.destroy()
        panel = login.MyPanel(self.master)
        panel.pack(expand=True, fill="both")
    
    def button_2_click(self):
        self.destroy()
        panel = inventario.MyPanel(self.master)
        panel.pack(expand=True, fill="both")

    def button_3_click(self):
        self.destroy()
        panel = facturacion.MyPanel(self.master)
        panel.pack(expand=True, fill="both")

    def button_4_click(self):
        self.destroy()
        panel = cotizaciones.MyPanel(self.master)
        panel.pack(expand=True, fill="both")

    def button_5_click(self):
        pass

    def button_6_click(self):
        print("button_6 clicked")

    def button_7_click(self):
        print("button_7 clicked")

    def button_8_click(self):
        print("button_8 clicked")

    def load_image(self, filename):
        return PhotoImage(file=self.assets_path / filename)
    
    def create_image(self, x, y, image):
        return super().create_image(x, y, image=image)
