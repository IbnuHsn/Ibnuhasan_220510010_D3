import tkinter as tk
import math

def hitung_luas_dan_volume():
    jari_jari = float(entry_r.get())

    luas_permukaan = 4 * math.pi * (jari_jari**2)
    volume = (4/3) * math.pi * (jari_jari**3)

    hasil_text = f"Luas Permukaan Bola: {luas_permukaan:.2f} satuan luas\nVolume Bola: {volume:.2f} satuan volume"
    label_hasil.config(text=hasil_text)

def reset_entries():
    entry_r.delete(0, 'end')
    label_hasil.config(text="")

app = tk.Tk()
app.title("Kalkulator Bola")

label_jari_jari = tk.Label(app, text="Jari-Jari Bola:")
label_jari_jari.pack()

entry_r = tk.Entry(app)
entry_r.pack()

button_hitung = tk.Button(app, text="Hitung Luas & Volume", command=hitung_luas_dan_volume)
button_hitung.pack()

button_reset = tk.Button(app, text="Reset", command=reset_entries)
button_reset.pack()

label_hasil = tk.Label(app, text="")
label_hasil.pack()

app.mainloop()