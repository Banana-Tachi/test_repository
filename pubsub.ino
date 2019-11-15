//third_sub_pubのまま？

//sub side
#include <ros.h>
#include <std_msgs/String.h>

//pub side
//#include"ros/ros.h"
//#include"std_msgs/String.h"
//#include<sstream>

//ros::Subscriber sub;
//ros::Publisher pub;

ros::NodeHandle nh;

std_msgs::String msg;
ros::Publisher pub("my_topic3",&msg);

void messageCallback(const std_msgs::String& msg){  
  //pub side

  pub.publish(&msg);
}

ros::Subscriber<std_msgs::String> sub("my_topic", messageCallback);
//ros::Publisher pub("my_topic3",msg);

void setup(){
  nh.initNode();
  nh.advertise(pub);
  nh.subscribe(sub);
  //ros::init(argc,argv,"sub_pub");
  

  //ros::Subscriber sub = nh.subscribe("my_topic",10,messageCallback);
  //ros::Publisher pub = nh.advertise <std_msgs::String>("my_topic3",1000);
  
  //ros::spin();
  return 0;
}

void loop(){
  nh.spinOnce();
}
