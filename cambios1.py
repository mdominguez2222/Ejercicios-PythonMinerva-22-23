'''
import flet as ft

def main(page):
    def button_clicked(e):
        t.value = (
            f"Switch values are:  {c1.value}, {c2.value}, {c3.value}.")
        page.update()

    t = ft.Text()
    c1 = ft.Switch(label="Tocino", value=False)
    c2 = ft.Switch(label="Carne", value=False)
    c3 = ft.Switch(label="vERDURA", value=False)
    
    b = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    page.add(c1, c2, c3, b, t)

ft.app(target=main)
'''

import flet as ft


vAlimentos = []

def main(page: ft.Page):
    page.title= "TIENDA DOMÍNGUEZ"
    def guardarenCesta(e):
        textoCestapop.value = vAlimentos
        page.update()

    def añadirAlimentos(e):
        vAlimentos = v
        #textComida.value = vAlimentos
        #for i in vAlimentos:
        #    textComida.value += "-" + i

        page.update()

    #Funciones del pop up cesta (mostrar alimentos en la cesta)

    def bs_dismissed(e):
        print("Dismissed!")

    def mostrar(e):
        bs.open = True
        bs.update()

    def cerrar(e):
        bs.open = False
        bs.update()

        

    t = ft.Text()
    c1 = ft.Switch(label="Tocino", value=False)
    c2 = ft.Switch(label="Carne", value=False)
    c3 = ft.Switch(label="verdura", value=False)
    v = ft.Switch.value(True)
    b = ft.ElevatedButton(text="Submit", on_click=añadirAlimentos)
    page.add(c1, c2, c3, b, t, v)


    #Crear texto
    t = ft.Text(value="Tienda Domínguez", color= "black", size=30, font_family="Times New Roman")
    page.add(t)

    #Poner en la pantalla el texto
    t.value="BIENVENIDO A TIENDA DOMÍNGUEZ"
    
    page.update() #Refrescar la pantalla para poner un nuevo texto


    textField_Nombre= ft.TextField(label="Nombre", hint_text="Escribe tu nombre")
    textField_Nombre
    #page.add(textField_Nombre)


    #Verduras
    dropDown_Verduras = ft.Dropdown(width=300,hint_text="Verduras", options=[ft.dropdown.Option("Zanahoria")])
    dropDown_Verduras.options.append(ft.dropdown.Option("Lechuga"))
    dropDown_Verduras.options.append(ft.dropdown.Option("Tomate"))
    dropDown_Verduras.options.append(ft.dropdown.Option("Espinacas"))
    page.update()


    #Carnes
    dropDown_Carnes = ft.Dropdown(width=300, hint_text="Carnes", options=[ft.dropdown.Option("Pollo")])
    dropDown_Carnes.options.append(ft.dropdown.Option("Solomillo"))
    dropDown_Carnes.options.append(ft.dropdown.Option("Cordero"))
    dropDown_Carnes.options.append(ft.dropdown.Option("Pluma"))
    page.update()

    #Crear fila
    fila = ft.Row(controls=[textField_Nombre, dropDown_Verduras, dropDown_Carnes])
    page.add(fila)

    #Botón añadir
    textComida = ft.TextField(label="Alimentos", hint_text="Alimentos añadidos")
    boton_añadir = ft.FilledButton("Añadir a la cesta", icon="add", on_click=añadirAlimentos)#ft.FilledButton("Button with icon", icon="add")
    page.add(boton_añadir)
    page.add(textComida)

    #Botón mostrar carrito
    boton_cesta= ft.FloatingActionButton(icon=ft.icons.SHOP, on_click= guardarenCesta)
    page.add(boton_cesta)


    textoCestapop = ft.Text("Cesta: ")
    bs = ft.BottomSheet(
        ft.Container(
            ft.Column(
                [
                    textoCestapop,
                    ft.ElevatedButton("Cerrar cesta", on_click=cerrar),
                ],
                tight=True,
            ),
            padding=10,
        ),
        open=False,
        on_dismiss=bs_dismissed,
    )
    page.overlay.append(bs)
    page.add(ft.FloatingActionButton(icon=ft.icons.SHOP, on_click=mostrar))

    #imagen
    img = ft.Image(src="https://www.ilcapo.net/wp-content/uploads/2019/01/productos-naturales-andiamo1.jpg",width=200, height=550,border_radius=ft.border_radius.all(10))
    page.add(img)
    


ft.app(target=main)#view="web_browser")