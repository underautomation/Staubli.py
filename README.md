# Staubli Communication SDK for Python

[![UnderAutomation Staubli communication SDK](https://raw.githubusercontent.com/underautomation/Staubli.NET/refs/heads/main/.github/assets/banner.png)](https://underautomation.com)

[![PyPI](https://img.shields.io/pypi/dm/UnderAutomation.Staubli?label=PyPI%20Downloads&logo=pypi)](https://pypi.org/project/UnderAutomation.Staubli/)
[![Python](https://img.shields.io/badge/Python-3.7+-blue)](#)
[![SOAP](https://img.shields.io/badge/Protocol-SOAP-orange)](#)
[![Platforms](https://img.shields.io/badge/OS-Windows%20%7C%20Linux%20%7C%20macOS-informational)](#)

### 🤖 Effortlessly Communicate with Staubli Robots from Python

The **Staubli Communication SDK for Python** wraps the native Staubli SOAP stack and exposes a clean, Pythonic API for automation engineers, researchers, and integrators. Use it to supervise industrial robots, orchestrate motion, exchange I/O, and manage VAL 3 applications—all without requiring additional Staubli software licenses.

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
- 📦 VAL 3 project and task management

---

## 📦 Installation

```bash
pip install UnderAutomation.Staubli
```

The package bundles the required .NET assemblies and depends on [`pythonnet`](https://github.com/pythonnet/pythonnet) to bridge Python and .NET. Make sure the target machine has a compatible .NET runtime installed.

---

## ✨ Features

### 🔌 Connect to Your Controller

```python
from underautomation.staubli.staubli_controller import StaubliController
from underautomation.staubli.connection_parameters import ConnectionParameters

controller = StaubliController()
parameters = ConnectionParameters("192.168.0.1")

parameters.soap.enable = True
parameters.soap.user = "default"
parameters.soap.password = "default"

controller.connect(parameters)
```

![UnderAutomation Staubli communication SDK](https://raw.githubusercontent.com/underautomation/Staubli.NET/refs/heads/main/.github/assets/Connect.jpg)

---

### 🔍 Explore System Information

- List robots: `controller.soap.get_robots()`
- Inspect controller parameters: `controller.soap.get_controller_parameters()`
- Retrieve DH parameters: `controller.soap.get_dh_parameters(robot=0)`

```python
robots = controller.soap.get_robots()
controller_params = controller.soap.get_controller_parameters()
dh = controller.soap.get_dh_parameters(robot=0)
```

![UnderAutomation Staubli communication SDK](https://raw.githubusercontent.com/underautomation/Staubli.NET/refs/heads/main/.github/assets/ControllerInfo.jpg)

---

### 📍 Track Positions & Joints

- Cartesian pose + joints: `controller.soap.get_current_cartesian_joint_position()`
- Joint-only feedback: `controller.soap.get_current_joint_position()`

```python
cartesian = controller.soap.get_current_cartesian_joint_position(robot=0)
print(cartesian.joints_position)
```

![UnderAutomation Staubli communication SDK](https://raw.githubusercontent.com/underautomation/Staubli.NET/refs/heads/main/.github/assets/CurrentPosition.jpg)

---

### 🧠 Kinematics Helpers

- Forward kinematics: `controller.soap.forward_kinematics(robot, joints)`
- Inverse kinematics: `controller.soap.reverse_kinematics(robot, joints, target, config, joint_range)`

```python
joints = controller.soap.get_current_joint_position(robot=0)
forward = controller.soap.forward_kinematics(0, joints)
joint_range = controller.soap.get_joint_range(robot=0)
reverse = controller.soap.reverse_kinematics(0, joints, forward.position, forward.config, joint_range)
```

![UnderAutomation Staubli communication SDK](https://raw.githubusercontent.com/underautomation/Staubli.NET/refs/heads/main/.github/assets/Kinematics.jpg)

---

### ⚙️ Motion Control Lifecycle

- Power management: `controller.soap.set_power(True)`
- Motion primitives: `move_l`, `move_jc`, `move_jj`, `move_c`
- Lifecycle control: `stop_motion`, `reset_motion`, `restart_motion`

```python
from underautomation.staubli.soap.data.motion_desc import MotionDesc
from underautomation.staubli.soap.data.frame import Frame

mdesc = MotionDesc()
mdesc.velocity = 250

frame = Frame()
frame.px, frame.py, frame.pz = 300, 0, 450

controller.soap.set_power(True)
controller.soap.move_l(0, frame, mdesc)
```

![UnderAutomation Staubli communication SDK](https://raw.githubusercontent.com/underautomation/Staubli.NET/refs/heads/main/.github/assets/Motion.jpg)

---

### 📡 Physical & Logical I/O Management

- Discover I/Os: `controller.soap.get_all_physical_ios()`
- Read states: `controller.soap.read_ios([...])`
- Write outputs: `controller.soap.write_ios([...], [...])`

```python
physical_ios = controller.soap.get_all_physical_ios()
controller.soap.write_ios(["out1"], [1.0])
```

![UnderAutomation Staubli communication SDK](https://raw.githubusercontent.com/underautomation/Staubli.NET/refs/heads/main/.github/assets/PhysicalIos.jpg)

---

### 📦 Application & Project Control

- Load projects: `controller.soap.load_project("Disk://project.pjx")`
- Inspect VAL apps: `controller.soap.get_val_applications()`
- Control lifecycle: `stop_application()`, `stop_and_unload_all()`

```python
controller.soap.load_project("Disk://project.pjx")
applications = controller.soap.get_val_applications()
controller.soap.stop_and_unload_all()
```

![UnderAutomation Staubli communication SDK](https://raw.githubusercontent.com/underautomation/Staubli.NET/refs/heads/main/.github/assets/ValApplications.jpg)

---

### 🔁 Task Supervision

- List VAL tasks: `controller.soap.get_tasks()`
- Control execution: `task_suspend`, `task_resume`, `task_kill`

```python
tasks = controller.soap.get_tasks()
controller.soap.task_kill(tasks[0].name, tasks[0].created_by)
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
🔗 [View EULA](https://underautomation.com/Staubli/eula)

Register your license at runtime with:

```python
from underautomation.staubli.staubli_controller import StaubliController

license_info = StaubliController.register_license("Your Company", "XXXX-XXXX")
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

- 📚 [Documentation](https://underautomation.com/Staubli/documentation)
- 📩 [Contact Support](https://underautomation.com/contact)

---

[⭐ Star the repo if useful](https://github.com/underautomation/Staubli.py/stargazers)  
[👁️ Watch for updates](https://github.com/underautomation/Staubli.py/watchers)
