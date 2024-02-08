from turtle import Turtle

myTurtle = Turtle()
myTurtle.speed(0)
myTurtle.screen.setup(800, 500)

# рисуем котика  
def draw_rectHead(head):
    for i in range(1):
        #щечка
        myTurtle.left(50)
        myTurtle.circle(head /1, 70 )
        #уши  
        myTurtle.right(50)
        myTurtle.forward(60)
        myTurtle.right(50)
        myTurtle.backward(60)
        myTurtle.right(235)
        # макушка
        myTurtle.circle(head /2, 50 )
        # ушко левое 
        myTurtle.right(50)
        myTurtle.forward(60)
        myTurtle.right(50)
        myTurtle.backward(60)
        myTurtle.right(290)
        # тело 
        myTurtle.circle(head /20, 55 )
        myTurtle.right(58)
        myTurtle.circle(head /1, 20 )
        myTurtle.forward(100)
        myTurtle.left(10)
        myTurtle.circle(head /1, 150 )
        # задняя лапка
        myTurtle.left(15)
        myTurtle.forward(100)
        myTurtle.circle(head /10, 180 )
        myTurtle.forward(80)
        myTurtle.left(180)
        myTurtle.forward(80)
        myTurtle.left(15)
        myTurtle.circle(head /2, 180 )
        myTurtle.left(180)
        myTurtle.up()
        myTurtle.circle(head /-2, -180 )
        myTurtle.left(175)
        myTurtle.down()
        # пузико и передняя лапа 
        myTurtle.forward(260)
        myTurtle.circle(head /10, 180 )
        myTurtle.forward(100)
        myTurtle.right(100)
        myTurtle.forward(10)
        # мордачка
        myTurtle.up()
        myTurtle.forward(100)
        myTurtle.left(80)
        myTurtle.forward(70)
        myTurtle.down()
        myTurtle.circle(head /20, 360 ) # левый глаз
        myTurtle.left(170)
        myTurtle.up()
        myTurtle.forward(30)
        myTurtle.down()
        myTurtle.circle(head /20, 360 ) # правый глаз
        # носик
        myTurtle.up()
        myTurtle.right(90)
        myTurtle.forward(5)
        myTurtle.right(65)
        myTurtle.down()
        myTurtle.forward(25) # верх носа
        myTurtle.left(150)
        myTurtle.forward(15) # левоя боковая
        myTurtle.left(60)
        myTurtle.forward(15) # правая боковая
        myTurtle.up()
        myTurtle.backward(15)
        myTurtle.left(250)
        myTurtle.down()
        myTurtle.circle(head /8, 180 )
        myTurtle.up()
        myTurtle.left(90)
        myTurtle.forward(25)
        myTurtle.down()
        myTurtle.right(110)
        myTurtle.circle(head /8, -180 )


# вызов функции для рисования круга
draw_rectHead(100)



myTurtle.screen.exitonclick()
myTurtle.screen.mainloop()