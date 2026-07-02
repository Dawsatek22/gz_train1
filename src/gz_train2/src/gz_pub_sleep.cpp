#include <chrono>
#include <functional>
#include <memory>
#include <string>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/int32.hpp"
#include <unistd.h>

using namespace std::chrono_literals;

//using std::placeholders::1;

class Sleep_publisher : public rclcpp::Node {

    public:

    Sleep_publisher() : Node 
    ("sleep_publisher")

    { 
      sleep_pub = this->create_publisher<std_msgs::msg::Int32>("/sleep",10);
      timer_ = this->create_wall_timer(
        2000ms, std::bind(&Sleep_publisher::sleep_msg, this));
    }
        private:

        void sleep_msg() {

            auto msg = std_msgs::msg::Int32();

            msg.data = 20;
            RCLCPP_INFO(this->get_logger(), "i send the topic from the sleep publisher with the value ='%i",msg.data);
  sleep_pub ->publish(msg);
             sleep(4);
   msg.data = 0;
            RCLCPP_INFO(this->get_logger(), "i sent the topic from the sleep publisher with the value ='%i",msg.data);
  sleep_pub ->publish(msg);
             sleep(3);

             msg.data = 10;
            RCLCPP_INFO(this->get_logger(), "i sent the topic from the sleep publisher with the value ='%i",msg.data);
  sleep_pub ->publish(msg);
             sleep(3);
                      msg.data = 20;
            RCLCPP_INFO(this->get_logger(), "i sent the topic from the sleep publisher with the value ='%i",msg.data);
  sleep_pub ->publish(msg);
             sleep(3);

                    msg.data = 0;
            RCLCPP_INFO(this->get_logger(), "i sent the topic from the sleep publisher with the value ='%i",msg.data);
  sleep_pub ->publish(msg);
             sleep(3);



 } 
    
rclcpp::TimerBase::SharedPtr timer_;

        rclcpp::Publisher<std_msgs::msg::Int32>::SharedPtr sleep_pub;


    };


int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<Sleep_publisher>());
  rclcpp::shutdown();
  return 0;
}