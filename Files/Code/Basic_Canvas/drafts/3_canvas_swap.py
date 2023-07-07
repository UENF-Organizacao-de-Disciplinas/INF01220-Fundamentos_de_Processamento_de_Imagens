from tkinter import *
from PIL import Image, ImageTk

root = Tk()  # Creating main window interface


def swap_func():
    """ Swaps frames """
    info = frame_a1.grid_info()
    row_1, col_1 = info['row'], info['column']
    info = frame_a2.grid_info()
    row_2, col_2 = info['row'], info['column']
    local_frame_a1 = Frame(root, width=50, height=50, bg='red')
    local_frame_a2 = Frame(root, width=50, height=50, bg='green')
    frame_a1.grid(row=row_2, column=col_2)
    frame_a2.grid(row=row_1, column=col_1)


frame_a1 = Frame(root, width=50, height=50, bg='red')
frame_a2 = Frame(root, width=50, height=50, bg='green')
frame_b1 = Frame(root, width=100, height=100, bg='black')
frame_b2 = Frame(root, width=100, height=100, bg='blue')

frame_a1.grid(row=0, column=0)
frame_a2.grid(row=0, column=1)
frame_b1.grid(row=1, column=0)
frame_b2.grid(row=1, column=1)

swap_btn = Button(root, text='SWAP', command=swap_func)
swap_btn.grid(row=2, column=0, columnspan=2)


root.mainloop()  # running program
