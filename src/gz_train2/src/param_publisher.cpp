#include <chrono>
#include <functional>
#include <string>

#include <rclcpp/rclcpp.hpp>
#include "std_msgs/msg/string.hpp"
#include <unistd.h>

using namespace std::chrono_literals;
using namespace std;


using namespace std::chrono_literals;

class Param_pub : public rclcpp::Node
{
public:
  Param_pub()
  : Node("minimal_param_node")
  {
    this->declare_parameter("my_parameter", "world");

    auto timer_callback = [this](){
      std::string my_param = this->get_parameter("my_parameter").as_string();

      RCLCPP_INFO(this->get_logger(), "Hello %s!", my_param.c_str());

      std::vector<rclcpp::Parameter> all_new_parameters{rclcpp::Parameter("my_parameter", "world")};
      this->set_parameters(all_new_parameters);
    };
    timer_ = this->create_wall_timer(1000ms, timer_callback);
  }

private:
  rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc,char ** argv) {
rclcpp::init(argc, argv);
rclcpp::spin(make_shared<Param_pub>());
rclcpp::shutdown();
return 0;

}