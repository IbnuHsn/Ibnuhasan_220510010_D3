import tkinter as tk

def hitung_luas_dan_volume():
    panjang = float(entry_p.get())
    lebar = float(entry_l.get())
    tinggi = float(entry_t.get())
    
    tinggisisi = 0.5 * panjang * tinggi
    luas_alas = panjang * lebar
    luas_sisi = (2 * 0.5 * panjang * tinggisisi) + (2 * 0.5 * lebar * tinggisisi)
    
    luas_permukaan = luas_alas + luas_sisi
    volume = (1/3) * luas_alas * tinggi
    
    hasil_text = f"Luas Permukaan Limas: {luas_permukaan} M²\nVolume Limas: {volume} M³"
    label_hasil.config(text=hasil_text)

def reset_entries():
    entry_p.delete(0, 'end')
    entry_l.delete(0, 'end')
    entry_t.delete(0, 'end')
    label_hasil.config(text="")

app = tk.Tk()
app.title("Kalkulator Limas Segiempat (Alas Persegi Panjang)")

label_panjang = tk.Label(app, text="Panjang Alas:")
label_panjang.pack()

entry_p = tk.Entry(app)
entry_p.pack()

label_lebar = tk.Label(app, text="Lebar Alas:")
label_lebar.pack()

entry_l = tk.Entry(app)
entry_l.pack()

label_tinggi = tk.Label(app, text="Tinggi Limas:")
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