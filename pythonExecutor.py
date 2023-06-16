import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox as messagebox
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import sys
import requests
import random
import string
import time
import concurrent.futures

BACKGROUND_COLOR = "#2c2c2c"
TEXT_COLOR = "#ffffff"
BUTTON_COLOR = "#383838"
BUTTON_TEXT_COLOR = "#ffffff"

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
    if file_path:
        try:
            with open(file_path, "r") as file:
                script = file.read()
                code_entry.delete("1.0", tk.END)
                code_entry.insert(tk.END, script)
        except Exception as e:
            messagebox.showerror("Error", str(e))

def save_file():
    script = code_entry.get("1.0", tk.END)
    file_path = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python Files", "*.py")])
    if file_path:
        try:
            with open(file_path, "w") as file:
                file.write(script)
                messagebox.showinfo("Success", "File saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

def execute_script():
    script = code_entry.get("1.0", tk.END)

    try:
        exec(script)
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return

    messagebox.showinfo("Success", "Script executed successfully.")

def clear_code():
    code_entry.delete("1.0", tk.END)

def exit_application():
    sys.exit()

window = tk.Tk()
window.title("Python Script Executor")
window.configure(bg=BACKGROUND_COLOR)

code_frame = tk.Frame(window, bg=BACKGROUND_COLOR)
code_frame.grid(row=0, column=0, sticky="nsew")

code_entry = tk.Text(code_frame, font=("Courier New", 11), wrap='none', bg=BACKGROUND_COLOR, fg=TEXT_COLOR)
code_entry.grid(row=0, column=0, sticky="nsew")

vscrollbar = tk.Scrollbar(code_frame, orient=tk.VERTICAL, command=code_entry.yview, bg=BACKGROUND_COLOR)
vscrollbar.grid(row=0, column=1, sticky="ns")

hscrollbar = tk.Scrollbar(code_frame, orient=tk.HORIZONTAL, command=code_entry.xview, bg=BACKGROUND_COLOR)
hscrollbar.grid(row=1, column=0, sticky="ew")

code_entry.config(yscrollcommand=vscrollbar.set, xscrollcommand=hscrollbar.set)

code_frame.rowconfigure(0, weight=1)
code_frame.columnconfigure(0, weight=1)

button_frame = tk.Frame(window, bg=BACKGROUND_COLOR)
button_frame.grid(row=1, column=0, sticky="ew", padx=10, pady=10)

execute_button = tk.Button(button_frame, text="Execute", command=execute_script, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR)
execute_button.pack(side=tk.LEFT, padx=(0, 10))

clear_button = tk.Button(button_frame, text="Clear", command=clear_code, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR)
clear_button.pack(side=tk.LEFT, padx=(0, 10))

open_button = tk.Button(button_frame, text="Open File", command=open_file, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR)
open_button.pack(side=tk.LEFT, padx=(0, 10))

save_button = tk.Button(button_frame, text="Save File", command=save_file, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR)
save_button.pack(side=tk.LEFT, padx=(0, 10))

exit_button = tk.Button(button_frame, text="Exit", command=exit_application, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR)
exit_button.pack(side=tk.RIGHT)

window.mainloop()
