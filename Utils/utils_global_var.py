import tkinter as tk

class Global_Variable:
    shape=""
    preview_shape=""
    undo_stack=[]
    redo_stack=[]
    stroke_color = tk.StringVar(value="white")
    global current_line# 1= solid, 2=Dashed, 3=Dotted
    current_line=1
    insert_image=None
    image_on_canvas=None
    inserted_image=[]
    original_image=None
    canvas_virtual_size=100000
    pencil_select=0