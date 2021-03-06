import numpy as np
import cv2
import random
import time

def collision_with_apple(apple_position, score):
    apple_position = [random.randrange(1,50)*8,random.randrange(1,50)*11]
    score += 1
    return apple_position, score
    # return score apple_postition with  tuple 

def collision_with_boundaries(snake_head):
    if snake_head[0]>650 or snake_head[0]<0 or snake_head[1]>400 or snake_head[1]<0 :
        return 1
    else:
        return 0
    # set the end game side
def collision_with_self(snake_position):
    snake_head = snake_position[0]
    if snake_head in snake_position[1:]:
        return 1
    else:
        return 0

img = np.zeros((400,650,3),dtype='uint8')
# Initial Snake and Apple position
snake_position = [[250,250],[240,250],[230,250]]
apple_position = [random.randrange(1,50)*8,random.randrange(1,50)*11]
score = 0
prev_button_direction = 1
button_direction = 1
snake_head = [250,250]
while True:
    cv2.imshow('snackline',img)
    cv2.waitKey(1)
    img = np.zeros((400,650,3),dtype='uint8')
    # Display Apple
    cv2.circle(img, (apple_position[0], apple_position[1]), 5, (0, 0, 255), -1)
    
    # Display Snake
    for position in snake_position:
        cv2.circle(img,(position[0],position[1]),5,(0,255,0),3)
   # cv2.putText(img, 'Your score {}'.format(score), (380, 65), cv2.FONT_HERSHEY_SIMPLEX, 1, (46, 62, 88), 2)
    # Takes step after fixed time
    t_end = time.time() + 0.2
    k = -1
    while time.time() < t_end:
        if k == -1:
            k = cv2.waitKey(1)
        else:
            continue
            
    # 0-Left, 1-Right, 3-Up, 2-Down, q-Break
    # a-Left, d-Right, w-Up, s-Down

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

    # Change the head position based on the button direction
    if button_direction == 1:
        snake_head[0] += 10
    elif button_direction == 0:
        snake_head[0] -= 10
    elif button_direction == 2:
        snake_head[1] += 10
    elif button_direction == 3:
        snake_head[1] -= 10

    # Increase Snake length on eating apple
    if snake_head == apple_position:
        apple_position, score = collision_with_apple(apple_position, score)
        snake_position.insert(0,list(snake_head))

    else:
        snake_position.insert(0,list(snake_head))
        snake_position.pop()
     
    # On collision kill the snake and print the score
    if collision_with_boundaries(snake_head) == 1 or collision_with_self(snake_position) == 1:
        img = np.zeros((400,650,3),dtype='uint8')
        cv2.putText(img, 'GAME OVER', (125, 165), cv2.FONT_HERSHEY_SIMPLEX, 2, (100, 215, 250), 2)
        cv2.putText(img, 'Your score {}'.format(score), (125, 265), cv2.FONT_HERSHEY_SIMPLEX, 2, (46, 62, 88), 2)
        cv2.imshow('snackline',img)
        cv2.waitKey(0)
        break
        
cv2.destroyAllWindows()

