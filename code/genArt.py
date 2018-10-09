import sys

try:
    import turtle
except Exception as e:
    print (e)
    sys.exit()

window = turtle.Screen()

window.exitonclick()
