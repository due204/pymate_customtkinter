from customtkinter import CTk
from customtkinter import CTkButton
from customtkinter import CTkLabel
from customtkinter import CTkComboBox
from customtkinter import set_appearance_mode
from customtkinter import set_default_color_theme
from tkinter import PhotoImage
from os import system


class Mimate():
    def __init__(self, parent):
        # Vista principal
        self.parent = parent
        self.parent.title("Py Mate")
        logo = PhotoImage(file="mate.png")
        self.parent.call("wm", "iconphoto", self.parent._w, logo)
        vent_x = self.parent.winfo_screenwidth() // 2 - 200 // 2
        vent_y = self.parent.winfo_screenheight() // 2 - 150 // 2
        tam_y_pos = "300x" + "250+" + str(vent_x) + "+" + str(vent_y)
        self.parent.geometry(tam_y_pos)  # Ancho, largo y posicion
        self.parent.resizable(False, False)
        self.parent.bind("<KeyPress-Escape>", self.salir)
        
        self.vista()

    def vista(self):
        #Vista y posicionamiento de los widget
        #Labes
        self.label_home = CTkLabel(root, text="Icono de home")
        self.label_home.place(x=10, y=10)
        self.label_lugares = CTkLabel(root, text="Icono de lugares")
        self.label_lugares.place(x=10, y=50)
        self.label_red = CTkLabel(root, text="Icono de red")
        self.label_red.place(x=10, y=90)
        self.label_papelera = CTkLabel(root, text="Icono de papelera")
        self.label_papelera.place(x=10, y=130)
        self.label_volumenes = CTkLabel(root, text="Icono de volumenes")
        self.label_volumenes.place(x=10, y=170)

        #Comboboxs
        self.spin_home = CTkComboBox(root, width=80, values=["Ver", "No ver"], state="readonly")
        self.spin_home.set("Ver")
        self.spin_home.place(x=200, y=10)
        self.spin_lugares = CTkComboBox(root, width=80, values=["Ver", "No ver"], state="readonly")
        self.spin_lugares.set("Ver")
        self.spin_lugares.place(x=200, y=50)
        self.spin_red = CTkComboBox(root, width=80, values=["Ver", "No ver"], state="readonly")
        self.spin_red.set("Ver")
        self.spin_red.place(x=200, y=90)
        self.spin_papelera = CTkComboBox(root, width=80, values=["Ver", "No ver"], state="readonly")
        self.spin_papelera.set("Ver")
        self.spin_papelera.place(x=200, y=130)
        self.spin_volumenes = CTkComboBox(root, width=80, values=["Ver", "No ver"], state="readonly")
        self.spin_volumenes.set("Ver")
        self.spin_volumenes.place(x=200, y=170)

        #Boton
        self.boton = CTkButton(root, width=80, text="Guardar", command=self.guardar)
        self.boton.place(x=200, y=210)

    def guardar(self):
        #Obteniendo los datos
        self.home = self.validar(self.spin_home.get())
        system("gsettings set org.mate.caja.desktop home-icon-visible %s" %self.home)
        self.lugares = self.validar(self.spin_lugares.get())
        system("gsettings set org.mate.caja.desktop computer-icon-visible %s" %self.lugares)
        self.red = self.validar(self.spin_red.get())
        system("gsettings set org.mate.caja.desktop network-icon-visible %s" %self.red)
        self.papelera = self.validar(self.spin_papelera.get())
        system("gsettings set org.mate.caja.desktop trash-icon-visible %s" %self.papelera)
        self.volumenes = self.validar(self.spin_volumenes.get())
        system("gsettings set org.mate.caja.desktop volumes-visible %s" %self.volumenes)
        self.salir()

    def validar(self, dato):
        #Valida los datos
        if dato == "Ver":
            return "true"
        else:
            return "false"

    def salir(self, *args):
        self.parent.destroy()
        self.parent.quit()
        print("Saliendo del programa")


if __name__ == "__main__":
    set_appearance_mode("dark")
    set_default_color_theme("dark-blue")
    root = CTk()
    Mimate(root)
    root.mainloop()