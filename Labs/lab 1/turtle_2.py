'''
Draw a polygon according to the users input and fill them with the same color.

Using turtle graphics to prompt the user to input the number of sides of
the polygon. Then draw the shape with the number of sides given. Ask the user for input
of how much red, green, and blue is wanted in the polygon. Then fill in
the shapes with the color according to the users input.

Charlie Say
Lab 1
January 16, 2019

define main() function
create inputs and variables using floats
create condition that input must be 0 <= red, green, blue <= 1
calculate degrees
create loops for how many sides are drawn
fill in the polygons
make exceptions to reloop program if error
end program

function: turtle_lab()
variables: sides, red, green, blue
loops: for, while
formulas: degrees = 180 - 180*(sides - 2)/sides
conditions: if 0 <= red, green, blue <= 1
'''

def turtle_lab():
    '''
    loops and conditions. variables, expressions.
    ask for inputs for variables
    draw polygons
    '''

    import turtle

    while True:
        try:

            sides = int(input("How many sides of the polygon would you like to draw? "))
            red = float(input("How much red would you like to fill in the polygon (any number between 0.0 - 1)? "))
            green = float(input("How much green would you like to fill in the polygon (any number between 0.0 - 1)? "))
            blue = float(input("How much blue would you like to fill in the polygon (any number between 0.0 - 1)? "))

            turtle.up()
            turtle.goto(-200,100)
            turtle.setup(width = 600, height = 300, startx = 1200, starty = 100)
            
            if(0 <= red,green,blue <= 1):       

                degrees = 180 - 180*(sides - 2)/sides

                turtle.color(red,green,blue)
                turtle.begin_fill()

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

                turtle.end_fill()

        except Exception:
            print("Those aren't valid inputs! Only numbers between 0.0 and 1. Try again!")
            turtle_lab()
        
        print("Thank You for using my program! :)")
        turtle.done()
        
        
turtle_lab()

