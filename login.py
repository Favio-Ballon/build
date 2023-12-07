from tkinter import Tk, Canvas, Entry, Button, PhotoImage
from pathlib import Path
import inventario
import conexion

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\favio\Downloads\prueba\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class MyPanel(Canvas):
    def __init__(self, master):
        super().__init__(
            master,
            bg="#14103D",
            height=720,
            width=1080,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        OUTPUT_PATH = Path(__file__).parent
        self.assets_path = OUTPUT_PATH / Path(r"C:\Users\favio\Downloads\prueba\build\assets\frame0")
        self.create_widgets()

    def create_widgets(self):
        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.create_image(
            404.0,
            360.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.image_2 = self.create_image(
            810.0,
            360.0,
            image=self.image_image_2
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.button_1_click,
            relief="flat"
        )
        self.button_1.place(
            x=700.0,
            y=556.0,
            width=246.0,
            height=43.0
        )

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.create_image(
            823.0,
            435.5,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            self,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=710.0,
            y=414.0,
            width=226.0,
            height=41.0
        )

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.create_image(
            823.0,
            293.5,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            self,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2.place(
            x=710.0,
            y=272.0,
            width=226.0,
            height=41.0
        )

        self.create_text(
            705.0,
            218.0,
            anchor="nw",
            text="Agencia",
            fill="#FFFFFF",
            font=("Inter", 35 * -1)
        )

        self.create_text(
            705.0,
            360.0,
            anchor="nw",
            text="Contraseña",
            fill="#FFFFFF",
            font=("Inter", 35 * -1)
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        self.image_3 = self.create_image(
            822.0,
            75.0,
            image=self.image_image_3
        )

    def button_1_click(self):
        self.agencia_nombre = self.entry_2.get()
        self.agencia_id = None
        if(self.agencia_nombre != None):
            conexion.cur.execute(("SELECT id FROM agencia WHERE nombre iLIKE '"+self.agencia_nombre+"'"))
            temp = conexion.cur.fetchone()
            if(temp != None):
                self.agencia_id = temp[0]
        #Cambia de ventana a inventario.py Si existe una id de agencia
        if(self.agencia_id != None):
            self.destroy()
            panel = inventario.MyPanel(self.master,self.agencia_id)
            panel.pack(expand=True, fill="both")


if __name__ == "__main__":
    root = Tk()
    panel = MyPanel(root)
    panel.pack(expand=True, fill="both")
    root.mainloop()
