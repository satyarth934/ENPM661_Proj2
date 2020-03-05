import numpy as np
import cv2
import matplotlib.pyplot as plt
# from planar import Polygon


def circle(x,y,radius):
    if ((x-225)**2+(y-50)**2) < (25+radius)**2:
        return True
    else:
        return False

def ellipse(x,y,radius):
    if ((x-150)**2.0)/(40**2) + ((y-100)**2.0)/(20**2) <= 1:
        return True
    else:
        return False

def diamond(x,y,radius):
    #points of the diamond
    p1 = [225.0, 160-radius]
    p2 = [250.0+radius, 175]
    p3 = [225.0, 190+radius]
    p4 = [200.0-radius, 175]

    m1 = (p2[1]-p1[1])/(p2[0]-p1[0])
    b1 = p1[1]-m1*p1[0]

    m2 = (p2[1]-p3[1])/(p2[0]-p3[0])
    b2 = p2[1]-m2*p2[0]

    m3 = (p3[1]-p4[1])/(p3[0]-p4[0])
    b3 = p3[1]-m3*p3[0]

    m4 = (p1[1]-p4[1])/(p1[0]-p4[0])
    b4 = p4[1]-m4*p4[0]

    if m1*x + b1 < y and m2*x + b2 > y and m3*x + b3 > y and m4*x + b4 < y:
        return True
    else:
        return False

def rectangle(x,y,radius):
    #points of the rectangle
    p1 = [39.0, 127-radius]
    p2 = [104.0+radius, 165]
    p3 = [95.0, 170+radius]
    p4 = [30.0-radius, 132]

    m1 = (p2[1]-p1[1])/(p2[0]-p1[0])
    b1 = p1[1]-m1*p1[0]

    m2 = (p2[1]-p3[1])/(p2[0]-p3[0])
    b2 = p2[1]-m2*p2[0]

    m3 = (p3[1]-p4[1])/(p3[0]-p4[0])
    b3 = p3[1]-m3*p3[0]

    m4 = (p1[1]-p4[1])/(p1[0]-p4[0])
    b4 = p4[1]-m4*p4[0]

    if m1*x + b1 < y and m2*x + b2 > y and m3*x + b3 > y and m4*x + b4 < y:
        return True
    else:
        return False

def polygon(x,y,radius):
    #points of the rectangle
    p1 = [25.0, 15-radius]
    p2 = [75.0, 15-radius]
    p3 = [100.0+radius, 50]
    p4 = [75.0, 80+radius]
    p5 = [50.0, 50+radius]
    p6 = [20.0-radius, 80+radius]

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

    if  (m1*x + b1 < y and m2*x + b2 > y and m6*x + b6 < y and m56*x + b56) or (m22*x + b22 < y and m3*x + b3 > y and m4*x + b4 > y and m5*x + b5 < y):
        return True
    else:
        return False



def getMap():
    height = 200
    width = 300
    mask = (np.full([height,width], 0, dtype='uint8'))

    #rectangle test
    x = 95
    y = 168
    #diamond test
    x = 225
    y = 175

    #ellipse test
    x = 111
    y = 1

    #polygon test
    # x = 50
    # y = 30
    radius = 0
    count = 0

    #make obstacles visible
    for i in range(200):
        for j in range(300):
            if circle(j,i,0) or ellipse(j,i,0) or rectangle(j,i,0) or diamond(j,i,0) or polygon(j,i,0):
                mask[i][j] = 200


    plt.figure("mask")
    plt.imshow(mask)
    plt.show()

    # while(1):
    #     cv2.imshow("test",mask)

    #     if(circle(x,y,radius)):
    #         print("circle")

    #     if(diamond(x,y,radius)):
    #         print("diamond")

    #     if(rectangle(x,y,radius)):
    #         print("rectangle")

    #     if(ellipse(x,y,radius)):
    #         print("ellipse")

    #     if(polygon(x,y,radius)):
    #         print("polygon")

    #     #if 'q' is pressed then quit video
    #     key = cv2.waitKey(1) & 0xFF
    #     if key == 27 or key == ord("q"):
    #         break

    # cleanup the camera and close any open windows
    # camera.release()
    cv2.destroyAllWindows()

    return mask


def main():
    mask = getMap()
    print(mask.shape)


if __name__ == '__main__':
    main()


# #Initalize GoalNode
# GoalNode = [[[1,2,3],[4,5,6],[7,8,0]]]
# #Input StartNode
# row1 = [int(input('Enter puzzle values left to right and press enter after each number \n')),int(input()),int(input())]
# row2 = [int(input()),int(input()),int(input())]
# row3 = [int(input()),int(input()),int(input())]
# StartNode = [row1,row2,row3]
# AllMoves = ["Start"]
# AllNodes = []
# AllNodes.append(StartNode)
#
# #Initalize queue
# Q = queue.Queue()
# Q.put(StartNode)
# Visited = []
# NodesInfo = []
# sol = 0 #solution not found
#
# count = 0
# count2 = 0
# #While loop to perform movements and save nodes until GoalNode is reached
# while(Q.qsize()!=0) and (sol != 1):
#     CurrentNode = Q.get()
#     Visited.append(CurrentNode)
#     #Perform each movie if able
#
#     for move in [up,down,left,right,up_left,up_right,down_left,down_right]:
#         NewNode, Move, Cost = move(CurrentNode, height, width)
#         #If there is a NewNode, then...
#         if NewNode:
#             #If NewNode is not in Visited yet...
#             if NewNode not in Visited:
#
#                 #Add node and movement to list
#                 AllNodes.append(NewNode)
#                 AllMoves.append(Move)
#                 count2+=1
#                 #Save current node and parent node
#                 NodesInfo.append([(count2),count])
#                 #If NewNode = GoalNode, then finished
#                 if NewNode in GoalNode:
#                     print("FINISHED!!!")
#                     sol = 1 #solution found
#                 else:
#                     #If not finished, put NewNode in queue
#                     Q.put(NewNode)
#             else:
#                 if Cost > CostToCome:
#                     CostToCome = CostToCome +
#     #Print count ever 1000 iterations
#     count+=1
#     if(count%1000==0):
#         print(count)
#
# #Perform back tracking with desired node BackwardsNode
# BackwardsNode = [[1,2,3],[4,5,6],[7,8,0]]
# NodePath, Answer = generate_path(BackwardsNode)
# print(Answer)
# #Write NodePath to a text file
# with open("nodePath.txt","wb") as f:
#     w = csv.writer(f,delimiter='\n',lineterminator='\n\r\n')
#     w.writerows(NodePath)
# #Write NodePath to a text file
# with open("Nodes.txt","wb") as f:
#     w = csv.writer(f,delimiter='\n',lineterminator='\n\r\n')
#     w.writerows(Visited)
# #Write NodesInfo to a text file
# with open("NodesInfo.txt","wb") as f:
#     w = csv.writer(f,lineterminator='\n')
#     w.writerows(NodesInfo)
# #Write Directions to text file
# with open("Optimal_Path_Directions.txt","wb") as f:
#     w = csv.writer(f,lineterminator='\n')
#     w.writerows(Answer)
