import os
import tkinter as tk
from tkinter import filedialog

class PDFFileIterator:
    def __init__(self, directory):
        self.directory = directory
        self.files = []
        self.current_index = 0

        # Obtener la lista de archivos PDF en el directorio
        for file in os.listdir(self.directory):
            file_path = os.path.join(self.directory, file)
            if os.path.isfile(file_path) and file_path.lower().endswith('.pdf'):
                self.files.append(file_path)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < len(self.files):
            file_path = self.files[self.current_index]
            file_name = os.path.basename(file_path)
            self.current_index += 1
            return file_name
        else:
            raise StopIteration

def seleccionar_directorio():
    directorio = filedialog.askdirectory()
    if directorio:
        global iterador
        iterador = PDFFileIterator(directorio)
        mostrar_archivos(iterador)

def mostrar_archivos(iterador):
    lista_archivos.delete(0, tk.END)
    for index, file_name in enumerate(iterador, start=1):
        lista_archivos.insert(tk.END, f"{index}. {file_name}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Explorador de Archivos PDF")
ventana.geometry("500x500")

#Texto de entrada
label_tipo = tk.Label(ventana, text="Busca tus PDFs : ")
label_tipo.pack()

# Variables globales
iterador = None

# Botón para seleccionar el directorio
boton_seleccionar = tk.Button(ventana, text="Seleccionar directorio", command=seleccionar_directorio)
boton_seleccionar.pack(pady=10)

#Texto de entrada
label_tipo = tk.Label(ventana, text="Tus resultados : ")
label_tipo.pack()

# Lista de archivos
lista_archivos = tk.Listbox(ventana, width=75, height=20)
lista_archivos.pack(pady=20)

# Ejecutar la aplicación
ventana.mainloop()
