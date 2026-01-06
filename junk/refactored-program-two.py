# import tkinter as tk
# from tkinter import colorchooser, messagebox, filedialog, scrolledtext
# from PIL import Image, ImageTk, ImageGrab
# import math
# import time
# import threading

# # =========================
# # WINDOW
# # =========================
# window = tk.Tk()
# window.title("Vision Draw")
# window.geometry("1100x650")
# window.minsize(900, 550)

# # =========================
# # MAIN STRUCTURE (PACK ONLY)
# # =========================
# top_frame = tk.Frame(window, bg="#D6F5EF")
# top_frame.pack(side="top", fill="x")

# canvas_frame = tk.Frame(window, bg="#134B40")
# canvas_frame.pack(side="top", fill="both", expand=True)

# bottom_frame = tk.Frame(window, bg="#134B40", height=35)
# bottom_frame.pack(side="bottom", fill="x")

# # =========================
# # MENU BAR
# # =========================
# menu_frame = tk.Frame(top_frame, bg="#FF9578", height=30)
# menu_frame.pack(side="top", fill="x")

# tk.Button(menu_frame, text="Save", command=lambda: saveImageEvent()).pack(side="left", padx=5)
# tk.Button(menu_frame, text="Clear", command=lambda: ClearAllEvent()).pack(side="left", padx=5)
# tk.Button(menu_frame, text="Undo", command=lambda: undo()).pack(side="left", padx=5)
# tk.Button(menu_frame, text="Redo", command=lambda: redo()).pack(side="left", padx=5)

# tk.Button(menu_frame, text="Help", command=lambda: help_window()).pack(side="right", padx=5)
# tk.Button(menu_frame, text="About", command=lambda: aboutus_window()).pack(side="right", padx=5)

# # =========================
# # TOOLBAR AREA
# # =========================
# toolbar_area = tk.Frame(top_frame, bg="#D6F5EF")
# toolbar_area.pack(side="top", fill="x", pady=5)

# # ---------- TOOLS ----------
# tool_frame = tk.LabelFrame(toolbar_area, text="Tools", bg="#D6F5EF")
# tool_frame.pack(side="left", padx=10)

# tk.Button(tool_frame, text="Pencil", width=8, command=usePencil)\
#     .grid(row=0, column=0, padx=5, pady=5)

# tk.Button(tool_frame, text="Eraser", width=8, command=useEraser)\
#     .grid(row=1, column=0, padx=5, pady=5)

# tk.Button(tool_frame, text="Text", width=8, command=addText)\
#     .grid(row=0, column=1, padx=5, pady=5)

# tk.Button(tool_frame, text="Insert Img", width=8, command=insert)\
#     .grid(row=1, column=1, padx=5, pady=5)

# # ---------- SHAPES ----------
# shape_frame = tk.LabelFrame(toolbar_area, text="Shapes", bg="#D6F5EF")
# shape_frame.pack(side="left", padx=10)

# tk.Button(shape_frame, text="Line", width=8, command=select_line)\
#     .grid(row=0, column=0, padx=5, pady=5)

# tk.Button(shape_frame, text="Rect", width=8, command=select_rectangle)\
#     .grid(row=0, column=1, padx=5, pady=5)

# tk.Button(shape_frame, text="Circle", width=8, command=select_circle)\
#     .grid(row=1, column=0, padx=5, pady=5)

# tk.Button(shape_frame, text="Triangle", width=8, command=select_triangle)\
#     .grid(row=1, column=1, padx=5, pady=5)

# # ---------- COLORS ----------
# color_frame = tk.LabelFrame(toolbar_area, text="Colors", bg="#D6F5EF")
# color_frame.pack(side="right", padx=10)

# def choose_color():
#     c = colorchooser.askcolor()[1]
#     if c:
#         stroke_color.set(c)
#         current_color_label.config(bg=c)

# basic_colors = ["black", "red", "green", "blue", "yellow", "orange"]

# for i, c in enumerate(basic_colors):
#     tk.Button(color_frame, bg=c, width=3,
#               command=lambda col=c: stroke_color.set(col))\
#         .grid(row=0, column=i, padx=2)

# tk.Button(color_frame, text="More", command=choose_color)\
#     .grid(row=1, column=0, columnspan=6, pady=5)

# current_color_label = tk.Label(color_frame, bg="black", width=6)
# current_color_label.grid(row=2, column=0, columnspan=6)

# # =========================
# # CANVAS
# # =========================
# canvas = tk.Canvas(canvas_frame, bg="white")
# canvas.pack(fill="both", expand=True)

# canvas.bind("<B1-Motion>", paint)
# canvas.bind("<ButtonRelease-1>", paint)
# canvas.bind("<ButtonPress-3>", start_shape)
# canvas.bind("<ButtonRelease-3>", drawshape)
# canvas.bind("<B3-Motion>", on_right_drag)

# # =========================
# # STATUS BAR / ZOOM
# # =========================
# status_label = tk.Label(bottom_frame, text="Ready", fg="white", bg="#134B40")
# status_label.pack(side="left", padx=10)

# zoom_frame = tk.Frame(bottom_frame, bg="#134B40")
# zoom_frame.pack(side="right", padx=10)

# zoom_scrollbar = tk.Scale(
#     zoom_frame, from_=5, to=300,
#     orient="horizontal", length=200,
#     command=apply_zoom_from_scrollbar
# )
# zoom_scrollbar.set(100)
# zoom_scrollbar.pack()

# # =========================
# # STARTUP
# # =========================
# # usePencil()
# window.mainloop()
