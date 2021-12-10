from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

with open("data.txt") as file:
    current_highscore = file.read()
    
    


class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(current_highscore)
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.goto(-125, 250)
        self.write(f"Score: {self.score}", align=ALIGNMENT, move=False, font=FONT)
        self.goto(125, 250)
        self.write(f"High Score: {self.high_score}", align=ALIGNMENT, move=False, font=FONT)


    

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("data.txt", mode="w") as file:
            file.write(str(self.high_score))
        self.score = 0

    def game_over(self):
        
        self.clear()
        
        
        

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        
