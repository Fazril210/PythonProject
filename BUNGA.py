import turtle as tur
import colorsys as cs

tur.setup(800,800)
tur.speed(0)
tur.width(2)
tur.bgcolor("black")
for a in range(25):
    for b in range(15):
        tur.color(cs.hsv_to_rgb(b/15,a/25,1))
        tur.right(90)
        tur.circle(200-a*8,90)
        tur.left(90)
        tur.circle(200-a*8,90)
        tur.right(180)
        tur.circle(50,24)
tur.hideturtle()
tur.done()