"""
turtle_interpreter.py
Jordyn Kim
CS151-B Computational Thinking: Visual Media
Fall 2020
11/22/2020
Lab 10: Event-based programming
Write TurtleInterpreter to translate a L-system string into turtle movement and drawing commands.
"""

import turtle


class TurtleInterpreter:
    # Create a Turtle object global variable
    turt = turtle.Turtle()
    # Create a Screen object global variable
    screen = turtle.Screen()

    def __init__(self, width=800, height=800, bgColor='white'):
        '''TurtleInterpreter constructor.
        Creates instance variables for a Turtle object and a Screen object with a particular window
        `width`, `height`, and background color `bgColor`.
       
        Parameters:
        -----------
        width: int. width of the Screen object (DEFAULT: 800)
        height: int. height of the Screen object (DEFAULT: 800)
        bgColor: str. color of the Screen object (DEFAULT: white)
        '''

        # Set the screen's height, width, and color based on the parameters
        TurtleInterpreter.screen.screensize(width, height)
        TurtleInterpreter.screen.setup(width = width, height = height)
        TurtleInterpreter.screen.bgcolor(bgColor)

        # Turn the screen's tracer off.
        TurtleInterpreter.screen.tracer(False)

        self.stack = []
        self.state = []

        # Hide turtle
        TurtleInterpreter.turt.hideturtle()


    def setbgColor(self, color):
        """
        Set the turtle screen's background color

        Parameters:
        -----------
        color: str. background color
        """
        TurtleInterpreter.turt.screen.bgcolor(color)


    def setColor(self, c):
        """
        Set the turtle's pen color to the color c
        
        Parameters:
        -----------
        c: str. Turtle's pen color
        """
        TurtleInterpreter.turt.color(c, c)


    def beginFill(self):
        """
        Begin filling the shape
        """
        TurtleInterpreter.turt.begin_fill()


    def endFill(self):
        """
        End filling the shape
        """
        TurtleInterpreter.turt.end_fill()
    

    def setWidth(self, w):
        """
        Set the turtle's pen width to the int w

        Parameters:
        -----------
        w: int. Turtle's pen width
        """
        TurtleInterpreter.turt.pensize(w)


    def goto(self, x, y, heading=None):
        """
        A goto function that places the turtle at (x, y) and sets 
        the heading to heading if the value of the heading parameter passed in is not None
        
        Parameters:
        -----------
        x: int. Turtle's x coordinate
        y: int. Turtle's y coordinate
        heading: int. Turtle's direction in degrees (DEFAULT: None)
        """
        TurtleInterpreter.turt.penup()
        TurtleInterpreter.turt.goto(x, y)
        TurtleInterpreter.turt.pendown()
        # the heading to heading if the value of the heading parameter passed in is not None
        if heading != None:
            TurtleInterpreter.turt.setheading(heading)


    def getScreen(self):
        """
        Returns the Screen object, a class global variable
        """
        return TurtleInterpreter.screen


    def getScreenWidth(self):
        """
        Get the screen's window width
        """
        return TurtleInterpreter.screen.screensize()[0]


    def getScreenHeight(self):
        """
        Get the screen's window height
        """
        return TurtleInterpreter.screen.screensize()[1]


    def getColor(self):
        """
        Get the turtle's color
        """
        return TurtleInterpreter.turt.color()


    def hold(self):
        '''Holds the screen open until user clicks or presses 'q' key'''

        # Hide the turtle cursor and update the screen
        TurtleInterpreter.turt.hideturtle()
        TurtleInterpreter.screen.update()

        # Close the window when users presses the 'q' key
        TurtleInterpreter.screen.onkey(turtle.bye, 'q')

        # Listen for the q button press event
        TurtleInterpreter.screen.listen()

        # Have the turtle listen for a click
        TurtleInterpreter.screen.exitonclick()
    

    def write(self, sentence, x, y, color='black', align='center', font=("Courier New", 20, "normal")):
        """
        Write the string

        Parameters
        ------------
        sentence: str. What you want to write
        x: int. x coordinate
        y: int. y coordinate
        color: str. or RGB. Color of the turtle (DEFAULT: black)
        align: str. Alignment of the text (DEFAULT: center)
        font: tuple. (DEFAULT: ("Courier New", 20, "normal"))
        """
        
        # store original color
        originalColor = self.getColor()
        # go to a position
        self.goto(x, y)
        # change color
        self.setColor(color)
        # write the string
        TurtleInterpreter.turt.write(sentence, align=align, font=font)
        # change the turtle back to the original color
        self.setColor(originalColor[0])


    def drawString(self, lsysString, distance, angle):
        '''Interpret each character in an L-system string as a turtle command.

        Parameters:
        -----------
        lsysString: str. The L-system string with characters that will be interpreted as drawing
            commands.
        distance: distance to travel with F command.
        angle: turning angle (in deg) for each right/left command.
        '''

        # Walk through the lsysString character-by-character and
        for char in lsysString:
            # have the turtle object (instance variable) carry out the appropriate commands
            if char == "F":
                # move turtle forward
                TurtleInterpreter.turt.forward(distance) 
            if char == "+":
                # turn turtle left
                TurtleInterpreter.turt.left(angle)
            if char == '-':
                # turn turtle right
                TurtleInterpreter.turt.right(angle)
            if char == '{':
                # have the turtle start filling
                TurtleInterpreter.turt.begin_fill()
            if char == '}':
                # have the turtle stop filling
                TurtleInterpreter.turt.end_fill()
            if char == '[':
                # save the current turtle state (position and heading)
                self.stack.append(TurtleInterpreter.turt.heading())
                self.stack.append(TurtleInterpreter.turt.position())
            if char == ']':
                # restore the previous turtle state (position and heading)
                prevPos = self.stack.pop()
                prevHeading = self.stack.pop()
                x = prevPos[0]
                y = prevPos[1]
                self.goto(x, y, heading=prevHeading)
            if char == '<':
                # save the current turtle color state.
                self.state.append(TurtleInterpreter.turt.color()[0])
            if char == '>': 
                # restore the current turtle color state.
                prevColor = self.state.pop()
                self.setColor(prevColor)
            if char == 'g':
                # set the turtle's color to green (e.g. (0.15, 0.5, 0.2)).
                self.setColor((0.15, 0.5, 0.2))
            if char == 'y':
                # set the turtle's color to yellow (e.g. (0.8, 0.8, 0.3)).
                self.setColor((0.8, 0.8, 0.3))
            if char == 'r':
                # set the turtle's color to red (e.g. (0.7, 0.2, 0.3)).
                self.setColor((0.7, 0.2, 0.3))
            if char == 'L':
                # draw a leaf at the current turtle position
                # save turtle's position
                self.stack.append(TurtleInterpreter.turt.position())
                # fill the leaf
                self.beginFill()
                # leaf is half a circle
                TurtleInterpreter.turt.circle(distance/4, 180)
                # end the fill
                self.endFill()
                # restore turtle's position
                prevPos = self.stack.pop()
                x = prevPos[0]
                y = prevPos[1]
                TurtleInterpreter.turt.goto(x, y)
            if char == 'B':
                # draw a red berry at the current turtle position
                # save the current turtle color state.
                self.state.append(TurtleInterpreter.turt.color()[0])
                # set the turtle's color to red (e.g. (0.7, 0.2, 0.3)).
                self.setColor((0.7, 0.2, 0.3))
                # fill the cherry
                self.beginFill()
                # cherry is a circle
                TurtleInterpreter.turt.circle(distance/4)
                # end the fill
                self.endFill()
                # restore previous color
                prevColor = self.state.pop()
                self.setColor(prevColor)
            if char == 'S':
                # draw snowball
                # save the current turtle color state.
                self.state.append(TurtleInterpreter.turt.color()[0])
                # set the turtle's color to white
                self.setColor('white')
                # fill the snowball
                self.beginFill()
                # snowball is a circle
                TurtleInterpreter.turt.circle(distance/2)
                # end the fill
                self.endFill()
                # restore color
                prevColor = self.state.pop()
                self.setColor(prevColor)
            if char == 'C':
                # draw a circle
                TurtleInterpreter.turt.circle(distance/2)


        # Call the update method on the screen object to make sure
        # everything drawn shows up at the very end of the method
        TurtleInterpreter.screen.update()

