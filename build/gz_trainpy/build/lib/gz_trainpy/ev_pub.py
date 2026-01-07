# this simple publisher
import rclpy
from rclpy.node import Node


from std_msgs.msg import Int32


from evdev import InputDevice, categorize, ecodes #  to control the motor with a joystick
dev = InputDevice('/dev/input/event17') # reads device input 
print(dev) 
# below are few buttons to make commands (it was used and tested with the xbox onev controller)
Btn_a = 304 # a button
Btn_b = 305 # b button
Btn_x = 307 # x button
Btn_y = 308 # y button
""" this is a code to control a pololu motoron hat with evdev and adafruit blinka library """
# for more info links are below:
# to learn on how to use the evdev module: https://pypi.org/project/evdev/
# on how to connect gamepad to the pi: https://pimylifeup.com/raspberry-pi-bluetooth/ 
# pololu hat : https://github.com/pololu/motoron-python.git
#for adafruit blinka  and supporting modules: https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/overview
# board and busio are for the pi and the i2c communnication

from time import sleep

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('evdev_publisher')
        self.publisher_ = self.create_publisher(Int32, 'topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        
        
        for event in dev.read_loop():
            if event.type == ecodes.EV_KEY:
                
                print(categorize(event))

            if event.code == Btn_a:
                msg = Int32()
                msg.data = 30
                self.publisher_.publish(msg)
                self.get_logger().info('Publishing: "%s"' % msg.data)
               
                print("Press A Button: motor going forward")
                
       
                print("motor stopped")
            if event.code == Btn_b:
                msg = Int32()
                msg.data = 0
                self.publisher_.publish(msg)
                self.get_logger().info('Publishing: "%s"' % msg.data)
                
       
                print("Press B Button")
       


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()