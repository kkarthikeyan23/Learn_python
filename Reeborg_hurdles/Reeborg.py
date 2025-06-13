def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if front_is_clear():
        move()
        turn_right()
    elif wall_in_front():
        turn_left()

    # else:
    # turn_right()