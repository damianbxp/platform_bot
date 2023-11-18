import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64MultiArray
import math

class Test_Publisher(Node):
    def __init__(self):
        super().__init__("Test_publisher")
        self.publisher_ = self.create_publisher(Float64MultiArray, "/velocity_controller/commands", 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Float64MultiArray()
        # msg.data = [2.0* math.sin(self.i)**3,0.0,0.0,0.0]
        msg.data = [1.0,0.0,0.0,0.0]


        self.i += 0.1

        self.publisher_.publish(msg)
        self._logger.info(f"Setted velocity: {msg.data}")

def main(args=None):
    rclpy.init(args=args)

    test_publisher = Test_Publisher()

    rclpy.spin(test_publisher)

    test_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
