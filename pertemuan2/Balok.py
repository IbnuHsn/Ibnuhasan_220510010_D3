import tkinter as tk

def hitung_luas_dan_volume():
    panjang = float(entry_p.get())
    lebar = float(entry_l.get())
    tinggi = float(entry_t.get())
    luas = 2 * (panjang * lebar) + 2 * (panjang * tinggi) + 2 * (lebar * tinggi)
    volume = panjang * lebar * tinggi
    hasil_text = f"Luas Balok: {luas} M²\nVolume Balok: {volume} M³"
    label_hasil.config(text=hasil_text)

def reset_entries():
    entry_p.delete(0, 'end')
    entry_l.delete(0, 'end')
    entry_t.delete(0, 'end')
    label_hasil.config(text="")

app = tk.Tk()
app.title("Kalkulator Balok")

label_panjang = tk.Label(app, text="Panjang:")
label_panjang.pack()

entry_p = tk.Entry(app)
entry_p.pack()

label_lebar = tk.Label(app, text="Lebar:")
label_lebar.pack()

entry_l = tk.Entry(app)
entry_l.pack()

label_tinggi = tk.Label(app, text="Tinggi:")
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