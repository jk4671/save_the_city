"""
asteriods.py
Jordyn Kim
CS151-B Computational Thinking: Visual Media
Fall 2020
11/22/2020
Lab 10: Event-based programming
Create Game class and simulate Asteroids game
Credit: Brian Marks
"""

import home
import turtle_interpreter as ti
import turtle
import random


class Game:
    def __init__(self, playerSpeed=20, turnRate=10, enemyNumb=3, collisionRadius=30):
        '''Game constructor.
        Creates instance variables and runs methods neccessary to play the 70s arcade game Asteriods
       
        Parameters:
        -----------
        playerSpeed: int. Pixel of player's movement (DEFAULT: 20)
        turnRate: int. Angle of player's turn (DEFAULT: 10)
        enemyNumb: int. Number of enemies (DEFAULT: 3)
        collisionRadius: int. Defines how close the player needs to get to an enemy 
                        for the game to register that a collision happened (DEFAULT: 30)
        '''

        # Draw background of the scene (from Project09)
        home.main()

        # Make TurtleInterpreter object
        self.terp = ti.TurtleInterpreter()

        # Create an instance variable for Screen object
        self.screen = self.terp.getScreen()

        # Make player
        turt = self.makePlayer()
        self.player = turt

        # Player's pixel movement and turn rate
        self.moveDist = playerSpeed
        self.turnRate = turnRate

        # Minimum and maximum x and y positions that game enemies can occupy
        self.enemyX = 300
        self.enemyX2 = -300
        self.enemyY = 300
        self.enemyY2 = -300

        # Create enemyNumb count of enemies
        self.enemyNumb = enemyNumb
        enemyList = self.makeEnemies(self.enemyNumb)
        self.enemies = enemyList

        # Define how close the player needs to get to an enemy for the game to register that a collision happened
        self.collisionRadius = collisionRadius

        # Create game events 
        self.setupEvents()


    def run(self):
        '''Turns the tracer animations on (but speeds up animations) and starts the main game loop.
        '''
        # Call the tracer method on your `Screen` instance variable,
        # passing in True as the parameter to turn animations on.
        self.screen.tracer(True)

        # Call the listen method on your `Screen` instance variable
        # so that keyboard presses are not registered as events
        self.screen.listen()

        # Call the mainloop method on your `Screen` instance variable.
        self.screen.mainloop()


    def makePlayer(self):
        """
        Create Turtle object that is the main player that will move under keyboard control.
        
        Return
        -------------
        turt: Turtle object. Player turtle
        """
        # Create Turtle object with fastest speed
        turt = turtle.Turtle()
        turt.speed(10)

        # Register a new image to be the Turtle object
        self.screen.register_shape('rocketship.gif')
        turt.shape('rocketship.gif')

        # Pick the main player turtle's pen up and have it face northward.
        turt.penup()
        turt.setheading(90)

        # Return the Turtle object
        return turt

    
    def up(self):
        """
        Move the player Turtle object forward by its speed
        """
        self.player.forward(self.moveDist)


    def down(self):
        """
        Move the player Turtle object backward by its speed
        """
        self.player.backward(self.moveDist)


    def left(self):
        """
        Turn the player Turtle object left by its turn rate
        """
        self.player.left(self.turnRate)


    def right(self):
        """
        Turn the player Turtle object right by its turn rate
        """
        self.player.right(self.turnRate)


    def setupEvents(self):
        """
        This method should be responsible for creating your game events
        """
        # Keyboard callback events to up, down, left, right methods
        self.screen.onkeypress(self.up, "Up")
        self.screen.onkeypress(self.down, "Down")
        self.screen.onkeypress(self.left, "Left")
        self.screen.onkeypress(self.right, "Right")
        
        # Keybaord callback to quit the function when the user presses the "q" key
        self.screen.onkey(quit, 'q')

        # Add a timer event to make the enemies move repeatedly every 50 msec
        self.screen.ontimer(self.moveEnemiesRandomly, 50)

        # Add a timer event to check for collisions with the enemies every 50 msec
        self.screen.ontimer(self.checkForCollisions, 50)


    def placeEnemyRandomly(self, turt):
        """
        A method for placing an enemy randomly in the enemy region

        Parameters:
        -----------
        turt: Turtle object. Enemy turtle object
        """
        # Max, min x-axis: -300, 300
        # Max, min y-axis: -300, 300
        turt.goto(random.randint(self.enemyX2, self.enemyX), random.randint(self.enemyY2, self.enemyY))


    def makeEnemies(self, n):
        """
        A method to create some number of enemies

        Parameters:
        -----------
        n: int. Number of enemies you would like to make

        Return:
        -----------
        enemyList: list. List containing enemy turtles
        """
        # Enemy storage list
        enemyList = []

        # Create n Turtle objects and store them in a list.
        for i in range(n):
            # Create a Turtle object with fastest speed
            enemyTurt = turtle.Turtle()
            enemyTurt.speed(10)

            # Change enemy to a pink square
            enemyTurt.shape('square')
            enemyTurt.color('Pink', 'Pink')

            # Pick up their pens and place on screen randomly
            enemyTurt.penup()
            self.placeEnemyRandomly(enemyTurt)

            # Store created enemy to enemyList
            enemyList.append(enemyTurt)

        # Return the list of enemy Turtle objects.
        return enemyList


    def moveEnemiesRandomly(self):
        """
        Randomly move the enemies
        """
        # For each enemy Turtle in enemies list, set position to the current position 
        # plus a small random (x, y) offset.
        for enemy in self.enemies:
            enemyPosX , enemyPosY = enemy.position()
            enemy.goto(enemyPosX+random.randint(-5,5), enemyPosY+random.randint(-5,5))
        
        # Add a timer event to make the enemies move repeatedly every 50 msec
        self.screen.ontimer(self.moveEnemiesRandomly, 50)


    def checkForCollisions(self):
        """
        Collision detection to place enemy at random position if rocket collides with enemy
        """
        # Obtain player's x- and y-coordinates
        playerX = self.player.xcor()
        playerY = self.player.ycor()

        # Collect every enemie's x- and y-coordinates
        for enemy in self.enemies:
            enemyX = enemy.xcor()
            enemyY = enemy.ycor()

            # Calculate the distance between the main player and each enemy.
            if abs(playerX - enemyX) < self.collisionRadius and abs(playerY - enemyY) < self.collisionRadius:
                
                # If the distance is less than the collision radius, print "BOOM!" and call placeEnemyRandomly on the enemy that the player collided with.
                print("BOOM!")
                self.placeEnemyRandomly(enemy)

        # When done checking for collisions, add another event to call this function again in 50 msec
        self.screen.ontimer(self.checkForCollisions, 50)


def main():
    """
    Main code to create and simulate the game
    """
    # Create Game
    game = Game()
    # Simulate Game
    game.run()


if __name__ == '__main__':
    # Run the game
    main()