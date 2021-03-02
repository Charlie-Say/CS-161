'''
Draw a polygon according to the users input.

Using turtle graphics to prompt the user to input the number of sides.
Draw the shape with the given number of sides. Draw two of the same shapes.

Charlie Say
Lab 1
January 16, 2019

define main function
use for loop for first polygon
use while loop for second polygon
loop program if input is invalid
create exceptions
end program

functions: main(), turtle_lab()
variables: sides, degrees
formulas: degrees = 180 - 180*(sides - 2)/sides
'''


def turtle_lab():
    '''
    variables and loops.
    while & for loops
    drawing polygons
    '''
    import turtle

    while True:
        try:

            sides = int(input("How many sides of the polygon would you like to draw? "))
            degrees = 180 - 180*(sides - 2)/sides

            turtle.up()
            turtle.goto(-200,100)
            turtle.setup(width = 600, height = 300, startx = 1200, starty = 100)
            # draw a regular polygon using "for"
            for i in range(sides):
                        
                turtle.down()
                turtle.forward(100)
                turtle.right(degrees)

            turtle.up()
            turtle.forward(300)
                
            # draw the regular polygon using "while"
            count = 0

            while count < sides:
                count = count + 1

                turtle.down()
                turtle.forward(100)
                turtle.right(degrees)

        except Exception:
            print("Invalid input! Try again!")
            turtle_lab()

        print("Thank You for using my program! :)")
        turtle.done()

        

turtle_lab()

