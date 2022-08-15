import cv2 as cv
import numpy as np
from PIL import Image, ImageTk


def read_img(name_file):
    """
    Позволяет открывать изображения с разными именами,
    в случае когда имя содержит киррилические символы,
    возникают проблемы чтения функции cv2.imread
    :param name_file: имя файла;
    :return: изображение как объект
    """
    with open(name_file, "rb") as f:
        chunk = f.read()
    chunk_arr = np.frombuffer(chunk, dtype=np.uint8)
    img = cv.imdecode(chunk_arr, cv.IMREAD_COLOR)
    return img


def array_to_image_tk(img, width, height):
    img = cv.resize(img, (width, height), interpolation=cv.INTER_AREA)
    img_cv = cv.cvtColor(img, cv.COLOR_BGR2RGBA)
    current_image = Image.fromarray(img_cv)
    return ImageTk.PhotoImage(current_image)