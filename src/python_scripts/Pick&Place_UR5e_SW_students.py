import os
from robodk.robolink import *
from robodk.robomath import *
import tkinter as tk
from tkinter import messagebox

# Define relative path to the .rdk file
relative_path = "src/roboDK/Pick&Place_UR5e_students.rdk"
absolute_path = os.path.abspath(relative_path)

# Start RoboDK with the project file
RDK = Robolink()
RDK.AddFile(absolute_path)

# Retrieve items from the RoboDK station
robot = RDK.Item("UR5e")
base = RDK.Item("UR5e Base")
tool = RDK.Item("2FG7")
init_target = RDK.Item("Init")
pick_target = RDK.Item("Pick")
table = RDK.Item("Table")
cube = RDK.Item("cube")

# Hide the cube initially
cube.setVisible(False)

# Set cube pose and parent
cube_pose = pick_target.Pose()
cube.setPose(cube_pose)
cube.setParent(table)

# Set robot frame, tool and speed
robot.setPoseFrame(base)
robot.setPoseTool(tool)
robot.setSpeed(20)

# Move to initial position and show cube
def move_to_init():
    print("Init")
    robot.MoveL(init_target, True)
    print("Init_target REACHED")
    cube.setVisible(True)

# Move to pick position and attach cube to tool
def pick_cube():
    print("Pick")
    robot.MoveL(pick_target, True)
    cube.setParentStatic(tool)
    print("Pick FINISHED")

# Main sequence
def main():
    move_to_init()
    pick_cube()
    move_to_init()

# Ask user for confirmation before closing RoboDK
def confirm_close():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    response = messagebox.askquestion(
        "Close RoboDK",
        "Do you want to save changes before closing RoboDK?",
        icon='question'
    )

    if response == 'yes':
        RDK.Save()  # Save the current project
        RDK.CloseRoboDK()
        print("RoboDK saved and closed.")
    else:
        RDK.CloseRoboDK()
        print("RoboDK closed without saving.")

# Run main and handle closing
if __name__ == "__main__":
    main()
    #confirm_close()