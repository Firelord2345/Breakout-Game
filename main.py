import turtle
from paddle import Paddle
from ball import Ball
from game import Game

# Set up the screen
screen = turtle.Screen()
screen.title("Breakout Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)

# Create game objects
paddle = Paddle(screen)
ball = Ball(screen)
game = Game(screen, paddle, ball)

# Start the game loop
game.start_game()

screen.mainloop()  # Keeps the window open
