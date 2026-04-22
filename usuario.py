import tkinter as Ventana

class Formulario:
    def __init__(self):
        self.usuario = ""
        self.contrasena = ""
        self.login_exitoso = False 

    def ventana_principal(self):
        self.formulario = Ventana.Tk()
        self.formulario.title("INICIAR SESION")
        self.formulario.geometry("450x600")
        self.formulario.config(cursor="hand2")
        
        self.formulario.bind('<Return>', lambda e: self.hacer_clic())
        
        self.iniciar_preguntas() 
        return self.formulario
    
    def iniciar_preguntas(self):
        Ventana.Label(self.formulario, text="Correo").pack(pady=10)
        self.entry_nombre = Ventana.Entry(self.formulario,)
        self.entry_nombre.pack()

        Ventana.Label(self.formulario, text="Contraseña").pack(pady=10)
        self.entry_cedula = Ventana.Entry(self.formulario, show="*")
        self.entry_cedula.pack()

        self.check_recordar = Ventana.Checkbutton(self.formulario, text="¿Desea recordar la sesión?")
        self.check_recordar.pack(pady=10)

        # Aplicación de Lambda aquí
        Ventana.Button(self.formulario, text="Ingresar", command=lambda: self.hacer_clic()).pack(pady=20)

    def hacer_clic(self):
        user = self.entry_nombre.get().strip()
        passw = self.entry_cedula.get().strip()

        if user == "" or passw == "":
            print("Error: Los campos no pueden estar vacíos")
        else:
            self.login_exitoso = True 
            self.formulario.destroy()
