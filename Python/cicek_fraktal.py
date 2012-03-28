from graphics import*

colormap = ['blue', 'yellow', 'green']
win = GraphWin("MyCircle", 900, 900)

def tiny(x, y, r):
    c = Circle(Point((x-r), y), r/2)
    c.draw(win)
    c.setFill(colormap[0])
    d = Circle(Point((x+r), y), r/2)
    d.draw(win)
    d.setFill(colormap[0])
    e = Circle(Point(x, y), r)
    e.draw(win)
    e.setFill(colormap[1])
    f = Circle(Point(x, y-r), r/2)
    f.draw(win)
    f.setFill(colormap[0])
    g = Circle(Point(x, y+r), r/2)
    g.draw(win)
    g.setFill(colormap[0])

def hmm(a, b, R):  # merkezdeki buyuk dairenin koordinatlari a ve b dir. R ise yaricapidir.
    tiny(a-R, b, R/2)
    tiny(a+R, b, R/2)
    om = Circle(Point(a, b), R)
    om.draw(win)
    om.setFill(colormap[2])
    tiny(a, b-R, R/2)
    tiny(a, b+R, R/2)
    win.getMouse()
    win.close()

hmm(350, 350, 100)
    
