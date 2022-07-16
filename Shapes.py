import turtle as t
import random

tim = t.Turtle()

colours=["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","wheat","SlateGrey","SeaGreen"]

def shape(side):
    deg=360/side
    for _ in range(side):
        tim.forward(100)
        tim.left(deg)

for shape_side_n in range(3,10):
    tim.color(random.choice(colours))
    shape(shape_side_n)