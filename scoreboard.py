from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 250)
        with open("data.txt") as file:
            self.high_score = int(file.read())

        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f" Your Score: {self.score}\n High Score: {self.high_score}", False, align="center", font=("Arial", 12, "bold"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", 'w') as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()


