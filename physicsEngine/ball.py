output_width = 19
left_wall = 0

"""Simulates a ball's movement and collision with the edges of a screen."""

def move(position, speed, right_wall):
    new_position = position + speed
    if new_position >= right_wall:
        return right_wall
    elif new_position <= left_wall:
        return 0
    else:
       return new_position
    """Returns the ball's new position after one time step.
    The ball moves in straight line at the given speed.
    """

def maybe_bounce(position, speed, right_wall):
    """Returns the ball's new speed, which stays the same unless the ball
    bounces off of a wall.
    """
    if position >= right_wall:
        # Reverses direction and loses a bit of speed.
        speed = speed * -0.75
    elif position <= left_wall:
        speed = speed * -0.75

    return speed
