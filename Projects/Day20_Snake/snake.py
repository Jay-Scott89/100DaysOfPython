from turtle import Turtle

START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in START_POS:
            self.add_segment(position)
            
    def add_segment(self, position):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DIST)
    
    def grow(self):
        self.add_segment(self.segments[-1].position())

    def _would_hit_neck(self, heading):
        head_x, head_y = self.head.position()

        if heading == 90:
            next_pos = (head_x, head_y + MOVE_DIST)
        elif heading == 270:   # down
            next_pos = (head_x, head_y - MOVE_DIST)
        elif heading == 0:     # right
            next_pos = (head_x + MOVE_DIST, head_y)
        elif heading == 180:   # left
            next_pos = (head_x - MOVE_DIST, head_y)
        else:
            return False
        return next_pos == self.segments[1].position()

    def up(self):
        new_heading = 90
        if not self._would_hit_neck(new_heading):
            self.head.setheading(new_heading)

    def down(self):
        new_heading = 270
        if not self._would_hit_neck(new_heading):
            self.head.setheading(new_heading)

    def left(self):
        new_heading = 180
        if not self._would_hit_neck(new_heading):
            self.head.setheading(new_heading)

    def right(self):
        new_heading = 0
        if not self._would_hit_neck(new_heading):
            self.head.setheading(new_heading)



