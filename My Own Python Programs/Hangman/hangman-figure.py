import turtle
t = turtle.Pen()

#Setting the position of the turtle
t.up()
t.backward(150)
t.left(90)
t.backward(150)
t.down()

#Step 1: Making the stand
t.forward(435)
t.right(90)
t.forward(230)
t.right(45)
t.forward(130)
t.right(45)

#Step 2: Face
t.up()
t.backward(3)
t.right(90)
t.forward(5)
t.down()
t.circle(50)

#Step 3: Body
t.up()
t.left(90)
t.forward(100)
t.down()
t.forward(150)

#Step 4: Right Hand
t.up()
t.right(180)
t.forward(145)
t.left(150)
t.down()
t.forward(115)

#Step 5: Left Hand
t.up()
t.right(180)
t.forward(115)
t.right(115)
t.down()
t.forward(115)

#Step 6: Right Leg
t.up()
t.right(180)
t.forward(115)
t.right(215)
t.forward(145)
t.right(35)
t.down()
t.forward(120)

#Step 7: Left Leg
t.up()
t.right(180)
t.forward(120)
t.right(120)
t.down()
t.forward(120)
