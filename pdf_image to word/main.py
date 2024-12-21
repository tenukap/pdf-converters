import pytesseract
from PIL import Image
from fire.test_components import simple_decorator
from pdf2image import convert_from_path
from docx import Document
import os
import tkinter as tk
from tkinter import ttk


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
poppler_path = r"C:\Users\ACER\AppData\Local\Programs\VS Code\vs code- python\pdf converters\pdf_image to word\poppler-24.08.0\Library\bin"

no_of_files = 0
file_entry = ""

paths =[]
#functions
def get_num_files():
    no_of_files = int(no_files_entry.get())
    print(no_of_files)
    return no_of_files

def get_file_path():
    file_entry = str(path_entry.get())
    for count in range (no_of_files):
        paths[no_of_files] = file_entry

    convert()
    return file_entry
print(paths)

def convert():
    count = 0
    for count in range(no_of_files):
        images = convert_from_path(
        pdf_path = paths[no_of_files] ,
        poppler_path=poppler_path,
    )

        text = " "
        for image in images:
            text += pytesseract.image_to_string(image)

    document = Document()
    document.add_paragraph(text)
    document.save(f"sample{count}.docx")

    if os.path.exists(f"sample{count}.docx"):
        print("Document created successfully.")
    else:
        print("Document was not created.")

    count += 1



window = tk.Tk()
window.title("PDF to Word Converter")
window.geometry("300x300")

window.columnconfigure(0 , weight=1)
window.columnconfigure(1, weight=1)

#label for the no of files
Label01 = ttk.Label(master=window, text= "no of files")
Label01.pack()


#input field
input_frame01 = ttk.Frame( master = window)
no_files_entry = ttk.Entry(master = input_frame01, width=20,)
button = ttk.Button( master=input_frame01, text="Enter", command=get_num_files, )
#packing

no_files_entry.pack(side = 'left', padx =10)
button.pack(side = 'left')
input_frame01.pack(padx = 10)

Label02 = ttk.Label(master = window, text="file path" )
Label02.pack()

input_frame02 = ttk.Frame(master=window)
path_entry = ttk.Entry(master = window,width=20) # when u enter the path of the file remove the qoutation marks
button2 = ttk.Button(window,text="enter", command=get_file_path)
input_frame02.pack(padx = 10)
path_entry.pack(side = 'left', padx =10)
button2.pack(side= 'left')

window.mainloop()