from tkinter import *
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator
from gtts import gTTS
import pyperclip
import os
import tempfile
import threading
from playsound import playsound

# Language name to ISO code mapping for gTTS
language_codes = {
    'english': 'en',
    'spanish': 'es',
    'french': 'fr',
    'german': 'de',
    'hindi': 'hi',
    'chinese': 'zh-CN',
    'arabic': 'ar',
    'urdu': 'ur',
    'japanese': 'ja',
    'italian': 'it'
}

languages = list(language_codes.keys())

# Translate text function
def translate_text():
    src = source_lang.get().lower()
    tgt = target_lang.get().lower()
    text = input_text.get("1.0", END).strip()

    if not text:
        messagebox.showwarning("Empty Input", "Please enter text to translate.")
        return

    try:
        translated = GoogleTranslator(source=src, target=tgt).translate(text)
        output_text.delete("1.0", END)
        output_text.insert(END, translated)
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

# Copy translated text
def copy_text():
    text = output_text.get("1.0", END).strip()
    if text:
        pyperclip.copy(text)
        messagebox.showinfo("Copied", "Translated text copied to clipboard.")

# Speak translated text using gTTS
def speak_text():
    text = output_text.get("1.0", END).strip()
    lang_name = target_lang.get().lower()
    lang = language_codes.get(lang_name, 'en')

    if not text:
        messagebox.showwarning("Empty", "No text to speak.")
        return

    def run_speech():
        try:
            tts = gTTS(text=text, lang=lang)
            temp_dir = tempfile.gettempdir()
            file_path = os.path.join(temp_dir, "translated_speech.mp3")
            tts.save(file_path)
            playsound(file_path)
            os.remove(file_path)  # Clean up
        except Exception as e:
            messagebox.showerror("Speech Error", f"Error: {str(e)}")

    threading.Thread(target=run_speech).start()

# Setup GUI
root = Tk()
root.title("🌐 Language Translator")
root.geometry("700x550")
root.configure(bg="#f0f4f7")

font_title = ("Segoe UI", 18, "bold")
font_label = ("Segoe UI", 12)
font_text = ("Segoe UI", 11)

# Title
Label(root, text="Language Translation Tool", font=font_title, bg="#f0f4f7", fg="#003366").pack(pady=20)

# Input
Label(root, text="Enter Text:", font=font_label, bg="#f0f4f7").pack(anchor='w', padx=20)
input_text = Text(root, height=5, width=80, font=font_text, wrap=WORD)
input_text.pack(padx=20)

# Language selectors
frame = Frame(root, bg="#f0f4f7")
frame.pack(pady=15)

Label(frame, text="From:", font=font_label, bg="#f0f4f7").grid(row=0, column=0, padx=5)
source_lang = ttk.Combobox(frame, values=languages, state="readonly", width=20, font=font_text)
source_lang.set("english")
source_lang.grid(row=0, column=1, padx=10)

Label(frame, text="To:", font=font_label, bg="#f0f4f7").grid(row=0, column=2, padx=5)
target_lang = ttk.Combobox(frame, values=languages, state="readonly", width=20, font=font_text)
target_lang.set("spanish")
target_lang.grid(row=0, column=3, padx=10)

# Translate button
Button(root, text="Translate", command=translate_text, bg="#007acc", fg="white",
       font=("Segoe UI", 12, "bold"), width=20, height=2).pack(pady=10)

# Output
Label(root, text="Translated Text:", font=font_label, bg="#f0f4f7").pack(anchor='w', padx=20)
output_text = Text(root, height=5, width=80, font=font_text, wrap=WORD)
output_text.pack(padx=20)

# Buttons: Copy and Speak
btn_frame = Frame(root, bg="#f0f4f7")
btn_frame.pack(pady=15)

Button(btn_frame, text="📋 Copy", command=copy_text, bg="#4CAF50", fg="white",
       font=("Segoe UI", 10, "bold"), width=12).grid(row=0, column=0, padx=15)

Button(btn_frame, text="🔊 Speak", command=speak_text, bg="#FF9800", fg="white",
       font=("Segoe UI", 10, "bold"), width=12).grid(row=0, column=1, padx=15)

root.mainloop()
