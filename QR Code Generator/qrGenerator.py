import pyqrcode
from tkinter import *
import os

# This Function is responsible to take the input -> Convert it to Image Code -> Convert Image code to png.
def get_code():
    data_var = data.get()
    qr = pyqrcode.create(str(data_var))
    
    # Kullanıcının masaüstünde "png" adlı bir klasörü varsa, bu klasöre kaydedilir.
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    output_path = os.path.join(desktop_path, "png", "code.png")
    
    # Klasörü oluştur
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    qr.png(output_path, scale=6)

# Get a Tk window of 400 * 200
base = Tk()
base.geometry("400x200")
base.title("QR Kod Oluşturucu")

# Variable to store text for QR Code
data = StringVar()

# Field to input text
dataEntry = Entry(textvariable=data, width="30")
dataEntry.place(x=80, y=50)

# Call get_code() on click
button = Button(base, text="Oluştur", command=get_code, width="30", height="2", bg="grey")
button.place(x=80, y=100)

base.mainloop()

