
import flet as ft


vAlimentos = []

def main(page: ft.Page):
    page.title= "TIENDA DOMÍNGUEZ"
    def guardarenCesta(e):
        vAlimentos.append(dropDown_Carnes.value)
        print(vAlimentos)

        

    #Crear texto
    t = ft.Text(value="Tienda Domínguez", color= "black", size=30, font_family="Times New Roman")
    page.add(t)
    #Poner en la pantalla el texto
       #add hace dos cosas: 1-Añadir 2-Actualizar
    t.value="BIENVENIDO"
    
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

    #Botón mostrar carrito
    boton_cesta= ft.FloatingActionButton(icon=ft.icons.SHOP, on_click= guardarenCesta)
    page.add(boton_cesta)

    


ft.app(target=main)




'''
import flet as ft


vAlimentos = []

def main(page: ft.Page):
    page.title= "TIENDA DOMÍNGUEZ"
    def guardarenCesta(e):
        vAlimentos.append(dropDown_Carnes.value)
        vAlimentos.append(dropDown_Verduras.value)
        textComida.value = vAlimentos
        print(vAlimentos)

    def añadirAlimentos(e):
        vAlimentos.append(dropDown_Carnes.value)
        vAlimentos.append(dropDown_Verduras.value)
        for i in vAlimentos:
            textComida.value += "-" + i

        page.update()

    #Opcion mostrar alimentos en la cesta

    def bs_dismissed(e):
        print("Dismissed!")

    def mostrar(e):
        bs.open = True
        bs.update()

    def cerrar(e):
        bs.open = False
        bs.update()

    
        

    #Crear texto
    t = ft.Text(value="Tienda Domínguez", color= "black", size=30, font_family="Times New Roman")
    page.add(t)
    #Poner en la pantalla el texto
       #add hace dos cosas: 1-Añadir 2-Actualizar
    t.value="BIENVENIDO"
    
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


    bs = ft.BottomSheet(
        ft.Container(
            ft.Column(
                [
                    ft.Text("Alimentos añadidos"),
                    ft.ElevatedButton("Cerrar cesta", on_click=cerrar),
                ],
                tight=True,
            ),
            padding=10,
        ),
        open=True,
        on_dismiss=bs_dismissed,
    )
    page.overlay.append(bs)
    page.add(ft.FloatingActionButton(icon=ft.icons.SHOP, on_click=mostrar))

    


ft.app(target=main)#view="web_browser")
'''