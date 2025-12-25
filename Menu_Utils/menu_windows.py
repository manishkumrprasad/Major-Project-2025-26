# import tkinter as tk

# class MenuWindow():
#     def __init__(self , window):
#         self.window = window
#     def help_window():
#         new_window = tk.Toplevel(window)
#         new_window.title("Help")
#         new_window.geometry("400x600")

#         help_text = (
#             "                               Paint Application Help\n\n"
#             "• Getting Started  \n "

#             "→ Select a tool from the toolbar (e.g., Brush, Eraser).\n"
#             "→ Choose a color from the color palette.\n"
#             "→ Start drawing by clicking and dragging on the canvas.\n \n"


#             "• Tools & Their Functions\n"
#             "→ Eraser: Remove parts of your drawing.\n"
#             "→ Brush: Draw freehand lines on the canvas.\n"
#             "→ Color Picker: Pick any color for the brush.\n"
#             "→ Fill Tool (if available):** Fill a closed area with a selected color.\n"
#             "→ Line/Rectangle/Ellipse:** Draw shapes (click and drag).\n"
#             "→ Clear Canvas: Erase the entire canvas.\n"
#             "→ Undo/Redo: Revert or repeat your last action.\n \n"

#             "• 3. File Options\n "

#             "→ New: Start a new canvas.\n"
#             "→ Open: Load an existing image (optional).\n"
#             "→ Save: Save your drawing as an image file.\n \n"

#             "• 4. Shortcuts (if any)\n"

#             "→ `Ctrl + Z`: Undo\n"
#             "→ `Ctrl + S`: Save\n"
#             "→ `Ctrl + N`: New Canvas\n \n"

#             "• 5. Tips\n "

#             "→ Hold `Shift` while drawing shapes for perfect squares/circles (if implemented).\n"
#             "→ Use a stylus for better precision on touch-enabled devices.\n \n"

#             "• 6. About\n"

#             "PaintApp v1.0\n"
#             "Developed by Team Ricky Include Ricky Singh ,Arun Shaw And Manish Kumar Prasad\n "
#             "© 2025 All Rights Reserved\n"
            
#         )
#         text_area = scrolledtext.ScrolledText(new_window, wrap=tk.WORD, font=("Arial", 12))
#         text_area.insert(tk.END, help_text)
#         text_area.config(state='disabled')  # Make it read-only
#         text_area.pack(expand=True, fill='both')

#     def aboutus_window():
#         new_window = tk.Toplevel(window)
#         new_window.title("About Us")
#         new_window.geometry("400x600")

        
#         about_text = (
#             "                                       About Us\n\n"

#             "PaintApp v1.0\n\n"
            
#             "This paint application was developed with the goal of providing a simple, "
#             "user-friendly drawing tool built using Python's Tkinter library.\n\n"

#             "🛠 Features include:\n"
#             "• Freehand drawing (brush)\n"
#             "• Eraser tool\n"
#             "• Shape drawing (lines, rectangles, ellipses)\n"
#             "• Color selection and fill tool\n"
#             "• Undo/Redo and file operations\n\n"

#             "👨‍💻 Developed By:\n"
#             "• Ricky Singh\n"
#             "• Arun Kumar Ray\n"
#             "• Manish Kumar Prasad\n\n"

#             "© 2025 All Rights Reserved\n"
#             "Thank you for using our application!"
#         )

#         text_area = scrolledtext.ScrolledText(new_window, wrap=tk.WORD, font=("Arial", 12))
#         text_area.insert(tk.END, about_text)
#         text_area.config(state='disabled')  # Read-only
#         text_area.pack(expand=True, fill='both')


#     def setting_window():
#         new_window = tk.Toplevel(window)
#         new_window.title("Setting")
#         new_window.geometry("700x400")
#         label = tk.Label(new_window, text="This is a new window")
#         label.pack(pady=20)

#     def add_text_window():
#         new_window = tk.Toplevel(window)
#         new_window.title("Add Text To Canvas")
#         new_window.geometry("600x300")
#         label = tk.Label(new_window, text="Enter The Text You Want To Display :")
#         label.pack(pady=20)

#         global textofentry
#         global entry 
#         textofentry = tk.StringVar(value = "Enter Here")

#         entry = tk.Entry(new_window , justify="center" , font=("Arial", 10) , textvariable=textofentry , width=50)
#         entry.place(x = 100, y = 80)
#         btn = tk.Button(new_window , text="Add" , command= add_Text  , width = 10, height = 2, highlightthickness=0 , relief="flat",bd=1)
#         btn.place(x = 250 , y = 120)


#         # Sliders for X and Y position
#         global x_slider , y_slider
#         x_slider = tk.Scale(new_window, from_=0, to=1280, orient="horizontal", label="X Position" , length=200)
#         x_slider.set(200)  # default center
#         x_slider.place(x = 50 , y = 200)

#         y_slider = tk.Scale(new_window, from_=0, to=800, orient="horizontal", label="Y Position" , length=200)
#         y_slider.set(125)