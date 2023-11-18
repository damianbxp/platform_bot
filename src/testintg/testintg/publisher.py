import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math

class Test_Publisher(Node):
    def __init__(self):
        super().__init__("Test_publisher")
        self.publisher_ = self.create_publisher(Twist, "/diff_drive_base_controller/cmd_vel_unstamped", 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 2* math.sin(self.i)**3
        self.i += 0.1

        self.publisher_.publish(msg)
        self._logger.info(f"Setted velocity: {msg.linear.x}")

def main(args=None):
    rclpy.init(args=args)

    test_publisher = Test_Publisher()

    rclpy.spin(test_publisher)

    test_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
