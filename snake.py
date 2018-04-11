from graphics import *
import time
import random

def main () :
    #Create cells Grid
    rows = 48
    columns = 64
    cellSize = 10
    Grid = [[0 for x in range(columns)] for y in range(rows)]

    #Create window
    width = columns * cellSize
    height = rows * cellSize
    win = GraphWin("Snake", width, height)

    #Put black background
    background = Rectangle(Point(0, 0), Point(width, height))
    background.setFill('black')
    background.draw(win)

    #Starting parameters
    posX = 25
    posY = 10
    dir = 3
    text = ''
    quit = False
    lose = False
    length = 4
    snake = []
    ateThisTurn = False
    score = 0
    Time=10

    #Food class
    class newFood :
        def __init__ (self):
            self.posX = random.randint(0, columns-1)
            self.posY = random.randint(0, rows-1)
            Grid[self.posY][self.posX] = 2
            self.rect = Rectangle(Point(self.posX*cellSize, self.posY*cellSize), Point((self.posX+1)*cellSize, (self.posY+1)*cellSize))
            self.rect.setFill('red')
            self.rect.draw(win)
        def destroy (self) :
            self.rect.undraw()
            Grid[self.posY][self.posX] = 0

    #First Food
    food = newFood()

    #Set initial blocks for snake
    for i in range(0, length) :
        rect = Rectangle(Point((posX-i)*cellSize, posY*cellSize), Point((posX-i+1)*cellSize, (posY+1)*cellSize))
        rect.setFill('white')
        rect.draw(win)
        snake.insert(0, rect)
        Grid[posY][posX-i] = 1

    while quit == False :
        if lose == False :
            #Get the pressed key
            input = win.checkKey()

            #Change direction
            if input == 'Up' and dir!=1:
                dir = 0
            elif input == 'Down' and dir!=0:
                dir = 1
            elif input == 'Left' and dir!=3:
                dir = 2
            elif input == 'Right' and dir!=2:
                dir = 3

            #Update position based on direction
            if dir == 0 :
                posY -= 1
            elif dir == 1 :
                posY += 1
            elif dir == 2 :
                posX -= 1
            elif dir == 3 :
                posX += 1

            #Check colision with walls or itself
            if posX < 0 or posX+1 > columns or posY < 0 or posY+1 > rows or Grid[posY][posX] == 1 :
                lose = True
            #Move snake if no collision
            else :
                #Check if eating the food
                if Grid[posY][posX] == 2 :
                    ateThisTurn = True
                    food.destroy()
                    food = newFood()
                    length += 1
                    score += 1
                    Time=Time*1.01

                #Create new rectangle
                newRect = Rectangle(Point(posX*cellSize, posY*cellSize), Point((posX+1)*cellSize, (posY+1)*cellSize))
                newRect.setFill('white')
                newRect.draw(win)
                snake.append(newRect)
                #Update Grid
                Grid[posY][posX] = 1

                if ateThisTurn :
                    ateThisTurn = False
                else :
                    #Remove last rectangle from snake
                    snake[0].undraw()
                    Grid[int(snake[0].getP1().getY()/cellSize)][int(snake[0].getP1().getX()//cellSize)] = 0
                    snake.pop(0)


        #You just lost the game ;)
        if lose == True :
            #Undraw snake and food
            food.destroy()
            for rect in snake :
                rect.undraw()
            #Display You lost and wait for a keypress to quit
            message = Text(Point(width/2, height/2),"You lost")
            message.setFill('white')
            message.draw(win)
            scoreMsg = Text(Point(width/2, height/2+15),"Your score : "+str(score))
            scoreMsg.setFill('white')
            scoreMsg.draw(win)
            win.getKey()
            quit = True

        time.sleep(1.0/Time)

main()
