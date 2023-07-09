from tkinter import *
from tkinter import ttk, Tk, Label
from PIL import Image, ImageTk

root = Tk()  # Creating main window interface

images = []
files = [
    'bg.png',
    'color.jpg',
    'dog.png',
    'dice.png',
    'wheel.png',
    'water.png',
]


def fill_images():
    """ add images """
    base = 'Files/Code/Basic_Canvas/img/'
    for file in files:
        file_path = base+file
        pil_image = Image.open(file_path)
        ttk_image = ImageTk.PhotoImage(pil_image)
        images.append(ttk_image)


fill_images()


selected_image = StringVar()
selected_image.set(files[0])

select_image_list = ttk.Combobox(root)
select_image_list['values'] = files
select_image_list['textvariable'] = selected_image

select_image_list.grid(row=0, column=0)


def place_new_image():
    """ places new image """
    # Remove previously placed image label
    global img_block
    img_block.grid_remove()

    value = select_image_list.get()
    img_label = Label(root, image=images[files.index(value)])
    img_label.grid(row=1, column=0)

    # Assign new image label to img_block
    img_block = img_label


def set_new_image(event):
    """ sets new image """
    place_new_image()


img_block = Label(root)
img_block.grid(row=1, column=0)

select_image_list.bind('<<ComboboxSelected>>', set_new_image)

root.mainloop()  # running program
