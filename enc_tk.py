import cv2
import os
import tkinter as tk
from tkinter import filedialog, messagebox

class ImageEncryptorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Encryptor")
        self.root.geometry("400x300")
        
        # Select Image
        self.select_btn = tk.Button(root, text="Select Image", command=self.select_image)
        self.select_btn.pack(pady=10)
        
        self.image_path_label = tk.Label(root, text="No image selected")
        self.image_path_label.pack()
        
        # Secret Message Entry
        tk.Label(root, text="Enter Secret Message:").pack()
        self.msg_entry = tk.Entry(root, width=40)
        self.msg_entry.pack(pady=5)
        
        # Password Entry
        tk.Label(root, text="Enter Password:").pack()
        self.pass_entry = tk.Entry(root, width=20, show="*")
        self.pass_entry.pack(pady=5)
        
        # Encrypt Button
        self.encrypt_btn = tk.Button(root, text="Encrypt", command=self.encrypt_message)
        self.encrypt_btn.pack(pady=10)

    def select_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
        if self.image_path:
            self.image_path_label.config(text=f"Selected: {os.path.basename(self.image_path)}")

    def encrypt_message(self):
        if not hasattr(self, "image_path") or not self.image_path:
            messagebox.showerror("Error", "No image selected!")
            return

        msg = self.msg_entry.get()
        password = self.pass_entry.get()

        if not msg or not password:
            messagebox.showerror("Error", "Message and Password cannot be empty!")
            return

        # Append delimiter to message
        msg += '###'
        
        img = cv2.imread(self.image_path)
        if img is None:
            messagebox.showerror("Error", "Error loading image.")
            return
        
        binary_msg = ''.join([format(ord(char), '08b') for char in msg])
        data_len = len(binary_msg)
        
        if data_len > img.shape[0] * img.shape[1] * 3:
            messagebox.showerror("Error", "Message is too long to be encoded in the selected image.")
            return

        data_index = 0
        for values in img:
            for pixel in values:
                for i in range(3):
                    if data_index < data_len:
                        pixel[i] = int(format(pixel[i], '08b')[:-1] + binary_msg[data_index], 2)
                        data_index += 1
                    if data_index >= data_len:
                        break

        encrypted_path = "encryptedImage.png"
        cv2.imwrite(encrypted_path, img)
        with open("passcode.txt", "w") as file:
            file.write(password)

        os.system(f"start {encrypted_path}")
        messagebox.showinfo("Success", "Message encrypted and saved!")

# Run the GUI application
root = tk.Tk()
app = ImageEncryptorApp(root)
root.mainloop()
