import flet as ft


def main(page: ft.Page):
    page.title= "TIENDA DOMÍNGUEZ"
    def cambiarColor(e):
       t.value= textField_Nombre.value
       page.update()

    #Crear texto
    t = ft.Text(value="Tienda Domínguez", color= "black", size=30, font_family="Times New Roman")

    #Poner en la pantalla el texto
    page.add(t)   #add hace dos cosas: 1-Añadir 2-Actualizar

    t.value="BIENVENIDO"
    page.update() #Refrescar la pantalla para poner un nuevo texto

    #Componente Botón               Generar icono                        Declarar función
    boton= ft.FloatingActionButton(icon=ft.icons.ADD, on_click= cambiarColor)
    page.add(boton)

    
    textField_Nombre= ft.TextField(label="Nombre", hint_text="Escribe tu nombre")
    textField_Nombre
    #page.add(textField_Nombre)

    dropDown_Menu = ft.Dropdown(width=300,hint_text="Alimentos", options=[ft.dropdown.Option("Verduras")])
    #page.add(dropDown_Menu)
    dropDown_Menu.options.append(ft.dropdown.Option("Carnes"))
    page.update()

    #Crear fila
    fila = ft.Row(controls=[textField_Nombre, dropDown_Menu])
    page.add(fila)

    def boton_añadir(e):
        lista_Alimentos.options.append(ft.dropdown.Option(option_textbox.value))
        lista_Alimentos.value = option_textbox.value
        option_textbox.value = ""
        page.update()

    def boton_borrar(e):
        option = find_option(lista_Alimentos.value)
        if option != None:
            lista_Alimentos.options.remove(option)
            # d.value = None
            page.update()

    lista_Alimentos = ft.Dropdown()
    option_textbox = ft.TextField(hint_text="Añade alimentos")
    add = ft.ElevatedButton("Añadir", on_click=boton_añadir)
    delete = ft.OutlinedButton("Borrar", on_click=boton_borrar)
    page.add(lista_Alimentos, ft.Row(controls=[option_textbox, add, delete]))

    vAlimentos = []
    vAlimentos.append(add)



ft.app(target=main)