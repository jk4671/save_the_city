"""
beginDraw.py
Jordyn Kim
CS151-B Computational Thinking: Visual Media
Fall 2020
11/22/2020
Lab 10: Event-based programming
Beginning screen of my game
"""

import shapes
import random


def messageBox(rectangle, xcor, ycor, message, boxColor='Light Pink', fontColor='White', scale=1, fontSize=20):
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
    scale: int. The scale of the textbox (DEFAULT: 1)
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


def main():
    """
    The main function to draw the intro scene of mygame
    """
    # Create Star and Rectangle objects
    star = shapes.Star(distance=10, color='gold', fill=True)
    rectangle = shapes.Rectangle(distance=100, color='Light Pink', fill=True)

    # Set the background color black
    rectangle.getTI().getScreen().bgcolor('Black')

    # Draw stars
    for i in range(20):
        star.draw(random.randint(-400, 400), random.randint(-400, 400), scale=0.2)
    
    # Draw the title of my game
    messageBox(rectangle, -200, 100, "SAVE THE CITY\n", scale=2, fontSize=45)
    
    # Draw the instructions
    messageBox(rectangle, -200, -200, "\nInstructions:\nYou are given 30 seconds.\nUse your arrow keys (up, down, left, right)\nto move the basket to collect\nthe dropping bombs.\nYou win if you catch 50%\nof bombs deployed.", boxColor='Lavender', fontColor='black', scale=2)
    
    # Draw how to leave the game
    messageBox(rectangle, -100, -330, "If you need to exit \nthe game, press q.", boxColor='Cornflower Blue', fontColor='black', scale=1, fontSize=17)

    # rectangle.getTI().hold()

if __name__ == '__main__':
    # Draw the intro scene of mygame
    main()