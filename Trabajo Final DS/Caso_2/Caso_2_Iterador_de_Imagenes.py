from tkinter import Tk, Label, Entry, Button, messagebox, font
from PIL import ImageTk, Image

class ImageIterator:
    def __init__(self, image_paths):
        self.image_paths = image_paths
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.image_paths):
            raise StopIteration
        image_path = self.image_paths[self.index]
        image = Image.open(image_path)
        return image

class ImageViewer:
    def __init__(self, image_paths):
        self.iterator = ImageIterator(image_paths)
        self.root = Tk()
        self.root.title("Iterador de imagenes")
        self.root.resizable(False, False)
        self.label = Label(self.root)
        self.label.pack()
        self.search_entry = Entry(self.root, width= 45)
        self.search_entry.place(x=0, y=2)
        self.search_entry.configure(font=font.Font(size=13))
        self.search_button = Button(self.root, text="Buscar", command=self.search_images, width=17)
        self.search_button.place(x=275, y=2)
        self.previous_button = Button(self.root, text="Atrás", command=self.show_previous, width=27)
        self.previous_button.pack(side="left", padx=0, pady=0)
        self.next_button = Button(self.root, text="Siguiente", command=self.show_next, width=27)
        self.next_button.pack(side="right", padx=0, pady=0)

    def search_images(self):
        search_term = self.search_entry.get().lower()
        matching_paths = [path for path in self.iterator.image_paths if search_term in path.lower()]
        if matching_paths:
            self.iterator = ImageIterator(matching_paths)
            self.show_next()
        else:
            messagebox.showinfo("Búsqueda", "No se encontraron imágenes coincidentes")
            self.iterator.index = -1  # Reiniciar el índice al realizar una nueva búsqueda

    def show_previous(self):
        try:
            image = next(self.iterator)
            self.show_image(image)
        except StopIteration:
            self.label.config(text="No hay más imágenes")
            self.iterator.index = -1  # Reiniciar el índice al alcanzar el final de la lista

    def show_next(self):
        try:
            image = next(self.iterator)
            self.show_image(image)
        except StopIteration:
            self.label.config(text="No hay más imágenes")
            self.iterator.index = -1  # Reiniciar el índice al alcanzar el final de la lista

    def show_image(self, image):
        image = image.resize((400, 400))
        photo = ImageTk.PhotoImage(image)
        self.label.config(image=photo)
        self.label.image = photo

    def run(self):
        self.show_next()
        self.root.mainloop()

# Ejemplo de lista de rutas de imágenes
image_paths = ["Caso_2/images/image1.jpg", "Caso_2/images/image2.jpg", "Caso_2/images/image3.jpg", "Caso_2/images/image4.jpg", "Caso_2/images/image5.jpg"]

# Crear la instancia de ImageViewer y ejecutar la aplicación
viewer = ImageViewer(image_paths)
viewer.run()
