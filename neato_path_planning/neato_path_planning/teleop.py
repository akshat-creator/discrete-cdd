import tty
import select
import sys
import termios
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

settings = termios.tcgetattr(sys.stdin)

class TeleopNode(Node):
    def __init__(self):
        super().__init__('teleop')
        self.pub = self.create_publisher(Twist, "cmd_vel", 10)
        timer_period = 0.05
        self.create_timer(timer_period, self.run_loop)

    def run_loop(self):
        msg = Twist()
        key = getKey()
        
        if key == "w":
            msg.linear.x = 0.1
            print("forward")
        if key == "s":
            msg.linear.x = -0.1
            print("backward")
        if key == "x":
            msg.linear.x = 0.0
            print("stop")
        if key == "a":
            msg.angular.z = 0.3
            print("turn left")
        if key == "d":
            msg.angular.z = -0.3
            print("turn right")
        if key == '\x03':
            raise KeyboardInterrupt
        self.pub.publish(msg)

def getKey():
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

def main():
    print('Hi from comprobo_warmup_project.')
    rclpy.init()
    node = TeleopNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        rclpy.shutdown()
        
if __name__ == '__main__':
    main()
