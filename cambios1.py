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

def main(page: ft.Page):
    page.add(ft.Image(src=f"/imagenes/bananaicono.png"))
    

ft.app(target=main, assets_dir="imagenes")#view="web_browser)