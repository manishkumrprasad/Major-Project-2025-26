import tkinter as tk
from main import stroke_color,current_color_label , colorFrame
class Color_Fun:
    def RedColor():
        stroke_color.set("Red")
        current_color_label.config(bg="red")
        redButton=tk.Button(colorFrame ,bg="Red",width=3 , height=1,activebackground="red", command=RedColor, highlightthickness=0 , relief="flat")
        redButton.grid(row=0,column=0 ,padx=5 , pady=5)


    def GreenColor():
        stroke_color.set("Green")
        current_color_label.config(bg="Green")
        greenButton=tk.Button(colorFrame ,bg="Green",width=3,height = 1,activebackground="green", command=GreenColor, highlightthickness=0 , relief="flat")
        greenButton.grid(row=0,column=1,padx=5 , pady=5)

    def BlueColor():
        stroke_color.set("Blue")
        current_color_label.config(bg="Blue")
        blueButton=tk.Button(colorFrame ,bg="Blue",width=3,height = 1,activebackground="blue", command=BlueColor, highlightthickness=0 , relief="flat")
        blueButton.grid(row=0,column=2,padx=5 , pady=5)

    def YellowColor():
        stroke_color.set("Yellow")
        current_color_label.config(bg="Yellow")
        yellowButton=tk.Button(colorFrame ,bg="Yellow",width=3,height = 1,activebackground="yellow", command=YellowColor, highlightthickness=0 , relief="flat")
        yellowButton.grid(row=0,column=3,padx=5 , pady=5)

    def GreyColor():
        stroke_color.set("Grey")
        current_color_label.config(bg="Grey")
        greyButton=tk.Button(colorFrame ,bg="grey",width=3,height = 1,activebackground="grey", command=GreyColor, highlightthickness=0 , relief="flat")
        greyButton.grid(row=0,column=4,padx=5 , pady=5)

    def BlackColor():
        stroke_color.set("Black")
        current_color_label.config(bg="Black")
        blackButton=tk.Button(colorFrame ,bg="black",width=3,height = 1,activebackground="Black" ,command=BlackColor, fg="white", highlightthickness=0 , relief="flat")
        blackButton.grid(row=1,column=0,padx=5 , pady=5)

    def WhiteColor():
        stroke_color.set("White")
        current_color_label.config(bg="White")
        whiteButton=tk.Button(colorFrame ,bg="White",width=3,height = 1,activebackground="white", command=WhiteColor, highlightthickness=0 , relief="flat")
        whiteButton.grid(row=1,column=1,padx=3 , pady=3)

    def OrangeColor():
        stroke_color.set("Orange")
        current_color_label.config(bg="Orange")
        orangeButton=tk.Button(colorFrame ,bg="Orange",width=3,height = 1,activebackground="Orange", command=OrangeColor, highlightthickness=0 , relief="flat")
        orangeButton.grid(row=1,column=2,padx=3 , pady=3)

    def PurpleColor():
        stroke_color.set("Purple")
        current_color_label.config(bg="Purple")
        purpleButton=tk.Button(colorFrame ,bg="Purple",width=3,height = 1, activebackground="Purple",command=PurpleColor, highlightthickness=0 , relief="flat")
        purpleButton.grid(row=1,column=3,padx=3 , pady=3)

    def PinkColor():
        stroke_color.set("Pink")
        current_color_label.config(bg="Pink")
        pinkButton=tk.Button(colorFrame ,bg="pink",width=3,height = 1, activebackground="pink",command=PinkColor, highlightthickness=0 , relief="flat")
        pinkButton.grid(row=1,column=4,padx=1 , pady=1)