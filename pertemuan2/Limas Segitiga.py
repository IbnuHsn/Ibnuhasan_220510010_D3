import tkinter as tk

def hitung_luas_dan_volume():
    alas = float(entry_a.get())
    tinggi_alas = float(entry_ta.get())
    tinggi_limas = float(entry_tl.get())

    luas_alas = 0.5 * alas * tinggi_alas
    luas_permukaan = luas_alas + 3 * ((alas * tinggi_limas) / 2)
    volume = (luas_alas * tinggi_limas) / 3

    hasil_text = f"Luas Permukaan Limas Segitiga: {luas_permukaan} satuan luas\nVolume Limas Segitiga: {volume} satuan volume"
    label_hasil.config(text=hasil_text)

def reset_entries():
    entry_a.delete(0, 'end')
    entry_ta.delete(0, 'end')
    entry_tl.delete(0, 'end')
    label_hasil.config(text="")

app = tk.Tk()
app.title("Kalkulator Limas Segitiga")

label_alas = tk.Label(app, text="Panjang Alas Segitiga:")
label_alas.pack()

entry_a = tk.Entry(app)
entry_a.pack()

label_tinggi_alas = tk.Label(app, text="Tinggi Alas Segitiga:")
label_tinggi_alas.pack()

entry_ta = tk.Entry(app)
entry_ta.pack()

label_tinggi_limas = tk.Label(app, text="Tinggi Limas:")
label_tinggi_limas.pack()

entry_tl = tk.Entry(app)
entry_tl.pack()

button_hitung = tk.Button(app, text="Hitung Luas & Volume", command=hitung_luas_dan_volume)
button_hitung.pack()

button_reset = tk.Button(app, text="Reset", command=reset_entries)
button_reset.pack()

label_hasil = tk.Label(app, text="")
label_hasil.pack()

app.mainloop()