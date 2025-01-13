import turtle

class Paddle:
    def __init__(self, screen):
        self.screen = screen
        self.paddle = turtle.Turtle()
        self.paddle.speed(0)
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=1, stretch_len=5)
        self.paddle.penup()
        self.paddle.goto(0, -250)

        # Paddle movement speed
        self.speed = 20

        # Keyboard bindings
        self.screen.listen()
        self.screen.onkey(self.move_left, "Left")
        self.screen.onkey(self.move_right, "Right")

    def move_left(self):
        x = self.paddle.xcor()
        if x > -350:
            self.paddle.setx(x - self.speed)

    def move_right(self):
        x = self.paddle.xcor()
        if x < 350:
            self.paddle.setx(x + self.speed)

    def reset_position(self):
        self.paddle.goto(0, -250)
