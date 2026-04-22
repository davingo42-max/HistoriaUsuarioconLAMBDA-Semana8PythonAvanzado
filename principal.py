from usuario import Formulario
from informacion import Informacion

inicio = Formulario()
ventana_1 = inicio.ventana_principal()
ventana_1.mainloop() 

if inicio.login_exitoso:
    app_info = Informacion()
    ventana_2 = app_info.ventana_datos()
    ventana_2.mainloop()
else:
    print("Programa finalizado abruptamente.")