"""
Example: Move a Staubli robot using the UnderAutomation SDK.

This script demonstrates how to:
  1. Connect to a Staubli controller via SOAP
  2. Read the current joint and cartesian positions
  3. Compute forward and inverse kinematics and display the results
  4. Power on the robot, execute a joint move to the zero position, and power off

Requirements:
  - A Staubli controller (or emulator) reachable at the specified IP address
  - The UnderAutomation.Staubli Python package installed

Usage:
  python example_move_robot.py
"""

from underautomation.staubli.connection_parameters import ConnectionParameters
from underautomation.staubli.soap.data.frame import Frame
from underautomation.staubli.staubli_controller import StaubliController
from underautomation.staubli.soap.data.motion_desc import MotionDesc

# ---------------------------------------------------------------------------
# 1. Create a controller instance and connect
# ---------------------------------------------------------------------------
controller = StaubliController()

# If you get a InvalidLicenseException while connecting, get a trial license key from https://underautomation.com/license
#StaubliController.register_license("licensee", "license_key")

params = ConnectionParameters("127.0.0.1")
controller.connect(params)
print("Connected to the controller.\n")

# ---------------------------------------------------------------------------
# 2. Read current position and compute forward kinematics
# ---------------------------------------------------------------------------
# Get the current joint angles (in degrees)
joints = controller.soap.get_current_joint_position()

# Compute forward kinematics for robot index 0
fk = controller.soap.forward_kinematics(0, joints)

# Display forward kinematics result
print("=== Forward Kinematics (joints -> cartesian) ===")
print(f"  Joint positions : {list(joints)}")
pos = fk.position
print(f"  Position matrix (Frame):")
print(f"            N          O          A          P")
print(f"    X  {pos.nx:>10.4f}  {pos.ox:>10.4f}  {pos.ax:>10.4f}  {pos.px:>10.4f}")
print(f"    Y  {pos.ny:>10.4f}  {pos.oy:>10.4f}  {pos.ay:>10.4f}  {pos.py:>10.4f}")
print(f"    Z  {pos.nz:>10.4f}  {pos.oz:>10.4f}  {pos.az:>10.4f}  {pos.pz:>10.4f}")
print(f"  Config         : {fk.config}")
print()


# ---------------------------------------------------------------------------
# 3. Prepare motion descriptor for the move
# ---------------------------------------------------------------------------
mdesc = MotionDesc()
mdesc.config = fk.config               # Use the current robot configuration
mdesc.acceleration = 100                # Acceleration  (%)
mdesc.deceleration = 100                # Deceleration  (%)
mdesc.velocity = 100                    # Joint velocity (%)
mdesc.frequency = 100                   # Interpolation frequency (%)
mdesc.translation_velocity = 100        # Translation velocity (mm/s)
mdesc.rotation_velocity = 100           # Rotation velocity (deg/s)
mdesc.tool = Frame()                    # Tool frame  (identity)
mdesc.frame = Frame()                   # World frame (identity)

# ---------------------------------------------------------------------------
# 4. Warn the user, power on, move, then power off
# ---------------------------------------------------------------------------
print("WARNING: The robot will be powered on and moved to joint position [0, 0, 0, 0, 0, 0].")
input("Press ENTER to continue...")

# Power on the robot arm
controller.soap.set_power(True)
print("Robot powered on.")

# Execute a joint move (MoveJ) to the zero position on robot index 0
target_joints = [0, 0, 0, 0, 0, 0]
ret = controller.soap.move_jj(0, target_joints, mdesc)
print(f"MoveJ result: {ret.return_code}")

# Power off the robot arm
controller.soap.set_power(False)
print("Robot powered off.")