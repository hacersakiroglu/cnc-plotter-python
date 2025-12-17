STEPS_PER_MM = 80

def move (current_x,current_y,target_x,target_y):
    dx = target_x- current_x
    dy = target_y - current_y
    
    step_x = int (dx * STEPS_PER_MM)
    step_y = int (dy * STEPS_PER_MM)

    command = f"X:{step_x} Y:{step_y}"

    print ("MOVE :")
    print ("from :",(current_x,current_y))
    print ("to :", (target_x, target_y))
    print ("dx,dy :" ,( dx, dy))
    print ("steps :" ,( step_x,step_y))
    print ("CMD :" , command)
    print()

    return target_x,target_y,command


current_x = 0
current_y = 0

current_x, current_y,cmd = move(current_x, current_y, 8, 0)
print ("Send to Arduino ->",cmd)
current_x, current_y,cmd = move(current_x, current_y, 4, 4)
print ("Send to Arduino ->",cmd)
