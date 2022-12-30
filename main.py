import random
from tkinter import *
from rainbow_circle import RainbowCircle
import xml.etree.ElementTree as ET
import re

def get_tag_name(xml_el):
    s = re.findall(r"\'.*\'", str(xml_el))[0]
    return s[1:-1]

tk = Tk()
canvas = Canvas(tk, width=1000, height=1000, bg="white")
canvas.pack()

tree = ET.parse("circles.xml")
root = tree.getroot()

style = "circle"
width = 0
center = (500, 500)
radius = 400
speed = 4
circle_start = 90

el = random.choice(root)
el_name = get_tag_name(el)
style = el_name
if el_name == "ring":
    width = int(el.get("width"))
center = (int(el.get("cx")), int(el.get("cy")))
radius = int(el.get("radius"))
speed = int(el.get("speed"))
circle_start = int(el.get("start"))

while(True):
    rc = RainbowCircle(canvas, center, radius, circle_start, style, width)
    rc.draw()
    tk.update_idletasks()
    tk.update()
    canvas.delete("all")
    circle_start = (circle_start + speed) % 360
