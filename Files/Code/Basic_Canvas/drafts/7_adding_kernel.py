""" New clean table """

from tkinter import Tk, ttk, Label, StringVar, Frame, Entry
from PIL import Image, ImageTk


files = [
    'bg.png',
    'color.jpg',
    'dog.png',
    'dice.png',
    'wheel.png',
    'water.png',
]
grey_methods = ['Mean', 'R', 'G', 'B']
default_kernels = ['Gaussiana', 'Prewitt',
                   'Laplace', 'Gradiente-X', 'Gradiente-Y']
file_paths = []
tk_images = []
text_var = []
entries = []

current_image_index = 0
current_grey_index = 0
current_photo_image = None
current_kernel_index = 0

root = Tk()  # Creating main window interface
TITLE = 'Processamento de Imagem'
root.configure(bg='#333')
root.title(TITLE)


selected_image = StringVar()

f_tools = Frame(root)
select_image = ttk.Combobox(f_tools, state='readonly')
select_gray = ttk.Combobox(f_tools, state='readonly')
select_list_kernel = ttk.Combobox(f_tools, state='readonly')
f_kernel = Frame(f_tools)

f_img = Frame(root)


def fill_images():
    """ add images """
    base = 'Files/Code/Basic_Canvas/img/'
    for file in files:
        file_path = base+file
        file_paths.append(file_path)
        pil_image = Image.open(file_path)
        ttk_image = ImageTk.PhotoImage(pil_image)
        tk_images.append(ttk_image)


def place_image(local_image):
    """ asdasf """
    global img_block, current_photo_image

    img_block.grid_remove()

    img_label = Label(f_img, image=local_image)
    img_label.grid(row=0, column=0)

    img_block = img_label
    current_photo_image = local_image


def set_new_image(_):
    """ places new image """
    # Remove previously placed image label
    def update_global_image():
        """ asdafs """
        global current_image_index
        value = select_image.get()
        current_image_index = files.index(value)

    update_global_image()
    place_image(tk_images[current_image_index])


def apply_grey(_):
    """ asdasd """
    def updage_global_grey():
        """ asdaf """
        global current_grey_index
        value = select_gray.get()
        current_grey_index = grey_methods.index(value)

    def convert_to_gray(img_choice, grey_choice):
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

        local_img = Image.open(file_paths[img_choice])
        conv_image = local_img.convert("RGB")

        pil_img = None
        if grey_choice == 0:
            pil_img = method_mean(conv_image)
        elif grey_choice == 1:
            pil_img = method_r(conv_image)
        elif grey_choice == 2:
            pil_img = method_g(conv_image)
        elif grey_choice == 3:
            pil_img = method_b(conv_image)
        else:
            pil_img = local_img
        returned_imagetk_photoimage = ImageTk.PhotoImage(pil_img)
        return returned_imagetk_photoimage

    updage_global_grey()

    msg = 'Applying "' + grey_methods[current_grey_index]
    msg += '" to "' + files[current_image_index] + '".'
    print(msg)

    grey_img = convert_to_gray(current_image_index, current_grey_index)
    place_image(grey_img)


def change_kernel(_):
    """ asdafjaofij """


def configure_elements():
    """ image combox """
    selected_image.set(files[current_image_index])
    select_image['values'] = files
    select_image['textvariable'] = selected_image
    select_image.bind('<<ComboboxSelected>>', set_new_image)

    select_gray['values'] = grey_methods
    select_gray.current(current_grey_index)
    select_gray.bind('<<ComboboxSelected>>', apply_grey)

    select_list_kernel['values'] = default_kernels
    select_list_kernel.current(current_kernel_index)
    select_gray.bind('<<ComboboxSelected>>', change_kernel)


def place_elements():
    """ Placing elements """
    f_tools.grid(row=0, column=0, sticky='N')
    select_image.grid(row=0, column=0, sticky='N')
    select_gray.grid(row=1, column=0, sticky='N')
    select_list_kernel.grid(row=2, column=0)
    f_kernel.grid(row=3, column=0)

    f_img.grid(row=0, column=1)
    img_block.grid(row=0, column=0)


def place_kernel_matrix(local_frame):
    """ Kernel """
    def create_matrix(local_frame, rows=3, cols=3):
        """ Creates a matrix """
        for i in range(rows):
            text_var.append([])
            entries.append([])
            for j in range(cols):
                text_var[i].append(StringVar())
                entries[i].append(
                    Entry(local_frame, textvariable=text_var[i][j], width=3))
                entries[i][j].grid(row=i, column=j)

    create_matrix(local_frame)


fill_images()
configure_elements()

img_block = Label(f_img, image=tk_images[0])

place_kernel_matrix(f_kernel)

place_elements()
root.mainloop()  # running program
