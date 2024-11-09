#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class TurtleSquare(Node):
    def __init__(self):
        super().__init__('turtle_square')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

        #side lenght of the square
        self.side_length = 4
        time.sleep(2) 

    def move_square(self):
        move_cmd = Twist()
        turn_cmd = Twist()
        
        move_cmd.linear.x = 1.0  # Forward speed
        turn_cmd.angular.z = 1.57  # Turn speed to 90 degrees

        for _ in range(4):  
            self.move_straight(move_cmd)
            self.turn(turn_cmd)

        self.publisher.publish(Twist())

    def move_straight(self, move_cmd):
        move_duration = self.side_length / move_cmd.linear.x
        end_time = time.time() + move_duration
        while time.time() < end_time:
            self.publisher.publish(move_cmd)
            time.sleep(0.1)

    def turn(self, turn_cmd):
        turn_duration = 1.0  
        end_time = time.time() + turn_duration
        while time.time() < end_time:
            self.publisher.publish(turn_cmd)
            time.sleep(0.1)

def main():
    rclpy.init()
    turtle_square = TurtleSquare()
    turtle_square.move_square()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
