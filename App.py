import tkinter as tk
import yt_dlp
from tkinter import filedialog

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

root = tk.Tk()
root.config(bg="white")
root.geometry("600x450")
root.title("Landri Downloader")

frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor="center")

titleFrame = tk.Frame(frame)
titleFrame.pack(side="top")

image = tk.PhotoImage(file="./YTLogo.png")
image = image.subsample(3)
label = tk.Label(frame, text="INSERT THE LINK", font=("Verdana", 35), fg="red", width=20, height=2)
LinkInput = tk.Entry(frame, font=("Helvetica", 24), width=30)
Dlvideo = tk.Button(frame, text="Download", font=("Verdana", 24), command=lambda: download(LinkInput.get()))

labelimg = tk.Label(titleFrame, image=image)
labelDl = tk.Label(titleFrame, text="DL", font=("Verdana", 60), fg="black", width=2, height=2)

labelimg.pack(side="left")
labelDl.pack(side="left")

label.pack()
Dlvideo.pack(side="bottom", pady=30)
LinkInput.pack(side="bottom")


frame.configure(bg="white")
label.configure(bg="white")
Dlvideo.configure(bg="white")
frame.configure(bg="white")
labelimg.configure(bg="white")
labelDl.configure(bg="white")
titleFrame.configure(bg="white")


root.mainloop()

