"""
mygame.py
Jordyn Kim
CS151-B Computational Thinking: Visual Media
Fall 2020
11/22/2020
Lab 10: Event-based programming
Create MyGame class and simulate my game
"""

import home
import turtle_interpreter as ti
import turtle
import random
import time
import doneDraw
import beginDraw


class MyGame:
    def __init__(self, moveDist=10, enemyNumb=3, collisionRadius=30):
        '''MyGame constructor.
        Creates instance variables and runs methods neccessary to play my own game
       
        Parameters:
        -----------
        moveDist: int. Pixel of player's movement (DEFAULT: 10)
        enemyNumb: int. Number of enemies (DEFAULT: 3)
        collisionRadius: int. Defines how close the player needs to get to an enemy 
                        for the game to register that a collision happened (DEFAULT: 30)
        '''
        # Make TurtleInterpreter object
        self.terp = ti.TurtleInterpreter()

        # Create an instance variable for Screen object
        self.screen = self.terp.getScreen()

        # Draw the intro scene with instructions and pause for a bit
        beginDraw.main()
        time.sleep(10)

        # Draw background of the scene (from Project09)
        home.main()

        # Make player
        turt = self.makePlayer()
        self.player = turt

        # Player's pixel movement
        self.moveDist = moveDist

        # Minimum and maximum x positions that game enemies can occupy
        self.enemyX = 300
        self.enemyX2 = -300

        # Keep track of enemy count
        self.enemyTotal = 0

        # Create enemyNumb count of enemies
        self.enemyNumb = enemyNumb
        enemyList = self.makeEnemies(self.enemyNumb)
        self.enemies = enemyList

        # Define how close the player needs to get to an enemy for the game to register that a collision happened
        self.collisionRadius = collisionRadius

        # Create score counter
        counter = self.makeCounter()
        self.counter = counter

        # Initialize score
        self.score = 0

        # Make explosion turtle
        explosion = self.makeExplosion()
        self.explosion = explosion

        # Initialize state as True (will be turned to False after 30 sec of game)
        self.state=True

        # Initialize win or lose status as lost (will be turned to true when you collect more than 50% of bombs deployed)
        self.winOrLose='lost'

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
        self.screen.register_shape('basket.gif')
        turt.shape('basket.gif')

        # Pick the main player turtle's pen up and have it face northward.
        turt.penup()
        turt.setheading(90)

        # Return the Turtle object
        return turt


    def up(self):
        """
        Move the player Turtle object up by its speed
        """
        self.player.setheading(90)
        self.player.forward(self.moveDist)


    def down(self):
        """
        Move the player Turtle object down by its speed
        """
        self.player.setheading(270)
        self.player.forward(self.moveDist)


    def left(self):
        """
        Move the player Turtle object left by its speed
        """
        self.player.setheading(180)
        self.player.forward(self.moveDist)


    def right(self):        
        """
        Move the player Turtle object right by its speed
        """
        self.player.setheading(0)
        self.player.forward(self.moveDist)


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
        self.screen.onkeypress(quit, 'q')

        # Add a timer event to make the enemies move repeatedly every 30 msec
        self.screen.ontimer(self.moveEnemiesRandomly, 30)

        # Add a timer event to check for collisions with the enemies every 50 msec
        self.screen.ontimer(self.checkForCollisions, 30)

        # Stop the game after 30 seconds
        self.screen.ontimer(self.done, 30000)


    def placeEnemyRandomly(self, turt):
        """
        A method for placing an enemy randomly in the enemy region

        Parameters:
        -----------
        turt: Turtle object. Enemy turtle object
        """

        # Tally up created enemies in total
        self.enemyTotal += 1

        # Hide enemy before moving
        turt.hideturtle()
        # Always on top of screen at max, min x-axis (-300, 300)
        turt.goto(random.randint(self.enemyX2, self.enemyX), 300)
        # Hide enemy after moving
        turt.showturtle()


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

            # Change enemy to a bomb
            self.screen.register_shape('bomb.gif')
            enemyTurt.shape('bomb.gif')

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
        # minus small random y offset depending on the enemyNumb
        for enemy in self.enemies:
            enemyPosX , enemyPosY = enemy.position()
            enemy.goto(enemyPosX, enemyPosY-random.random()*10*self.enemyNumb/2)
        
        # Add a timer event to make the enemies move repeatedly every 30 msec
        self.screen.ontimer(self.moveEnemiesRandomly, 30)


    def checkForCollisions(self):
        """
        Collision detection to place enemy at random position if rocket collides with enemy
        """
        # Obtain player's x- and y-coordinates
        playerX = self.player.xcor()
        playerY = self.player.ycor()
        

        # Only run the following series of events if state is True
        if self.state==True:
            # Collect every enemie's x- and y-coordinates
            for enemy in self.enemies:
                enemyX = enemy.xcor()
                enemyY = enemy.ycor()

                # Calculate the distance between the main player and each enemy.
                if abs(playerX - enemyX) < self.collisionRadius and abs(playerY - enemyY) < self.collisionRadius:
                    # If the distance is less than the collision radius, prince 'Nice', 
                    print("NICE!")
                    # Call placeEnemyRandomly on the enemy that the player collided with.
                    self.placeEnemyRandomly(enemy)
                    # Increase score
                    self.score += 1
                    # Change counter on the screen
                    self.changeCounter()
   
                # If enemy moves out of the boundary
                if enemyY <= -350:
                    # Stamp the enemy
                    enemy.stamp()
                    # Call placeEnemyRandomly on the enemy
                    self.placeEnemyRandomly(enemy)
                    # Mark the explosion 
                    self.markExplosion(enemyX, -350)
        
        # When done checking for collisions, add another event to call this function again in 30 msec
        self.screen.ontimer(self.checkForCollisions, 20)


    def makeCounter(self):
        """
        A method to create a tally on screen

        Return:
        -----------
        turt: Turtle object. Score counter turtle
        """

        # Create a fast Turtle object
        turt = turtle.Turtle()
        turt.speed(10)

        # Hide the turtle object
        turt.hideturtle()

        # Make the turtle black
        turt.color('Black', 'Black')

        # Lift pen and write SAVED on top of the moon
        turt.penup()
        turt.goto(-335, 280)
        turt.write("SAVED", font=('Arial', 25, 'normal'))

        # Return the turtle
        return turt


    def changeCounter(self):
        """
        Method to rewrite the score on the screen
        """
        self.counter.clear()
        self.counter.write(self.score, font=('Arial', 30, 'normal'))


    def markExplosion(self, xcord, ycord):
        """
        Method to stamp the explosion turtle

        Parameters:
        -----------
        xcord: int. x-coordinate to stamp the explosion
        ycord: int. y-coordinate to stamp the explosion
        """
        self.explosion.goto(xcord, ycord)
        self.explosion.stamp()


    def makeExplosion(self):
        """
        A method to create an explosion on screen that will appear when enemy reaches the bottom of the screen
        
        Return:
        -----------
        turt: Turtle object. Explosion turtle object
        """
        # Create Turtle object with fastest speed
        turt = turtle.Turtle()
        turt.speed(10)

        # Register a new image to be the Turtle object
        self.screen.register_shape('explosion.gif')
        turt.hideturtle()
        turt.shape('explosion.gif')

        # Pick the turtle's pen up and have it face northward.
        turt.penup()
        turt.setheading(90)

        # Return the Turtle object
        return turt


    def done(self):
        """
        Method with ending page and win or lose status
        """
        # Turn state into False
        self.state=False
        # Clear the counter and explosion Turtles
        self.counter.clear()
        self.explosion.clear()
        # Clear the screen
        self.screen.clear()

        # If you caught more than 50% of enemies deployed, change winOrLose to "won"
        if self.score > self.enemyTotal-self.score:
            self.winOrLose = 'won'
        
        # Draw the ending screen with # of enemies caught, # enemies survived, whether you won or lost
        doneDraw.main(self.score, self.enemyTotal-self.score, self.winOrLose)


def main(userLevel):
    """
    Main code to create and simulate the game

    Parameters:
    -----------
    userLevel: int. Level of game
    """
    # Create Game (with number and speed of enemies depending on the level)
    mygame = MyGame(enemyNumb=3*userLevel)
    # Simulate Game
    mygame.run()


if __name__ == '__main__':
    # User input of the level
    userLevel = input("CHOOSE YOUR LEVEL: 1, 2, 3: ")    
    userLevel = int(userLevel)
    levels = [1, 2, 3]

    # Exit if user does not choose the write number
    if userLevel not in levels:
        print("YOU MUST CHOOSE 1, 2, OR 3")
        exit()

    # Run the game
    main(userLevel)