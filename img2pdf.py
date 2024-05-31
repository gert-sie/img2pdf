from PIL import Image
import tkinter as tk
from tkinter import Tk, ttk, Button, Canvas
import os

window = Tk()
window.geometry("1000x600")
os_name=os.name
window.title(f"Bilder Konvertieren nach PDF-Dokument (Betriebssystem={os.name})")
images = [
    Image.open("/home/gert/Bilder/" + f)
    for f in ["20230821_112419.jpg", "20230821_112447.jpg"]
]
pdf_path = "/home/gert/Bilder/bilder-test.pdf"
    
images[0].save(
    pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:]
)
canvas = Canvas(window,width = 600,height = 400,bg = 'white')
canvas.pack()
python_image = tk.PhotoImage(f'/home/gert/Bilder/pinwheel-8829_128.gif')
image_item = canvas.create_image(
    (10, 10),
    image=python_image
)
canvas = tk.Canvas(root, width=600, height=400, bg='white')
canvas.pack(anchor=tk.CENTER, expand=True)

python_image = tk.PhotoImage(file='/home/gert/Bilder/pinwheel-8829_128.gif')
canvas.create_image(
    (100, 100),
    image=python_image
)

window.mainloop()
