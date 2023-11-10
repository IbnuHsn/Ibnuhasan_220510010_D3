import tkinter as tk
import math

def hitung_luas_dan_volume():
    jari_jari = float(entry_r.get())
    tinggi = float(entry_t.get())

    luas_permukaan = 2 * math.pi * jari_jari * (jari_jari + tinggi)
    volume = math.pi * (jari_jari ** 2) * tinggi

    hasil_text = f"Luas Permukaan Silinder: {luas_permukaan:.2f} satuan luas\nVolume Silinder: {volume:.2f} satuan volume"
    label_hasil.config(text=hasil_text)

def reset_entries():
    entry_r.delete(0, 'end')
    entry_t.delete(0, 'end')
    label_hasil.config(text="")

app = tk.Tk()
app.title("Kalkulator Silinder/Tabung")

label_jari_jari = tk.Label(app, text="Jari-Jari Silinder:")
label_jari_jari.pack()

entry_r = tk.Entry(app)
entry_r.pack()

label_tinggi = tk.Label(app, text="Tinggi Silinder:")
label_tinggi.pack()

entry_t = tk.Entry(app)
entry_t.pack()

button_hitung = tk.Button(app, text="Hitung Luas & Volume", command=hitung_luas_dan_volume)
button_hitung.pack()

button_reset = tk.Button(app, text="Reset", command=reset_entries)
button_reset.pack()

label_hasil = tk.Label(app, text="")
label_hasil.pack()

app.mainloop()