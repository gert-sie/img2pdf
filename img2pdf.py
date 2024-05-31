from PIL import Image  
from tkinter import ttk

window = Tk()
window.geometry("1000x600")
os_name=os.name
window.title(f"Bilder Konvertieren nach PDF-Dokument (Betriebssystem={os.name})")
images = [
    Image.open("/home/gert/Bilder/" + f)
    for f in ["*.jpg"]
]

pdf_path = "/home/gert/Bilder/bilder-test.pdf"
    
images[0].save(
    pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:]
)
