import numpy as np
import cv2
import random
import time

def collision_with_apple(apple_position, score):
    apple_position = [random.randrange(1,65)*10,random.randrange(1,40)*10]
    score += 1
    return apple_position, score
    #回傳score及apple位置

def collision_with_boundaries(snake_head):
    if snake_head[0]>=650 or snake_head[0]<0 or snake_head[1]>=400 or snake_head[1]<0 :
        return 1
    else:
        return 0
    # 檢測有無碰到邊界
def collision_with_self(snake_position):
    snake_head = snake_position[0]
    if snake_head in snake_position[1:]:
        return 1
    else:
        return 0
    # 檢測有無碰到自己
img = np.zeros((400,650,3),dtype='uint8')
# 初始化蘋果跟蛇的位置
snake_position = [[250,250],[240,250],[230,250]]
apple_position = [random.randrange(1,65)*10,random.randrange(1,40)*10]
score = 0
prev_button_direction = 1
button_direction = 1
snake_head = [250,250]
while True:
    cv2.imshow('snackline',img)
    cv2.waitKey(1)
    img = np.zeros((400,650,3),dtype='uint8')
    #創出蘋果
    cv2.circle(img, (apple_position[0], apple_position[1]), 5, (0, 0, 255), -1)
    # 畫蛇
    for position in snake_position:
        cv2.circle(img,(position[0],position[1]),5,(0,255,0),-1)
    cv2.putText(img, 'Your score {}'.format(score), (380, 65), cv2.FONT_HERSHEY_SIMPLEX, 1, (46, 62, 88), 2)
    
    t_end = time.time() + 0.2
    k = -1
    while time.time() < t_end:
        if k == -1:
            k = cv2.waitKey(125)
        else:
            continue
            
    #根據偵測到的事件，儲存上下左右

    if k == ord('a') and prev_button_direction != 1:
        button_direction = 0
    elif k == ord('d') and prev_button_direction != 0:
        button_direction = 1
    elif k == ord('w') and prev_button_direction != 2:
        button_direction = 3
    elif k == ord('s') and prev_button_direction != 3:
        button_direction = 2
    elif k == ord('q'):
        break
    else:
        button_direction = button_direction
    prev_button_direction = button_direction

    # 根據狀態做出相應行動
    if button_direction == 1:
        snake_head[0] += 10
    elif button_direction == 0:
        snake_head[0] -= 10
    elif button_direction == 2:
        snake_head[1] += 10
    elif button_direction == 3:
        snake_head[1] -= 10

    # 身體碰到蘋果就加一分，並亂數生成蘋果位置
    if snake_head == apple_position:
        apple_position, score = collision_with_apple(apple_position, score)
        snake_position.insert(0,list(snake_head))

    else:
        snake_position.insert(0,list(snake_head))
        snake_position.pop()
     
    # 碰到邊界或碰到自身
    if collision_with_boundaries(snake_head) == 1 or collision_with_self(snake_position) == 1:
        img = np.zeros((400,650,3),dtype='uint8')
        cv2.putText(img, 'GAME OVER', (125, 165), cv2.FONT_HERSHEY_SIMPLEX, 2, (100, 215, 250), 2)
        cv2.putText(img, 'Your score {}'.format(score), (125, 265), cv2.FONT_HERSHEY_SIMPLEX, 2, (46, 62, 88), 2)
        cv2.imshow('snackline',img)
        cv2.waitKey(0)
        break
        
cv2.destroyAllWindows()

