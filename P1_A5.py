import stddraw
import P1_module
mx=None
my=None
x = None
stddraw.setXscale(-1,1)
stddraw.setYscale(-1,1)

P1_module.draw_hash()

key = True
count=1
stddraw.setFontSize(20)

stddraw.setPenColor(stddraw.BLACK)
stddraw.text(-0.8,0.9," Player 1 : O")
stddraw.text(-0.8,0.8," Player 2 : X")

stddraw.setPenColor(stddraw.WHITE)

array = [[0,0,0],
        [0,0,0],
        [0,0,0]]

while key:

    if stddraw.mousePressed():

        mx = stddraw.mouseX()
        my = stddraw.mouseY()
        stddraw.setFontSize(28)
        stddraw.setPenColor(stddraw.WHITE)
        stddraw.filledRectangle(0.0, 0.7, 0.9, 0.2)

        if count%2==0:

            stddraw.setPenColor(stddraw.BLACK)
            if x==1 or x==2:
                stddraw.text(0.5, 0.8, " GAME OVER")
            stddraw.text(0.5,0.8," Player 2's Turn")
            stddraw.setFontSize(46)
            stddraw.setPenColor(stddraw.RED)
            #B1
            if (mx< -0.2 and mx> -0.6):
                if (my> -0.6 and my< -0.2):
                    if array[0][0]==0:
                        stddraw.text(-0.4,-0.4, "O")
                        array[0][0]=1
                        count += 1

            #B2
            if (mx> -0.2 and mx< 0.2):
                if (my> -0.6 and my< -0.2):
                    if array[0][1] == 0:
                        stddraw.text(0,-0.4, "O")
                        array[0][1]=1
                        count += 1
            #B3
            if (mx>0.2 and mx<0.6):
                if (my> -0.6 and my< -0.2):
                    if array[0][2] == 0:
                        stddraw.text(0.4, -0.4, "O")
                        array[0][2] = 1
                        count += 1

            #B4
            if (mx>-0.6 and mx<-0.2):
                if (my> -0.2 and my< 0.2):
                    if array[1][0] == 0:
                        stddraw.text(-0.4,0, "O")
                        array[1][0] = 1
                        count += 1

            # B5
            if (mx > -0.2 and mx < 0.2):
                if (my > -0.2 and my < 0.2):
                    if array[1][1] == 0:
                        stddraw.text(0, 0, "O")
                        array[1][1] = 1
                        count += 1
            #B6
            if (mx > 0.2 and mx < 0.6):
                if (my > -0.2 and my < 0.2):
                    if array[1][2] == 0:
                        stddraw.text(0.4, 0, "O")
                        array[1][2] = 1
                        count += 1
            #B7
            if (mx > -0.6 and mx < -0.2):
                if (my > 0.2 and my < 0.6):
                    if array[2][0] == 0:
                        stddraw.text(-0.4, 0.4, "O")
                        array[2][0] = 1
                        count += 1
            #B8
            if (mx > -0.2 and mx < 0.2):
                if (my > 0.2 and my < 0.6):
                    if array[2][1]== 0:
                        stddraw.text(0, 0.4, "O")
                        array[2][1] = 1
                        count += 1

            #B9
            if (mx > 0.2 and mx < 0.6):
                if (my > 0.2 and my < 0.6):
                    if array[2][2] == 0:
                        stddraw.text(0.4, 0.4, "O")
                        array[2][2] = 1
                        count += 1

        elif count%2!=0:

            stddraw.setPenColor(stddraw.BLACK)
            if x==1 or x==2:
                stddraw.text(0.5, 0.8, "GAME OVER")
            stddraw.text(0.5, 0.8, " Player 1's Turn")

            stddraw.setFontSize(46)
            stddraw.setPenColor(stddraw.BLUE)
            #B1
            if (mx< -0.2 and mx> -0.6):
                if (my> -0.6 and my< -0.2):
                    if array[0][0] == 0:
                        stddraw.text(-0.4,-0.4, "X")
                        array[0][0]=2
                        count += 1
            #B2
            if (mx> -0.2 and mx< 0.2):
                if (my> -0.6 and my< -0.2):
                    if array[0][1] == 0:
                        stddraw.text(0,-0.4, "X")
                        array[0][1]=2
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
            #B5
            if (mx > -0.2 and mx < 0.2):
                if (my > -0.2 and my < 0.2):
                    if array[1][1] == 0:
                        stddraw.text(0, 0, "X")
                        array[1][1] = 2
                        count += 1
            #B6
            if (mx > 0.2 and mx < 0.6):
                if (my > -0.2 and my < 0.2):
                    if array[1][2] == 0:
                        stddraw.text(0.4, 0, "X")
                        array[1][2] = 2
                        count += 1
            #B7
            if (mx > -0.6 and mx < -0.2):
                if (my > 0.2 and my < 0.6):
                    if array[2][0] == 0:
                        stddraw.text(-0.4, 0.4, "X")
                        array[2][0] = 2
                        count += 1
            #B8
            if (mx > -0.2 and mx < 0.2):
                if (my > 0.2 and my < 0.6):
                    if array[2][1] == 0:
                        stddraw.text(0, 0.4, "X")
                        array[2][1] = 2
                        count += 1
            #B9
            if (mx > 0.2 and mx < 0.6):
                if (my > 0.2 and my < 0.6):
                    if array[2][2] == 0:
                        stddraw.text(0.4, 0.4, "X")
                        array[2][2] = 2
                        count += 1


        if (array[0][0] == 1 and array[0][1] == 1 and array[0][2] == 1) or (
                array[0][0] == 1 and array[1][0] == 1 and array[2][0] == 1) or (
                array[0][0] == 1 and array[1][1] == 1 and array[2][2] == 1) or (
                array[1][0]== 1 and array[1][1] == 1 and array[1][2] == 1 )or(
                array[2][0]== 1 and array[2][1] == 1 and array[2][2] == 1)or(
                array[0][2]== 1 and array[1][1] == 1 and array[2][0] == 1)or(
                array[0][1] == 1 and array[1][1] == 1 and array[2][1] == 1)or(
                array[0][2] == 1 and array[1][2] == 1 and array[2][2] == 1):

            stddraw.setFontSize(30)
            stddraw.setPenColor(stddraw.GREEN)
            if (array[0][0] == 1 and array[0][1] == 1 and array[0][2] == 1):
                stddraw.line(-0.5,-0.4,0.5,-0.4)
            if (array[0][0] == 1 and array[1][0] == 1 and array[2][0] == 1):
                stddraw.line(-0.4, -0.5, -0.4, 0.5)
            if (array[0][0] == 1 and array[1][1] == 1 and array[2][2] == 1):
                stddraw.line(-0.5, -0.5, 0.5, 0.5)
            if (array[1][0] == 1 and array[1][1] == 1 and array[1][2] == 1):
                stddraw.line(-0.5, 0, 0.5, 0)
            if (array[2][0] == 1 and array[2][1] == 1 and array[2][2] == 1):
                stddraw.line(-0.5, 0.4, 0.5, 0.4)
            if (array[0][2] == 1 and array[1][1] == 1 and array[2][0] == 1):
                stddraw.line(0.5, -0.5, -0.5, 0.5)
            if (array[0][1] == 1 and array[1][1] == 1 and array[2][1] == 1):
                stddraw.line(0, -0.5, 0, 0.5)
            if (array[0][2] == 1 and array[1][2] == 1 and array[2][2] == 1):
                stddraw.line(0.4, -0.5, 0.4, 0.5)
            stddraw.setPenColor(stddraw.BLUE)

            stddraw.text(0, -0.8, "P L A Y E R  1   W O N")
            stddraw.setPenColor(stddraw.WHITE)
            stddraw.filledRectangle(0.2, 0.7, 0.9, 0.2)
            stddraw.setPenColor(stddraw.BLUE)
            stddraw.text(0.5, 0.8, " GAME OVER")
            x = 1
            break


        elif (array[0][0] == 2 and array[0][1] == 2 and array[0][2] == 2) or (
                array[0][0] == 2 and array[1][0] == 2 and array[2][0] == 2) or (
                array[0][0] == 2 and array[1][1] == 2 and array[2][2] == 2) or (
                array[1][0]== 2 and array[1][1] == 2 and array[1][2] == 2)or(
                array[2][0]== 2 and array[2][1] == 2 and array[2][2] == 2)or(
                array[0][2]== 2 and array[1][1] == 2 and array[2][0] == 2)or(
                array[0][1] == 2 and array[1][1] == 2 and array[2][1] == 2)or(
                array[0][2] == 2 and array[1][2] == 2 and array[2][2] == 2):
            stddraw.setFontSize(30)
            stddraw.setPenColor(stddraw.GREEN)
            if (array[0][0] == 2 and array[0][1] == 2 and array[0][2] == 2):
                stddraw.line(-0.5, -0.4, 0.5, -0.4)
            if (array[0][0] == 2 and array[1][0] == 2 and array[2][0] == 2):
                stddraw.line(-0.4, -0.5, -0.4, 0.5)
            if (array[0][0] == 2 and array[1][1] == 2 and array[2][2] == 2):
                stddraw.line(-0.5, -0.5, 0.5, 0.5)
            if (array[1][0] == 2 and array[1][1] == 2 and array[1][2] == 2):
                stddraw.line(-0.5, 0, 0.5, 0)
            if (array[2][0] == 2 and array[2][1] == 2 and array[2][2] == 2):
                stddraw.line(-0.5, 0.4, 0.5, 0.4)
            if (array[0][2] == 2 and array[1][1] == 2 and array[2][0] == 2):
                stddraw.line(0.5, -0.5, -0.5, 0.5)
            if (array[0][1] == 2 and array[1][1] == 2 and array[2][1] == 2):
                stddraw.line(0, -0.5, 0, 0.5)
            if (array[0][2] == 2 and array[1][2] == 2 and array[2][2] == 2):
                stddraw.line(0.4, -0.5, 0.4, 0.5)
            stddraw.setPenColor(stddraw.BLUE)


            stddraw.text(0,-0.8,"P L A Y E R  2   W O N")
            stddraw.setPenColor(stddraw.WHITE)
            stddraw.filledRectangle(0.2, 0.7, 0.9, 0.2)
            stddraw.setPenColor(stddraw.BLUE)
            stddraw.text(0.5, 0.8, " GAME OVER")
            x = 2
            break


        print (x)
        print(array)

        if x!=1 and x!=2:
            if array[0][0]!=0 and array [0][1]!=0 and array[0][2]!=0 and array[1][0]!=0 and array [1][1]!=0 and array[1][2]!=0 and array[2][0]!=0 and array [2][1]!=0 and array[2][2]!=0:
                stddraw.setPenColor(stddraw.RED)
                stddraw.text(0, -0.8, "D R A W")
    stddraw.show(0)

    if stddraw.hasNextKeyTyped():
       key = False

stddraw.show(100000)