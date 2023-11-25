import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64MultiArray



class Controller(Node):
    def __init__(self):
        super().__init__("Platform_Controller")
        self.publisher = self.create_publisher(Float64MultiArray, "/velocity_controller/commands", 10)
        self.subscriber = self.create_subscription(Twist, "/cmd_vel", self.listener_callback, 10)
        self._logger.info("Node Created")

    def listener_callback(self, msg: Twist):
        command = Float64MultiArray()

        # teleop Twist conversion
        x = -msg.linear.y
        y = msg.linear.x
        rz = -msg.angular.z

        # denominator = max(abs(x) + abs(y) + abs(rz), 1)
        denominator = 1
        command.data = [
            (y+x+rz)/denominator,
            (y-x-rz)/denominator,
            (y-x+rz)/denominator,
            (y+x-rz)/denominator,
        ]
        self.publisher.publish(command)
        self._logger.info(f"X: {x} Y:{y} RZ:{rz} [{command.data[0]}, {command.data[1]}, {command.data[2]}, {command.data[3]}]")


def main(args=None):
    rclpy.init(args=args)

    platform_controller = Controller()

    rclpy.spin(platform_controller)

    platform_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
