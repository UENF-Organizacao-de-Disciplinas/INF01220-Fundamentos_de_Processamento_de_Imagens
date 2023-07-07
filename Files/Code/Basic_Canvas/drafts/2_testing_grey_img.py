""" Code """

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


def convert_to_gray(local_img, choice):
    """ Converting """
    def method_r(my_img):
        """ Return R channel """
        r_ch, _, _ = my_img.split()
        return r_ch

    def method_g(my_img):
        """ Return R channel """
        _, g_ch, _ = my_img.split()
        return g_ch

    def method_b(my_img):
        """ Return R channel """
        _, _, b_ch = my_img.split()
        return b_ch

    def method_mean(my_img):
        """ getting gray mean """
        width, height = my_img.size
        new_img = Image.new('RGB', (width, height), color='black')
        pixels = my_img.load()
        new_img_pixels = new_img.load()
        for i in range(width):
            for j in range(height):
                r_px, g_px, b_px = pixels[i, j]
                mean = int((r_px+g_px+b_px)/3)
                new_img_pixels[i, j] = (mean, mean, mean)
        return new_img

    print(type(image))
    conv_image = local_img.convert("RGB")
    print(type(conv_image))
    returned_img = None
    if choice == 0:
        returned_img = method_mean(conv_image)
    elif choice == 1:
        returned_img = method_r(conv_image)
    elif choice == 2:
        returned_img = method_g(conv_image)
    elif choice == 3:
        returned_img = method_b(conv_image)
    else:
        returned_img = local_img
    print(type(returned_img))
    return returned_img


FOLDER_PATH = 'Files/Code/Basic_Canvas/img/'
PATH = FOLDER_PATH + 'color.jpg'

image = Image.open(PATH)
gray_image = convert_to_gray(image, 0)
gray_image.show()
