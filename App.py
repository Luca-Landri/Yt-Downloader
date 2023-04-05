import tkinter as tk
from pytube import YouTube


root = tk.Tk()
root.geometry("600x400")
root.title("Landri Downloader")

frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor="center")


label = tk.Label(frame, text="INSERT THE LINK", font=("Helvetica", 35), fg="red", width=20, height=2)
input_field = tk.Entry(frame, font=("Helvetica", 24))
button = tk.Button(frame, text="Download", font=("Helvetica", 24), command=lambda: download(input_field.get()), pady=10, padx=10)


label.pack(side="top", fill="both")
input_field.pack( side="top", fill="both")
button.pack(side=tk.TOP)

root.mainloop()
