import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, Quaternion
from nav_msgs.msg import Odometry
import math

class PathFollowNode(Node):
    def __init__(self):
        super().__init__('follow_path')

        self.x = 0.0
        self.y = 0.0
        self.angle = 0.0

        self.twist_pub = self.create_publisher(Twist, "cmd_vel", 10)
        self.odom_sub = self.create_subscription(Odometry, 'odom', self.handle_odometry, 10)
        timer_period = 0.1
        self.timer = self.create_timer(timer_period, self.run_loop)

        self.complete_seg = False
        self.complete_turn = False
        self.complete_dist = False

        self.calc_turn = False
        self.calc_dist = False
        self.target_angle = 0.0
        self.target_dist = 0.0
        self.target_coord = [0.0, 0.0]

        self.unit = 0.5
        self.path = [[0.0, 0.0], [self.unit, self.unit], [2*self.unit, 2*self.unit], [2*self.unit, 3*self.unit], [3*self.unit, 4*self.unit], [4*self.unit, 4*self.unit]]

        self.path_idx = 0

        self.angular_in = 0.0
        self.linear_in = 0.0
        
    def handle_odometry(self, msg:Odometry):
        self.x = msg.pose.pose.position.x
        self.y = msg.pose.pose.position.y
        self.angle = quaternion_to_yaw(msg.pose.pose.orientation)

    def run_loop(self):
        msg = Twist()

        if self.path_idx != len(self.path)-1:
            current_point = self.path[self.path_idx]
            target_point = self.path[self.path_idx + 1]
            current_vector = [target_point[0]-current_point[0], target_point[1]-current_point[1]]

            # Turn to node
            if not self.complete_turn and self.angle != 0.0:
                if not self.calc_turn:
                    if current_vector == [-self.unit, self.unit]:
                        self.target_angle = 7*math.pi/4
                    if current_vector == [0.0, self.unit]:
                        self.target_angle = 3*math.pi/2
                    if current_vector == [self.unit, self.unit]:
                        self.target_angle = 5*math.pi/4
                    if current_vector == [self.unit, 0.0]:
                        self.target_angle = math.pi
                    if current_vector == [self.unit, -self.unit]:
                        self.target_angle = 3*math.pi/4
                    if current_vector == [0.0, -self.unit]:
                        self.target_angle = math.pi/2
                    if current_vector == [-self.unit, -self.unit]:
                        self.target_angle = math.pi/4
                    if current_vector == [-self.unit, 0.0]:
                        self.target_angle = 0.0

                    curr_angle_diff = self.angle - self.target_angle
                    if (curr_angle_diff < 0.0 and abs(curr_angle_diff) > math.pi) or (curr_angle_diff > 0.0 and abs(curr_angle_diff) < math.pi):
                        self.angular_in = -0.15
                    else:
                        self.angular_in = 0.15
                    self.calc_turn = True                

                msg.angular.z = self.angular_in

                if abs(self.angle - self.target_angle) < math.pi/120:
                    self.complete_turn = True
                    msg.angular.z = 0.0

            # Drive to node
            if self.complete_turn and self.x != 0.0:
                if not self.calc_dist:
                    self.target_coord = [self.x + current_vector[0], self.y + current_vector[1]]
                    self.calc_dist = True

                msg.linear.x = 0.1

                if math.dist([self.x, self.y], self.target_coord) < 0.075:
                    self.complete_dist = True
                    msg.linear.x = 0.0

            if self.complete_dist and self.complete_turn:
                self.complete_dist = False
                self.complete_turn = False
                self.calc_dist = False
                self.calc_turn = False
                self.path_idx += 1

        self.twist_pub.publish(msg)
        

def quaternion_to_yaw(quat: Quaternion):
    x = quat.x
    y = quat.y
    z = quat.z
    w = quat.w

    t1 = 2.0 * (w * z + x * y)
    t2 = 1.0 - 2.0 * (y * y + z * z)
    yaw_z = math.atan2(t1, t2)

    return yaw_z + math.pi

def main():
    rclpy.init()
    node = PathFollowNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()