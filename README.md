# Staubli Robot Communication SDK for Python

[![PyPI](https://img.shields.io/pypi/v/UnderAutomation.Staubli?label=PyPI&logo=pypi)](https://pypi.org/project/UnderAutomation.Staubli/)
[![PyPI downloads](https://img.shields.io/pypi/dm/UnderAutomation.Staubli?label=Downloads&logo=pypi)](https://pypi.org/project/UnderAutomation.Staubli/)
[![Python](https://img.shields.io/badge/Python-3.7_to_3.13-blue)](#compatibility)
[![Platforms](https://img.shields.io/badge/OS-Windows_Linux_macOS-informational)](#compatibility)
[![License](https://img.shields.io/badge/license-commercial-blue)](https://underautomation.com/staubli/eula)

**UnderAutomation.Staubli** is a Python package that communicates with Staubli **CS8** and **CS9** robot
controllers through the **SOAP server** of the controller. Nothing is installed on the controller. No
other Staubli software is needed on the PC.

Use it to read the robots and the controller parameters, read positions, compute the kinematics, move the
robot, read and write I/O, and manage VAL 3 applications and tasks, from a Python script.

- Product page: [underautomation.com/staubli](https://underautomation.com/staubli)
- Documentation: [underautomation.com/staubli/documentation/get-started-python](https://underautomation.com/staubli/documentation/get-started-python)
- Also available for .NET: [Staubli.NET](https://github.com/underautomation/Staubli.NET). LabVIEW: available on request, [contact us](https://underautomation.com/contact).

## How it works

The package wraps the .NET library `UnderAutomation.Staubli.dll` with [pythonnet](https://github.com/pythonnet/pythonnet).
The DLL is inside the package: `pip install` installs everything, including pythonnet.

- **Windows:** the DLL runs on the .NET Framework 4.x of Windows. Nothing else to install.
- **Linux and macOS:** install the .NET runtime (for example .NET 8), then tell pythonnet to use it before
  you start Python:

  ```bash
  export PYTHONNET_RUNTIME=coreclr
  ```

  Without this variable, pythonnet uses Mono, its default runtime on Linux and macOS. You can also choose
  the runtime in your code, before the first import of the package:

  ```python
  from pythonnet import load
  load("coreclr")
  ```

## Installation

Python 3.7 to 3.13 is supported (the limit of pythonnet 3.0.5). Install the package in a virtual
environment:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux and macOS
source .venv/bin/activate

pip install UnderAutomation.Staubli
```

Or install it from the sources of this repository:

```bash
git clone https://github.com/underautomation/Staubli.py.git
cd Staubli.py
pip install -e .
```

## Getting started

```python
from underautomation.staubli.staubli_controller import StaubliController
from underautomation.staubli.connection_parameters import ConnectionParameters

# The SDK runs in trial mode for 30 days. Register your key to remove the trial limit.
# StaubliController.register_license("Your Company", "your-license-key")

parameters = ConnectionParameters("192.168.0.254")
parameters.soap.user = "default"      # user of the controller
parameters.soap.password = "default"
parameters.soap.port = 851            # default SOAP port

controller = StaubliController()
controller.connect(parameters)

joints = controller.soap.get_current_joint_position(0)
print(list(joints))

controller.disconnect()
```

`parameters.ping_before_connect` (True by default) pings the controller before the connection.

## From .NET names to Python names

The Python API is the .NET API with Python names. The [.NET documentation](https://underautomation.com/staubli/documentation)
applies to Python.

| .NET | Python |
| --- | --- |
| Method `GetCurrentJointPosition(0)` | `get_current_joint_position(0)` |
| Property `Soap.User` | `soap.user` |
| Static method `StaubliController.RegisterLicense(...)` | `StaubliController.register_license(...)` |
| Enum value `LicenseState.Trial` | `LicenseState.Trial` (an `IntEnum`) |
| Array `double[]` | list-like object, use `list(...)` to copy it |
| `Nullable<int>` | `int \| None` |

Each type is in the module named after it, in snake case:
`UnderAutomation.Staubli.Soap.Data.MotionDesc` is `underautomation.staubli.soap.data.motion_desc.MotionDesc`.

## Features

Everything is reached through `controller.soap`.

### Controller and robots

```python
robots = controller.soap.get_robots()
for parameter in controller.soap.get_controller_parameters():
    print(parameter.name, parameter.value)

dh = controller.soap.get_dh_parameters(0)
joint_range = controller.soap.get_joint_range(0)
```

### Positions and kinematics

```python
joints = controller.soap.get_current_joint_position(0)

position = controller.soap.get_current_cartesian_joint_position(0)
print(position.cartesian_position.x, position.cartesian_position.y, position.cartesian_position.z)

# Joints to frame, then frame to joints
fk = controller.soap.forward_kinematics(0, joints)
ik = controller.soap.reverse_kinematics(0, joints, fk.position, fk.config, joint_range)
print(list(ik.joint), ik.result)
```

### Motion

```python
from underautomation.staubli.soap.data.motion_desc import MotionDesc
from underautomation.staubli.soap.data.frame import Frame

mdesc = MotionDesc()
mdesc.velocity = 50               # % of the nominal joint speed
mdesc.acceleration = 100          # %
mdesc.deceleration = 100          # %
mdesc.translation_velocity = 250  # mm/s
mdesc.rotation_velocity = 100     # deg/s
mdesc.tool = Frame()
mdesc.frame = Frame()

controller.soap.set_power(True)

result = controller.soap.move_jj(0, [0, 0, 90, 0, 90, 0], mdesc)
print(result.return_code)

target = Frame()
target.px, target.py, target.pz = 300, 0, 450
controller.soap.move_l(0, target, mdesc)

controller.soap.stop_motion()
controller.soap.set_power(False)
```

### Inputs / Outputs

```python
for io in controller.soap.get_all_physical_ios():
    print(io.name, io.type_str, io.description)

states = controller.soap.read_ios(["BasicDO_1"])
print(states[0].value, states[0].state)

responses = controller.soap.write_ios(["BasicDO_1"], [1.0])
```

### VAL 3 applications and tasks

```python
controller.soap.load_project("Disk://myProject/myProject.pjx")
for application in controller.soap.get_val_applications():
    print(application.name, application.loaded, application.is_running)

for task in controller.soap.get_tasks():
    print(task.name, task.state, task.created_by)

controller.soap.stop_and_unload_all()
```

## Examples

The folder [`examples`](examples) contains scripts ready to run. The first run asks the address of the
controller, the SOAP user, the password and the port, and saves them in `examples/robot_config.json`. It
also checks the license and asks a key when the trial has ended.

| Script | What it does |
| --- | --- |
| [`examples/controller/controller_info.py`](examples/controller/controller_info.py) | Controller parameters, robots, DH parameters and joint ranges. |
| [`examples/motion/motion_move_robot.py`](examples/motion/motion_move_robot.py) | Positions, forward and inverse kinematics, then a joint move to the zero position. |
| [`examples/io/io_read.py`](examples/io/io_read.py) | Lists the physical I/O, then reads the I/O you choose. |
| [`examples/io/io_write.py`](examples/io/io_write.py) | Lists the physical I/O, then writes the I/O you choose. |
| [`examples/applications/applications_load_start.py`](examples/applications/applications_load_start.py) | Lists the VAL 3 applications, loads and starts a project, then suspends, resumes and kills its task. |

Run a script from the root of the repository:

```bash
python examples/controller/controller_info.py
```

`examples/motion/motion_move_robot.py` moves the robot. Check the surroundings of the robot first.

## Compatibility

- **Python:** 3.7 to 3.13, with pythonnet 3.0.5.
- **Operating systems:** Windows (.NET Framework), Linux and macOS (.NET runtime and `export PYTHONNET_RUNTIME=coreclr`).
- **Controllers:** Staubli CS8 and CS9, and the emulator of Staubli Robotics Suite.

## License

This SDK needs a commercial license. A 30-day trial starts at the first use, no key needed. After the
trial, register your key in your code:

```python
from underautomation.staubli.staubli_controller import StaubliController

license_info = StaubliController.register_license("Your Company", "your-license-key")
print(license_info.state)
```

- License agreement: [underautomation.com/staubli/eula](https://underautomation.com/staubli/eula) and [License.md](License.md)
- Trial key: [underautomation.com/license](https://underautomation.com/license?sdk=staubli)
- Prices and quote: [underautomation.com/staubli](https://underautomation.com/staubli)

## Support

- Documentation: [underautomation.com/staubli/documentation](https://underautomation.com/staubli/documentation)
- Issues: [GitHub Issues](https://github.com/underautomation/Staubli.py/issues)
- Contact: [underautomation.com/contact](https://underautomation.com/contact)
