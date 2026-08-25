import sketchingpy
import random


sketch = sketchingpy.Sketch2DWeb(500, 500)
sketch.set_rect_mode("corner")
sketch.set_arc_mode("corner")

# draw grid with two types of lines
sketch.set_stroke("lightgray")
sketch.set_stroke_weight(1)
for i in range(26):
    j = 20 * i  # every 20 pixels
    sketch.draw_line(0, j, 500, j)  # horizontal
    sketch.draw_line(j, 0, j, 500)  # vertical

sketch.set_stroke("gray")
sketch.set_stroke_weight(4)
for i in range(6):
    j = 100 * i  # every 100 pixels
    sketch.draw_line(0, j, 500, j)
    sketch.draw_line(j, 0, j, 500)


# draw lots of random shapes inside the grid squares
colors = ["red", "green", "blue", "yellow", "orange", "pink", "brown", "black"]
shapes = ["rect", "circle"]
margin = 3
amount_of_shapes = 150

sketch.clear_stroke()
for _ in range(amount_of_shapes):
    color = random.choice(colors)
    shape = random.choice(shapes)
    x = int(random.random() * 25)
    y = int(random.random() * 25)
    
    sketch.set_fill(color)
    if shape == "rect":
        sketch.draw_rect(x * 20 + margin, y * 20 + margin, 20 - 2 * margin, 20 - 2 * margin)
    elif shape == "circle":
        sketch.draw_arc(x * 20 + margin, y * 20 + margin, 20 - 2 * margin, 20 - 2 * margin, 0, 360)

sketch.show()
