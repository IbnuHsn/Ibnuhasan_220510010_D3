import tkinter as tk
from tkinter import ttk
from googletrans import Translator

def translate_to_english(text):
    translator = Translator()
    translation = translator.translate(text, src='id', dest='en')
    return translation.text

def translate_to_portuguese(text):
    translator = Translator()
    translation = translator.translate(text, src='id', dest='pt')
    return translation.text

def translate_to_romanian(text):
    translator = Translator()
    translation = translator.translate(text, src='id', dest='ro')
    return translation.text

def on_click_translate():
    input_text = input_text_var.get()
    english_translation = translate_to_english(input_text)
    portuguese_translation = translate_to_portuguese(input_text)
    romanian_translation = translate_to_romanian(input_text)

    output_text_var.set(f"English: {english_translation}\nPortuguese: {portuguese_translation}\nRomanian: {romanian_translation}")

app = tk.Tk()
app.title("Translator Indonesia to English, Portuguese, and Romanian")

frame = ttk.Frame(app, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

input_text_var = tk.StringVar()
output_text_var = tk.StringVar()

input_text_entry = ttk.Entry(frame, textvariable=input_text_var, width=50)
input_text_entry.grid(row=0, column=0, sticky=(tk.W, tk.E))

translate_button = ttk.Button(frame, text="Translate", command=on_click_translate)
translate_button.grid(row=0, column=1, padx="5")

output_text_label = ttk.Label(frame, textvariable=output_text_var, wraplength=500)
output_text_label.grid(row=1, column=0, columnspan=2, pady="5")

app.mainloop()