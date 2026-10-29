"""Small Tkinter app that fetches a random password from the password.ninja API.

Click "Generate" to get a password, "Copy" to put it on the clipboard.
Requires the 'requests' package (see requirements.txt).
"""

import tkinter as tk

import requests

API_URL = (
    "https://password.ninja/api/password"
    "?minPassLength=12&instruments=true&colours=true&shapes=true&food=true"
    "&sports=true&transport=true&symbols=true&numOfPasswords=1&maxLength=14"
    "&excludeSymbols=sfha"
)
TIMEOUT_SECONDS = 10


def fetch_password():
    """Return a password string from the API. Raises requests.RequestException on failure."""
    response = requests.get(API_URL, timeout=TIMEOUT_SECONDS)
    response.raise_for_status()
    return response.text.strip().strip('"').capitalize()


def set_entry_text(text):
    password_entry.delete(0, tk.END)
    password_entry.insert(0, text)


def generate_password():
    try:
        set_entry_text(fetch_password())
    except requests.RequestException:
        set_entry_text("Failed to retrieve password")


def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    root.update()  # keeps the text on the clipboard after the window closes


root = tk.Tk()
root.title("Password Generator")

entry_frame = tk.Frame(root)
entry_frame.pack(pady=20)

password_entry = tk.Entry(entry_frame, font=("Helvetica", 24), bd=0, bg="lightgrey")
password_entry.pack(padx=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

tk.Button(button_frame, text="Generate", command=generate_password).grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="Copy", command=copy_password).grid(row=0, column=1, padx=10)

root.mainloop()
