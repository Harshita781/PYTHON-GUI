import turtle as t
def shape(side):
    deg=int(360/side)
    for _ in range(deg):
        t.forward(100)
        t.left(deg)

side=int(input("Enter side of a shape:"))
shape(side)