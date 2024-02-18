# %%
import math

board_x = 254
board_y = 127

hole1 = (0,0)
hole2 = (127,0)
hole3 = (0, 127)
hole4 = (127,127)
hole5 = (254, 0)
hole6 = (254, 127)

holeList = [hole1, hole2, hole3, hole4, hole5, hole6]

ball = (1,1)
target1 = (240, 120)
target2 = (123, 90)
targetList = [target1, target2]

evalList = []
evaluation = None
targetBall = None
hole = None

for j in range(len(targetList)):
    temp = []
    target = targetList[j]
    tan1 = (target[1] - ball[1]) / (target[0] - ball[0])
    theta1 = math.atan(tan1)
    for i in range(len(holeList)):
        tan2 = (holeList[i][1] - ball[1]) / (holeList[i][0] - ball[0])
        eval_tan = abs((tan2 - tan1) / (1 + tan2*tan1))
        if evaluation == None or eval_tan < evaluation:
            evaluation = eval_tan
            targetBall = target
            hole = holeList[i]

print(targetBall)
print(hole)

