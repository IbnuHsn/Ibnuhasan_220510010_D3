import tkinter as tk

def hitung_luas_dan_volume():
    alas = float(entry_a.get())
    tinggi_alas = float(entry_ta.get())
    tinggi_prisma = float(entry_tp.get())

    luas_alas = 0.5 * alas * tinggi_alas
    keliling_alas = 3 * alas
    luas_permukaan = (keliling_alas * tinggi_prisma) + 2 * luas_alas
    volume = luas_alas * tinggi_prisma

    hasil_text = f"Luas Permukaan Prisma Segitiga: {luas_permukaan} satuan luas\nVolume Prisma Segitiga: {volume} satuan volume"
    label_hasil.config(text=hasil_text)

def reset_entries():
    entry_a.delete(0, 'end')
    entry_ta.delete(0, 'end')
    entry_tp.delete(0, 'end')
    label_hasil.config(text="")

app = tk.Tk()
app.title("Kalkulator Prisma Segitiga")

label_alas = tk.Label(app, text="Panjang Alas Segitiga:")
label_alas.pack()

entry_a = tk.Entry(app)
entry_a.pack()

label_tinggi_alas = tk.Label(app, text="Tinggi Alas Segitiga:")
label_tinggi_alas.pack()

entry_ta = tk.Entry(app)
entry_ta.pack()

label_tinggi_prisma = tk.Label(app, text="Tinggi Prisma:")
label_tinggi_prisma.pack()

entry_tp = tk.Entry(app)
entry_tp.pack()

button_hitung = tk.Button(app, text="Hitung Luas & Volume", command=hitung_luas_dan_volume)
button_hitung.pack()

button_reset = tk.Button(app, text="Reset", command=reset_entries)
button_reset.pack()

label_hasil = tk.Label(app, text="")
label_hasil.pack()

app.mainloop()