"""
A class representing a robot with a specified width and height.

Args:
    width (float): The width of the robot (default is 2.0).
    height (float): The height of the robot (default is 3.0).

Returns:
    None
"""
class Robot:
    def __init__(self, width = 2.0, height = 3.0):
        self.width = width
        self.height = height