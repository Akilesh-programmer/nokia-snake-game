from turtle import Turtle

class Snake:
    def __init__(self):
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []

        for position in self.starting_positions:
            self.new_segment = Turtle(shape="square")
            self.new_segment.penup()
            self.new_segment.color("white")
            self.new_segment.goto(position)
            self.segments.append(self.new_segment)

    def forward(self):
        for segment in self.segments:
            segment.forward(20)

    def turn_left(self):
        number_of_segments = 0
        for segment in self.segments:
            number_of_segments += 1
        
        times_running = 0

        for segment in self.segments:

            tobe = 0
            times_running += 1

            if times_running != 1:
                for n in range(times_running - 1):
                    segment.forward(20)
                    tobe += 1
            segment.left(90)

            for n in range(number_of_segments - tobe):
                segment.forward(20)

    def turn_right(self):
        number_of_segments = 0
        for segment in self.segments:
            number_of_segments += 1
        
        times_running = 0

        for segment in self.segments:

            tobe = 0
            times_running += 1

            if times_running != 1:
                for n in range(times_running - 1):
                    segment.forward(20)
                    tobe += 1
            segment.right(90)

            for n in range(number_of_segments - tobe):
                segment.forward(20)