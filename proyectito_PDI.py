from tkinter import filedialog
import openpyxl
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import *
from PIL import Image, ImageTk

def convertir_txt_a_excel():
    txt_file_path = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])

    if txt_file_path:
        excel_file = openpyxl.Workbook()
        excel_sheet = excel_file.active

        with open(txt_file_path, 'r') as txt_file:
            for line in txt_file:
                line = line.strip().split(',')
                excel_sheet.append(line)
                
    
        excel_file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Archivos de Excel", "*.xlsx")])
        
        
        if excel_file_path:
            excel_file.save(excel_file_path)
            excel_file.close()
            mensaje = f'Archivo de Excel guardado en: {excel_file_path}'
            messagebox.showinfo("Éxito", mensaje)

root = tk.Tk()
root.title("Convertir TXT a Excel")
root.configure(bg = 'pink')
root.geometry("500x500")

image = Image.open("txtimagen.png")
image = image.resize((100, 100))
image = ImageTk.PhotoImage(image)

image_label = tk.Label(root, image=image)
image_label.pack()

frame = tk.Frame(root)
frame.pack(pady=20)


convert_button = tk.Button(frame, text="Convertir a Excel", command=convertir_txt_a_excel)
convert_button.pack()



root.mainloop()
