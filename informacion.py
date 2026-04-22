import tkinter as Ventana
from tkinter import ttk 

class Informacion:
    def ventana_datos(self):
        self.info = Ventana.Tk()
        self.info.title("REGISTRO COMPLETO DE CLIENTES")
        self.info.geometry("800x900")

        Ventana.Label(self.info, text="¿Cuál es el tipo de documento?").pack()
        self.combo_tipo_doc = ttk.Combobox(self.info, values=["Cédula de Ciudadanía", "Tarjeta de Identidad", "Pasaporte"])
        self.combo_tipo_doc.pack()

        Ventana.Label(self.info, text="Ingrese su identificación:").pack()
        self.entry_id = Ventana.Entry(self.info, width=30)
        self.entry_id.pack()


        Ventana.Label(self.info, text="¿Cuál es su fecha de nacimiento? (DD/MM/AAAA)").pack()
        self.entry_fecha = Ventana.Entry(self.info, width=30)
        self.entry_fecha.pack()

        Ventana.Label(self.info, text="¿Cuál es su ciudad?").pack()
        self.entry_ciudad = Ventana.Entry(self.info, width=30)
        self.entry_ciudad.pack()

        Ventana.Label(self.info, text="¿Cuál es su dirección?").pack()
        self.entry_direccion = Ventana.Entry(self.info, width=30)
        self.entry_direccion.pack()


        Ventana.Label(self.info, text="¿Cuál es su género?").pack(pady=5)
        self.genero_var = Ventana.StringVar(value="M")
        Ventana.Radiobutton(self.info, text="Masculino", variable=self.genero_var, value="M").pack()
        Ventana.Radiobutton(self.info, text="Femenino", variable=self.genero_var, value="F").pack()

        Ventana.Label(self.info, text="¿Servicios de preferencia?").pack(pady=5)
        Ventana.Checkbutton(self.info, text="Soporte Técnico").pack()
        Ventana.Checkbutton(self.info, text="Ventas").pack()

        Ventana.Label(self.info, text="Nivel de satisfacción (0-10):").pack()
        self.escala = Ventana.Scale(self.info, from_=0, to=10, orient="horizontal")
        self.escala.pack()

        Ventana.Label(self.info, text="Observaciones adicionales:").pack()
        self.txt_obs = Ventana.Text(self.info, height=4, width=40)
        self.txt_obs.pack()

        # Aplicación de Lambda aquí
        Ventana.Button(self.info, text="Finalizar Registro", command=lambda: self.hacer_clic()).pack(pady=20)
        return self.info

    def hacer_clic(self):
        tipo_doc = self.combo_tipo_doc.get()
        identificacion = self.entry_id.get().strip()
        fecha = self.entry_fecha.get().strip()
        ciudad = self.entry_ciudad.get().strip()
        direccion = self.entry_direccion.get().strip()
        genero = self.genero_var.get()

        if (tipo_doc == "" or identificacion == "" or fecha == "" or 
            ciudad == "" or direccion == "" or genero == ""):
            print("Error: Todos los campos son obligatorios para cerrar el registro.")
        else:
            print("Registro procesado con éxito. Todos los datos capturados.")
            self.info.destroy()