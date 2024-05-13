class Move:
    """
    A class representing a move with a specified length and change in angle.

    Args:
        length (float): The length of the move.
        dtheta (float): The change in angle for the move.

    Returns:
        None
    """

    def __init__(self, length, dtheta):
        self.length = length
        self.dtheta = dtheta
