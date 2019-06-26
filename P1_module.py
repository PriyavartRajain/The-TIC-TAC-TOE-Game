import stddraw
x = None
mx=None
my=None
def draw_hash():
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.line(-0.6,0.2,0.6,0.2)
    stddraw.line(-0.6,-0.2,0.6,-0.2)
    stddraw.setPenRadius(0.01)
    stddraw.line(-0.2,0.6,-0.2,-0.6)
    stddraw.line(0.2,0.6,0.2,-0.6)
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.line(-0.6, -0.6, 0.6, -0.6)
    stddraw.line(0.6, -0.6, 0.6, 0.6)
    stddraw.line(0.6, 0.6, -0.6, 0.6)
    stddraw.line(-0.6, 0.6, -0.6, -0.6)

def P1():
    stddraw.setPenColor(stddraw.BLACK)
    if x == 1 or x == 2:
        stddraw.text(0.5, 0.8, " GAME OVER")
    stddraw.text(0.5, 0.8, " Player 2's Turn")
    stddraw.setFontSize(46)

    # B1
    if (mx < -0.2 and mx > -0.6):
        if (my > -0.6 and my < -0.2):
            if array[0][0] == 0:
                stddraw.text(-0.4, -0.4, "O")
                array[0][0] = 1
                count += 1

    # B2
    if (mx > -0.2 and mx < 0.2):
        if (my > -0.6 and my < -0.2):
            if array[0][1] == 0:
                stddraw.text(0, -0.4, "O")
                array[0][1] = 1
                count += 1
    # B3
    if (mx > 0.2 and mx < 0.6):
        if (my > -0.6 and my < -0.2):
            if array[0][2] == 0:
                stddraw.text(0.4, -0.4, "O")
                array[0][2] = 1
                count += 1

    # B4
    if (mx > -0.6 and mx < -0.2):
        if (my > -0.2 and my < 0.2):
            if array[1][0] == 0:
                stddraw.text(-0.4, 0, "O")
                array[1][0] = 1
                count += 1

    # B5
    if (mx > -0.2 and mx < 0.2):
        if (my > -0.2 and my < 0.2):
            if array[1][1] == 0:
                stddraw.text(0, 0, "O")
                array[1][1] = 1
                count += 1
    # B6
    if (mx > 0.2 and mx < 0.6):
        if (my > -0.2 and my < 0.2):
            if array[1][2] == 0:
                stddraw.text(0.4, 0, "O")
                array[1][2] = 1
                count += 1
    # B7
    if (mx > -0.6 and mx < -0.2):
        if (my > 0.2 and my < 0.6):
            if array[2][0] == 0:
                stddraw.text(-0.4, 0.4, "O")
                array[2][0] = 1
                count += 1
    # B8
    if (mx > -0.2 and mx < 0.2):
        if (my > 0.2 and my < 0.6):
            if array[2][1] == 0:
                stddraw.text(0, 0.4, "O")
                array[2][1] = 1
                count += 1

    # B9
    if (mx > 0.2 and mx < 0.6):
        if (my > 0.2 and my < 0.6):
            if array[2][2] == 0:
                stddraw.text(0.4, 0.4, "O")
                array[2][2] = 1
                count += 1


def P2():
    stddraw.setPenColor(stddraw.BLACK)
    if x == 1 or x == 2:
        stddraw.text(0.5, 0.8, " GAME OVER")
    stddraw.text(0.5, 0.8, " Player 1's Turn")

    stddraw.setFontSize(46)

    # B1
    if (mx < -0.2 and mx > -0.6):
        if (my > -0.6 and my < -0.2):
            if array[0][0] == 0:
                stddraw.text(-0.4, -0.4, "X")
                array[0][0] = 2
                count += 1
    # B2
    if (mx > -0.2 and mx < 0.2):
        if (my > -0.6 and my < -0.2):
            if array[0][1] == 0:
                stddraw.text(0, -0.4, "X")
                array[0][1] = 2
                count += 1

    # B3
    if (mx > 0.2 and mx < 0.6):
        if (my > -0.6 and my < -0.2):
            if array[0][2] == 0:
                stddraw.text(0.4, -0.4, "X")
                array[0][2] = 2
                count += 1
    # B4
    if (mx > -0.6 and mx < -0.2):
        if (my > -0.2 and my < 0.2):
            if array[1][0] == 0:
                stddraw.text(-0.4, 0, "X")
                array[1][0] = 2
                count += 1
    # B5
    if (mx > -0.2 and mx < 0.2):
        if (my > -0.2 and my < 0.2):
            if array[1][1] == 0:
                stddraw.text(0, 0, "X")
                array[1][1] = 2
                count += 1
    # B6
    if (mx > 0.2 and mx < 0.6):
        if (my > -0.2 and my < 0.2):
            if array[1][2] == 0:
                stddraw.text(0.4, 0, "X")
                array[1][2] = 2
                count += 1
    # B7
    if (mx > -0.6 and mx < -0.2):
        if (my > 0.2 and my < 0.6):
            if array[2][0] == 0:
                stddraw.text(-0.4, 0.4, "X")
                array[2][0] = 2
                count += 1
    # B8
    if (mx > -0.2 and mx < 0.2):
        if (my > 0.2 and my < 0.6):
            if array[2][1] == 0:
                stddraw.text(0, 0.4, "X")
                array[2][1] = 2
                count += 1
    # B9
    if (mx > 0.2 and mx < 0.6):
        if (my > 0.2 and my < 0.6):
            if array[2][2] == 0:
                stddraw.text(0.4, 0.4, "X")
                array[2][2] = 2
                count += 1
