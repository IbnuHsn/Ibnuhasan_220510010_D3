import flet as ft

def main(page: ft.Page):
    page.bgcolor = "#1640D6"
    page.window_width =400
    page.window_resizable = False
    

    harga_rental_mobil = 450000
    harga_rental_motor = 60000
    

    def btn_click(e):
        if tipe_kendaraan.value == "mobil":
            hitung_mobil = int(jam_rental.value) * harga_rental_mobil
            biaya.value = hitung_mobil
            page.update()

        elif tipe_kendaraan.value == "motor":
            hitung_motor = int(jam_rental.value) * harga_rental_motor
            biaya.value = hitung_motor
            page.update()

    jam_rental = ft.TextField(label="LAMA PEMINJAMAN")
    tipe_kendaraan = ft.TextField(label="Jenis Kendaraan. Motor / Mobil")
    biaya = ft.TextField()

    page.add(
        ft.AppBar(title=ft.Text("APLIKASI RENTAL MOBIL & MOTOR"), bgcolor="black"),
        jam_rental,
        tipe_kendaraan,
        ft.ElevatedButton("HITUNG", on_click=btn_click, ),
        biaya
    )

ft.app(target=main)