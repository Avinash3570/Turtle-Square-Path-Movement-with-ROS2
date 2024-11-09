**Turtle Square Path Movement with ROS2**

This project demonstrates a simple ROS2 node that controls a simulated turtle to move in a square path by publishing linear and angular velocity commands. The code uses Python and ROS2’s `rclpy` library to control the turtle’s forward movement and 90-degree turns.

## **Table of Contents**

* Overview  
* Project Structure  
* Dependencies  
* Code Explanation  
* Usage  
* Future Improvements

## **Overview**

The objective of this project is to control a turtlebot to move in a square path in a simulated environment using ROS2. The project introduces essential ROS2 concepts such as nodes, publishers, and message types, providing a foundation for ROS-based robotic movement control.

## **Dependencies**

* **Python 3**  
* **ROS2**: This project is compatible with ROS2 distributions (e.g., Foxy, Galactic).  
* **geometry\_msgs**: For the `Twist` message type, which controls linear and angular velocities.  
    
    
  


## **Code Explanation**

### **Imports and Initialization**

The code imports necessary ROS2 and message libraries, initialises the node, and sets up the publisher that sends movement commands to the `/turtle1/cmd_vel` topic.

### **Main Movement Logic**

1. **move\_square()**: Controls the turtle’s movement in a square path by sequentially moving forward and turning.  
   * **move\_cmd**: Sets forward speed.  
   * **turn\_cmd**: Sets turn speed to achieve a 90-degree rotation.  
2. **move\_straight()**: Calculates the duration to move the turtle straight for one side of the square.  
3. **turn()**: Rotates the turtle by 90 degrees at a predefined angular speed.

### **Functions**

* `move_straight()`: Publishes a linear velocity for a specified duration to cover one side of the square.  
* `turn()`: Publishes an angular velocity to make the turtle turn 90 degrees.

## **Future Improvements**

* **Dynamic Side Length**: Add parameterization for different square sizes.  
* **Variable Speed**: Allow user-defined speed for both forward and turning movements.  
* **Enhanced Patterns**: Extend functionality to create other polygonal or custom paths.

