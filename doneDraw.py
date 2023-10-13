"""
doneDraw.py
Jordyn Kim
CS151-B Computational Thinking: Visual Media
Fall 2020
11/22/2020
Lab 10: Event-based programming
Ending screen of my game
"""

import shapes
import random


def messageBox(rectangle, star, xcor, ycor, message, boxColor='Light Pink', fontColor='White', scale=2, fontSize=20):
    """
    Compound textbox using Rectangle object and str

    Parameters:
    -----------
    rectangle: Rectangle object
    xcor: int. x-coordinate to stamp the explosion
    ycord: int. y-coordinate to stamp the explosion
    message: str. The message to display
    boxColor: str. The color of the display box (DEFAULT: 'Light Pink')
    fontColor: str. The color of the font (DEFAULT: 'White')
    scale: int. The scale of the textbox (DEFAULT: 2)
    fontSize: int. The font size (DEFAULT: 20)
    """
    # Draw the rectangle with the set color
    rectangle.setColor(boxColor)
    # Adjust the rectangle size
    rectangle.setDistance(100*scale)
    # Draw the rectangle at particular x- and y-coord
    rectangle.draw(xcor, ycor)
    # Write text on the box
    rectangle.getTI().write(message, xcor+100*scale, ycor+20*scale, color=fontColor, font=("Helvetica", fontSize, "normal"))


def main(score, lost, winOrLose):
    """
    The main function to draw the ending scene of mygame

    Parameters:
    -----------
    score: int. The total number of bombs caught
    lost: int. The total number of bombs not caught
    winOrLose: str. Whether you won the game or not (Win if you catch more than 50% of deployed bombs)
    """
    # Create Star and Rectangle objects
    star = shapes.Star(distance=10, color='gold', fill=True)
    rectangle = shapes.Rectangle(distance=100, color='Light Pink', fill=True)

    # Set the background color black
    rectangle.getTI().getScreen().bgcolor('Black')

    # Draw stars
    for i in range(20):
        star.draw(random.randint(-400, 400), random.randint(-400, 400), scale=0.2)
    
    # Draw that time's over
    messageBox(rectangle, star, -200, 0, "   TIME'S UP\n\nGAME'S OVER", fontSize=40)
    
    # Draw how many bombs caught
    messageBox(rectangle, star, -100, -150, "You caught\n"+str(score)+" bombs", boxColor="Lavender", fontColor='Black',scale=1)
    
    # Draw how many bombs not caught
    messageBox(rectangle, star, -100, -250, "BUT...\n"+str(lost)+" bombs\nweren't caught", boxColor="Salmon", fontColor='Black',scale=1)
    
    # Draw wheter you won or not
    messageBox(rectangle, star, -100, -350, "So you\n"+winOrLose, boxColor="Medium Spring Green", fontColor='Black',scale=1, fontSize=30)

    # rectangle.getTI().hold()

if __name__ == '__main__':
    # Draw the ending scene of mygame
    main(3, 3, 'won')