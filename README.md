# QR Code Generator Documentation

## Overview

This document provides a comprehensive overview of a QR Code Generator application built using Python's Tkinter library. The application allows users to input text, generate a QR code from that text, and download the QR code as an image file. The application utilizes the `qrcode` library for QR code generation and the `PIL` (Pillow) library for image handling.

## Dependencies

To run this application, the following libraries must be installed:
- `tkinter`: Standard Python interface to the Tk GUI toolkit.
- `qrcode`: Python library for generating QR codes.
- `Pillow`: Python Imaging Library for opening, manipulating, and saving image files.

You can install the required libraries using pip:

```bash
pip install qrcode[pil] pillow
```

## Code Description

### Global Variables

```python
generated_image = None
```
- **generated_image**: A global variable that stores the generated QR code image as a PIL Image object.

### Functions

#### `generate_qrcode()`

```python
def generate_qrcode():
```
- **Functionality**: This function handles the generation of the QR code based on user input. It retrieves the text from the entry field, validates it, and generates a QR code image.

- **Process**:
  1. Retrieves text input from `qr_text_entry`.
  2. Checks if the input text is not empty.
  3. Obtains the desired size from `size_var`.
  4. Creates a QRCode object and adds the input text.
  5. Generates the QR code image and resizes it according to the specified size.
  6. Updates the `generated_image` variable with the new image.
  7. Displays the QR code in the application window via `qr_label`.
  8. If the input is empty, displays a warning message.

#### `download_qrcode()`

```python
def download_qrcode():
```
- **Functionality**: This function handles downloading the generated QR code image as a PNG file.

- **Process**:
  1. Checks if `generated_image` is not `None`.
  2. Saves the image as "qrcode.png".
  3. Displays a success message upon saving.
  4. If no QR code has been generated, displays an error message.

### GUI Setup

The application window is set up as follows:

```python
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("500x500")
root.config(bg="#f0f0f0")
```
- **root**: The main Tkinter window object.
- **title**: Sets the title of the application window.
- **geometry**: Specifies the window size (500x500 pixels).
- **bg**: Sets the background color of the window.

### UI Components

- **Title Label**:
  ```python
  title_label = tk.Label(root, text="QR Code Generator", font=heading_font, bg="#f0f0f0", fg="#333333")
  ```
  - Displays the title of the application.

- **QR Code Text Entry**:
  ```python
  qr_text_entry = tk.Entry(root, width=40, font=("Helvetica", 12))
  ```
  - Allows the user to input the text to be converted into a QR code.

- **Size Selection Dropdown**:
  ```python
  size_var = tk.StringVar(value="200")
  size_menu = tk.OptionMenu(root, size_var, "100", "200", "300", "400")
  ```
  - Lets the user select the size of the generated QR code from predefined options (100, 200, 300, 400).

- **Buttons**:
  - **Generate QR Code**:
    ```python
    generate_button = tk.Button(root, text="Generate QR Code", command=generate_qrcode, font=("Helvetica", 12), bg="#4CAF50", fg="white", relief="raised", bd=2)
    ```
    - Calls the `generate_qrcode()` function when clicked.
  
  - **Download QR Code**:
    ```python
    download_button = tk.Button(root, text="Download QR Code", command=download_qrcode, font=("Helvetica", 12), bg="#2196F3", fg="white", relief="raised", bd=2)
    ```
    - Calls the `download_qrcode()` function when clicked.
    - This will download the image in the same folder but change the location to save the image.

- **QR Code Display Label**:
  ```python
  qr_label = tk.Label(root, bg="#f0f0f0")
  ```
  - Displays the generated QR code image.

### Main Event Loop

```python
root.mainloop()
```
- Starts the Tkinter event loop, allowing the application to run and respond to user input.

## Conclusion

This QR Code Generator application provides an intuitive interface for generating and downloading QR codes based on user input. With its straightforward design and functionality, it serves as a practical tool for various applications, from sharing links to storing contact information.