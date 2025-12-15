def move (current_x,current_y,target_x,target_y):
    delta_x = target_x-current_x
    delta_y =target_y-current_y

    print(" MOVE:")
    print( "from:" ,( current_x , current_y))
    print( "to :" , ( target_x , target_y))
    print( "delta:" , ( delta_x , delta_y))
    print()

    return target_x,target_y
