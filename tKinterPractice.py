import tkinter as tk
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
import weather_forecast


def my_function():
    print("Button clicked!")

root = tk.Tk()

style = ttk.Style()
style.configure("TButton", foreground="dark blue", background="white")

label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 18), foreground="blue")
label.pack(pady=20)

button = tk.Button(root, text="Click Me", background="light blue", padx=10, pady=5, command=my_function)
button.pack()

entry = tk.Entry(root)
entry.pack()

# image = Image.open("example.jpeg")
# tk_image = ImageTk.PhotoImage(image)


# label = tk.Label(root, image=tk_image)
label.pack()


root.mainloop()
