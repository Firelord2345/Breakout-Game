import turtle
import random

class Ball:
    def __init__(self, screen):
        self.screen = screen
        self.ball = turtle.Turtle()
        self.ball.speed(0)  # Set maximum speed for the ball
        self.ball.shape("square")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(0, -230)
        
        # Set initial velocity for the ball (no vibration)
        self.x_velocity = 4  # Initial horizontal speed
        self.y_velocity = 4  # Initial vertical speed

    def move(self):
        # Smooth movement, no jittering
        x = self.ball.xcor()
        y = self.ball.ycor()
        self.ball.setx(x + self.x_velocity)
        self.ball.sety(y + self.y_velocity)

    def bounce(self, paddle):
        # Check if the ball hits the paddle
        if self.ball.ycor() > paddle.paddle.ycor() + 10 and self.ball.ycor() < paddle.paddle.ycor() + 20:
            if self.ball.xcor() > paddle.paddle.xcor() - 50 and self.ball.xcor() < paddle.paddle.xcor() + 50:
                # Ball hits the paddle, reverse its vertical direction
                self.y_velocity = -self.y_velocity

                # Randomize horizontal direction a little, but keep the ball steady
                self.x_velocity += random.choice([0.5, -0.5])

                # Keep velocity within a reasonable range to avoid excessive jittering
                if abs(self.x_velocity) < 5:
                    self.x_velocity *= 1.05
                if abs(self.y_velocity) < 5:
                    self.y_velocity *= 1.05

    def check_border_collision(self):
        x = self.ball.xcor()
        y = self.ball.ycor()

        # Bounce off left and right borders
        if x > 390 or x < -390:
            self.x_velocity = -self.x_velocity

        # Bounce off top border
        if y > 290:
            self.y_velocity = -self.y_velocity

        # Ball falls below the paddle (game over condition)
        if y < -290:
            return True
        return False

    def reset_position(self):
        self.ball.goto(0, -230)
        self.x_velocity = 4
        self.y_velocity = 4