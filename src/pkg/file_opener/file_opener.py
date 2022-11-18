import tkinter as tk
from tkinter import filedialog

def open_file() -> str:
  tk.Tk().withdraw()
  file_path = filedialog.askopenfilename()
  return file_path