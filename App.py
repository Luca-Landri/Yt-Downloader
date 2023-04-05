import tkinter as tk
root = tk.Tk()
root.geometry("600x400")
root.title("Landri Downloader")


label = tk.Label(root, text="Hello World", font=("Helvetica", 24))
label.pack(side=tk.TOP, pady = (150, 0))


button = tk.Button(root, text="Click Me")
button.pack(side=tk.BOTTOM, pady = (0, 150))

root.mainloop()
