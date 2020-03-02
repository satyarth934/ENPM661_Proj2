import numpy as np
import cv2
# from planar import Polygon

height = 200
width = 300
mask = np.full([height,width], 0, dtype='uint8')

def circle(x,y,radius):
    if ((x-225)**2+(y-50)**2) < (25+radius)**2:
        return True
    else:
        return False

def ellipse(x,y,radius):
    if ((x-150)**2)/40**2 + ((y-100)**2)/(20**2) < 1:
        return True
    else:
        return False

# Function to find the line given two points
def lineFromPoints(P,Q):

    a = Q[1] - P[1]
    b = P[0] - Q[0]
    c = a*(P[0]) + b*(P[1])

    if(b<0):
        print("The line passing through points P and Q is:",
              a ,"x ",b ,"y = ",c ,"\n")
    else:
        print("The line passing through points P and Q is: ",
              a ,"x + " ,b ,"y = ",c ,"\n")


def diamond(x,y,radius):
    #points of the diamond
    p1 = [225, 160-radius]
    p2 = [250+radius, 175]
    p3 = [225, 190+radius]
    p4 = [200-radius, 175]

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
    p1 = [39, 127-radius]
    p2 = [104+radius, 165]
    p3 = [95, 170+radius]
    p4 = [30-radius, 132]

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
    p1 = [25, 15-radius]
    p2 = [75, 15-radius]
    p3 = [100+radius, 50]
    p4 = [75, 80+radius]
    p5 = [50, 50+radius]
    p6 = [20-radius, 80+radius]

    m1 = (p2[1]-p1[1])/(p2[0]-p1[0])
    b1 = p1[1]-m1*p1[0]

    m2 = (p3[1]-p2[1])/(p3[0]-p2[0])
    b2 = p2[1]-m2*p2[0]

    m3 = (p3[1]-p4[1])/(p3[0]-p4[0])
    b3 = p3[1]-m3*p3[0]

    m4 = (p4[1]-p5[1])/(p4[0]-p5[0])
    b4 = p4[1]-m4*p4[0]

    m5 = (p5[1]-p6[1])/(p5[0]-p6[0])
    b5 = p5[1]-m5*p5[0]

    m6 = (p1[1]-p6[1])/(p1[0]-p6[0])
    b6 = p6[1]-m6*p6[0]

    if m1*x + b1 < y and m2*x + b2 < y and m3*x + b3 > y and m4*x + b4 > y and m5*x + b5 > y and m6*x + b6 < y:
        return True
    else:
        return False


while(1):
    cv2.imshow("test",mask)

    #if 'q' is pressed then quit video
    key = cv2.waitKey(1) & 0xFF
    if key == 27 or key == ord("q"):
        break

# cleanup the camera and close any open windows
# camera.release()
cv2.destroyAllWindows()


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
