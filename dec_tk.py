import cv2
import os
import tkinter as tk
from tkinter import filedialog, messagebox

class ImageDecryptorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Decryptor")
        self.root.geometry("400x300")
        
        # Select Image
        self.select_btn = tk.Button(root, text="Select Image", command=self.select_image)
        self.select_btn.pack(pady=10)
        
        self.image_path_label = tk.Label(root, text="No image selected")
        self.image_path_label.pack()
        
        # Password Entry
        tk.Label(root, text="Enter Password:").pack()
        self.pass_entry = tk.Entry(root, width=20, show="*")
        self.pass_entry.pack(pady=5)
        
        # Decrypt Button
        self.decrypt_btn = tk.Button(root, text="Decrypt", command=self.decrypt_message)
        self.decrypt_btn.pack(pady=10)

    def select_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
        if self.image_path:
            self.image_path_label.config(text=f"Selected: {os.path.basename(self.image_path)}")

    def decrypt_message(self):
        if not hasattr(self, "image_path") or not self.image_path:
            messagebox.showerror("Error", "No image selected!")
            return

        try:
            with open("passcode.txt", "r") as file:
                stored_password = file.read().strip()
        except FileNotFoundError:
            messagebox.showerror("Error", "Password file not found!")
            return

        pas = self.pass_entry.get()
        if pas != stored_password:
            messagebox.showerror("Error", "Incorrect password!")
            return

        img = cv2.imread(self.image_path)
        if img is None:
            messagebox.showerror("Error", "Error loading image.")
            return

        binary_msg = ''
        for values in img:
            for pixel in values:
                for i in range(3):
                    binary_msg += format(pixel[i], '08b')[-1]

        all_bytes = [binary_msg[i:i+8] for i in range(0, len(binary_msg), 8)]
        decoded_msg = ''
        for byte in all_bytes:
            decoded_msg += chr(int(byte, 2))
            if decoded_msg[-3:] == '###':
                break

        messagebox.showinfo("Decrypted Message", f"Decrypted Message: {decoded_msg[:-3]}")

# Run the GUI application
root = tk.Tk()
app = ImageDecryptorApp(root)
root.mainloop()
