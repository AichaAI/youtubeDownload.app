from tkinter import *
from tkinter import filedialog
from pytube import YouTube
import threading

root = Tk()
root.title("Youtube Downloader")
root.geometry("600x320")
root.resizable(False, False)
root.iconphoto(False, PhotoImage(file="youtube.png"))


# my Functions

def browse():
    directory = filedialog.askdirectory(title="Save video")
    folderLink.delete(0, "end")
    folderLink.insert(0, directory)


def down_yt():
    status.config(text="Status: Downloading ...")
    link = ytLink.get()
    folder = folderLink.get()
    YouTube(link, on_complete_callback=finsh, on_progress_callback=update_progress).streams.filter(progressive=True, file_extension="mp4").order_by(
        "resolution").desc().first().download(folder)


def update_progress(stream, chunk, remaining):
    total_size = stream.filesize
    downloaded = total_size - remaining
    percentage = (downloaded / total_size) * 100
    status.config(text=f"Status: Downloading... {percentage:.2f}%")


def finsh(streams=None, chunk=None, file_handle=None, remaining=None):
    status.config(text="Status : Complete")


# Youtube logo
ytlogo = PhotoImage(file="youtube_icon.png").subsample(2)
ytitle = Label(root, image=ytlogo)
ytitle.place(relx=0.5, rely=0.25, anchor="center")

# YouTube link

ytLabel = Label(root, text="Youtube Link")
ytLabel.place(x=25, y=150)
ytLink = Entry(root, width=60)
ytLink.place(x=140, y=150)

# Download Folder

folderLabel = Label(root, text="Download Folder")
folderLabel.place(x=25, y=183)

folderLink = Entry(root, width=50)
folderLink.place(x=140, y=183)

# Browse Button

browse = Button(root, text="Browse", command=browse)
browse.place(x=455, y=180)


# Download Button
download = Button(root, text="Download", command=lambda: threading.Thread(target=down_yt).start())
download.place(x=280, y=220)

# Status Bar
status = Label(root, text="Status :Ready", font="Calibre 10 italic", fg="black", bg="white", anchor="w")
status.place(rely=1, anchor="sw", relwidth=1)

root.mainloop()
