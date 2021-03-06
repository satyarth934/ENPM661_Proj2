import cv2
import numpy as np
import matplotlib.pyplot as plt


##
## To check if the coordinate is in the cirlce obstacle
##
## :param      x:       x coordinate
## :type       x:       int
## :param      y:       y coordinate
## :type       y:       int
## :param      radius:  The radius of the robot
## :type       radius:  int
##
## :returns:   True if the coordinate lies within the circle, False otherwise
## :rtype:     boolean
##
def circle(x,y,radius):
    #checks if the coordinate is within the geometrical equation
    if ((x-225)**2+(y-50)**2) < (25+radius)**2:
        return True
    else:
        return False


##
## To check if the coordinate is in the ellipse obstacle
##
## :param      x:       x coordinate
## :type       x:       int
## :param      y:       y coordinate
## :type       y:       int
## :param      radius:  The radius of the robot
## :type       radius:  int
##
## :returns:   True if the coordinate lies within the ellipse, False otherwise
## :rtype:     boolean
##
def ellipse(x,y,radius):
    #checks if the coordinate is within the geometrical equation
    if ((x-150)**2.0)/(40+radius)**2 + ((y-100)**2.0)/(20+radius)**2 <= 1:
        return True
    else:
        return False


##
## To check if the coordinate is in the diamond obstacle
##
## :param      x:       x coordinate
## :type       x:       int
## :param      y:       y coordinate
## :type       y:       int
## :param      radius:  The radius of the robot
## :type       radius:  int
##
## :returns:   True if the coordinate lies within the diamond, False otherwise
## :rtype:     boolean
##
def diamond(x,y,radius):
    #create the points of the diamond
    p1 = [225.0, 160-radius]
    p2 = [250.0+radius, 175]
    p3 = [225.0, 190+radius]
    p4 = [200.0-radius, 175]

    # make lines connecting the connecting the points
    # m is the slope and b is the y-intercept
    m1 = (p2[1]-p1[1])/(p2[0]-p1[0])
    b1 = p1[1]-m1*p1[0]

    m2 = (p2[1]-p3[1])/(p2[0]-p3[0])
    b2 = p2[1]-m2*p2[0]

    m3 = (p3[1]-p4[1])/(p3[0]-p4[0])
    b3 = p3[1]-m3*p3[0]

    m4 = (p1[1]-p4[1])/(p1[0]-p4[0])
    b4 = p4[1]-m4*p4[0]

    #make inequalities with the lines so that bounds make up the shape of the obstacle
    if m1*x + b1 < y and m2*x + b2 > y and m3*x + b3 > y and m4*x + b4 < y:
        return True
    else:
        return False


##
## To check if the coordinate is in the rectangle obstacle
##
## :param      x:       x coordinate
## :type       x:       int
## :param      y:       y coordinate
## :type       y:       int
## :param      radius:  The radius of the robot
## :type       radius:  int
##
## :returns:   True if the coordinate lies within the rectangle, False otherwise
## :rtype:     boolean
##
def rectangle(x,y,radius):
    #points of the rectangle
    p1 = [35.0, 123-radius]
    p2 = [100.0+radius, 161]
    p3 = [95.0, 170+radius]
    p4 = [30.0-radius, 132]

    #make lines connecting the connecting the points
    #m is the slobe and b is the y-intercept
    m1 = (p2[1]-p1[1])/(p2[0]-p1[0])
    b1 = p1[1]-m1*p1[0]

    m2 = (p2[1]-p3[1])/(p2[0]-p3[0])
    b2 = p2[1]-m2*p2[0]

    m3 = (p3[1]-p4[1])/(p3[0]-p4[0])
    b3 = p3[1]-m3*p3[0]

    m4 = (p1[1]-p4[1])/(p1[0]-p4[0])
    b4 = p4[1]-m4*p4[0]

    #make inequalities with the lines so that bounds make up the shape of the obstacle
    if m1*x + b1 < y and m2*x + b2 > y and m3*x + b3 > y and m4*x + b4 < y:
        return True
    else:
        return False


##
## To check if the coordinate is in the polygon obstacle
##
## :param      x:       x coordinate
## :type       x:       int
## :param      y:       y coordinate
## :type       y:       int
## :param      radius:  The radius of the robot
## :type       radius:  int
##
## :returns:   True if the coordinate lies within the polygon, False otherwise
## :rtype:     boolean
##
def polygon(x,y,radius):
    #points of the polygon
    p1 = [25.0, 15-(radius)]
    p2 = [75.0, 15-radius]
    p3 = [100.0+radius, 50]
    p4 = [75.0, 80+radius]
    p5 = [50.0, 50+radius]
    p6 = [20.0, 80+radius]

    #make lines connecting the connecting the points
    #m is the slobe and b is the y-intercept

    #two separate shapes
    #first shape
    m6 = (p1[1]-p6[1])/(p1[0]-p6[0])
    b6 = p6[1]-m6*p6[0]

    m1 = (p2[1]-p1[1])/(p2[0]-p1[0])
    b1 = p1[1]-m1*p1[0]

    m2 = (p2[1]-p5[1])/(p2[0]-p5[0])
    b2 = p2[1]-m2*p2[0]

    m56 = (p5[1]-p6[1])/(p5[0]-p6[0])
    b56 = p2[1]-m56*p2[0]

    #second shape
    m22 = (p2[1]-p3[1])/(p2[0]-p3[0])
    b22 = p2[1]-m22*p2[0]

    m3 = (p3[1]-p4[1])/(p3[0]-p4[0])
    b3 = p3[1]-m3*p3[0]

    m4 = (p4[1]-p5[1])/(p4[0]-p5[0])
    b4 = p4[1]-m4*p4[0]

    m5 = (p2[1]-p5[1])/(p2[0]-p5[0])
    b5 = p5[1]-m5*p5[0]

    #make inequalities with the lines so that bounds make up the shape of the obstacle
    #combines thet two shapes above
    if  (m1*x + b1 < y and m2*x + b2 > y and m6*x + b6 < y and m56*x + b56) or (m22*x + b22 < y and m3*x + b3 > y and m4*x + b4 > y and m5*x + b5 < y):
        return True
    else:
        return False


def insideObstacle(row, col, radius):
    return (circle(col, row, radius) or ellipse(col, row, radius) or rectangle(col, row, radius) or diamond(col, row, radius) or polygon(col, row, radius))

##
## Gets the map with the defined obstacles in it.
##
## :param      radius:     The radius
## :type       radius:     int
## :param      visualize:  Visualize only if this argument is true
## :type       visualize:  boolean
##
## :returns:   The map.
## :rtype:     numpy matrix
##
def getMap(radius=0, visualize=False):
    #Initalize maze
    height = 200
    width = 300
    #make the background all black
    mask = (np.full([height,width], 0, dtype='uint8'))

    # #rectangle test
    # x = 95
    # y = 168
    # #diamond test
    # x = 225
    # y = 175
    # #polygon test
    # x = 50
    # y = 30
    #ellipse test
    x = 100
    y = 100

    #make obstacles visible
    for i in range(200):
        for j in range(300):
            if insideObstacle(i, j, radius):
                #if the coordinates are within an obstacle make that pixel lighter
                mask[i][j] = 100

    if visualize:
        while(1):

            cv2.imshow("HSV",mask)
            #if 'q' is pressed then quit video
            key = cv2.waitKey(1) & 0xFF
            if key == 27 or key == ord("q"):
                break

        # cleanup the camera and close any open windows
        cv2.destroyAllWindows()

    return mask


def main():
    mask = getMap(0,True)
    print(mask.shape)


if __name__ == '__main__':
    main()
