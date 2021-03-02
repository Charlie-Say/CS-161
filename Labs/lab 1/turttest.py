#prompt the user for the number of sides of a polygon.
#define variables & expressions

def turtlab():
    import turtle
    
    while True:
        try:
            sides = int(input("How many sides of the polygon would you like to draw? "))
            color = input("What color would you like to fill in the polygon? ")
            #degree formula for polygon
            degrees = 180 - 180*(sides - 2)/sides

            #user input of colors using inputer and variable
            turtle.color(color)
            #start color fill of polygon
            turtle.begin_fill()

            #draw a regular polygon using "for"
            for i in range(sides):
                        
                #drop pen onto surface. move forward. turn according to user input angle (degrees)
                turtle.down()
                turtle.forward(100)
                turtle.right(degrees)

            #move away from the first polygon. move pen up and forward
            turtle.up()
            turtle.forward(300)
                
            #draw the regular polygon using "while"
            count = 0

            while count < sides:
                count = count + 1

                turtle.down()
                turtle.forward(100)
                turtle.right(degrees)

            #end color fill of polygon
            turtle.end_fill()
                    
        except Exception:
            print("Invalid input! Try again!")
            turtlab()

        print("Thank You for using my program! :)")

        turtle.done()

        

turtlab()

