# Description
[Università degli studi di Genova](https://unige.it/en/ "University of Genova")

Professor: [Carmine Recchiuto](https://github.com/CarmineD8 "Carmine Recchiuto")

Student: [AmirMahdi Matin](https://github.com/amirmat98 "AmirMahdi Matin")  - 5884715 - Robotics Engineering 

# Second assignment of Research Track 1 course

# Table of Contents
- [Introcudction](#Introcudction)
- [Documentation](#Documentation)
    - [Instalation](#Instalation)
    - [Structure](#Structure)
- [Explanation](#Explanation)
    - [First Node](#First-Node-(DefineTargetService))
    - [Second Node](#Second-Node-(TargetPositionService))
    - [Third Node](#Third-Node-(TargetDistanceService))
- [Further improvements](#Further-improvements)


## Introcudction

A ROS-based implementation that makes use of the Python programming language, with a particular emphasis on the details of the development action clients, services, and custom messages for a program that has already been built and is based on the autonomous operation of a robot throughout a simulated environment.

It can be said that the following implementations were successfully completed:

1. his involves the establishment of a node that allows for the selection of a new target for the drone to be made in real time.
2. Data was gathered through the usage of drones by sending individualized messages.
3. The development of a service that has the capability of returning the coordinates that the user has chosen.
4. The development of a service that displays the user's distance and the average velocity of the robot by making use of the data on the messages that have been prepared specifically for the user.

## Documentation

### Instalation

In order to clone the code and the entire package from the GitHub repository into a ROS workspace, you will need to use the following line of code in your terminal (clone it into a ROS workspace). Additionally, the documentation regarding the code may be seen in the link that has been provided.

```bash
$ git clone https://github.com/amirmat98/Research_Track1_Assignment2.git
```

After that, we are required to run the launch file that has already been written within our workspace.

```
roslaunch project.launch
```

### Structure
The following are the primary sections of the rt1_a2_2023 archive:
- **`scripts` Directory:**
    - `bug_as.py` :
        - **bug0 algorithm** using node that combines the two "previous" nodes.
        - An action client might be constructed to connect with it since it is designed as an action server.

    - `go_to_point_service.py` :
        - The function node is charge of directing the robot's movement toward the destination.
        - Three states(*Fix Heading*, *Go Straight*, and *Done*)make up its implementation.

    - `wall_follow_service.py` :
        - node in the service chain that controls the actions of robots when they are identified as a potential threat to the path to the desired destination.
        - It has three functions that, when activated, cause the robot to turn left and continue following it until it reaches its destination.

    - `DefineTargetService.py` : See [Explanation - First Node](#First-Node-(DefineTargetService))
    - `TargetPositionService.py` : See [Explanation - Second Node](#Second-Node-(TargetPositionService))
    - `TargetDistanceService.py` : See [Explanation - Third Node](Third-Node (TargetDistanceService))

- **`msg` Directory:**

- **`srv` Directory:**

- **`action` Directory:**

- **`config` Directory:**

- **`launch` Directory:**
    - `assignment1.launch`: ROS script that starts the simulation by running all the necessary nodes and settings.
    - `sim_w1.launch`: 

- **`urdf` Directory:**

- **`world` Directory:**

- **`root` Directory:**
    - `CMakeLists.txt` :
        - The package's configuration file; it includes all of the package's dependencies and other related files.
    - `LICENCSE` :
    - `package.xml` :
    - `README.md` :


## Explanation (including pseudocode)

Being that everything was created using the Python language, we are able to locate all of the files that are associated with it under the'scripts' folder.
- Within the'DefineTargetService.py' file, the action client was written according to the instructions.
- Both the 'TargetDistanceService.py' and the 'TargetPositionService.py' files contained the programming code for the services.

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

### Second Node (TargetPositionService)

- callback:
    - Process updates from the message containing the current target position.
- PreviousTargetImplementation Function:
    - If a response is received for the previous target position, set the data in a message format.
    - Otherwise, log the response to the ROS log.
- Main Functions:
    - Initialize the ROS node.
    - Set up subscribers to receive target position messages.
    - Create a ROS service to handle requests for retrieving the last target position.
    - Continuously wait for events, such as incoming ROS messages or signals from the operating system.


### Third Node (TargetDistanceService)
- Collecting Parameters:
    - Get the value of the average velocity window size parameter.
    - Get information out of personalized messages.
- TargetPosCallback:
    - React to messages with the target location.
- RobotPosVelCallback:
    - Oversee changes sent by the robot's location and speed notifications.
    - Include the new velocity in the list if it would make the list smaller than the window size.
    - Take off the oldest recorded velocity and add the most recent one if the list of velocities is the same size as the window.
- RobotToTargetCallback:
    - To store the outcomes of the distance computation, create a response object.
    - Notify the ROS log of the target's location.
    - Find the distance between the robot's present location and the desired destination using a mathematical function.
- Main Functions:
    - Set up the ROS node.
    - Subscribers may be set up to receive messages including the position-velocity of the robot and the target location.
    - Make a ROS service that can respond to queries for the robot's distance from a target.
    - Keep waiting for anything to happen, like an operating system signal or a ROS message.

## Further improvements
There are a few ways that this project may be enhanced.
Not only is the robot unnecessarily sluggish, but it also turns left if it encounters a wall, which means it may take more time than necessary to get to a nearby goal point. 
Furthermore, other than restarting the software, there isn't much you can do if it becomes trapped in a corner of a wall while it's moving.
Last but not least, the robot has no idea where the map ends; for example, if you tell it to go to a spot beyond the field, it will keep going in the same direction. A possible approach may be to restrict user input and reject targets beyond the known map limits. 
