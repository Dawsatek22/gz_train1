#include <functional>
#include <memory>
#include <iostream>
#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/int32.hpp"
#include <unistd.h>

///using std::placeholders::1;

class Sleep_publisher : public rclcpp::Node {

    public:

    Sleep_publisher() : Node 
    ("sleep_publisher")

    { 
      sleep_pub = this->create_publisher<std_msgs::msg::Int32>("/sleep",10);

    }
        private:

        void sleep_msg() {
while (true) {
            auto msg = std_msgs::msg::Int32();

            msg.data = 22;
            RCLCPP_INFO(this->get_logger(), "i receive the topic from the sleep publisher with the value ='%i",msg.data);
  sleep_pub ->publish(msg);
             sleep(0.5);


 } }
    

        rclcpp::Publisher<std_msgs::msg::Int32>::SharedPtr sleep_pub;


    };


int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<Sleep_publisher>());
  rclcpp::shutdown();
  return 0;
}