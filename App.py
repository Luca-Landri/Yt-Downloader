import tkinter as tk
from pytube import YouTube


root = tk.Tk()
root.config(bg="white")
root.geometry("600x400")
root.title("Landri Downloader")

frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor="center")

titleFrame = tk.Frame(frame)
titleFrame.pack(side="top")

image = tk.PhotoImage(file="./YTLogo.png")
image = image.subsample(3)
label = tk.Label(frame, text="INSERT THE LINK", font=("Verdana", 35), fg="red", width=20, height=2)
LinkInput = tk.Entry(frame, font=("Helvetica", 24))
Dlvideo = tk.Button(frame, text="Download", font=("Verdana", 24), command=lambda: download(LinkInput.get()), relief="ridge")

labelimg = tk.Label(titleFrame, image=image)
labelDl = tk.Label(titleFrame, text="DL", font=("Verdana", 60), fg="black", width=2, height=2)

labelimg.pack(side="left")
labelDl.pack(side="left")

label.pack()
Dlvideo.pack(side="bottom", pady=30)
LinkInput.pack(side="bottom")



label.configure(bg="white")
Dlvideo.configure(bg="white")
frame.configure(bg="white")
labelimg.configure(bg="white")
labelDl.configure(bg="white")
titleFrame.configure(bg="white")


root.mainloop()

