import tkinter as tk
from tkinter import messagebox
import json
import urllib.request
import urllib.error

API_URL = "http://127.0.0.1:8000"


def call_api(method, path, data=None):
    url = API_URL + path
    body = None
    headers = {"Content-Type": "application/json"}
    if data is not None:
        body = json.dumps(data).encode("utf-8")
    request = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(request, timeout=5) as response:
            return response.status, json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        try:
            detail = json.loads(e.read().decode("utf-8"))
        except Exception:
            detail = {"error": str(e)}
        return e.code, detail
    except Exception as e:
        return None, {"error": "Cannot connect to FastAPI. Start the backend first.", "detail": str(e)}


def show_response(status, data):
    status_label.config(text=f"HTTP Status: {status if status else 'ERROR'}")
    output.delete("1.0", tk.END)
    output.insert(tk.END, json.dumps(data, indent=4, ensure_ascii=False))


def get_character(path):
    status, data = call_api("GET", path)
    show_response(status, data)


def add_character():
    name = name_entry.get().strip()
    age_text = age_entry.get().strip()
    show = show_entry.get().strip()
    power = power_entry.get().strip()
    if not name or not age_text or not show or not power:
        messagebox.showwarning("Missing data", "Please fill all fields.")
        return
    try:
        age = int(age_text)
    except ValueError:
        messagebox.showerror("Invalid age", "Age must be a number.")
        return
    payload = {"name": name, "age": age, "show": show, "power": power}
    status, data = call_api("POST", "/character", payload)
    show_response(status, data)


root = tk.Tk()
root.title("Cartoon API - Python Frontend")
root.geometry("850x650")
root.configure(padx=20, pady=20)

header = tk.Label(root, text="Cartoon API", font=("Arial", 24, "bold"))
header.pack(pady=(0, 5))
tk.Label(root, text="Click a button to send a request to FastAPI", font=("Arial", 11)).pack(pady=(0, 15))

buttons = tk.Frame(root)
buttons.pack(pady=5)
for text, path in [("Shinchan", "/shinchan"), ("Doraemon", "/doraemon"), ("Ben 10", "/ben10"), ("All Characters", "/characters")]:
    tk.Button(buttons, text=text, width=16, command=lambda p=path: get_character(p)).pack(side=tk.LEFT, padx=5)

status_label = tk.Label(root, text="HTTP Status: -", font=("Arial", 11, "bold"))
status_label.pack(anchor="w", pady=(20, 5))
output = tk.Text(root, height=15, width=95, font=("Consolas", 11))
output.pack(fill="both", expand=True)

form = tk.LabelFrame(root, text="POST /character - Add a character", padx=10, pady=10)
form.pack(fill="x", pady=15)

fields = [("Name", 0), ("Age", 1), ("Show", 2), ("Power", 3)]
entries = []
for label, col in fields:
    tk.Label(form, text=label).grid(row=0, column=col, padx=5)
    entry = tk.Entry(form, width=16)
    entry.grid(row=1, column=col, padx=5)
    entries.append(entry)
name_entry, age_entry, show_entry, power_entry = entries

tk.Button(form, text="POST Character", command=add_character, width=18).grid(row=1, column=4, padx=10)

root.mainloop()
