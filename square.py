import turtle
bob = turtle.Turtle()

def square(t, length):
    for i in range(4):
        t.fd(100)
        t.lt(90)

square(bob, 100)
