# Password Generator GUI

A small Tkinter app that fetches a random, memorable password from the [password.ninja](https://password.ninja) API.

- **Generate** requests a new password; **Copy** puts it on the clipboard.
- Handles network failures without crashing.
- `.pyw` extension means it launches without a console window on Windows.

```bash
pip install requests
python passwordninja.pyw
```

Tkinter ships with Python on Windows and macOS. On Debian/Ubuntu/Fedora, install it with your package manager (`python3-tk` / `python3-tkinter`).
