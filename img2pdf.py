from PIL import Image  # install by > python3 -m pip install --upgrade Pillow  # ref. https://pillow.readthedocs.io/en/latest/installation.html#basic-installation

images = [
    Image.open("/Users/apple/Desktop/" + f)
    for f in ["bbd.jpg", "bbd1.jpg", "bbd2.jpg"]
]

pdf_path = "/Users/apple/Desktop/bbd1.pdf"
    
images[0].save(
    pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:]
)
