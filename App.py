import tkinter as tk
import yt_dlp
from tkinter import filedialog
import threading

root = tk.Tk()
root.config(bg="white")
root.geometry("600x450")
root.title("Landri Downloader")


def download(url: str):
    path = filedialog.askdirectory()
    ydl_opts = {
        'outtmpl': f'{path}/%(title)s',
        'noplaylist': True,
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    }

    if url: 
        if path:
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                print(f"Download successful! Saved to {path}.")
                DlCompleted.pack()
            except Exception as e:
                print(f"An error occurred while downloading the video: {e}")
            finally:
                DlButton.config(state='normal')
                LinkInput.delete(0, tk.END)
        else:
            print("No path selected.")
            DlButton.config(state='normal')
            LinkInput.delete(0, tk.END)
            LinkInput.config(highlightbackground="red")
    else:
        print("No URL inserted.")
        DlButton.config(state='normal')
        LinkInput.delete(0, tk.END)
        LinkInput.config(highlightbackground="red")



def download_thread():
    DlButton.config(state='disabled')
    threading.Thread(target=download, args=(LinkInput.get(),)).start()


img = tk.PhotoImage(file="./Images/logo.png")
root.tk.call('wm', 'iconphoto', root._w, img)

frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor="center")

titleFrame = tk.Frame(frame)
titleFrame.pack(side="top")

image = tk.PhotoImage(file="./Images/YTLogo.png")
image = image.subsample(3)
label = tk.Label(frame, text="Insert the video link:", font=("Arial", 30), fg="black", width=40, height=2)
LinkInput = tk.Entry(frame, font=("Arial", 24), width=30, insertbackground='black', bg='white', bd=3, relief="solid", fg="black")
DlButton = tk.Button(frame, text="Download", command=download_thread, width=15, font=("Arial", 25))
DlCompleted = tk.Label(frame, text="Completed!", font=("Arial", 20), fg="black", width=40, height=2)


labelimg = tk.Label(titleFrame, image=image)
labelDl = tk.Label(titleFrame, text="DL", font=("Verdana", 50), fg="black", width=2, height=2)

labelimg.pack(side="left")
labelDl.pack(side="left")

label.pack()
DlButton.pack(side="bottom", pady=15)
LinkInput.pack(side="bottom", pady=15)

frame.configure(bg="white")
label.configure(bg="white")
frame.configure(bg="white")
labelimg.configure(bg="white")
labelDl.configure(bg="white")
titleFrame.configure(bg="white")
DlButton.configure(bg="white")
DlCompleted.configure(bg="white")

root.mainloop()
