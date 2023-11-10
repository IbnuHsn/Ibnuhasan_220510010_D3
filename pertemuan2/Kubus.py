import tkinter as tk

def hitung_luas_dan_volume():
    rusuk = float(entry_rusuk.get())
    luas = 6 * (rusuk ** 2)
    volume = rusuk ** 3
    hasil_text = f"Luas Kubus: {luas} satuan luas\nVolume Kubus: {volume} satuan volume"
    label_hasil.config(text=hasil_text)

app = tk.Tk()
app.title("Kalkulator Kubus")

label_sisi = tk.Label(app, text="Panjang Rusuk:")
label_sisi.pack()

entry_rusuk = tk.Entry(app)
entry_rusuk.pack()

button_hitung = tk.Button(app, text="Hitung Luas & Volume", command=hitung_luas_dan_volume)
button_hitung.pack()

label_hasil = tk.Label(app, text="")
label_hasil.pack()

app.mainloop()