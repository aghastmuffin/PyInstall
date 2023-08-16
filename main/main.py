import urllib.request
import requests
from threading import Thread
import tkinter as tk
from tkinter.ttk import *
from tkinter import *
from time import sleep
from win10toast import ToastNotifier

def download_progress_callback(count, block_size, total_size):
    percent = int(count * block_size * 100 / total_size)
    progressindv['value'] = percent
    root.update_idletasks()

def download_file(url):
    response = urllib.request.urlopen(url)
    file_size = int(response.headers['Content-Length'])
    filename = url.split("/")[-1]  # Get the last part of the URL as the filename
    urllib.request.urlretrieve(url, filename, reporthook=download_progress_callback)
    toaster = ToastNotifier()
    if root.state()=="iconic":
        toaster.show_toast("WinstallPy", "The Requested Install was completed while the application was in the background", duration=10, threaded=True)

def download_all_files():
    a = requests.get("https://")  # YOUR CONFIGURED MAIN LIST, CAN BE GITHUB RAW! ALSO CAN BE A FILE.
    if a.status_code == 200:
        a = a.text
        b = a.split(":")  # please separate your links with semicolons
    else:
        print(a.status_code, "ERROR!! QUITTING")
        quit(a.status_code)
    for url in b:
        download_file(url)
        progress['value'] += 100 / len(b)
        root.update_idletasks()


root = tk.Tk()
root.title("WinstallPy 3.0")
copyrigh = Label(root, text="Apache Licence 2023!")
instruc = Label(root, text="Configure Endpoints to download files")
start = Button(root, text="Start Download", command=lambda: Thread(target=download_all_files).start())
progress = Progressbar(root, orient=HORIZONTAL, length=100, mode='determinate')
progressindv = Progressbar(root, orient=HORIZONTAL, length=100, mode='determinate')
copyrigh.config(width=4)
root.geometry("400x200")

instruc.grid(row=0, column=0)
start.grid(row=1, column=0)
progress.grid(row=2, column=0)
copyrigh.grid(row=10, column=0)
root.mainloop()
