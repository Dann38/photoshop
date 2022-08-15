from tkinter import *
import sys
import argparse
from lib.entry import read_img, array_to_image_tk
from tkinter import filedialog


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--photo')
    return parser


class App:
    def __init__(self, filename=None):
        self.filename = filename

        self.root = Tk()

        if filename:
            self.img = read_img(filename)
            self.img_block()
        else:
            self.img = Button(
                text="Выбрать изображение!",
                width=25,
                height=5,
                bg="blue",  # Цвет кнопки
                fg="yellow",  # Цвет текста
                command=self.select_img  # Команда при нажатие
            )
            self.img.grid(column=1, row=1)
        self.root.mainloop()

    def select_img(self):
        self.filename = filedialog.askopenfilename(title="Select file",
                                                   filetypes=(("image files", "*.jpg"),
                                                              ("all files", "*.*")))
        self.img = read_img(self.filename)
        self.img_block()

    def img_block(self):
        sh = self.img.shape
        h = sh[0]
        w = sh[1]
        WIDTH = 900
        HEIGHT = WIDTH * h // w
        canva = Canvas(self.root, width=WIDTH // 2, height=HEIGHT // 2, bg="gray")
        canva.grid(column=1, row=1)

        canvawidth = int(canva.winfo_reqwidth())
        canvaheight = int(canva.winfo_reqheight())

        self.img = array_to_image_tk(self.img, canvawidth, canvaheight)
        canva.create_image(0, 0, image=self.img, anchor='nw')


if __name__ == "__main__":
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    if namespace.photo:
        App(namespace.photo)
    else:
        App()



