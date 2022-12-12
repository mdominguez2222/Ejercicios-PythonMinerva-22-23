from tkinter import *
from tkinter import ttk
from tkinter import messagebox


ventana = Tk()
ventana.title("Almacenamiento de datos")
ventana.geometry("350x300")
ventana.resizable(width=False,height=False)
ventana.config(background="beige")


combo_alimentos1 = ttk.Combobox(ventana, values=["Carnes", "Verduras"], state="readonly")
combo_alimentos1.set("Alimentos")
combo_alimentos1.place(x=90, y =250)

combo_alimentos2 = ttk.Combobox(ventana, values=[""], state="readonly")
combo_alimentos2.set("")
combo_alimentos2.place(x=90,y=200)

boton_Guardar = ttk.Button(ventana, text="Guardar")


ventana.mainloop()