'''
CS161 lab_1
using turtle graphics to prompt the user to input the number of sides.
draw the shape with the number of sides given by the user.
ask the user for input of how much red, green, and blue is wanted in the polygon.
make sure the values of the input is 1 => n => 0
create an exception if the input is invalid
'''


def turtle_lab():
    # import turtle
    import turtle

    # start a while condition/loop to make sure input is valid
    while True:
        try:
            # define variables & expressions
            # prompt the user for the number of sides of a polygon and color
            sides = int(input("How many sides of the polygon would you like to draw? "))
            red = float(input("How much red would you like to fill in the polygon (any number between 0 - 1)? "))
            
            green = float(input("How much green would you like to fill in the polygon (any number between 0 - 1)? "))
            
            blue = float(input("How much blue would you like to fill in the polygon (any number between 0 - 1)? "))
            
            if(0 <= red,green,blue <= 1):       

                # degree formula for polygon
                degrees = 180 - 180*(sides - 2)/sides

                # user input of colors using input and variable
                turtle.color(red,green,blue)
                # start color fill of polygon
                turtle.begin_fill()

        
                # draw a regular polygon using "for"
                for i in range(sides):
                            
                    # drop pen onto surface. move forward. turn according to user input angle (degrees)
                    turtle.down()
                    turtle.forward(100)
                    turtle.right(degrees)

                # move away from the first polygon. move pen up and forward
                turtle.up()
                turtle.forward(300)
                    
                # draw the regular polygon using "while"
                count = 0

                while count < sides:
                    count = count + 1

                    turtle.down()
                    turtle.forward(100)
                    turtle.right(degrees)

                # end color fill of polygon
                turtle.end_fill()

        except Exception:
            print("Those aren't valid inputs! Try again!")
            turtle_lab()
        

        print("Thank You for using my program! :)")
        # end the program by using turtle.bye() or turtle.done()
        turtle.done()
        
        

turtle_lab()

