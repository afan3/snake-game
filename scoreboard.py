from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")

if __name__ == "__main__":
    print('')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        with open("data.txt") as data:
            self.highScore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,  280)
        self.updateScore()

    def increaseScore(self):
        self.score += 1
        self.updateScore()

    def updateScore(self):
        self.clear()
        self.write(arg=f"Score : {self.score} High Score : {self.highScore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highScore:
            self.highScore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highScore}")
        self.score = 0
        self.updateScore()
