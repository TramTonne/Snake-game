from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        #read highscore from the data text file
        with open("data.txt") as data:
            self.high_score = int(data.read())
        # self.highscore = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.update_score()
        self.hideturtle()
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} | Highscore: {self.high_score}", align="center", font=("Courier",24,"normal"))
    #increase score when snake eat the food
    def score_increment(self):
        self.score+=1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",mode ="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    # def collision(self):
    #     self.color("white")
    #     self.goto(0,0)
    #     self.write("Game Over",align="center",font=("Courier",24,"normal"))