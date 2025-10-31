# calc_gui_safe.py
import tkinter as tk
from tkinter import messagebox
from calc_cli_safe import safe_eval   # pastikan file calc_cli_safe.py ada di folder yang sama

class CalcGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Safe Calculator GUI")
        self.geometry("320x420")
        self.resizable(False, False)

        self.entry = tk.Entry(self, font=("Arial", 18), borderwidth=2, relief="groove")
        self.entry.pack(fill="x", padx=10, pady=10, ipady=8)

        btns = [
            ['7','8','9','/'],
            ['4','5','6','*'],
            ['1','2','3','-'],
            ['0','.','%','+'],
            ['(',')','**','C'],
            ['sqrt','sin','cos','=']
        ]

        for r, row in enumerate(btns):
            frame = tk.Frame(self)
            frame.pack(expand=True, fill="both")
            for c, ch in enumerate(row):
                b = tk.Button(frame, text=ch, font=("Arial", 14), command=lambda ch=ch: self.on_button(ch))
                b.pack(side="left", expand=True, fill="both", padx=2, pady=2)

    def on_button(self, ch):
        if ch == 'C':
            self.entry.delete(0, tk.END)
            return
        if ch == '=':
            expr = self.entry.get()
            try:
                val = safe_eval(expr)
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(val))
            except Exception as e:
                messagebox.showerror("Error", str(e))
            return
        # fungsi matematika seperti sqrt akan dimasukkan sebagai nama panggilan
        if ch in ('sqrt','sin','cos'):
            self.entry.insert(tk.END, f"{ch}(")
        else:
            self.entry.insert(tk.END, ch)

if __name__ == "__main__":
    app = CalcGUI()
    app.mainloop()
