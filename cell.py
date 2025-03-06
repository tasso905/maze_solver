from graphics import Line, Point

class Cell:
    def __init__(self, x1, y1, x2, y2, win):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = win

        self.has_left_wall =  True
        self.has_right_wall = True 
        self.has_top_wall = True 
        self.has_bottom_wall = True

    def draw(self):
        if self.has_left_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(line, "black")
        if self.has_right_wall:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(line, "black")
        if self.has_top_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(line, "black")
        if self.has_bottom_wall:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(line, "black")
            
    def draw_move(self, to_cell, undo=False):
        # Calculate center points of both cells
        current_center_x = (self._x1 + self._x2) / 2
        current_center_y = (self._y1 + self._y2) / 2
        
        to_center_x = (to_cell._x1 + to_cell._x2) / 2
        to_center_y = (to_cell._y1 + to_cell._y2) / 2
        
        # Create a line from current cell center to target cell center
        line = Line(
            Point(current_center_x, current_center_y),
            Point(to_center_x, to_center_y)
        )
        
        # Choose color based on undo flag
        color = "gray" if undo else "red"
        
        # Draw the line
        self._win.draw_line(line, color)