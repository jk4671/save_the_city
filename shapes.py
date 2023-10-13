"""
shapes.py
Jordyn Kim
CS151-B Computational Thinking: Visual Media
Fall 2020
11/22/2020
Lab 10: Event-based programming
Stores Shape class and child shape classes (square, rectangle, triangle, star, and circle)
"""

import turtle_interpreter as ti


class Shape:
    def __init__(self, distance=100, angle=90, color=(0, 0, 0), lsysString=''):
        '''Shape constructor

        Parameters:
        -----------
        distance: float. Distance in pixels to go when moving the turtle forward
        angle: float. Angle in degrees to turn when turning the turtle left/right
        color: tuple of 3 floats. Default turtle pen color
        lsysString: str. The L-system string of drawing commands to draw the shape
            (e.g. made up of 'F', '+', '-', ...)
        '''

        # Create instance variables for all the parameters
        self.distance = distance
        self.angle = angle
        self.color = color
        self.lsysString = lsysString

        # Create an instance variable for a new TurtleInterpreter object
        self.terp = ti.TurtleInterpreter(width=800, height=800, bgColor='white')
    

    def getTI(self):
        """
        Get the TurtleInterpreter object
        """
        return self.terp

    
    def getString(self):
        """
        Get shape's L-system string
        """
        return self.lsysString


    def setColor(self, c):
        """
        Set the shape's color

        Parameters:
        -----------
        c: str. or tuple. color of the turtle
        """
        self.color = c


    def setDistance(self, dist):
        """
        Set the shape's edge distance
    
        Parameters:
        -----------
        dist: flt. turtle's distance for 'F'
        """
        self.distance = dist

    
    def setAngle(self, a):
        """
        Set the shape's turning angle

        Parameters:
        -----------
        a: flt. turtle's angle for '+' or '-'
        """
        self.angle = a


    def setString(self, s):
        """
        Set the L-system string

        Parameters:
        -----------
        s: str. L-system string
        """
        self.lsysString = s


    def draw(self, x_pos, y_pos, scale=1.0, heading=0):
        '''Draws the L-system string at the position `(x, y)` = `(x_pos, y_pos)` with the turtle
        facing the heading `heading`. The turtle drawing distance is scaled by `scale`.
        
        Parameters:
        -----------
        x_pos: flt. x-coordinate
        y_pos: flt. y-coordinate
        scale: flt. scale of the drawing distance (DEFAULT: 1)
        heading: flt. orientation of the shape (DEFAULT: 0)
        '''
        self.terp.goto(x_pos, y_pos, heading=heading)
        self.terp.setColor(self.color)
        self.terp.drawString(self.lsysString, self.distance*scale, self.angle)

class Square(Shape):
    def __init__(self, distance=100, color=(0, 0, 0), fill=False):
        '''Square constructor

        Parameters:
        -----------
        distance: float. Distance in pixels to go when moving the turtle forward
        color: tuple of 3 floats. Default turtle pen color
        fill: bool. True or False fill
        '''
        # Create a variable for the L-system string that would draw a square.
        self.lsysString = 'F+F+F+F'

        # if the fill parameter is true, concatenate the { and } characters
        # to the beginning and end of the L-system string,
        # updating the value of the L-system string.
        if fill:
            self.lsysString = '{' + self.lsysString + '}'

        # Call the parent's constructor, passing along values for all its
        # parameters.
        super().__init__(distance=distance, color=color, lsysString=self.lsysString)
        

class Rectangle(Shape):
    def __init__(self, distance=100, color=(0, 0, 0), fill=False):
        '''Rectangle constructor

        Parameters:
        -----------
        distance: float. Distance in pixels to go when moving the turtle forward
        color: tuple of 3 floats. Default turtle pen color
        fill: bool. True or False fill
        '''
        # Create a variable for the L-system string that would draw a rectangle.
        self.lsysString = 'FF+F+FF+F'

        # if the fill parameter is true, concatenate the { and } characters
        # to the beginning and end of the L-system string,
        # updating the value of the L-system string.
        if fill:
            self.lsysString = '{' + self.lsysString + '}'

        # Call the parent's constructor, passing along values for all its
        # parameters.
        super().__init__(distance=distance, color=color, lsysString=self.lsysString)
        

class Triangle(Shape):
    def __init__(self, distance=100, color=(0, 0, 0), fill=False):
        '''Triangle constructor

        Parameters:
        -----------
        distance: float. Distance in pixels to go when moving the turtle forward
        color: tuple of 3 floats. Default turtle pen color
        fill: bool. True or False fill
        '''
        # Create a variable for the L-system string that would draw a triangle.
        self.lsysString = 'F+F+F'

        # if the fill parameter is true, concatenate the { and } characters
        # to the beginning and end of the L-system string,
        # updating the value of the L-system string.
        if fill:
            self.lsysString = '{' + self.lsysString + '}'   
        # Call the parent's constructor, passing along values for all its
        # parameters.
        super().__init__(distance=distance, color=color, angle=240, lsysString=self.lsysString)
        

class Star(Shape):
    def __init__(self, distance=40, color=(0, 0, 0), fill=False):
        '''Star constructor

        Parameters:
        -----------
        distance: float. Distance in pixels to go when moving the turtle forward
        color: tuple of 3 floats. Default turtle pen color
        fill: bool. True or False fill
        '''
        # Create a variable for the L-system string that would draw a star.
        self.lsysString = 'F-F++F-F++F-F++F-F++F-F++F-F'

        # if the fill parameter is true, concatenate the { and } characters
        # to the beginning and end of the L-system string,
        # updating the value of the L-system string.
        if fill:
            self.lsysString = '{' + self.lsysString + '}'   
        # Call the parent's constructor, passing along values for all its
        # parameters.
        super().__init__(distance=distance, color=color, angle=60, lsysString=self.lsysString)


class Circle(Shape):
    def __init__(self, distance=40, color=(0, 0, 0), fill=False):
        '''Circle constructor

        Parameters:
        -----------
        distance: float. Distance in pixels to go when moving the turtle forward
        color: tuple of 3 floats. Default turtle pen color
        fill: bool. True or False fill
        '''
        # Create a variable for the L-system string that would draw a circle.
        self.lsysString = 'C'

        # if the fill parameter is true, concatenate the { and } characters
        # to the beginning and end of the L-system string,
        # updating the value of the L-system string.
        if fill:
            self.lsysString = '{' + self.lsysString + '}'   
        # Call the parent's constructor, passing along values for all its
        # parameters.
        super().__init__(distance=distance, color=color, angle=60, lsysString=self.lsysString)


def testShapes():
    """
    Main function to test the shapes
    """
    # make all shapes
    square = Square(color = 'blue', fill=False)
    triangle = Triangle(color = 'red', fill=True)
    star = Star(color = 'yellow', fill=True)
    circle = Circle(distance=20, color='Aqua', fill=False)
    rectangle = Rectangle(distance=10, color='peru', fill=True)
    
    # draw all shapes at different locations, sizes, and orientations
    square.draw(-200, 0, scale=0.5, heading=80)
    triangle.draw(200, 0, scale=0.3, heading=30)
    star.draw(100, 100, scale=2, heading=100)
    circle.draw(-100, -100, scale=0.8, heading=90)
    rectangle.draw(10, -180, scale=1.2, heading=30)

    # keep window open
    square.getTI().hold()


if __name__ == '__main__':
    testShapes()