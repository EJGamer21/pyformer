def calculate_motion(obj, axis, delta):
    return (
        (getattr(obj.velocity, axis) * delta)
        + (getattr(obj.acceleration, axis) * 0.5)
        * (delta**2)
    )
