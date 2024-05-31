from PIL import Image  
'''from tkinter import *'''
from tkinter import Tk, Button, Canvas
import os

window = Tk()
window.geometry("1000x600")
os_name=os.name
window.title(f"Bilder Konvertieren nach PDF-Dokument (Betriebssystem={os.name})")
images = [
    Image.open("/home/gert/Bilder/" + f)
    for f in ["20230821_112419.jpg", "20230821_112447.jpg"]
]
canvas = Canvas(window,width = 600,height = 400,bg = '#6699ff')
pdf_path = "/home/gert/Bilder/bilder-test.pdf"
    
images[0].save(
    pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:]
)
canvas.pack()
python_image = tk.PhotoImage(file='/home/gert/Bilder/20230821_112419.jpg')
canvas.create_image(
    (100, 100),
    image=python_image
window.mainloop()
