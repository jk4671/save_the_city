"""
home.py
Jordyn Kim
CS151-B Computational Thinking: Visual Media
Fall 2020
11/22/2020
Lab 10: Event-based programming
Create a new scene representing a scene near your home
"""

import shapes
import tree
import random


def building(rectangle, square, x, y, s):
    """
    Create a tall gray building using Rectangle and Square objects

    Parameters:
    -----------
    rectangle: Rectangle obj.
    square: Square obj.
    x: flt. x-coordinate
    y: flt. y-coordinate
    s: flt. size of the building
    """

    # make the building using a Rectangle object
    rectangle.setColor('slate gray')
    rectangle.draw(x, y, scale=s, heading=90)

    # make multiple windows using a Square object
    square.setColor('black')
    square.setDistance(20)
    
    # make 6 rows and 4 columns
    for i in range(6):
        for j in range(4):
            square.draw(x-85*s+20*j*s, y+20*s+30*i*s, scale = 0.7*s, heading=0)
    

def main():
    """
    Main function to draw a scene in Chicago
    """

    # create shape objects 
    square = shapes.Square(distance=400, color = 'gray',fill=True)
    rectangle = shapes.Rectangle(distance=100, color='slate gray', fill=True)
    unfilledRectangle = shapes.Rectangle(distance=100, color='yellow', fill=False)
    circle = shapes.Circle(distance=100, color='cornsilk', fill=True)
    star = shapes.Star(distance=10, color='gold', fill=True)
    mytree1 = tree.Tree(distance=5, color='Burlywood', iterations=5, filename='systemJ.txt')
    mytree2 = tree.Tree(distance=5, color='Burlywood', iterations=5, filename='systemJ.txt')
    mytree3 = tree.Tree(distance=5, color='Burlywood', iterations=5, filename='systemJ.txt')

    # store trees into a list
    treeList = [mytree1, mytree2, mytree3]

    # draw cement
    square.setColor('gray')
    square.draw(-400, -900, scale=2, heading=0)

    # draw Lake Michigan
    square.setColor('royal blue')
    square.draw(-400, -100, scale=2, heading=0)

    # draw the sky
    square.setColor('dark blue')
    square.draw(-400, 0, scale=2, heading=0)

    # draw the highway with yellow outline
    rectangle.setColor('black')
    rectangle.draw(-400, -750, scale=4, heading=0)
    unfilledRectangle.draw(-400, -750, scale=4, heading=0)

    # draw moon
    circle.draw(-300, 250, scale=1, heading=0)
    
    # draw buildings side by side
    for i in range(5):
        building(rectangle, square, -50-40*i, -100-60*i, 1+0.2*i)
        building(rectangle, square, 150+60*i, -100-60*i, 1+0.2*i)
    
    # draw random trees side by side 
    for i in range(9):
        choosenTree = random.choice(treeList)
        choosenTree.draw(-50-20*i, -100-30*i, scale=0.3)
        choosenTree.draw(50+20*i, -100-30*i, scale=0.3)

    # draw stars
    for i in range(20):
        star.draw(random.randint(-400, 400), random.randint(100, 400), scale=0.2)
    
    # keep window open
    # square.getTI().hold()


if __name__ == '__main__':
    main()