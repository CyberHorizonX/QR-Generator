import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont
import qrcode
from PIL import ImageTk, Image

# Store the generated PIL image globally
generated_image = None



def generate_qrcode():
    global generated_image  # Declare to use the global variable
    
    qr_text = qr_text_entry.get()
    if len(qr_text) > 0:
        size = int(size_var.get())
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_text)
        qr.make(fit=True)
        
        # Generate the PIL image
        img = qr.make_image(fill='black', back_color='white').resize((size, size))
        generated_image = img  # Store the generated image globally
        
        # Display QR Code in the window
        img_tk = ImageTk.PhotoImage(img)
        qr_label.config(image=img_tk)
        qr_label.image = img_tk
    else:
        messagebox.showwarning("Input Error", "Please enter text to generate QR code.")

def download_qrcode():
    global generated_image  # Use the global generated image
    
    if generated_image:
        # Save the PIL image as a file
        generated_image.save("qrcode.png")
        messagebox.showinfo("Success", "QR code saved as qrcode.png")
    else:
        messagebox.showwarning("Error", "No QR code to download.")

# Set up the window
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("500x500")
root.config(bg="#f0f0f0")

# Set a custom font for headings
heading_font = tkfont.Font(family="Helvetica", size=16, weight="bold")

# Add a title label
title_label = tk.Label(root, text="QR Code Generator", font=heading_font, bg="#f0f0f0", fg="#333333")
title_label.pack(pady=20)

# Entry to input QR code text
qr_text_entry = tk.Entry(root, width=40, font=("Helvetica", 12))
qr_text_entry.pack(pady=10)

# Dropdown for size selection
size_var = tk.StringVar(value="200")  # Default size
size_menu = tk.OptionMenu(root, size_var, "100", "200", "300", "400")
size_menu.config(font=("Helvetica", 12), bg="#ffffff", width=10)
size_menu.pack(pady=10)

# Buttons to generate QR code and download
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qrcode, font=("Helvetica", 12), bg="#4CAF50", fg="white", relief="raised", bd=2)
generate_button.pack(pady=10, ipady=5)

download_button = tk.Button(root, text="Download QR Code", command=download_qrcode, font=("Helvetica", 12), bg="#2196F3", fg="white", relief="raised", bd=2)
download_button.pack(pady=10, ipady=5)

# Label to display the generated QR code
qr_label = tk.Label(root, bg="#f0f0f0")
qr_label.pack(pady=20)

# Start the GUI event loop
root.mainloop()
