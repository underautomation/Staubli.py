"""
Example: Controller Information - Staubli Robot

This script demonstrates how to retrieve various controller and robot information:
  1. Connect to a Staubli controller via SOAP
  2. Display controller parameters (system information)
  3. Retrieve the list of robots connected to the controller
  4. Display Denavit-Hartenberg (DH) parameters for each robot
  5. Display joint ranges (min/max) for each robot

Requirements:
  - A Staubli controller (or emulator) reachable at the specified IP address
  - The UnderAutomation.Staubli Python package installed

Usage:
  python example_controller_info.py
"""

from underautomation.staubli.connection_parameters import ConnectionParameters
from underautomation.staubli.staubli_controller import StaubliController

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
# 2. Get controller parameters
# ---------------------------------------------------------------------------
print("\n" + "=" * 60)
print("CONTROLLER PARAMETERS")
print("=" * 60)
params_list = controller.soap.get_controller_parameters()
print(f"\n  {'Key':<30}  {'Name':<30}  {'Value'}")
print(f"  {'-'*30}  {'-'*30}  {'-'*30}")

for param in params_list:
    key = param.key if param.key else ""
    name = param.name if param.name else ""
    value = param.value if param.value else ""
    print(f"  {key:<30}  {name:<30}  {value}")

# ---------------------------------------------------------------------------
# 3. Get list of robots
# ---------------------------------------------------------------------------
print("=" * 60)
print("ROBOTS")
print("=" * 60)

robots = controller.soap.get_robots()
print(f"Number of robots: {len(robots)}\n")

for i, robot in enumerate(robots):
    print(f"  Robot {i}:")
    print(f"    Arm        : {robot.arm}")
    print(f"    Tuning     : {robot.tuning}")
    print(f"    Kinematic  : {robot.kinematic}")
    print(f"    Mount Type : {robot.mount_type}")
    print()

# ---------------------------------------------------------------------------
# 4. Get DH parameters for each robot
# ---------------------------------------------------------------------------
print("=" * 60)
print("DH PARAMETERS (Denavit-Hartenberg)")
print("=" * 60)

for i in range(len(robots)):
    print(f"\n  Robot {i} DH Parameters:")
    print(f"    {'Joint':>6}  {'Theta':>10}  {'D':>10}  {'A':>10}  {'Alpha':>10}  {'Beta':>10}")
    print(f"    {'-'*6}  {'-'*10}  {'-'*10}  {'-'*10}  {'-'*10}  {'-'*10}")
    
    dh_params = controller.soap.get_dh_parameters(i)
    for j, dh in enumerate(dh_params):
        print(f"    {j+1:>6}  {dh.theta:>10.4f}  {dh.d:>10.4f}  {dh.a:>10.4f}  {dh.alpha:>10.4f}  {dh.beta:>10.4f}")

# ---------------------------------------------------------------------------
# 5. Get joint ranges for each robot
# ---------------------------------------------------------------------------
print("\n" + "=" * 60)
print("JOINT RANGES")
print("=" * 60)

for i in range(len(robots)):
    print(f"\n  Robot {i} Joint Ranges:")
    print(f"    {'Joint':>6}  {'Min (rad)':>12}  {'Max (rad)':>12}")
    print(f"    {'-'*6}  {'-'*12}  {'-'*12}")
    
    joint_range = controller.soap.get_joint_range(i)
    min_vals = list(joint_range.min)
    max_vals = list(joint_range.max)
    
    for j in range(len(min_vals)):
        print(f"    {j+1:>6}  {min_vals[j]:>12.2f}  {max_vals[j]:>12.2f}")




print("\nDone.")
