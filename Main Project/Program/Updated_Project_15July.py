# All Required Packages And Libraries Required For This Project
import tkinter as tk
from tkinter import colorchooser
from tkinter import Button
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import filedialog
from PIL import ImageGrab as ImageGrab

window = tk.Tk()
window.geometry("1100x600")
appicon = tk.PhotoImage(file="Icons/App_Icon.png")
window.iconphoto(False , appicon)

window.title("Paint Application")
window.resizable(True , True)
# ------------------------------------------Parent-Frame-Section-Open----------------------------------------------------------+

# Parent Paint Toolbars / Which Will Contain All The Tools Frame Such As toolbar , color pallette , file management , help box etc
frameOne = tk.Frame(window , bg="#D6F5EF" , width=1280,height=160)
frameOne.grid(row=0 , column=0 , sticky=tk.NW)

# Parent Paint Frame Which Contain Only The Canvas Frame
frameTwo = tk.Frame(window , bg="yellow" , width=1280,height=800)
frameTwo.grid(row=1 , column=0)

frameFoot = tk.Frame(window , bg="yellow" , width=1280,height = 35)
frameFoot.place(x = 0 , y = 565)
# ------------------------------------------Parent-Frame-Section-Close----------------------------------------------------------+

# ------------------------------------------Icon-Section-Open----------------------------------------------------------+

#The Icon Section Contains All The Icon That Are Going To Be Used Throughout The Program  
iconOfPencil = tk.PhotoImage(file="Icons/Small_Pencil.png")
iconOfEraser = tk.PhotoImage(file="Icons/Small_Eraser.png")
iconOfFont = tk.PhotoImage(file="Icons/Small_Font.png")
iconOfGlass = tk.PhotoImage(file="Icons/Small_Glass.png")
iconOfFill = tk.PhotoImage(file="Icons/Small_Fill.png")
iconOfSave = tk.PhotoImage(file="Icons/Small_Save.png")
iconOfClear = tk.PhotoImage(file="Icons/Small_Clear.png")
iconOfSelectColor = tk.PhotoImage(file="Icons/Small_MoreColorsWithPlus.png")

iconOfZoomIn = tk.PhotoImage(file="Icons/Small_Zoom_In.png")
iconOfZoomOut = tk.PhotoImage(file="Icons/Small_Zoom_Out.png")

# ------------------------------------------Icon-Section-Close----------------------------------------------------------+

#-------------------------------------------Color-Box-Frame-Open--------------------------------------------------------------------+
# This Compartment Of The Code Handle The Position And Other Things Of The Color Selection Box
def selectcolor():
    selectedcolor = colorchooser.askcolor("red" , title="Select Color")
    stroke_color.set(selectedcolor[1])

colorBoxButton= Button(frameOne  , width=55, height=55, command=selectcolor , image= iconOfSelectColor , bg="#D6F5EF" , activebackground="#D6F5EF" , highlightthickness=0 , relief="flat",bd=0)
colorBoxButton.place(x=610, y=60)

#-------------------------------------------Color-Box-Frame-Close--------------------------------------------------------------------+

#-------------------------------------------Colors-Frame-Open--------------------------------------------------------------------+
# This Section Handle The Required Basic Colors Of Sets At The Upper Frame Of The Paint Window
colorFrame=tk.Frame(frameOne , height=170, width=230 , borderwidth=0 ,relief="sunken" ,bg="#D6F5EF")
colorFrame.place(x=415,y=45)

redButton=Button(colorFrame ,bg="Red",width=3 , height=1,activebackground="red", command=lambda:stroke_color.set("Red"), highlightthickness=0 , relief="flat")
redButton.grid(row=0,column=0 ,padx=5 , pady=5)

greenButton=Button(colorFrame ,bg="Green",width=3,height = 1,activebackground="green", command=lambda:stroke_color.set("Green"), highlightthickness=0 , relief="flat")
greenButton.grid(row=0,column=1,padx=5 , pady=5)

blueButton=Button(colorFrame ,bg="Blue",width=3,height = 1,activebackground="blue", command=lambda:stroke_color.set("Blue"), highlightthickness=0 , relief="flat")
blueButton.grid(row=0,column=2,padx=5 , pady=5)

yellowButton=Button(colorFrame ,bg="Yellow",width=3,height = 1,activebackground="yellow", command=lambda:stroke_color.set("Yellow"), highlightthickness=0 , relief="flat")
yellowButton.grid(row=0,column=3,padx=5 , pady=5)

greyButton=Button(colorFrame ,bg="grey",width=3,height = 1,activebackground="grey", command=lambda:stroke_color.set("grey"), highlightthickness=0 , relief="flat")
greyButton.grid(row=0,column=4,padx=5 , pady=5)

blackButton=Button(colorFrame ,bg="black",width=3,height = 1,activebackground="Black" ,command=lambda:stroke_color.set("Black") , fg="white", highlightthickness=0 , relief="flat")
blackButton.grid(row=1,column=0,padx=5 , pady=5)

whiteButton=Button(colorFrame ,bg="White",width=3,height = 1,activebackground="white", command=lambda:stroke_color.set("White"), highlightthickness=0 , relief="flat")
whiteButton.grid(row=1,column=1,padx=3 , pady=3)

orangeButton=Button(colorFrame ,bg="Orange",width=3,height = 1,activebackground="Orange", command=lambda:stroke_color.set("Orange"), highlightthickness=0 , relief="flat")
orangeButton.grid(row=1,column=2,padx=3 , pady=3)

purpleButton=Button(colorFrame ,bg="Purple",width=3,height = 1, activebackground="Purple",command=lambda:stroke_color.set("Purple"), highlightthickness=0 , relief="flat")
purpleButton.grid(row=1,column=3,padx=3 , pady=3)

pinkButton=Button(colorFrame ,bg="pink",width=3,height = 1, activebackground="pink",command=lambda:stroke_color.set("pink"), highlightthickness=0 , relief="flat")
pinkButton.grid(row=1,column=4,padx=1 , pady=1)

MoreColors=Button

coloursLabel = tk.Label(frameOne , text="Colours" , width=20 ,bg="#D6F5EF"  )
coloursLabel.place(x = 470 , y = 130)
#-------------------------------------------Colors-Frame-Close--------------------------------------------------------------------+

# ------------------------------------------Tool-Functionality-Section-Open----------------------------------------------------------+
# This Part Of The Code Is Crucial As It Handles The Functionality Of The Buttons
stroke_color = tk.StringVar(value="white")

def usePencil():
    stroke_color.set("black")
    canvas.config(cursor = "crosshair")

def useEraser():
    stroke_color.set("white")
    canvas.config(cursor = "plus")

def addText():
    add_text_window()
# ------------------------------------------Tool-Functionality-Section-Close----------------------------------------------------------+


# ------------------------------------------Menu-Section-Open----------------------------------------------------------+
# The Menu Bar Will Contain Important Stuff Like File , Help , Edit , Undo , Redo , Setting Bar And Etc

menuFrame = tk.Frame(frameOne , height=30 , width=1280 , bg="#FF9578")
menuFrame.place(x=0,y=0)

# ------------------------------------------Menu-Section-Close----------------------------------------------------------+

#-------------------------------------------Save-Image-Frame-Open--------------------------------------------------------------------+
# Contains The Save Button Details
def SaveImage():
    filelocation= filedialog.asksaveasfilename(defaultextension="jpg")
    x=window.winfo_rootx()+35
    y=window.winfo_rooty()+250
    img = ImageGrab.grab(bbox=(x,y,x+1340,y+640))
    img.save(filelocation)
    showImage = messagebox.askyesno("Paint App", "Do you want open image?")
    print(showImage)
    if showImage:
        img.show()


saveImagebutton= Button(frameOne , image= iconOfSave ,command=SaveImage, width=20, height= 20 , highlightthickness=0 , relief="flat",bg="#FF9578" , activebackground="#FF9578",)
saveImagebutton.place(x=15, y=2)

#-------------------------------------------Save-Image-Frame-Close--------------------------------------------------------------------+

#-------------------------------------------Clear-image-Frame-Open------------------------------------------------------------------------+
# The Clear All Button Details
def clear() :
    if messagebox.askokcancel("Warning!", "Do you want to clear everything?"):
        canvas.delete('all')

clearImageFrame= Button(frameOne , width=20 , height=20, image = iconOfClear , command=clear, highlightthickness=0 , relief="flat" ,bg="#FF9578" , activebackground="#FF9578")
clearImageFrame.place(x=60, y=2)
#-------------------------------------------Clear-image-Frame-Close------------------------------------------------------------------------+

#-------------------------------------------New-Window-Open------------------------------------------------------------------------+
def help_window():
    new_window = tk.Toplevel(window)
    new_window.title("Help")
    new_window.geometry("400x600")

    help_text = (
        "                               Paint Application Help\n\n"
        "• Getting Started  \n "

        "→ Select a tool from the toolbar (e.g., Brush, Eraser).\n"
        "→ Choose a color from the color palette.\n"
        "→ Start drawing by clicking and dragging on the canvas.\n \n"


        "• Tools & Their Functions\n"
        "→ Eraser: Remove parts of your drawing.\n"
        "→ Brush: Draw freehand lines on the canvas.\n"
        "→ Color Picker: Pick any color for the brush.\n"
        "→ Fill Tool (if available):** Fill a closed area with a selected color.\n"
        "→ Line/Rectangle/Ellipse:** Draw shapes (click and drag).\n"
        "→ Clear Canvas: Erase the entire canvas.\n"
        "→ Undo/Redo: Revert or repeat your last action.\n \n"

        "• 3. File Options\n "

        "→ New: Start a new canvas.\n"
        "→ Open: Load an existing image (optional).\n"
        "→ Save: Save your drawing as an image file.\n \n"

        "• 4. Shortcuts (if any)\n"

        "→ `Ctrl + Z`: Undo\n"
        "→ `Ctrl + S`: Save\n"
        "→ `Ctrl + N`: New Canvas\n \n"

        "• 5. Tips\n "

        "→ Hold `Shift` while drawing shapes for perfect squares/circles (if implemented).\n"
        "→ Use a stylus for better precision on touch-enabled devices.\n \n"

        "• 6. About\n"

        "PaintApp v1.0\n"
        "Developed by Team Ricky Include Ricky Singh ,Arun Shaw And Manish Kumar Prasad\n "
        "© 2025 All Rights Reserved\n"
        
    )
    text_area = scrolledtext.ScrolledText(new_window, wrap=tk.WORD, font=("Arial", 12))
    text_area.insert(tk.END, help_text)
    text_area.config(state='disabled')  # Make it read-only
    text_area.pack(expand=True, fill='both')

def aboutus_window():
    new_window = tk.Toplevel(window)
    new_window.title("About Us")
    new_window.geometry("400x600")

    
    about_text = (
        "                                       About Us\n\n"

        "PaintApp v1.0\n\n"
        
        "This paint application was developed with the goal of providing a simple, "
        "user-friendly drawing tool built using Python's Tkinter library.\n\n"

        "🛠 Features include:\n"
        "• Freehand drawing (brush)\n"
        "• Eraser tool\n"
        "• Shape drawing (lines, rectangles, ellipses)\n"
        "• Color selection and fill tool\n"
        "• Undo/Redo and file operations\n\n"

        "👨‍💻 Developed By:\n"
        "• Ricky Singh\n"
        "• Arun Kumar Ray\n"
        "• Manish Kumar Prasad\n\n"

        "© 2025 All Rights Reserved\n"
        "Thank you for using our application!"
    )

    text_area = scrolledtext.ScrolledText(new_window, wrap=tk.WORD, font=("Arial", 12))
    text_area.insert(tk.END, about_text)
    text_area.config(state='disabled')  # Read-only
    text_area.pack(expand=True, fill='both')


def setting_window():
    new_window = tk.Toplevel(window)
    new_window.title("Setting")
    new_window.geometry("700x400")
    label = tk.Label(new_window, text="This is a new window")
    label.pack(pady=20)

def add_text_window():
    new_window = tk.Toplevel(window)
    new_window.title("Add Text To Canvas")
    new_window.geometry("600x300")
    label = tk.Label(new_window, text="Enter The Text You Want To Display :")
    label.pack(pady=20)

    global textofentry
    global entry 
    textofentry = tk.StringVar(value = "Enter Here")

    entry = tk.Entry(new_window , justify="center" , font=("Arial", 10) , textvariable=textofentry , width=50)
    entry.place(x = 100, y = 80)
    btn = tk.Button(new_window , text="Add" , command= printt  , width = 10, height = 2, highlightthickness=0 , relief="flat",bd=1)
    btn.place(x = 250 , y = 120)


    # Sliders for X and Y position
    global x_slider , y_slider
    x_slider = tk.Scale(new_window, from_=0, to=1280, orient="horizontal", label="X Position" , length=200)
    x_slider.set(200)  # default center
    x_slider.place(x = 50 , y = 200)

    y_slider = tk.Scale(new_window, from_=0, to=800, orient="horizontal", label="Y Position" , length=200)
    y_slider.set(125)
    y_slider.place(x = 350 , y = 200)

#-------------------------------------------New-Window-Close------------------------------------------------------------------------+

#--------------------------------------------Help-setting-Frame-Open------------------------------------------------------------------------------+
# The Help Button Details
HelpSettingFrame=tk.Frame(frameOne , height=30, width=240 , borderwidth=0 ,relief="sunken",bg="white")
HelpSettingFrame.place(x=850,y=0)

Help= Button(HelpSettingFrame , text="Help" , width=10, highlightthickness=0 , relief="flat",bg="#FF9578" , activebackground="#FF9578" , command=help_window)
Help.grid(row=0, column=0)

Setting= Button(HelpSettingFrame , text="Setting" , width=10, highlightthickness=0 , relief="flat",bg="#FF9578" , activebackground="#FF9578",command=setting_window)
Setting.grid(row=0, column=1)

About= Button(HelpSettingFrame , text="About us" , width=10, highlightthickness=0 , relief="flat",bg="#FF9578" , activebackground="#FF9578",command=aboutus_window)
About.grid(row=0, column=2)

#--------------------------------------------Help-Setting-Frame-Close-----------------------------------------------------------------------------+
#--------------------------------------------Zoom---------------------------------------------------------------------
# zoom_level=1.0
# def zoom(event):
#     global zoom_level
#     if not hasattr(zoom, 'min_zoom'):
#         zoom.min_zoom =0.1
#         zoom.max_zoom = 10.0
#     if event.delta > 0 or event.num == 4:
#         scale = 1.1
#         zoom_level *= scale
#     elif event.delta < 0 or event.num == 5:
#         scale = 0.9
#         zoom_level *= scale
#     else:
#         return
    

#     canvas.scale("all", event.x, event.y, scale, scale)
#     canvas.configure(scrollregion=canvas.bbox("all"))

# def zoom_fake(scale):
#     global zoom_level
#     zoom_level *= scale
#     canvas.scale("all", 0,0,scale,scale)
#     canvas.configure(scrollregion=canvas.bbox("all"))

# window.bind("<MouseWheel>", zoom)  # Windowindow
# window.bind("<Button-4>", zoom)    # Linux scroll up
# window.bind("<Button-5>", zoom)    # Linux scroll down

# zoom_in_button = Button(frameOne, text="Zoom In", command=lambda: zoom_fake(1.1), bg="#FF9578")
# zoom_in_button.place(x=210, y=2)

# zoom_out_button = Button(frameOne, text="Zoom Out", command=lambda: zoom_fake(0.9), bg="#FF9578")
# zoom_out_button.place(x=280, y=2)
# Zoom level and scroll sync
zoom_level = 1.0

zoomFrame = tk.Frame(frameFoot, width=300,height = 35 )
zoomFrame.place(x = 800 , y = 0)

# zoom_scrollbar = tk.Scale(frameFoot, from_=10, to=200, orient="horizontal",width = 7 ,length = 200 , label="         Zoom In/Zoom Out")
zoom_scrollbar = tk.Scale(zoomFrame, from_=10, to=200, orient="horizontal",width = 7 ,length = 200)
zoom_scrollbar.set(100)
zoom_scrollbar.place(x=50, y=-2)

zoom_Out_Label = tk.Label(zoomFrame ,  image= iconOfZoomOut , width=20 , height=20)
zoom_Out_Label.place(x = 10 , y = 10)

zoom_In_Label = tk.Label(zoomFrame , image= iconOfZoomIn , width=20 , height=20)
zoom_In_Label.place(x = 270 , y = 10)


def apply_zoom_from_scrollbar(value):
    global zoom_level
    scale = int(value) / (zoom_level * 100)
    zoom_level = int(value) / 100
    canvas.scale("all", 0, 0, scale, scale)
    canvas.configure(scrollregion=canvas.bbox("all"))

zoom_scrollbar.config(command=apply_zoom_from_scrollbar)

# Pan with middle mouse button
drag_start = [0, 0]

def start_pan(event):
    drag_start[0] = event.x
    drag_start[1] = event.y

def do_pan(event):
    dx = drag_start[0] - event.x
    dy = drag_start[1] - event.y
    canvas.xview_scroll(int(dx), "units")
    canvas.yview_scroll(int(dy), "units")
    drag_start[0] = event.x
    drag_start[1] = event.y

# Mouse wheel zoom
def zoom(event):
    global zoom_level
    if event.delta > 0 or event.num == 4:
        scale = 1.1
    elif event.delta < 0 or event.num == 5:
        scale = 0.9
    else:
        return

    if not (0.5 <= zoom_level * scale <= 5):
        return

    zoom_level *= scale
    canvas.scale("all", 0, 0, scale, scale)
    canvas.configure(scrollregion=canvas.bbox("all"))
    zoom_scrollbar.set(int(zoom_level * 100))

def zoom_fake(scale):
    global zoom_level
    if not (0.5 <= zoom_level * scale <= 5):
        return

    zoom_level *= scale
    canvas.scale("all", 0, 0, scale, scale)
    canvas.configure(scrollregion=canvas.bbox("all"))
    zoom_scrollbar.set(int(zoom_level * 100))

window.bind("<MouseWheel>", zoom)
window.bind("<Button-4>", zoom)
window.bind("<Button-5>", zoom)


#--------------------------------------------Zoom Close---------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------+
# Tool Frame Which Will Contain All The Required Tools etc - pencil , eraser , color
toolFrame = tk.Frame(frameOne , height=120 , width=120 , bg="#D6F5EF", highlightthickness=0 , relief="flat" )
toolFrame.place(x = 20  , y = 50 )

#Pencil Button/Icon -> Onclicking The Button The User Can Use The Pencil
pencilIcon = tk.Button(toolFrame ,  width=25 , height=25 , image= iconOfPencil , command=usePencil, highlightthickness=0 , relief="flat" )
pencilIcon.place(x = 5 , y = 5 )

# Rubber Button/Icon
eraserIcon = tk.Button(toolFrame , width=25, height=25 , image=iconOfEraser , command= useEraser, highlightthickness=0 , relief="flat")
eraserIcon.place(x = 5 , y = 40)

# Font Icon
fontIcon = tk.Button(toolFrame , width=25, height=25 , image=iconOfFont, highlightthickness=0,command= addText , relief="flat")
fontIcon.place(x = 40 , y = 5)

# Glass Icon
glassIcon = tk.Button(toolFrame , width=25, height=25, image=iconOfGlass, highlightthickness=0 , relief="flat")
glassIcon.place(x = 40 , y = 40)

# Fill Icon
fillIcon = tk.Button(toolFrame , width=25, height=25, image=iconOfFill, highlightthickness=0 , relief="flat")
fillIcon.place(x=80, y = 5)

# One More Icon keep x = 80 and y = 40

# ToolLabel
toolLabel = tk.Label(toolFrame , text="Tool Bar" , width=25 , bg="#D6F5EF")
toolLabel.place(x=-30 , y= 80)

# ----------------------------------------------------------------------------------------------------
# Adding Borders Along The Different Tools
border_frame_one = tk.Frame(frameOne , width=2 , height= 100 , bg="black")
border_frame_one.place(x = 160 , y = 50)

border_frame_two = tk.Frame(frameOne , width=2 , height= 100 , bg="black")
border_frame_two.place(x = 400 , y = 50)

border_frame_three = tk.Frame(frameOne , width=2 , height= 100 , bg="black")
border_frame_three.place(x = 690 , y = 50)
# ----------------------------------------------------------------------------------------------------
# Implementing Scale For Pencil Stroke Size So That The User Can Use The Scale To Increase The Size Of The Pencil And Eraser Stroke
stroke_size = tk.IntVar(value = 5)

scale = tk.Scale(frameOne , from_=1, to=20 , orient="horizontal" , length=200 , bg="#D6F5EF" , background="#D6F5EF" ,troughcolor="#706D68",variable=stroke_size , highlightthickness=0)
scale.place(x = 180 ,y = 50)

scale_label = tk.Label(frameOne , text="Pencil & Eraser Size", bg="#D6F5EF")
scale_label.place(x=220 , y=130)

# ----------------------------------------------------------------------------------------------------
# The Canvas Frame Where The User Can Draw Things
canvas = tk.Canvas(frameTwo , width=1280 , height=800 , bg="white")
canvas.grid(row=0,column=0)
# ----------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------
#Creating Pencil Functionality For The Paint Program
prevPoint = [0,0]
currentPoint = [0,0]

# def paint(event):
#     # print(event.type)
#     global prevPoint
#     global currentPoint
#     x = event.x
#     y = event.y
#     currentPoint =[x,y]

#     if prevPoint != [0,0]:
#         canvas.create_line(prevPoint[0] , prevPoint[1] , currentPoint[0] , currentPoint[1] ,fill=stroke_color.get() , width=stroke_size.get() , capstyle=tk.ROUND , smooth=True , splinesteps=36)
            
#     prevPoint = currentPoint 

#     if event.type == "5":
#         prevPoint = [0,0]   

def paint(event):
    global prevPoint, currentPoint
    # Adjust mouse position according to zoom
    x = event.x / zoom_level
    y = event.y / zoom_level
    currentPoint = [x, y]

    if prevPoint != [0, 0]:
        line = canvas.create_line(prevPoint[0], prevPoint[1], currentPoint[0], currentPoint[1],
                                  fill=stroke_color.get(), width=stroke_size.get(),
                                  capstyle=tk.ROUND, smooth=True, splinesteps=36)

    prevPoint = currentPoint

    if event.type == "5":
        prevPoint = [0, 0]


canvas.bind("<B1-Motion>" , paint)
canvas.bind("<ButtonRelease-1>",paint)

def printt():
    entered_text = entry.get()
    x_pos_text = x_slider.get()
    y_pos_text = y_slider.get()
    textofentry.set(" ")
    
    canvas.create_text(x_pos_text, y_pos_text, text=entered_text, font=("Arial", 16), fill="black", tags="text")

# ----------------------------------------------------------------------------------------------------

window.mainloop()
