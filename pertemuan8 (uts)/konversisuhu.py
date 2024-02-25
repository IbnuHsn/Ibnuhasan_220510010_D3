import tkinter as tk
from tkinter import messagebox


def konversiCelsiusToFahrenheit(celsius):
    return (celsius * 9/5) + 32

def konversiFahrenheitToCelsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def konversiCelsiusToKelvin(celsius):
    return celsius + 273.15

def konversiCelciusToReamur(celsius):
    return celsius * 4/5

def konversi():
    try:
        celsius = float(entry_celsius.get())
        fahrenheit = konversiCelsiusToFahrenheit(celsius)
        kelvin = konversiCelsiusToKelvin(celsius)
        reamur = konversiCelciusToReamur(celsius)
        result = f"Celsius: {celsius}°C\nFahrenheit: {fahrenheit}°F\nKelvin: {kelvin}Reamur: {reamur}°R\nReamur"
        messagebox.showinfo("Hasil Konversi", result)
    except ValueError:
        messagebox.showerror("Error", "Input tidak valid. Silakan masukkan angka.")

root = tk.Tk()
root.title("Konversi Suhu")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

label_celsius = tk.Label(frame, text="Masukkan suhu dalam Celsius:")
label_celsius.pack()

entry_celsius = tk.Entry(frame)
entry_celsius.pack()

button_konversi = tk.Button(frame, text="Konversi", command=konversi)
button_konversi.pack(pady=10)

root.mainloop()