# Paint code - https://www.youtube.com/playlist?list=PLeb12iNltItFypA6pRWNsgb2y_wtCxZKL

""" TO DO List
- CREATE "ADD OPTION" WITH PRESET KERNELS
- BUTTON: CONVERT IMAGE TO GRAY SCALE
- MAKE BUTTONS SUNKABLE: The border's style of a frame can be flat, groove, raised, ridge, solid, or sunken. The default border style of a frame is flat.
"""

from tkinter import *
from tkinter import ttk
from tkinter import colorchooser
# import PIL.ImageGrab as ImageGrab
# from tkinter import filedialog
# from tkinter import messagebox
# from tkinter import Tk, Label, StringVar, Button, Entry
from PIL import Image, ImageTk


# Variables

TITLE = 'Kernels App'
CANVAS_WIDTH = 600
CANVAS_HEIGHT = 1100
CANVAS_GEOMETRY = str(CANVAS_HEIGHT) + 'x' + str(CANVAS_WIDTH)
FOLDER_PATH = 'Files/Code/Basic_Canvas/img/'
PATH = FOLDER_PATH + 'bg.png'


root = Tk()  # Creating main window interface

# Configuring window

root.title(TITLE)
root.geometry(CANVAS_GEOMETRY)
root.configure(bg='#333')

# Frame - 1 : Tools

# container.columnconfigure(index, weight)
# container.rowconfigure(index, weight)

# back-end functions

text_var = []
entries = []

matrix_rows, matrix_columns = (3, 3)

image_0 = Image.open(PATH)
img0 = ImageTk.PhotoImage(image_0)

image_wheel = Image.open(PATH)
img_wheel = ImageTk.PhotoImage(image_wheel)

current_image = img0
old_image = img_wheel

canvas_frame = Frame(root, bg='yellow')

# Visual elements functions


def get_mat(rows=matrix_rows, cols=matrix_columns):
    """ Get matrix function """
    matrix = []
    for i in range(rows):
        matrix.append([])
        for j in range(cols):
            matrix[i].append(text_var[i][j].get())
    print(matrix)


def create_submit_matrix_button():
    """ Submit button """
    button = Button(root, text='Submit', bg='bisque3',
                    width=15, command=get_mat)
    button.place(x=160, y=140)


index = 1


def turn_gray(text):
    """ asd """
    # frm.grid_forget()
    # frm.destroy()

    global current_image
    global old_image

    current_image, old_image = old_image, current_image

    global canvas_frame
    canvas_frame.forget()

    new_canvas_frame = Frame(root, bg='green', width=20, height=20)
    # new_canvas_frame_label = Label(new_canvas_frame, image=img_wheel)
    # new_canvas_frame_label.image = img_wheel
    global index
    index += 1
    new_canvas_frame.grid(row=0, column=index)
    # new_canvas_frame_label.grid(row=1, column=0)
    print(text)


def create_tools_frame():
    """ Tools frame
    [12:41, 04/07/2023] João Vítor Fernandes Dias: (1,2)
    - frame esquerdo: ferramentas
    - frame direito: canvas/imagem

    """

    def create_matrix(local_frame=root, rows=3, cols=3):
        """ Creates a matrix """
        for i in range(rows):
            # append an empty list to your two arrays
            # so you can append to those later
            text_var.append([])
            entries.append([])
            for j in range(cols):
                # append your StringVar and Entry
                text_var[i].append(StringVar())
                entries[i].append(
                    Entry(local_frame, textvariable=text_var[i][j], width=3))
                entries[i][j].grid(row=i, column=j)

    frame_tools = Frame(root)
    frame_tools_image = Frame(frame_tools)
    button_open = Button(frame_tools_image, text="Open", relief='raised')
    button_save = Button(frame_tools_image, text="Save", relief='raised')
    button_reset = Button(frame_tools_image, text="Reset", relief='raised')

    frame_tools_gray = Frame(frame_tools)
    select_list_gray = ttk.Combobox(frame_tools_gray, state='readonly')
    select_list_gray['values'] = ('Mean', 'R', 'G', 'B')
    select_list_gray.current(3)
    button_gray = Button(frame_tools_gray, text="Gray",
                         relief='raised', command=lambda: turn_gray(select_list_gray.current()))

    frame_tools_gray.grid(row=1, column=0)
    button_gray.grid(row=0, column=0)

    frame_tools_kernel = Frame(frame_tools)
    button_load_kernel = Button(
        frame_tools_kernel, text="Load Kernel", relief='raised')

    select_list_kernel = ttk.Combobox(frame_tools_kernel, state='readonly')
    select_list_kernel['values'] = ('Sobel', 'Fourier', 'Mean')
    select_list_kernel.current(2)

    frame_tools_kernel_matrix = Frame(frame_tools_kernel)
    create_matrix(frame_tools_kernel_matrix)

    frame_tools.grid(row=0, column=0)
    frame_tools_image.grid(row=0, column=0)
    frame_tools_kernel.grid(row=2, column=0)
    frame_tools_kernel_matrix.grid(row=1, column=0, columnspan=2)

    button_open.grid(row=0, column=0)
    button_save.grid(row=0, column=1)
    button_reset.grid(row=0, column=2)
    select_list_gray.grid(row=0, column=1)

    button_load_kernel.grid(row=0, column=0)
    select_list_kernel.grid(row=0, column=1)


def create_image_frame(local_current_image=current_image):
    """ Image frame """
    # my_canvas = Canvas(canvas_frame, bg="blue")
    # my_canvas.create_image(10, 10, anchor=NW, image=img1)

    canvas_frame_label = Label(canvas_frame, image=local_current_image)
    canvas_frame_label.image = local_current_image

    canvas_frame.grid(row=0, column=1)
    canvas_frame_label.grid(row=1, column=0)
    # my_canvas.grid(row=0, column=0)


# Creating interface
create_image_frame()
create_tools_frame()

# Run interface

root.mainloop()  # running program
