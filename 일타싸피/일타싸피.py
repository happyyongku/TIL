# %%
import math

board_x = 254
board_y = 127
r = 5.37

hole1 = (0,0)
hole2 = (board_x / 2,0)
hole3 = (0, board_y)
hole4 = (board_x / 2,board_y)
hole5 = (board_x, 0)
hole6 = (board_x, board_y)

holeList = [hole1, hole2, hole3, hole4, hole5, hole6]

ball = (244, 117)
target1 = (249, 122)
target2 = (123, 90)
targetList = [target1, target2]

evalList = []
evaluation = None
targetBall = None
hole = None

for j in range(len(targetList)):
    temp = []
    target = targetList[j]
    try:
        tan1 = (target[1] - ball[1]) / (target[0] - ball[0])
    except ZeroDivisionError:
        tan1 = math.tan(math.pi / 180 * 89.9)
    theta1 = math.atan(tan1)
    
    for i in range(len(holeList)):
        try :
            tan2 = (holeList[i][1] - ball[1]) / (holeList[i][0] - ball[0])
        except ZeroDivisionError:
            tan2 = math.tan(math.pi / 180 * 89.99)
        eval_tan = (tan2 - tan1) / (1 + tan2*tan1)
        if (evaluation == None) or (abs(eval_tan) < abs(evaluation)):
            evalution = eval_tan
            targetBall = target
            hole = holeList[i]
        elif abs(eval_tan) == abs(evaluation):
            if (tan1 >= 0) == (tan2 >= 0):
                evalution = eval_tan
            targetBall = target
            hole = holeList[i]

try : 
    tan3 = (hole[1] - targetBall[1]) / (hole[0] - targetBall[1])
except ZeroDivisionError:
    tan3 = math.tan(math.pi / 180 * 89.99)

rad = math.atan(tan3)
aim_x = targetBall[0] - 2 * r * math.cos(rad)
aim_y = targetBall[1] - 2 * r * math.sin(rad)

print(f'ball : {ball}')
print(f'targetBallall : {targetBall}')
print(f'hole : {hole}')
print((aim_x, aim_y))

