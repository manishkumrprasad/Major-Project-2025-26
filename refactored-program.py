import tkinter as tk
from tkinter import colorchooser
import ttkbootstrap as ttk

# =========================
# Main Window
# =========================
window = tk.Tk()
window.title("Vision Draw - Clean Layout")
window.geometry("1100x650")
window.minsize(900, 550)

# =========================
# MAIN FRAMES (PACK ONLY)
# =========================

menu_frame = ttk.Frame(window, bootstyle = "danger", height=30)
menu_frame.pack(side="top", fill="x")

toolbar_Frame = ttk.Frame(window,  bootstyle = "primary")
toolbar_Frame.pack(side="top", fill="x")

canvas_frame_parent = ttk.Frame(window,  bootstyle = "black")
canvas_frame_parent.pack(side="top", fill="both", expand=True)

canvas_frame = ttk.Frame(canvas_frame_parent)
canvas_frame.pack(side="top", fill="both", expand=True)

footer_Frame = ttk.Frame(window,  bootstyle = "primary", height=30)
footer_Frame.pack(side="bottom", fill="x")

# =========================
# MENU BAR
# =========================


ttk.Button(menu_frame, text="Save" , bootstyle="primary-outline").pack(side="left", padx=5)
ttk.Button(menu_frame, text="Clear", bootstyle="primary-outline").pack(side="left", padx=5)
ttk.Button(menu_frame, text="Undo", bootstyle="primary-outline").pack(side="left", padx=5)

ttk.Button(menu_frame, text="Help", bootstyle="primary-outline").pack(side="right", padx=5)
ttk.Button(menu_frame, text="About", bootstyle="primary-outline").pack(side="right", padx=5)

# =========================
# TOOLBAR AREA
# =========================
toolbar_area = tk.Frame(toolbar_Frame, bg="#D6F5EF")
toolbar_area.pack(side="top", fill="x", pady=5)

# ---------- Tools ----------
tool_frame = tk.LabelFrame(toolbar_area, text="Tools", bg="#D6F5EF")
tool_frame.pack(side="left", padx=10)

current_tool = tk.StringVar(value="pencil")

def select_tool(name):
    current_tool.set(name)

tk.Button(tool_frame, text="Pencil", width=8,
          command=lambda: select_tool("pencil")).grid(row=0, column=0, padx=5, pady=5)

tk.Button(tool_frame, text="Eraser", width=8,
          command=lambda: select_tool("eraser")).grid(row=1, column=0, padx=5, pady=5)

tk.Button(tool_frame, text="Text", width=8,
          command=lambda: select_tool("text")).grid(row=0, column=1, padx=5, pady=5)

# ---------- Shapes ----------
shape_frame = tk.LabelFrame(toolbar_area, text="Shapes", bg="#D6F5EF")
shape_frame.pack(side="left", padx=10)

shape = tk.StringVar(value="")

def select_shape(s):
    shape.set(s)

tk.Button(shape_frame, text="Line", width=8,
          command=lambda: select_shape("line")).grid(row=0, column=0, padx=5, pady=5)

tk.Button(shape_frame, text="Rect", width=8,
          command=lambda: select_shape("rect")).grid(row=0, column=1, padx=5, pady=5)

tk.Button(shape_frame, text="Oval", width=8,
          command=lambda: select_shape("oval")).grid(row=1, column=0, padx=5, pady=5)

# ---------- Colors ----------
color_frame = tk.LabelFrame(toolbar_area, text="Colors", bg="#D6F5EF")
color_frame.pack(side="left", padx=10)

stroke_color = tk.StringVar(value="black")

def choose_color():
    c = colorchooser.askcolor()[1]
    if c:
        stroke_color.set(c)
        current_color_label.config(bg=c)

colors = [
    ("black", "secondary"),
    ("red", "danger"),
    ("green", "success"),
    ("blue", "primary"),
    ("yellow", "warning"),
    ("orange", "warning"),
    ("black", "secondary"),
    ("red", "danger"),
    ("green", "success"),
    ("blue", "primary"),
    ("yellow", "warning"),
    ("orange", "warning")
]

for i, (color, style) in enumerate(colors):
    if(i<6):
        ttk.Button(
            color_frame,
            width=0.8,
            bootstyle=style,
            command=lambda col=color: stroke_color.set(col)
        ).grid(row=0, column=i, padx=2)
    else:
        ttk.Button(
            color_frame,
            width=1,
            bootstyle=style,
            command=lambda col=color: stroke_color.set(col)
        ).grid(row=1, column=i-6, padx=2 , pady=2)


tk.Button(color_frame, text="More", command=choose_color).grid(row=2, column=0, columnspan=6, pady=5)

current_color_label = tk.Label(color_frame, bg="black", width=6)
current_color_label.grid(row=2, column=0, columnspan=6)

# =========================
# CANVAS
# =========================
canvas = tk.Canvas(canvas_frame, bg="white")
canvas.pack(fill="both", expand=True)

stroke_size = 4
prev_x, prev_y = None, None

def draw(event):
    global prev_x, prev_y
    if prev_x and prev_y:
        if current_tool.get() == "eraser":
            color = "white"
        else:
            color = stroke_color.get()

        canvas.create_line(
            prev_x, prev_y, event.x, event.y,
            fill=color, width=stroke_size, capstyle=tk.ROUND, smooth=True
        )
    prev_x, prev_y = event.x, event.y

def reset(event):
    global prev_x, prev_y
    prev_x, prev_y = None, None

canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", reset)

# =========================
# STATUS BAR
# =========================
status = tk.Label(footer_Frame, text="Ready", fg="white", bg="#134B40")
status.pack(side="left", padx=10)

# =========================
# START
# =========================
window.mainloop()
