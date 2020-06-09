#! python3

import turtle as tu

screen = tu.Screen()

fo = tu.Turtle()

fo.left(90)




def draw(i):
    
    if i<10:
        return
    else:
        
        fo.forward(i)
        fo.left(30)
        draw(i/2)
        fo.right(60)
        draw(i/2)
        fo.left(30)
        fo.backward(i)
draw(100)
input("Press any key to exit ...")