#jethexa_vm

##begin

1.roslaunch jethexa_gazebo jethexa_gazebo.launch  
![image](picture/gazebo.png)  

![image](picture/gazebo_sm.png)  

2.roslaunch jethexa_controller jethexa_controller.launch  

![image](picture/roslaunch_controller.png)  

3.rostopic pub /jethexa_controller/traveling jethexa_controller_interfaces/Traveling "{gait: 2, stride: 30.0, height: 20.0, direction: 0.0, rotation: 0.0, time: 0.8, steps: 30,
  relative_height: false, interrupt: false}"  

![image](picture/sm_in_gazebo.png)  

