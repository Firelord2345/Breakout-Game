import turtle
import time

class Game:
    def __init__(self, screen, paddle, ball):
        self.screen = screen
        self.paddle = paddle
        self.ball = ball
        self.score = 0
        self.level = 1
        self.game_over = False
        self.bricks = []
        self.create_bricks()

    def create_bricks(self):
        # Create bricks for the level
        for row in range(5):  # 5 rows of bricks
            brick_row = []
            for col in range(8):  # 8 columns of bricks
                brick = turtle.Turtle()
                brick.speed(0)
                brick.shape("square")
                brick.color("blue")
                brick.penup()
                brick.goto(-350 + (col * 90), 250 - (row * 30))
                brick_row.append(brick)
            self.bricks.append(brick_row)

    def check_collision_with_bricks(self):
        for row in self.bricks:
            for brick in row:
                if self.ball.ball.distance(brick) < 25:
                    brick.hideturtle()
                    self.score += 10
                    self.ball.y_velocity = -self.ball.y_velocity
                    row.remove(brick)
                    return True
        return False

    def level_up(self):
        if len(self.bricks) == 0:  # If all bricks are destroyed
            self.level += 1
            self.create_bricks()  # Create a new set of bricks
            self.ball.x_velocity += 1  # Increase ball speed for the next level
            self.ball.y_velocity += 1

    def start_game(self):
        while not self.game_over:
            self.ball.move()
            self.ball.bounce(self.paddle)
            self.game_over = self.ball.check_border_collision()

            if self.check_collision_with_bricks():
                self.level_up()

            if self.game_over:
                self.game_over_message()

            time.sleep(0.01)

    def game_over_message(self):
        game_over_turtle = turtle.Turtle()
        game_over_turtle.color("white")
        game_over_turtle.penup()
        game_over_turtle.hideturtle()
        game_over_turtle.goto(0, 0)
        game_over_turtle.write(f"Game Over! Score: {self.score}", align="center", font=("Courier", 24, "normal"))
        self.screen.update()
        time.sleep(2)
        self.reset_game()

    def reset_game(self):
        self.score = 0
        self.level = 1
        self.paddle.reset_position()
        self.ball.reset_position()
        self.bricks.clear()
        self.create_bricks()
        self.game_over = False
        self.start_game()
