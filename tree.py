"""
tree.py
Jordyn Kim
CS151-B Computational Thinking: Visual Media
Fall 2020
11/22/2020
Lab 10: Event-based programming
Stores child tree class
"""

import lsystem
import shapes


class Tree(shapes.Shape):
    def __init__(self, distance=5, angle=22.5, color=(0.5, 0.4, 0.3), iterations=3, filename=None):
        '''Tree constructor

        Parameters:
        -----------
        distance: float. Distance in pixels to go when moving the turtle forward
        angle: float. Angle in degrees to turn when turning the turtle left/right
        color: tuple of 3 floats. Default turtle pen color
        lsysString: str. The L-system string of drawing commands to draw the shape
            (e.g. made up of 'F', '+', '-', ...)
        iterations: int. Number of iterations to apply the replacement rules on the tree base string.
        filename: str. Filename for the text file that contains the tree L-system base string and
            1+ replacement rules.
        '''
        super().__init__(distance=distance, angle=angle, color=color)
        self.iterations = iterations
        self.filename = filename

        # if filename exists, read the filename
        if filename != None:
            self.read(self.filename) 
            

    def setIterations(self, iterations):
        """
        Set the number of L-system iterations:


        Parameters:
        -----------
        iterations: int. number of times you want to apply the iteration rule
        """
        self.iterations = iterations


    def read(self, filename):
        """
        Have the L-system object read in a base string and replacement rules from a file

        Parameters:
        -----------
        filename: str. The L-system file
        """
        lsys = lsystem.Lsystem(filename=filename)
        self.lsysString = lsys.buildString(self.iterations)
    

    def draw(self, x_pos, y_pos, scale=1.0, heading=90):
        """
        Extend the parent's draw method, but it should by default make 
        it so that the tree is drawn right-side up

        Parameters:
        -----------
        x_pos: flt. x-coordinate
        y_pos: flt. y-coordinate
        scale: flt. scale of the drawing distance (DEFAULT: 1)
        heading: flt. orientation of the shape (DEFAULT: 90)
        """
        super().draw(x_pos, y_pos, scale=scale, heading=heading)


def testShapes():
    """
    Main function to test the shapes
    """
    # make 3 trees
    tree1 = Tree(color='green', iterations=4,filename='systemJ.txt')
    tree2 = Tree(color='blue', iterations=5, filename='systemJ.txt')
    tree3 = Tree(color='purple', iterations=3, filename='systemJ.txt')

    # draw 3 trees
    tree1.draw(-200, 0, scale=2, heading=80)
    tree2.draw(200, -300, scale=0.5, heading=30)
    tree3.draw(100, 100, scale=4, heading=100)

    # keep window open
    tree1.getTI().hold()


if __name__ == '__main__':
    testShapes()