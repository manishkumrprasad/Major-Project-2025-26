#! In Use
# audio/sound_manager.py

import pygame

class SoundManager():
    def __init__(self):
        pygame.mixer.init()
        self.enabled = True

        self.sounds = {
            "welcome": pygame.mixer.Sound("Audio/Welcome.mp3"),

            "CameraOpen" : pygame.mixer.Sound("Audio/Camera Opened.mp3"),
            "CameraClose" :pygame.mixer.Sound("Audio/Camera Closed.mp3"),
            "SoundOn_Sound" : pygame.mixer.Sound("Audio/SoundOn.mp3"),
            "SoundOff_Sound" : pygame.mixer.Sound("Audio/SoundOff.mp3"),

            "Rectangle_Sound" :pygame.mixer.Sound("Audio/Rectangle.mp3"),
            "Circle_Sound" :pygame.mixer.Sound("Audio/Circle.mp3"),
            "Triangle_Sound" :pygame.mixer.Sound("Audio/Triangle.mp3"),
            "Heart_Sound":pygame.mixer.Sound("Audio/Heart.mp3"),
            "Pentagon_Sound":pygame.mixer.Sound("Audio/Pentagon.mp3"),
            "Line_Sound":pygame.mixer.Sound("Audio/Line.mp3"),
            "Arrow_Sound":pygame.mixer.Sound("Audio/Arrow.mp3"),

            "selectcolor_Sound" :pygame.mixer.Sound("Audio/SelectColor.mp3"),
            "Pencil_Sound":pygame.mixer.Sound("Audio/Pencil.mp3"),
            "DefaultBlack_Sound":pygame.mixer.Sound("Audio/DefaultBlack.mp3"),
            "Eraser_Sound":pygame.mixer.Sound("Audio/Eraser.mp3"),
            "OpenImage_Sound":pygame.mixer.Sound("Audio/OpenImage.mp3"),
            "Save_Sound":pygame.mixer.Sound("Audio/Save.mp3"),
            "ImageSaved_Sound":pygame.mixer.Sound("Audio/ImageSaved.mp3"),
            "clear_Sound":pygame.mixer.Sound("Audio/Clear.mp3"),
            "EverythingCleared_Sound":pygame.mixer.Sound("Audio/Everything Cleared.mp3"),

            "AiModeOn":pygame.mixer.Sound("Audio/MicOn.mp3"),
            "AiModeOff":pygame.mixer.Sound("Audio/MicOff.mp3"),
            "ArcResponse":pygame.mixer.Sound("Audio/ArcResponse.mp3"),
            "ArrowResponse":pygame.mixer.Sound("Audio/ArrowResponse.mp3"),
            "CircleResponse":pygame.mixer.Sound("Audio/CircleResponse.mp3"),
            "DashedLineResponse":pygame.mixer.Sound("Audio/DashedLineResponse.mp3"),
            "DottedLineResponse":pygame.mixer.Sound("Audio/DottedLineResponse.mp3"),
            "SolidLineResponse":pygame.mixer.Sound("Audio/SolidLineResponse.mp3"),
            "EraserResponse":pygame.mixer.Sound("Audio/EraserResponse.mp3"),
            "PencilResponse":pygame.mixer.Sound("Audio/PencilResponse.mp3"),
            "RectangleResponse":pygame.mixer.Sound("Audio/RectangleResponse.mp3"),
            "TriangleResponse":pygame.mixer.Sound("Audio/TriangleResponse.mp3"),
            "PentagonResponse":pygame.mixer.Sound("Audio/PentagonResponse.mp3"),
            "GoodAfternoon":pygame.mixer.Sound("Audio/GoodAfternoon.mp3"),
            "GoodMorning":pygame.mixer.Sound("Audio/GoodMorning.mp3"),
            "GoodEvening":pygame.mixer.Sound("Audio/GoodEvening.mp3"),
            "HelloSir":pygame.mixer.Sound("Audio/HelloSir.mp3"),
            "Sorry":pygame.mixer.Sound("Audio/Sorry.mp3"),
            "ThankYou":pygame.mixer.Sound("Audio/ThankYou.mp3"),
        }

    def play(self, name):
        if self.enabled and name in self.sounds:
            self.sounds[name].play()

    def toggle(self):
        self.enabled = not self.enabled
        return self.enabled
