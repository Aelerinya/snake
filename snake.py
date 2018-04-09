from graphics import *
import time

def main () :
    width = 640
    height = 480
    win = GraphWin("Snake", width, height)

    background = Rectangle(Point(0, 0), Point(width, height))
    background.setFill('black')
    background.draw(win)

    posX = 100
    posY = 100
    dir = 3
    text = ''
    quit = False
    lose = False
    size = 10

    rect1 = Rectangle(Point(posX, posY), Point(posX+size, posY+size))
    rect2 = Rectangle(Point(posX-size, posY), Point(posX, posY+size))
    rect3 = Rectangle(Point(posX-2*size, posY), Point(posX-size, posY+size))
    rect4 = Rectangle(Point(posX-3*size, posY), Point(posX-2*size, posY+size))

    snake = [rect4, rect3, rect2, rect1]
    for rect in snake :
        rect.setFill('white')
        rect.draw(win)

    while quit == False :
        if lose == False :
            input = win.checkKey()

            #change direction
            if input == 'Up' :
                dir = 0
            elif input == 'Down' :
                dir = 1
            elif input == 'Left' :
                dir = 2
            elif input == 'Right' :
                dir = 3

            #Update position based on direction
            if dir == 0 :
                posY -= size
            elif dir == 1 :
                posY += size
            elif dir == 2 :
                posX -= size
            elif dir == 3 :
                posX += size

            #Check colision
            if posX < 0 or posX+size > width or posY < 0 or posY+size > height :
                lose = True
            else :
                newRect = Rectangle(Point(posX, posY), Point(posX+size, posY+size))
                newRect.setFill('white')
                newRect.draw(win)
                snake.append(newRect)
                snake[0].undraw()
                snake.pop(0)



        if lose == True :
            for rect in snake :
                rect.undraw()

            message = Text(Point(width/2, height/2),"You lost")
            message.setFill('white')
            message.draw(win)
            win.getKey()
            quit = True

        time.sleep(1.0/10)

    #win.getMouse()
    #win.close()

main()
