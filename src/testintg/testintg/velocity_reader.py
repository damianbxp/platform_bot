import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class Velocity_Reader(Node):
    def __init__(self):
        super().__init__("velocity_reader")
        self.subscription = self.create_subscription(Twist, "/diff_drive_base_controller/cmd_vel_unstamped", self.listener_callback, 10)

    def listener_callback(self, msg:Twist):
        self._logger.info(f"Vel: {msg.linear.x}")

def main(args=None):
    rclpy.init(args=args)

    vel_reader = Velocity_Reader()

    rclpy.spin(vel_reader)

    vel_reader.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()