# CodeAlpha_Language-Translation-Tool

A simple yet powerful desktop application built using Python and Tkinter that allows users to:

Translate text between multiple languages.

Copy translated text to the clipboard.

Convert translated text to speech using Google Text-to-Speech (gTTS).

🚀 Features
🔤 Translate text between 10+ languages (English, Spanish, French, Urdu, Arabic, etc.).

📋 Copy translated text to clipboard.

🔊 Listen to the translated output with built-in speech synthesis.

💡 Clean and modern GUI with responsive layout.

🛠️ Tech Stack
Tkinter – for GUI development

deep_translator – for language translation using Google Translate

gTTS – for text-to-speech synthesis

playsound – to play audio

pyperclip – to copy text to clipboard

threading – for non-blocking audio playback

📦 Installation
Make sure you have Python installed. Then, install the required libraries:

bash
Copy
Edit
pip install deep-translator gTTS playsound pyperclip
▶️ How to Run
Simply run the Python script:

bash
Copy
Edit
python language_translator.py
🌍 Supported Languages
English

Spanish

French

German

Hindi

Chinese

Arabic

Urdu

Japanese

Italian

🖼️ UI Preview
Main Features:

Input and output text boxes

Dropdown menus to select source and target languages

Buttons to Translate, Copy, and Speak the text

⚠️ Notes
Internet connection is required for translation and speech features.

The playsound module may behave differently on some OS. Consider alternatives like pygame or pydub if needed.

📄 License
This project is open-source and free to use for educational and personal purposes.
