import flet as ft

def main(page: ft.Page):
    def bs_dismissed(e):
        print("Dismissed!")

    def mostrar(e):
        bs.open = True
        bs.update()

    def cerrar(e):
        bs.open = False
        bs.update()

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

    img = ft.Image(src="https://www.ilcapo.net/wp-content/uploads/2019/01/productos-naturales-andiamo1.jpg", width=200, height=800,border_radius=ft.border_radius.all(10))
    page.add(img)

ft.app(target=main)