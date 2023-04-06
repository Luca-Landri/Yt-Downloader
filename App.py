import tkinter as tk
import yt_dlp
from tkinter import filedialog
from tkinter import ttk

root = tk.Tk()
style = ttk.Style()
root.config(bg="white")
root.geometry("600x450")
root.title("Landri Downloader")


def download(url: str):
    path = filedialog.askdirectory()
    ydl_opts = {
        'outtmpl': f'{path}/%(title)s',
        'noplaylist': True,
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
    }

    if path:
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download(url)
            print(f"Download successful! Saved to {path}.")
        except Exception as e:
            print(f"An error occurred while downloading the video: {e}")




img = tk.PhotoImage(file="./Images/logo.png")
root.tk.call('wm', 'iconphoto', root._w, img)

frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor="center")

titleFrame = tk.Frame(frame)
titleFrame.pack(side="top")

image = tk.PhotoImage(file="./Images/YTLogo.png")
image = image.subsample(3)
label = tk.Label(frame, text="Insert the video link:", font=("Arial", 30), fg="black", width=40, height=2)
LinkInput = tk.Entry(frame, font=("Arial", 24), width=30, insertbackground='black', bg= 'white', bd= 3, relief= "solid", fg='black')
DlButton = tk.Button(frame, text="Download", command=lambda: download(LinkInput.get()), width=15, font=("Arial", 25))

labelimg = tk.Label(titleFrame, image=image)
labelDl = tk.Label(titleFrame, text="DL", font=("Verdana", 60), fg="black", width=2, height=2)

labelimg.pack(side="left")
labelDl.pack(side="left")

label.pack()
DlButton.pack(side="bottom", pady=30)
LinkInput.pack(side="bottom")


frame.configure(bg="white")
label.configure(bg="white")
frame.configure(bg="white")
labelimg.configure(bg="white")
labelDl.configure(bg="white")
titleFrame.configure(bg="white")
DlButton.configure(bg="white")


root.mainloop()

