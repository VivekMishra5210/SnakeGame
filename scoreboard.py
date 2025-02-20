from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_sb()

    def update_sb(self):
        self.write(f"Score : {self.score}", move=False, align='center', font=('Arial', 18, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, 'center', ('Arial', 26, 'normal'))

    def refresh_sb(self):
        self.score += 1
        self.clear()
        self.update_sb()
