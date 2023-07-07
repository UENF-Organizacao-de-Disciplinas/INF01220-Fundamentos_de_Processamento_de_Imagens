from tkinter import *
from tkinter import ttk
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

    index = option_list.index(selected_value.get())
    selected_frame = frame_list[index]
    selected_frame.grid(row=0, column=2, rowspan=2)


frame_Mean = Frame(root, width=30, height=30, bg='grey')
frame_R = Frame(root, width=30, height=30, bg='red')
frame_G = Frame(root, width=30, height=30, bg='green')
frame_B = Frame(root, width=30, height=30, bg='blue')

frame_list = [frame_Mean, frame_R, frame_G, frame_B]

frame_a1 = Frame(root, width=50, height=50, bg='red')
frame_a2 = Frame(root, width=50, height=50, bg='green')
frame_b1 = Frame(root, width=100, height=100, bg='black')
frame_b2 = Frame(root, width=100, height=100, bg='blue')

frame_a1.grid(row=0, column=0)
frame_a2.grid(row=0, column=1)
frame_b1.grid(row=1, column=0)
frame_b2.grid(row=1, column=1)

swap_btn = Button(root, text='SWAP', command=swap_func)
swap_btn.grid(row=2, column=0)

selection = IntVar()
selection.set(2)
selected_value = StringVar()
selected_value.set('R')

option_list = ['Mean', 'R', 'G', 'B']

select_list = ttk.Combobox(root)
select_list['values'] = option_list
select_list['textvariable'] = selected_value
# select_list.current(selection.get())

select_list.grid(row=2, column=1)

root.mainloop()  # running program
