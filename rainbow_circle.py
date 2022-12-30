from tkinter import *
import color_transform
from circle_attrs import *

class RainbowCircle:
    
    def __init__(self, canvas: Canvas, center: tuple, radius: int, start: int, style: str, width = 0):
        self.canvas = canvas
        x1 = center[0] - radius
        y1 = center[1] - radius
        x2 = center[0] + radius
        y2 = center[1] + radius
        self.cords = [x1, y1, x2, y2]
        if style == "circle":
            self.circle_attrs = CircleAttrs()
        else:
            self.circle_attrs = RingAttrs(width)
        self.start = start % 360
    
    def draw(self):
        satu = 0
        k = 1
        for i in range(0, 360):
            if satu == 100:
                k = -1
            if satu == 0:
                k = 1
            color = color_transform.hsv_to_string((i - self.start) % 360, int(satu), 100)
            self.circle_attrs.set_color(color)
            self.canvas.create_arc(self.cords, {"start": i, "extent": 1, **self.circle_attrs.get_attrs()})
            satu += (800 / 360) * k
            if satu < 0:
                satu = 0
            if satu > 100:
                satu = 100
        
