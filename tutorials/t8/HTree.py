# Provided by Dr. Marzieh Ahmadzadeh & Nick Cheng. Edited by Yufei Cui


from graphics import *


# you need to download graphics.py and place it in the same folder as this code
def HTree(order, size, x, y, win):
    ''' (int, int, float, float, GraphWin) -> NoneType
        draw an HTree
        the first int is the order of the H Tree,
        size is the size of the horizontal and vertical line  of each H tree
        x, y are the coordinate of the middle of the horizontal line of the H
        '''

    # it doesn't make sense to draw a HTree with order <= 0
    if order <= 0:  # need a way for the algorithm to stop (base case)
        pass
    else:
        # finding the left and right x-coordinate
        halfsize = size / 2
        x0 = x - halfsize
        x1 = x + halfsize

        # drawing the horizontal line
        line = Line(Point(x0, y), Point(x1, y))
        line.setWidth(2)
        line.draw(win)

        # finding the top and bottom y-coordinate
        y0 = y + halfsize
        y1 = y - halfsize

        # drawing the left vertical line
        line = Line(Point(x0, y0), Point(x0, y1))
        line.setWidth(2)
        line.draw(win)

        # drawing the left vertical line
        line = Line(Point(x1, y0), Point(x1, y1))
        line.setWidth(2)
        line.draw(win)

        # after this, we've done the drawing of order 1 HTree
        # and we want to use recursion to help us draw the rest

        # Question: how much recursion do we need to do?
        # 4. because there are 4 "points" after the initial "H" is drawn

        # for each of the 4 points, we want to draw HTree of order (order - 1)
        less_order = order - 1

        # Recursively draw the top left HTree
        HTree(less_order, halfsize, x0, y0, win)  # draw subHTrees with halfsize
        # Recursively draw the bottom left HTree
        HTree(less_order, halfsize, x0, y1, win)

        # Recursively draw the top left HTree
        HTree(less_order, halfsize, x1, y0, win)

        # Recursively draw the bottom right HTree
        HTree(less_order, halfsize, x1, y1, win)


if __name__ == "__main__":
    # title and dimensions
    win = GraphWin('HTree', 500, 500)
    # first parameter shows the order
    # if you want to see a clear HTree try the order of 1 -  6
    # if you want to see how slow a recursive function can work,
    # try it with order > 6

    HTree(5, 200, win.getWidth() / 2, win.getWidth() / 2, win)
    message = Text(Point(win.getWidth() / 2, 20),
                   'Click anywhere inside the window to quit.')
    message.draw(win)
    win.getMouse()
    win.close()
