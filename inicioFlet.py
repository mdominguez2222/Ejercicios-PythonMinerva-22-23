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