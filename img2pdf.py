from PIL import Image
import tkinter as tk
from tkinter import Tk, ttk, Button, Canvas, Label
import os

window = Tk()
window.geometry("1000x600")
os_name=os.name
window.title(f"Bilder Konvertieren nach PDF-Dokument (Betriebssystem={os.name})")
def konvertieren():
    images = [
        Image.open("/home/gert/Bilder/" + f)
        for f in ["20230821_112419.jpg", "20230821_112447.jpg"]
    ]
    pdf_path = "/home/gert/Bilder/bilder-test.pdf"
        
    images[0].save(
        pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:]
    )
canvas = Canvas(window,width = 600,height = 400,bg = 'white')
#canvas.pack()
canvas.pack(anchor=tk.CENTER, expand=True)

python_image = tk.PhotoImage(file='/home/gert/Bilder/pinwheel-8829_128.gif')
canvas.create_image(
    (100, 100),
    image=python_image
)
Suche_Bild_Text = "Suche Bild im Dateisystem"
l1 = Label (window,text=Suche_Bild_Text)
l1.place(x = 200, y = 250, width=120, height=15)

'''
# Load the image file
im = Image.open('/home/gert/Bilder/20230821_112419.jpg')
# Put the image into a canvas compatible class, and stick in an
# arbitrary variable to the garbage collector doesn't destroy it
canvas.image = Image.PhotoImage(im)
# Add the image to the canvas, and set the anchor to the top left / north west corner
canvas.create_image(0, 0, image=canvas.image, anchor='nw')
'''
window.mainloop()
