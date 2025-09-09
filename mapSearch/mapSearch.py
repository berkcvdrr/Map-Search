import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import scrolledtext
import webbrowser

def google_map_search():
    query = entry.get()
    output_text.delete(1.0, tk.END)

    if not query.strip():
        output_text.insert(tk.END, "Lütfen bir arama sorgusu girin.")
        return

    output_text.insert(tk.END, f"'{query}' için arama yapılıyor...\n")
    url = f"https://www.google.com/maps/search/{query.replace(' ', '+')}"

    try:
        webbrowser.open(url)
        output_text.insert(tk.END, "Google Maps tarayıcıda açıldı.\n")
        output_text.insert(tk.END, "Not: Google Maps sonuçları sınırlamalar nedeniyle doğrudan uygulamada gösterilemiyor.\n")
    except Exception as e:
        output_text.insert(tk.END, f"Hata oluştu: {str(e)}")

# GUI oluştur
window = tk.Tk()
window.title('Google Maps Sektörel Arama')

frame = tk.Frame(window)
frame.pack(pady=10)

tk.Label(frame, text="Arama Sorgusu:").pack(side=tk.LEFT)

entry = tk.Entry(frame, width=80)
entry.pack(side=tk.LEFT, padx=10)

search_button = tk.Button(window, text="Ara", command=google_map_search, bg="#4285F4", fg="white", padx=20)
search_button.pack(pady=5)

output_text = scrolledtext.ScrolledText(window, width=100, height=20)
output_text.pack(pady=10, padx=20)

entry.bind("<Return>", lambda event: google_map_search())

window.mainloop()
