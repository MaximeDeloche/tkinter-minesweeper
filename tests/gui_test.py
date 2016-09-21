#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk

window = tk.Tk()

def fct(event):
    event.widget["state"] = "disabled"

f = tk.Frame(window, height=200, width=100)
f.pack_propagate(False)
f.pack()
b = tk.Button(f, text="Bonjour")
b.pack(fill=tk.BOTH, expand=True)
b.bind("<Button-3>", fct)


window.mainloop()
