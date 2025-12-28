
#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>
#include <linux/joystick.h>
#include <signal.h>
#include <unistd.h>
#include "rclcpp/rclcpp.hpp"
#include <atomic>
#include <chrono>
#include <csignal>
#include <iostream>
#include <string>
#include <thread>
#include "std_msgs/msg/int32.hpp"
/**
 * Reads a joystick event from the joystick device.
 *
 * Returns 0 on success. Otherwise -1 is returned.
 */
int read_event(int fd, struct js_event *event)
{
    ssize_t bytes;

    bytes = read(fd, event, sizeof(*event));

    if (bytes == sizeof(*event))
        return 0;

    /* Error, could not read full event. */
    return -1;
}

/**
 * Returns the number of axes on the controller or 0 if an error occurs.
 */
size_t get_axis_count(int fd)
{
    __u8 axes;

    if (ioctl(fd, JSIOCGAXES, &axes) == -1)
        return 0;

    return axes;
}

/**
 * Returns the number of buttons on the controller or 0 if an error occurs.
 */
size_t get_button_count(int fd)
{
    __u8 buttons;
    if (ioctl(fd, JSIOCGBUTTONS, &buttons) == -1)
        return 0;

    return buttons;
}

/**
 * Current state of an axis.
 */
struct axis_state {
    short x, y;
};

/**
 * Keeps track of the current axis state.
 *
 * NOTE: This function assumes that axes are numbered starting from 0, and that
 * the X axis is an even number, and the Y axis is an odd number. However, this
 * is usually a safe assumption.
 *
 * Returns the axis that the event indicated.
 */
size_t get_axis_state(struct js_event *event, struct axis_state axes[3])
{
    size_t axis = event->number / 2;

    if (axis < 3)
    {
        if (event->number % 2 == 0)
            axes[axis].x = event->value;
        else
            axes[axis].y = event->value;
    }

    return axis;
}

int main(int argc, char *argv[])
{

      rclcpp::init(argc, argv);

    auto node = rclcpp::Node::make_shared("joy_publisher");
  auto publisher = node->create_publisher<std_msgs::msg::Int32>("joy", 10);
   auto message = std_msgs::msg::Int32();
 
    const char *device;
    int js;
    struct js_event event;
  message.data = 0;
         publisher->publish(message);

   rclcpp::executors::SingleThreadedExecutor executor;
  executor.add_node(node);
    if (argc > 1)
        device = argv[1];
    else
        device = "/dev/input/js0";

    js = open(device, O_RDONLY);

    if (js == -1)
        perror("Could not open joystick");

    /* This loop will exit if the controller is unplugged. */
    while (read_event(js, &event) == 0 && rclcpp::ok())
    {

    
 
   
        switch (event.type)
        {
           
            case JS_EVENT_BUTTON:
                printf("Button %u %s\n", event.number, event.value ? "pressed" : "released");
                break;
           
        }
        if (event.number == 3) {
           message.data = 30;
              publisher->publish(message);
            std::cout <<  "message data is:"<< message.data << '\n';

 RCLCPP_INFO(node->get_logger(), "Publishing: '%d'", message.data);
    executor.spin_some();
           

        }

        if (event.number == 4) {
            
           message.data = 40;
              publisher->publish(message);
            std::cout <<  "message data is:"<< message.data << '\n';
    executor.spin_some();
           
 RCLCPP_INFO(node->get_logger(), "Publishing: '%d'", message.data);
 
        }



             
        if (event.number == 0) {
           
      message.data = 0;
              publisher->publish(message);
            std::cout <<  "message data is:"<< message.data << '\n';
    executor.spin_some();
           
 RCLCPP_INFO(node->get_logger(), "Publishing: '%d'", message.data);


        }

        if (event.number == 2) {
          
    message.data = 20;
              publisher->publish(message);
            std::cout <<  "message data is:"<< message.data << '\n';
    executor.spin_some();
           
 RCLCPP_INFO(node->get_logger(), "Publishing: '%d'", message.data);

        }
    
 if (event.number == 1) {
          
     
         message.data = 10;
              publisher->publish(message);
            std::cout <<  "message data is:"<< message.data << '\n';
    executor.spin_some();
           
 RCLCPP_INFO(node->get_logger(), "Publishing: '%d'", message.data);
        }
        
            usleep(500);
    }
    
        fflush(stdout);
    

 
      rclcpp::shutdown();
    close(js);
    return 0;
      }