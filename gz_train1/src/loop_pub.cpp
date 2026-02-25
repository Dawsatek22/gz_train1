#include <string>
#include <memory>
#include <vector>
#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/int32.hpp"
#include <unistd.h>
#include <iostream>
std::shared_ptr<rclcpp::Node> node;


int main(int argc, char * argv[]) {
int i = 0;
rclcpp::init(argc, argv);
node = std::make_shared<rclcpp::Node>("publishing_loop");

auto publisher = node->create_publisher<std_msgs::msg::Int32>("loop",10);
std_msgs::msg::Int32  msg1;

RCLCPP_INFO(node->get_logger(),"node created");
  using namespace std::chrono_literals;
while (i < 20) {

msg1.data = 10;
publisher->publish(msg1);

RCLCPP_INFO(node->get_logger(),"msg data is '%i' ",msg1.data);
sleep(2);

msg1.data = 20;
publisher->publish(msg1);

RCLCPP_INFO(node->get_logger(),"msg data is '%i' ",msg1.data);
sleep(2);
msg1.data = 40;
publisher->publish(msg1);

RCLCPP_INFO(node->get_logger(),"msg data is '%i' ",msg1.data);
sleep(2);
i += 1;

std::cout << "i is "<< i << '\n';

}
rclcpp::spin(node);
rclcpp::shutdown();
return 0;
}