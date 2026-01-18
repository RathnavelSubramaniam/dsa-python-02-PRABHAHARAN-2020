from robot import Robot

r1 = Robot("Robo1", 2, 3)

# Before moving
print(r1.get_name(), "location before moving:", r1.get_location())

# Move the robot
r1.move(4, -1)

# After moving
print(r1.get_name(), "location after moving:", r1.get_location())
