from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

if __name__ == "__main__":
    print('')


class Snake:

    def __init__(self):
        self.segments = []
        self.createSnake()
        self.head = self.segments[0]

    def createSnake(self):
        for position in STARTING_POSITIONS:
            self.addSegment(position)

    def addSegment(self, position):
        newSegment = Turtle("square")
        newSegment.color("white")
        newSegment.penup()
        newSegment.goto(position)
        self.segments.append(newSegment)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.createSnake()
        self.head = self.segments[0]

    def extend(self):
        self.addSegment(self.segments[-1].position())
        # segments[-1] => is the last segment in the list
        # available before adding new segment

    def move(self):
        for segmentNumber in range(len(self.segments) - 1, 0, -1):
            newX = self.segments[segmentNumber - 1].xcor()
            newY = self.segments[segmentNumber - 1].ycor()
            self.segments[segmentNumber].goto(newX, newY)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
