// this is a node to test the dof3 urdf robot.

#include <rclcpp/rclcpp.hpp>

#include <sensor_msgs/msg/joint_state.hpp>
#include <cmath>
#include <rclcpp/rclcpp.hpp>
#include <sensor_msgs/msg/joint_state.hpp>
#include <tf2_ros/transform_listener.h>
#include <tf2_ros/buffer.h>
#include <geometry_msgs/msg/transform_stamped.hpp>

#include <thread>
#include <chrono>

using namespace std::chrono;

class JointStatePublisherNode : public rclcpp::Node {


public: 
JointStatePublisherNode():

Node("jtest1") {

this->declare_parameter<double>("a1",1.0);
this->declare_parameter<double>("a2",1.0);
this->declare_parameter<double>("a3",1.0);

angle1_ = this->get_parameter("a1").as_double();
angle2_ = this->get_parameter("a2").as_double();
angle3_  = this->get_parameter("a3").as_double();

joint_state_publisher_ = this->create_publisher<sensor_msgs::msg::JointState>("joint_states",10);

  tf_buffer_ = std::make_shared<tf2_ros::Buffer>(this->get_clock());
        tf_listener_ = std::make_shared<tf2_ros::TransformListener>(*tf_buffer_);

        
          RCLCPP_INFO(this->get_logger(), "Joint states (%f %f %f) were sent to the system.", angle1_, angle2_, angle3_);
        

// Set up a timer to periodically check for the transform and broadcast it
        timer_ = this->create_wall_timer(
            std::chrono::milliseconds(100),
            std::bind(&JointStatePublisherNode::broadcastJointState, this));
        }
private:
    void broadcastJointState()
    {
        // Create a JointState message
        auto joint_state = sensor_msgs::msg::JointState();
        joint_state.header.stamp = this->get_clock()->now();
        joint_state.name = {"link1","link2","link3"};
        joint_state.position = {angle1_, angle2_, angle3_};
        
        // Publish the joint state
        joint_state_publisher_->publish(joint_state);

    }

    double angle1_;
    double angle2_;
    double angle3_;
    rclcpp::Publisher<sensor_msgs::msg::JointState>::SharedPtr joint_state_publisher_;
    std::shared_ptr<tf2_ros::Buffer> tf_buffer_;
    std::shared_ptr<tf2_ros::TransformListener> tf_listener_;
    rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char **argv) {

    rclcpp::init(argc,argv);
    auto node = std::make_shared<JointStatePublisherNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}

