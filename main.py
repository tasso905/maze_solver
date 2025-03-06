from graphics import Window, Line, Point
from cell import Cell
import time

def main():
    win = Window(800, 600)
    #line = Line(Point(50,50), Point(400,400))
    #win.draw_line(line, "black")
    cell1 = Cell(50, 50, 100, 100, win)
    cell1.has_left_wall = False
    #cell1.draw()

    cell2 = Cell(125, 125, 200, 200, win)
    cell2.has_right_wall = False
    #cell2.draw()

    cell1.draw_move(cell2)

    cell3 = Cell(225, 225, 250, 250, win)
    cell3.has_bottom_wall = False
    #cell3.draw()

    cell2.draw_move(cell3, undo=True)

    cell4 = Cell(300, 300, 500, 500, win)
    cell4.has_top_wall = False
    #cell4.draw()

    cell3.draw_move(cell4)

    win.wait_for_close()

main()

