import tkinter as tk
from tkinter import ttk
import requests
from tkinter import messagebox
import customtkinter as ctk  # For modern UI elements

# Set appearance mode and default color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# Then you can modify individual colors if needed:
# ctk.set_widget_color("button", fg_color="#9c27b0", hover_color="#8e24aa")  # Set purple colors for buttons
# ctk.set_widget_color("frame", fg_color="#4a148c")  # Set dark purple for frames
# ctk.set_widget_color("label", text_color="#ba68c8")  # Set purple for labels

def get_exchange_rate(from_currency, to_currency):
    api_key = "8bf02fccfe81239f0e2ef21b"
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
    
    try:
        response = requests.get(url)
        data = response.json()
        if data['result'] == 'success':
            rates = data['conversion_rates']
            return rates.get(to_currency)
        else:
            return None
    except Exception as e:
        return None

class CurrencyConverterApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configure window
        self.title("Modern Currency Converter")
        self.geometry("500x600")
        self.configure(fg_color="#2E2E2E")

        # Create main frame
        self.main_frame = ctk.CTkFrame(self, fg_color="#2E2E2E", corner_radius=15)
        self.main_frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Title with modern styling
        self.title_label = ctk.CTkLabel(
            self.main_frame,
            text="Currency Converter",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color="#1a237e"
        )
        self.title_label.pack(pady=(30, 40))

        # Currency selection frame
        self.currency_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.currency_frame.pack(fill="x", padx=30, pady=10)

        # From Currency
        self.from_currency_label = ctk.CTkLabel(
            self.currency_frame,
            text="From Currency",
            font=ctk.CTkFont(size=14),
            text_color="#424242"
        )
        self.from_currency_label.pack(anchor="w")

        self.from_currency_var = tk.StringVar(value="USD")
        self.from_currency_combobox = ctk.CTkOptionMenu(
            self.currency_frame,
            values=["USD", "EUR", "GBP", "INR", "AUD", "JPY", "CAD", "CHF", "CNY", "NZD"],
            variable=self.from_currency_var,
            font=ctk.CTkFont(size=14),
            fg_color="#9c27b0",
            button_color="#1565c0",
            button_hover_color="#0d47a1",
            dropdown_hover_color="#1e88e5",
            dropdown_fg_color="#e3f2fd",
            dropdown_font=ctk.CTkFont(size=16)
        )
        self.from_currency_combobox.pack(fill="x", pady=(5, 20))

        # To Currency
        self.to_currency_label = ctk.CTkLabel(
            self.currency_frame,
            text="To Currency",
            font=ctk.CTkFont(size=14),
            text_color="#424242"
        )
        self.to_currency_label.pack(anchor="w")

        self.to_currency_var = tk.StringVar(value="EUR")
        self.to_currency_combobox = ctk.CTkOptionMenu(
            self.currency_frame,
            values=["USD", "EUR", "GBP", "INR", "AUD", "JPY", "CAD", "CHF", "CNY", "NZD"],
            variable=self.to_currency_var,
            font=ctk.CTkFont(size=14),
            fg_color="#9c27b0",
            button_color="#1565c0",
            button_hover_color="#0d47a1",
            dropdown_hover_color="#1e88e5",
            dropdown_fg_color="#e3f2fd",
            dropdown_font=ctk.CTkFont(size=16)
        )
        self.to_currency_combobox.pack(fill="x", pady=(5, 20))

        # Amount Entry
        self.amount_label = ctk.CTkLabel(
            self.currency_frame,
            text="Amount",
            font=ctk.CTkFont(size=14),
            text_color="#424242"
        )
        self.amount_label.pack(anchor="w")

        self.amount_entry = ctk.CTkEntry(
            self.currency_frame,
            placeholder_text="Enter amount",
            font=ctk.CTkFont(size=14),
            height=45,
            corner_radius=8
        )
        self.amount_entry.pack(fill="x", pady=(5, 30))

        # Convert Button
        self.convert_button = ctk.CTkButton(
            self.currency_frame,
            text="Convert",
            font=ctk.CTkFont(size=16, weight="bold"),
            height=45,
            corner_radius=8,
            fg_color="#2196f3",
            hover_color="#1976d2",
            command=self.convert_currency
        )
        self.convert_button.pack(fill="x", pady=(0, 20))

        # Result Frame
        self.result_frame = ctk.CTkFrame(
            self.main_frame,
            fg_color="#6a1b9a",
            corner_radius=10,
            height=100
        )
        self.result_frame.pack(fill="x", padx=30, pady=10)

        self.result_label = ctk.CTkLabel(
            self.result_frame,
            text="Converted amount will appear here",
            font=ctk.CTkFont(size=16),
            text_color="#ba68c8"
        )
        self.result_label.pack(pady=20)

    def convert_currency(self):
        try:
            amount = float(self.amount_entry.get())
            from_currency = self.from_currency_var.get()
            to_currency = self.to_currency_var.get()

            rate = get_exchange_rate(from_currency, to_currency)
            
            if rate:
                converted_amount = amount * rate
                self.result_label.configure(
                    text=f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}",
                    text_color="#1565c0"
                )
                self.result_frame.configure(fg_color="#e3f2fd")
            else:
                self.result_label.configure(
                    text="Error fetching exchange rates",
                    text_color="#d32f2f"
                )
                self.result_frame.configure(fg_color="#ffebee")
        except ValueError:
            self.result_label.configure(
                text="Please enter a valid amount",
                text_color="#d32f2f"
            )
            self.result_frame.configure(fg_color="#ffebee")

if __name__ == "__main__":
    app = CurrencyConverterApp()
    app.mainloop()