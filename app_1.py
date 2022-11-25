from tkinter import *
from tkinter import ttk
from tkinter import messagebox

usuario = ""
contraseña = ""
contraseña_repetida = ""
vNombres = []
vContraseña = []


def guardar_Datos():
    usuario = entry_nombre_usuario.get()
    contraseña = entry_pass_usuario.get()
    contraseña_repetida = entry_repite_pass_usuario.get()
    print(usuario + "-" + contraseña)

    if (contraseña==contraseña_repetida):        
        vNombres.append(usuario)       
        vContraseña.append(contraseña)
        entry_nombre_usuario.delete(0,len(usuario))
        entry_pass_usuario.delete(0,len(contraseña))
        entry_repite_pass_usuario.delete(0,len(contraseña_repetida))
        print(vNombres)
        print(vContraseña)
        messagebox.showinfo("Usuario Guardado", f"Usuario {usuario} guardado")



#Configuración ventana
ventana = Tk()
ventana.title("Almacenamiento de datos")
ventana.geometry("350x250")
ventana.resizable(width=False,height=False)
ventana.config(background="beige")


#Titulo principal
label_Titulo = ttk.Label(ventana, text="DATOS USUARIO",background="beige")


#Componentes para pedir los datos
label_nombre_usuario = ttk.Label(ventana, text="Nombre:")
entry_nombre_usuario = ttk.Entry(ventana)

label_pass_usuario = ttk.Label(ventana, text="Contraseña:")
entry_pass_usuario = ttk.Entry(ventana, show="*")

label_repite_pass_usuario = ttk.Label(ventana, text="Confirma contraseña:")
entry_repite_pass_usuario = ttk.Entry(ventana, show="*")

boton_Guardar = ttk.Button(ventana, text="Guardar", command=guardar_Datos)
boton_Salir = ttk.Button(ventana, text="Salir", command=ventana.destroy)


#Pintar en pantalla los componentes
label_Titulo.grid(row=0,column=0, pady=10)
label_nombre_usuario.grid(row=1,column=0,pady=10)
entry_nombre_usuario.grid(row=1,column=1,pady=10)

label_pass_usuario.grid(row=2,column=0,pady=10)
entry_pass_usuario.grid(row=2,column=1,pady=10)

label_repite_pass_usuario.grid(row=3,column=0,pady=10, padx=15)
entry_repite_pass_usuario.grid(row=3,column=1,pady=10)

boton_Guardar.grid(row=4,column=0,pady=30)
boton_Salir.grid(row=4,column=1,pady=30)








ventana.mainloop()