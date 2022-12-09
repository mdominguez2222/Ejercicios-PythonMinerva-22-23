
import flet as ft

# Utilizar flet como ft

def main(page: ft.Page):
    page.title= "APLICACIÓN FLET"
    def cambiarColor(e):
       t.value= textField_Nombre.value
       page.update()

    #Crear texto
    t = ft.Text(value="Introducción a Flet", color= "green", size=30)

    #Poner en la pantalla el texto
    page.add(t)   #add hace dos cosas: 1-Añadir 2-Actualizar

    t.value="BIENVENIDO"
    page.update() #Refrescar la pantalla para poner un nuevo texto

    #Componente Botón               Generar icono                        Declarar función
    boton= ft.FloatingActionButton(icon=ft.icons.ADD, on_click= cambiarColor)
    page.add(boton)

    
    textField_Nombre= ft.TextField(label="Nombre", hint_text="Escribe tu nombre")
    textField_Nombre
    page.add(textField_Nombre)

    dropDown_Menu = ft.Dropdown(width=300, options=[ft.dropdown.Option("Elección 1")])
    page.add(dropDown_Menu)
    dropDown_Menu.options.append(ft.dropdown.Option("Nueva"))
    page.update()

    slider_edad = ft.Slider(min=0, max=120, divisions=120, label="Edad: {value}")
    page.add(slider_edad)



ft.app(target=main)













'''
import flet as ft


def main(page: ft.Page):
    page.title="Tkinder  -  Flet  :)))"

    def cambiarColor(e):
        for i in range(10):
            text = ft.Text(value=f"Texto número {i}", size=30, color="red")

            page.add(text)




    #Componente Texto
    t = ft.Text(value="Introducción a Flet", color="blue", size=20)

    page.add(t) # add hace dos cosas: 1.Añadir  2.Actualizar la página
    #page.update() Actualiza los datos 


    #Componente Boton
    bt = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=cambiarColor)
    page.add(bt)





ft.app(target=main)
'''