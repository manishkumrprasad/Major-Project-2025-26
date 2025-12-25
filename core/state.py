# Contains all global variables 
import tkinter as tk

# Drawing state
shape = ""
preview_shape = None
stroke_color = tk.StringVar(value="white")
stroke_size = tk.IntVar(value=5)
current_line = 1

# Undo / Redo
undo_stack = []
redo_stack = []

# Canvas
canvas = None
original_image = None
image_id = None

# Audio / AI
sound_on = True
Ai_Mode = False
start_AI_is_running = False
