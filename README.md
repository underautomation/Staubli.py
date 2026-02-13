# Staubli Communication SDK for Python

[![UnderAutomation Staubli communication SDK](https://raw.githubusercontent.com/underautomation/Staubli.NET/refs/heads/main/.github/assets/banner.png)](https://underautomation.com)

[![PyPI](https://img.shields.io/pypi/dm/UnderAutomation.Staubli?label=PyPI%20Downloads&logo=pypi)](https://pypi.org/project/UnderAutomation.Staubli/)
[![Python](https://img.shields.io/badge/Python-3.7+-blue)](#)
[![SOAP](https://img.shields.io/badge/Protocol-SOAP-orange)](#)
[![Platforms](https://img.shields.io/badge/OS-Windows%20%7C%20Linux%20%7C%20macOS-informational)](#)

### 🤖 Effortlessly Communicate with Staubli Robots from Python

The **Staubli Communication SDK for Python** wraps the native Staubli SOAP stack and exposes a clean, Pythonic API for automation engineers, researchers, and integrators. Use it to supervise industrial robots, orchestrate motion, exchange I/O, and manage VAL3 applications—all without requiring additional Staubli software licenses.

🔗 **More Information:** [Documentation](https://underautomation.com/Staubli/documentation/get-started-python)  
🔗 Available also for **[🟣 .NET](https://github.com/underautomation/Staubli.NET)** & **[🟨 LabVIEW](https://github.com/underautomation/Staubli.vi)**

---

## 🚀 TL;DR

✅ Install the SDK with `pip install UnderAutomation.Staubli`.  
✅ Connect to Staubli controllers via the native SOAP protocol.  
✅ Control motion, read/write I/O, monitor robots, and manage applications directly from Python.

**Highlights:**

- ⚡ Real-time SOAP communication through the embedded `UnderAutomation.Staubli.dll`
- 🐍 Pythonic wrappers for controllers, parameters, and data objects
- 🔁 Full motion lifecycle & kinematics helpers
- 📡 Access to physical & logical I/Os
- 📦 VAL3 project and task management

---

## 📦 Installation

```bash
pip install UnderAutomation.Staubli
```

The package bundles the required .NET assemblies and depends on [`pythonnet`](https://github.com/pythonnet/pythonnet) to bridge Python and .NET. Make sure the target machine has a compatible .NET runtime installed.

On **Linux**, you should also install .NET Core and set environment variable PYTHONNET_RUNTIME to coreclr :

```bash
sudo apt-get install -y dotnet-runtime-8.0
PYTHONNET_RUNTIME=coreclr
```

---

## 📖 Examples

Ready-to-run scripts are included in the repository. Each example connects to a controller, demonstrates a specific feature, and can be executed directly.

| #   | File                                                                                                               | Description                                                                                                                  |
| --- | ------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| 1   | [`example_move_robot.py`](https://github.com/UnderAutomation/Staubli.py/blob/main/example_move_robot.py)           | Connect, compute forward & inverse kinematics, display results, then power on and move the robot to the zero joint position. |
| 2   | [`example_controller_info.py`](https://github.com/UnderAutomation/Staubli.py/blob/main/example_controller_info.py) | Retrieve and display robots, DH parameters, joint ranges, and controller parameters.                                         |
| 3   | [`example_read_ios.py`](https://github.com/UnderAutomation/Staubli.py/blob/main/example_read_ios.py)               | List all physical IOs, then interactively read any IO by name or index in a loop.                                            |
| 4   | [`example_write_ios.py`](https://github.com/UnderAutomation/Staubli.py/blob/main/example_write_ios.py)             | List all physical IOs, then interactively write values to any IO by name or index in a loop.                                 |
| 5   | [`example_applications.py`](https://github.com/UnderAutomation/Staubli.py/blob/main/example_applications.py)       | List VAL3 applications, load & start a project, then suspend, resume, and kill the task step by step.                        |

Run any example with:

```bash
python example_move_robot.py
```

> **Note:** Update the IP address in each script to match your controller before running. Also, if you encounter an `InvalidLicenseException`, obtain a trial license key from [underautomation.com/license](https://underautomation.com/license?sdk=staubli) and register it in the script.

---

## ✨ Features

### 🔌 Connect to Your Controller

```python
from underautomation.staubli.staubli_controller import StaubliController
from underautomation.staubli.connection_parameters import ConnectionParameters

controller = StaubliController()
parameters = ConnectionParameters("192.168.0.1")

# Optional: configure SOAP credentials and port
parameters.soap.enable = True
parameters.soap.user = "default"
parameters.soap.password = "default"

controller.connect(parameters)
```

You can also disable the pre-connection ping if needed:

```python
parameters.ping_before_connect = False
```

![UnderAutomation Staubli communication SDK](https://raw.githubusercontent.com/underautomation/Staubli.NET/refs/heads/main/.github/assets/Connect.jpg)

---

### 🔍 Explore System Information

- List robots: `controller.soap.get_robots()`
- Inspect controller parameters: `controller.soap.get_controller_parameters()`
- Retrieve DH parameters: `controller.soap.get_dh_parameters(robot=0)`
- Retrieve joint ranges: `controller.soap.get_joint_range(robot=0)`

```python
# List robots and display their properties
robots = controller.soap.get_robots()
for i, robot in enumerate(robots):
    print(f"Robot {i}: arm={robot.arm}, kinematic={robot.kinematic}, mount={robot.mount_type}")

# Controller parameters (serial number, firmware, etc.)
for param in controller.soap.get_controller_parameters():
    print(f"{param.key}: {param.value}")

# DH parameters for robot 0
for j, dh in enumerate(controller.soap.get_dh_parameters(0)):
    print(f"Joint {j}: theta={dh.theta}, d={dh.d}, a={dh.a}, alpha={dh.alpha}")

# Joint ranges for robot 0
joint_range = controller.soap.get_joint_range(0)
for j in range(len(joint_range.min)):
    print(f"Joint {j}: min={joint_range.min[j]:.2f}, max={joint_range.max[j]:.2f}")
```

![UnderAutomation Staubli communication SDK](https://raw.githubusercontent.com/underautomation/Staubli.NET/refs/heads/main/.github/assets/ControllerInfo.jpg)

---

### 📍 Track Positions & Joints

- Cartesian pose + joints: `controller.soap.get_current_cartesian_joint_position()`
- Joint-only feedback: `controller.soap.get_current_joint_position()`

The cartesian position is returned as a `Frame` (a 3×4 homogeneous matrix with columns N, O, A, P).

```python
# Get joint positions
joints = controller.soap.get_current_joint_position(robot=0)
print(f"Joints: {list(joints)}")

# Get full cartesian + joint position
cart = controller.soap.get_current_cartesian_joint_position(robot=0)
print(f"Joints: {list(cart.joints_position)}")
print(f"Position: X={cart.cartesian_position.x}, Y={cart.cartesian_position.y}, Z={cart.cartesian_position.z}")
```

![UnderAutomation Staubli communication SDK](https://raw.githubusercontent.com/underautomation/Staubli.NET/refs/heads/main/.github/assets/CurrentPosition.jpg)

---

### 🧠 Kinematics Helpers

- Forward kinematics: `controller.soap.forward_kinematics(robot, joints)` → returns a `Frame` position and `Config`
- Inverse kinematics: `controller.soap.reverse_kinematics(robot, joints, target, config, joint_range)` → returns joint values and a `ReversingResult`

```python
# Forward kinematics: joints → cartesian
joints = controller.soap.get_current_joint_position(robot=0)
fk = controller.soap.forward_kinematics(0, joints)
pos = fk.position
print(f"FK position: px={pos.px}, py={pos.py}, pz={pos.pz}")
print(f"FK config: {fk.config}")

# Inverse kinematics: cartesian → joints
joint_range = controller.soap.get_joint_range(robot=0)
ik = controller.soap.reverse_kinematics(0, joints, fk.position, fk.config, joint_range)
print(f"IK joints: {list(ik.joint)}")
print(f"IK result: {ik.result}")  # Success, NoConvergence, etc.
```

![UnderAutomation Staubli communication SDK](https://raw.githubusercontent.com/underautomation/Staubli.NET/refs/heads/main/.github/assets/Kinematics.jpg)

---

### ⚙️ Motion Control Lifecycle

- Power management: `controller.soap.set_power(True/False)`
- Motion primitives: `move_l`, `move_jc`, `move_jj`, `move_c`
- Lifecycle control: `stop_motion`, `reset_motion`, `restart_motion`

The `MotionDesc` object controls velocity, acceleration, tool frame, and world frame:

```python
from underautomation.staubli.soap.data.motion_desc import MotionDesc
from underautomation.staubli.soap.data.frame import Frame

mdesc = MotionDesc()
mdesc.velocity = 100              # Joint velocity (%)
mdesc.acceleration = 100          # Acceleration (%)
mdesc.deceleration = 100          # Deceleration (%)
mdesc.translation_velocity = 250  # Translation velocity (mm/s)
mdesc.rotation_velocity = 100     # Rotation velocity (deg/s)
mdesc.frequency = 100             # Interpolation frequency (%)
mdesc.tool = Frame()              # Tool frame (identity)
mdesc.frame = Frame()             # World frame (identity)

# Power on, move, power off
controller.soap.set_power(True)

# Joint move (MoveJJ)
result = controller.soap.move_jj(0, [0, 0, 0, 0, 0, 0], mdesc)
print(f"Move result: {result.return_code}")

# Linear move (MoveL)
target = Frame()
target.px, target.py, target.pz = 300, 0, 450
result = controller.soap.move_l(0, target, mdesc)

controller.soap.set_power(False)
```

![UnderAutomation Staubli communication SDK](https://raw.githubusercontent.com/underautomation/Staubli.NET/refs/heads/main/.github/assets/Motion.jpg)

---

### 📡 Physical & Logical I/O Management

- Discover I/Os: `controller.soap.get_all_physical_ios()`
- Read states: `controller.soap.read_ios(["io_name"])`
- Write outputs: `controller.soap.write_ios(["io_name"], [value])`

```python
# List all IOs
for io in controller.soap.get_all_physical_ios():
    print(f"{io.name} ({io.type_str}) - {io.description}")

# Read an IO
states = controller.soap.read_ios(["BasicDO_1"])
for s in states:
    print(f"Value={s.value}, State={s.state}, Locked={s.locked}, Simulated={s.simulated}")

# Write an IO
responses = controller.soap.write_ios(["BasicDO_1"], [1.0])
for r in responses:
    print(f"Found={r.found}, Success={r.success}")
```

![UnderAutomation Staubli communication SDK](https://raw.githubusercontent.com/underautomation/Staubli.NET/refs/heads/main/.github/assets/PhysicalIos.jpg)

---

### 📦 Application & Project Control

- Load projects: `controller.soap.load_project("Disk://project/project.pjx")`
- Start applications: `controller.soap.start_application("project_name")`
- Inspect VAL3 apps: `controller.soap.get_val_applications()`
- Stop and unload: `stop_application()`, `stop_and_unload_all()`

```python
# List available applications
for app in controller.soap.get_val_applications():
    print(f"{app.name} - loaded={app.loaded}, running={app.is_running}")

# Load and start a project
controller.soap.load_project("Disk://project/project.pjx")
controller.soap.start_application("MyProject")

# Stop everything
controller.soap.stop_and_unload_all()
```

![UnderAutomation Staubli communication SDK](https://raw.githubusercontent.com/underautomation/Staubli.NET/refs/heads/main/.github/assets/ValApplications.jpg)

---

### 🔁 Task Supervision

- List VAL3 tasks: `controller.soap.get_tasks()`
- Control execution: `task_suspend`, `task_resume`, `task_kill`

```python
# List all running tasks
for task in controller.soap.get_tasks():
    print(f"{task.name}: state={task.state!r}, priority={task.priority}, created_by={task.created_by}")

# Suspend, resume, and kill a task
controller.soap.task_suspend("MyTask", "default")
controller.soap.task_resume("MyTask", "default")
controller.soap.task_kill("MyTask", "default")
```

---

### 🔌 Disconnect

```python
controller.disconnect()
```

---

## ✅ Compatibility

- **Controllers:** CS8, CS9
- **Operating Systems:** Windows, Linux, macOS
- **Python:** 3.7+
- **Dependency:** pythonnet 3.0+

---

## 📜 License

**⚠️ Commercial license required**  
🔗 [View EULA](https://underautomation.com/staubli/eula)

Register your license at runtime with:

```python
from underautomation.staubli.staubli_controller import StaubliController

license_info = StaubliController.register_license("Your Company", "XXXX-XXXX")
print(license_info.is_licensed)
print(license_info.state)
```

---

## 🤝 Contributing

You're welcome to:

- Submit issues & pull requests
- Share feature suggestions
- Help improve documentation & samples

👉 [Contribute on GitHub](https://github.com/underautomation/Staubli.py)

---

## 📬 Need Help?

- 📚 [Documentation](https://underautomation.com/staubli/documentation)
- 📩 [Contact Support](https://underautomation.com/contact)

---

[⭐ Star the repo if useful](https://github.com/underautomation/Staubli.py/stargazers)  
[👁️ Watch for updates](https://github.com/underautomation/Staubli.py/watchers)
