# Description
[Università degli studi di Genova](https://unige.it/en/ "University of Genova")

Professor: [Carmine Recchiuto](https://github.com/CarmineD8 "Carmine Recchiuto")

Student: [AmirMahdi Matin](https://github.com/amirmat98 "AmirMahdi Matin")  - 5884715 - Robotics Engineering 

# Second assignment of Research Track 1 course

# Table of Contents
- [Introcudction](#Introcudction)
- [Documentation](#Documentation)
- [Explanation](#Explanation)
    - [First Node](#First-Node)


## Introcudction

A ROS-based implementation that makes use of the Python programming language, with a particular emphasis on the details of the development action clients, services, and custom messages for a program that has already been built and is based on the autonomous operation of a robot throughout a simulated environment.

It can be said that the following implementations were successfully completed:

1. his involves the establishment of a node that allows for the selection of a new target for the drone to be made in real time.
2. Data was gathered through the usage of drones by sending individualized messages.
3. The development of a service that has the capability of returning the coordinates that the user has chosen.
4. The development of a service that displays the user's distance and the average velocity of the robot by making use of the data on the messages that have been prepared specifically for the user.

## Documentation
In order to clone the code and the entire package from the GitHub repository into a ROS workspace, you will need to use the following line of code in your terminal (clone it into a ROS workspace). Additionally, the documentation regarding the code may be seen in the link that has been provided.

```bash
$ git clone https://github.com/amirmat98/Research_Track1_Assignment2.git
```

After that, we are required to run the launch file that has already been written within our workspace.

```
roslaunch project.launch
```

## Explanation (including pseudocode)

Being that everything was created using the Python language, we are able to locate all of the files that are associated with it under the'scripts' folder.
- Within the'set_target.py' file, the action client was written according to the instructions.
- Both the 'robot_to_target_service.py' and the 'last_target_service.py' files contained the programming code for the services.

### First Node (DefineTargetService)

```
function timer_callback()
    if goal has active state
        Print current position to logs
function cancel_callback()
    Handle cancel requests
    Log into rospy
function  target_callback()
    Handle target position updates
    Create a goal for the action server
    Send the goal to the action server
function state_callback()
    Obtain message from /odom
    Construct custom message
    Publish the data
function done_callback()
    Handle completion of the goal
    Log information to rospy
function feedback_callback()
    Handle the feedback data during execution
Main function
    Initialize the ROS node
    Create a SimpleActionClient
    Get the namespace
    Wait for the action server
    Set up subscribers
    Set up publishers
    Set up timer for periodic callbacls
    Start of the ROS node
    Wait for events
    Signal in case of shutdown
    Wait before exiting
```
