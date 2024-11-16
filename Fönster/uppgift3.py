import tkinter as tk
from tkinter import messagebox
import os
import requests

class FileEditorApp:
    def __init__(self, root):
        # Huvudfönster
        self.root = root
        self.root.title("File Editor")  # Fönstrets titel
        self.root.geometry("400x500")  # Fönstrets storlek

        # Textfält för att skriva eller visa text
        self.text_field = tk.Text(self.root, height=10, width=40)
        self.text_field.pack(pady=10)

        # Inmatningsfält för API-sökvillkor
        self.search_field = tk.Entry(self.root, width=30)
        self.search_field.pack(pady=5)
        self.search_field.insert(0, "Ange ett villkor (exempel: pris)")

        # Filnamn för att läsa och skriva till
        self.filnamn = "data.txt"

        # Knapp för att skriva text till fil
        self.save_button = tk.Button(self.root, text="Skriv till fil", command=self.skriva_till_fil)
        self.save_button.pack(pady=5)

        # Knapp för att läsa från fil
        self.load_button = tk.Button(self.root, text="Läs från fil", command=self.lasa_från_fil)
        self.load_button.pack(pady=5)

        # Knapp för att rensa textfältet
        self.clear_button = tk.Button(self.root, text="Rensa", command=self.rensa_textfält)
        self.clear_button.pack(pady=5)

        # Knapp för att hämta data från API
        self.fetch_button = tk.Button(self.root, text="Hämta data från API", command=self.hamta_data_fran_api)
        self.fetch_button.pack(pady=5)

    def skriva_till_fil(self):
        """Skriver innehållet från textfältet till fil."""
        text = self.text_field.get("1.0", tk.END).strip()  # Hämtar texten från textfältet
        if text:
            with open(self.filnamn, 'a') as file:  # Öppnar filen i append-läge
                file.write(text + "\n")
            messagebox.showinfo("Info", "Texten har sparats till fil.")
        else:
            messagebox.showwarning("Varning", "Textfältet är tomt.")

    def lasa_från_fil(self):
        """Läser från filen och visar innehållet i textfältet."""
        if os.path.exists(self.filnamn):
            with open(self.filnamn, 'r') as file:
                file_content = file.read()
                self.text_field.delete("1.0", tk.END)  # Rensa textfältet innan vi skriver ny text
                self.text_field.insert(tk.END, file_content)  # Sätt in innehållet från filen
        else:
            messagebox.showwarning("Varning", "Filen finns inte.")

    def rensa_textfält(self):
        """Rensar textfältet."""
        self.text_field.delete("1.0", tk.END)

    def hamta_data_fran_api(self):
        """Hämtar data från Fake Store API baserat på användarens inmatade villkor och sparar det i filen."""
        villkor = self.search_field.get().strip().lower()  # Hämta användarens sökvillkor
        if not villkor or villkor == "ange ett villkor (exempel: pris)":
            messagebox.showwarning("Varning", "Ange ett giltigt villkor för att hämta data.")
            return

        try:
            # API-anrop till Fake Store API
            response = requests.get("https://fakestoreapi.com/products", timeout=10)

            if response.status_code == 200:
                data = response.json()
                # Debug: skriv ut hela API-responsen för att se vad som hämtas
                print("Hämtad data från API:", data)

                # Filtrera produkter som matchar användarens villkor
                filtered_data = [
                    item for item in data if villkor in item['title'].lower()
                ]

                if filtered_data:
                    formatted_data = ""
                    for item in filtered_data:
                        formatted_data += f"Produkt: {item['title']}, Pris: ${item['price']}\n"
                
                    # Visa data i textfält och spara till fil
                    self.text_field.delete("1.0", tk.END)
                    self.text_field.insert(tk.END, formatted_data)
                    with open(self.filnamn, 'a') as file:
                        file.write(formatted_data + "\n")
                    messagebox.showinfo("Info", "Data har hämtats och sparats.")
                else:
                    messagebox.showinfo("Info", f"Ingen data hittades för villkoret: {villkor}.")
            else:
                messagebox.showerror("Fel", f"API-anrop misslyckades med statuskod {response.status_code}")

        except requests.exceptions.Timeout:
            messagebox.showerror("Fel", "Anslutningen till API:et tog för lång tid. Försök igen.")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Fel", f"Ett fel inträffade vid API-anrop: {str(e)}")
        except Exception as e:
            messagebox.showerror("Fel", f"Ett oväntat fel inträffade: {str(e)}")


# Skapar huvudfönstret för Tkinter
root = tk.Tk()

# Skapar och startar applikationen
app = FileEditorApp(root)

# Startar huvudloopen för Tkinter GUI
root.mainloop()
