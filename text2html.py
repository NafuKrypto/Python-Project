# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 17:41:50 2022

@author: hp
"""

import textile

import tkinter as tk

def convertToHtml():
    inp = T.get(1.0, "end-1c")
    html = textile.textile( inp )
    print("\nAfter converted to HTML: \n",html)
    lbl.config(text = "Converted Html : "+html) 
 
root = tk.Tk()
 
# specify size of window.
root.geometry("250x170")
 
# Create text widget and specify size.
T = tk.Text(root, height = 5, width = 52)

# Create button for next text.
T.pack()
b1 = tk.Button(root, text = "Submit", command=convertToHtml)
b1.pack() 

lbl = tk.Label(root, text = "")
lbl.pack() 
# Insert The Fact.
T.insert(tk.END,"""""" )
# Label Creation
tk.mainloop()
