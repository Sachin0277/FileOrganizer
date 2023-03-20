import os
import shutil
import tkinter as tk
from tkinter import filedialog


def choose_folder():
    global folder_path
    folder_path = filedialog.askdirectory()
    folder_path_label.config(text=folder_path)


def organize_files():
    extensions = {
        "Documents": [".pdf", ".docx", ".txt", ".pptx"],
        "Images": [".jpg", ".jpeg", ".png"],
        "Videos": [".mp4", ".avi", ".mov"],
        "Music": [".mp3", ".wav"],
        "Others": []
    }

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            for category, exts in extensions.items():
                for ext in exts:
                    if file_name.lower().endswith(ext):
                        category_path = os.path.join(folder_path, category)
                        if not os.path.exists(category_path):
                            os.mkdir(category_path)
                        shutil.move(file_path, os.path.join(category_path, file_name))
                        break
                else:
                    continue
                break
            else:
                other_path = os.path.join(folder_path, "Others")
                if not os.path.exists(other_path):
                    os.mkdir(other_path)
                shutil.move(file_path, os.path.join(other_path, file_name))

    result_label.config(text="Files organized successfully.")


root = tk.Tk()
root.title("File Organizer")
root.geometry("300x250")

folder_path_label = tk.Label(root, text="Sachin File Organizer", font=("Terminus", 18), foreground="sky blue")
folder_path_label.pack(pady=10)

folder_path = ""

choose_folder_button = tk.Button(root, text="Select folder", font=("Helvetica", 18), background="Yellow", command=choose_folder)
choose_folder_button.pack()

folder_path_label = tk.Label(root, text="")
folder_path_label.pack()

organize_button = tk.Button(root, text="Organize files", font=("Sans-serif", 18), background="green", command=organize_files)
organize_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
