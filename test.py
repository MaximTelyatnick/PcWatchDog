import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import argparse
import json

class MessageApp:
    def __init__(self, root, token="", channel_id="", message=""):
        self.root = root
        self.root.title("Message Sender")
        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Arial", 12), padding=5)
        self.style.configure("TButton", font=("Arial", 12), padding=5)
        self.style.configure("TEntry", font=("Arial", 12), padding=5)

        # Frame for padding
        self.main_frame = ttk.Frame(root, padding="10 10 10 10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Token
        self.token_label = ttk.Label(self.main_frame, text="Token:")
        self.token_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        self.token_entry = ttk.Entry(self.main_frame, width=40)
        self.token_entry.grid(row=0, column=1, padx=10, pady=10)
        self.token_entry.insert(0, token)  # Pre-fill the token entry if provided

        # Channel ID
        self.channel_id_label = ttk.Label(self.main_frame, text="Channel ID:")
        self.channel_id_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        self.channel_id_entry = ttk.Entry(self.main_frame, width=40)
        self.channel_id_entry.grid(row=1, column=1, padx=10, pady=10)
        self.channel_id_entry.insert(0, channel_id)  # Pre-fill the channel ID entry if provided

        # Message
        self.message_label = ttk.Label(self.main_frame, text="Message:")
        self.message_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
        self.message_entry = ttk.Entry(self.main_frame, width=40)
        self.message_entry.grid(row=2, column=1, padx=10, pady=10)
        self.message_entry.insert(0, message)  # Pre-fill the message entry if provided

        # Send Button
        self.send_button = ttk.Button(self.main_frame, text="Send", command=self.send_message)
        self.send_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Save Button
        self.save_button = ttk.Button(self.main_frame, text="Save", command=self.save_data)
        self.save_button.grid(row=4, column=0, columnspan=2, pady=10)

    def send_message(self):
        token = self.token_entry.get()
        channel_id = self.channel_id_entry.get()
        message = self.message_entry.get()

        # Here you would add your logic to send the message
        # For demonstration purposes, we'll just show a message box
        messagebox.showinfo("Info", f"Token: {token}\nChannel ID: {channel_id}\nMessage: {message}")

    def save_data(self):
        data = {
            "token": self.token_entry.get(),
            "channel_id": self.channel_id_entry.get(),
            "message": self.message_entry.get()
        }

        with open("data.json", "w") as outfile:
            json.dump(data, outfile)
        
        messagebox.showinfo("Info", "Data saved successfully")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Message Sender Application")
    parser.add_argument("--token", type=str, help="Token for authentication", default="")
    parser.add_argument("--channel_id", type=str, help="Channel ID to send message to", default="")
    parser.add_argument("--message", type=str, help="Message to send", default="")
    
    args = parser.parse_args()
    
    root = tk.Tk()
    app = MessageApp(root, token=args.token, channel_id=args.channel_id, message=args.message)
    root.mainloop()