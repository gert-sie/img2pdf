from PIL import Image  # install by > python3 -m pip install --upgrade Pillow  # ref. https://pillow.readthedocs.io/en/latest/installation.html#basic-installation

images = [
    Image.open("/home/gert/Bilder/" + f)
    for f in ["20240523_011830.jpg", "20240523_011913.jpg", "20240523_012402.jpg"]
]

pdf_path = "/home/gert/Bilder/bbd1.pdf"
    
images[0].save(
    pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:]
)
