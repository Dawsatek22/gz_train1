#include <functional>
#include <memory>
#include <iostream>
#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/int32.hpp"

using std::placeholders::_1;


class Gz_subscriber : public rclcpp::Node

{


    public:
    Gz_subscriber()
    : Node("Gz_topic_subscriber")
    {
        gz_sub = this->create_subscription<std_msgs::msg::Int32>(
            "/sleep",10,std::bind(&Gz_subscriber::topic_callback, this,_1));


    }

    private:


    
    void topic_callback(const std_msgs::msg::Int32 & msg)
    {
        
RCLCPP_INFO(this->get_logger(), "i receive the topic from gazebo with the value ='%i",msg.data);


    }

    rclcpp::Subscription<std_msgs::msg::Int32>::SharedPtr gz_sub;
};

int main(int argc, char * argv[])

{
    std::cout << "subcriber starts now" << '\n'; 
rclcpp::init(argc, argv);
rclcpp::spin(std::make_shared<Gz_subscriber>());
rclcpp::shutdown();

return 0;


}

