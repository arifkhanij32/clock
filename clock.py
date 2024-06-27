import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import time
import os

class NatureClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Clock")

        # Image paths
        self.image_dir = "C:/Users/Anifkhan/Desktop/Digit_clock&calculator/clock/templates"
        self.morning_img = self.load_image("morning.jpg")
        self.afternoon_img = self.load_image("afternoon.jpg")
        self.evening_img = self.load_image("evening.jpg")
        self.night_img = self.load_image("night.jpg")

        # Background label
        self.bg_label = tk.Label(self.root)
        self.bg_label.pack(fill=tk.BOTH, expand=tk.YES)

        # Time label
        self.time_label = tk.Label(self.root, font=('Helvetica', 48), fg='white', bg='black')
        self.time_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Update the time and background
        self.update_clock()

    def load_image(self, filename):
        path = os.path.join(self.image_dir, filename)
        try:
            return ImageTk.PhotoImage(Image.open(path))
        except FileNotFoundError:
            print(f"Error: The file {path} was not found.")
            return None

    def update_clock(self):
        current_time = time.strftime("%H:%M:%S")
        self.time_label.config(text=current_time)

        current_hour = int(time.strftime("%H"))

        if 6 <= current_hour < 12:
            self.bg_label.config(image=self.morning_img)
        elif 12 <= current_hour < 18:
            self.bg_label.config(image=self.afternoon_img)
        elif 18 <= current_hour < 21:
            self.bg_label.config(image=self.evening_img)
        else:
            self.bg_label.config(image=self.night_img)

        self.root.after(1000, self.update_clock)

if __name__ == "__main__":
    root = tk.Tk()
    app = NatureClock(root)
    root.geometry("800x600")
    root.mainloop()
