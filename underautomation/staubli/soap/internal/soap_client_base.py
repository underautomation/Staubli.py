import typing
from underautomation.staubli.soap.data.robot import Robot
from underautomation.staubli.soap.data.cartesian_joint_position import CartesianJointPosition
from underautomation.staubli.soap.data.cartesian_position import CartesianPosition
from underautomation.staubli.soap.data.parameter import Parameter
from underautomation.staubli.soap.data.val_application import ValApplication
from underautomation.staubli.soap.data.joint_range import JointRange
from underautomation.staubli.soap.data.physical_io import PhysicalIo
from underautomation.staubli.soap.data.dh_parameters import DhParameters
from underautomation.staubli.soap.data.controller_task import ControllerTask
from underautomation.staubli.soap.data.physical_io_state import PhysicalIoState
from underautomation.staubli.soap.data.physical_io_write_response import PhysicalIoWriteResponse
from underautomation.staubli.soap.data.i_forward_kinematics import IForwardKinematics
from underautomation.staubli.soap.data.i_reverse_kinematics import IReverseKinematics
from underautomation.staubli.soap.data.frame import Frame
from underautomation.staubli.soap.data.config import Config
from underautomation.staubli.soap.data.i_move_result import IMoveResult
from underautomation.staubli.soap.data.motion_desc import MotionDesc
from underautomation.staubli.soap.data.motion_return_code import MotionReturnCode
from underautomation.staubli.soap.data.power_return_code import PowerReturnCode
from UnderAutomation.Staubli.Soap.Internal import SoapClientBase as soap_client_base
from UnderAutomation.Staubli.Soap.Data import MotionReturnCode as motion_return_code
from UnderAutomation.Staubli.Soap.Data import PowerReturnCode as power_return_code

class SoapClientBase:
	'''Base class for SOAP client'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = soap_client_base()
		else:
			self._instance = _internal

	def disconnect(self) -> None:
		'''Disconnect SOAP client from robot'''
		self._instance.Disconnect()

	def get_robots(self) -> typing.List[Robot]:
		'''Get all the robots handled by this controller

		:returns: List of all robots
		'''
		return [Robot(x) for x in self._instance.GetRobots()]

	def get_current_cartesian_joint_position(self, robot: int=0, tool: CartesianPosition=None, frame: CartesianPosition=None) -> CartesianJointPosition:
		'''Get the Cartesian position and joint positions of a robot

		:param robot: Id of the robot (a controller can handle multiple robots, see method GetRobots()). Use 0 if you only have one robot
		:param tool: Tool pose in flange frame. If null, the position of the flange is returned
		:param frame: Frame in which the Cartesian position of the tool is returned
		:returns: Robot joint position and specified tool current cartesian position
		'''
		return CartesianJointPosition(self._instance.GetCurrentCartesianJointPosition(robot, tool._instance if tool else None, frame._instance if frame else None))

	def get_current_joint_position(self, robot: int=0) -> typing.List[float]:
		'''Get the current joint position of a robot

		:param robot: Id of the robot (a controller can handle multiple robots, see method GetRobots()). Use 0 if you only have one robot
		:returns: Position of each axis in radians
		'''
		return self._instance.GetCurrentJointPosition(robot)

	def get_controller_parameters(self) -> typing.List[Parameter]:
		'''Get the current Cartesian position of a robot end effector

		:returns: List of parameters
		'''
		return [Parameter(x) for x in self._instance.GetControllerParameters()]

	def get_val_applications(self) -> typing.List[ValApplication]:
		'''Get all the VAL applications available on the controller

		:returns: List of all applications
		'''
		return [ValApplication(x) for x in self._instance.GetValApplications()]

	def get_joint_range(self, robot: int=0) -> JointRange:
		'''Get the range Min-Max of each joint of a robot

		:param robot: Id of the robot (a controller can handle multiple robots, see method GetRobots()). Use 0 if you only have one robot
		:returns: The range of each axis
		'''
		return JointRange(self._instance.GetJointRange(robot))

	def get_all_physical_ios(self) -> typing.List[PhysicalIo]:
		'''Get all the physical I/O values of the controller

		:returns: Array of physical I/O
		'''
		return [PhysicalIo(x) for x in self._instance.GetAllPhysicalIos()]

	def get_dh_parameters(self, robot: int=0) -> typing.List[DhParameters]:
		'''Get Robot DH parameters

		:param robot: Id of the robot (a controller can handle multiple robots, see method GetRobots()). Use 0 if you only have one robot
		:returns: DH parameters
		'''
		return [DhParameters(x) for x in self._instance.GetDhParameters(robot)]

	def get_tasks(self) -> typing.List[ControllerTask]:
		'''Get all the tasks available on the controller

		:returns: Array of robot task
		'''
		return [ControllerTask(x) for x in self._instance.GetTasks()]

	def read_ios(self, ios: typing.List[str]) -> typing.List[PhysicalIoState]:
		'''Read the state of specified physical I/Os

		:param ios: I/O names to read
		:returns: Array of physical I/O states
		'''
		return [PhysicalIoState(x) for x in self._instance.ReadIos(ios)]

	def start_application(self, applicationPath: str) -> None:
		'''Start a VAL application on the controller

		:param applicationPath: Path to the VAL application to start
		'''
		self._instance.StartApplication(applicationPath)

	def stop_and_unload_all(self) -> None:
		'''Stop all VAL applications on the controller'''
		self._instance.StopAndUnloadAll()

	def stop_application(self) -> None:
		'''Stop application on the controller'''
		self._instance.StopApplication()

	def task_kill(self, taskName: str, createdBy: str) -> None:
		'''Kill a task on the controller

		:param taskName: Name of the task to kill
		'''
		self._instance.TaskKill(taskName, createdBy)

	def task_resume(self, taskName: str, createdBy: str) -> None:
		'''Resume a task on the controller

		:param taskName: Name of the task to suspend
		'''
		self._instance.TaskResume(taskName, createdBy)

	def task_suspend(self, taskName: str, createdBy: str) -> None:
		'''Suspend a task on the controller

		:param taskName: Name of the task to suspend
		'''
		self._instance.TaskSuspend(taskName, createdBy)

	def write_ios(self, ios: typing.List[str], values: typing.List[float]) -> typing.List[PhysicalIoWriteResponse]:
		'''Write values to specified physical I/Os

		:param ios: I/O names to write
		:param values: Values to write to the I/Os
		:returns: Array of physical I/O write responses
		'''
		return [PhysicalIoWriteResponse(x) for x in self._instance.WriteIos(ios, values)]

	def load_project(self, projectPath: str) -> None:
		'''Load a project in memory from disk (does not start it)

		:param projectPath: Path to the project file on the controller
		'''
		self._instance.LoadProject(projectPath)

	def forward_kinematics(self, robot: int, joints: typing.List[float]) -> IForwardKinematics:
		'''Calculate the forward kinematics of a robot based on its joint positions

		:param robot: Id of the robot (a controller can handle multiple robots, see method GetRobots()). Use 0 if you only have one robot
		:param joints: Joint positions in radians
		:returns: IForwardKinematics containing the calculated Cartesian position and orientation of the robot end effector
		'''
		return IForwardKinematics(self._instance.ForwardKinematics(robot, joints))

	def reverse_kinematics(self, robot: int, joint: typing.List[float], target: Frame, config: Config, jointRange: JointRange) -> IReverseKinematics:
		'''Calculate the reverse kinematics of a robot to reach a target position and orientation

		:param robot: Id of the robot (a controller can handle multiple robots, see method GetRobots()). Use 0 if you only have one robot
		:param joint: Initial joint positions in radians, used as a starting point for the calculation
		:param target: Target position and orientation to reach
		:param config: Configuration for the reverse kinematics calculation, such as orientation constraints
		:param jointRange: Range of each joint, used to limit the search space for the solution
		:returns: IReverseKinematics containing the calculated joint positions to reach the target position and orientation
		'''
		return IReverseKinematics(self._instance.ReverseKinematics(robot, joint, target._instance if target else None, config._instance if config else None, jointRange._instance if jointRange else None))

	def move_c(self, robot: int, frameB: Frame, frameC: Frame, mdesc: MotionDesc) -> IMoveResult:
		'''Move the robot to a target position using a Cartesian path

		:param robot: Id of the robot (a controller can handle multiple robots, see method GetRobots()). Use 0 if you only have one robot
		:param frameB: Starting position and orientation of the robot end effector
		:param frameC: Target position and orientation of the robot end effector
		:param mdesc: Motion description containing parameters such as speed, acceleration, ...
		:returns: IMoveResult containing the result of the move operation, such as success status and any errors encountered
		'''
		return IMoveResult(self._instance.MoveC(robot, frameB._instance if frameB else None, frameC._instance if frameC else None, mdesc._instance if mdesc else None))

	def move_jc(self, robot: int, frame: Frame, mdesc: MotionDesc) -> IMoveResult:
		'''Move the robot to a target position using a Cartesian path with joint constraints

		:param robot: Id of the robot (a controller can handle multiple robots, see method GetRobots()). Use 0 if you only have one robot
		:param frame: Target position and orientation of the robot end effector
		:param mdesc: Motion description containing parameters such as speed, acceleration, ...
		:returns: IMoveResult containing the result of the move operation, such as success status and any errors encountered
		'''
		return IMoveResult(self._instance.MoveJC(robot, frame._instance if frame else None, mdesc._instance if mdesc else None))

	def move_jj(self, robot: int, joints: typing.List[float], mdesc: MotionDesc) -> IMoveResult:
		'''Move the robot to a target position using joint positions

		:param robot: Id of the robot (a controller can handle multiple robots, see method GetRobots()). Use 0 if you only have one robot
		:param joints: Joint positions in radians to reach the target position
		:param mdesc: Motion description containing parameters such as speed, acceleration, ...
		:returns: IMoveResult containing the result of the move operation, such as success status and any errors encountered
		'''
		return IMoveResult(self._instance.MoveJJ(robot, joints, mdesc._instance if mdesc else None))

	def move_l(self, robot: int, frame: Frame, mdesc: MotionDesc) -> IMoveResult:
		'''Move the robot to a target position using a linear path in Cartesian space

		:param robot: Id of the robot (a controller can handle multiple robots, see method GetRobots()). Use 0 if you only have one robot
		:param frame: Target position and orientation of the robot end effector
		:param mdesc: Motion description containing parameters such as speed, acceleration, ...
		:returns: IMoveResult containing the result of the move operation, such as success status and any errors encountered
		'''
		return IMoveResult(self._instance.MoveL(robot, frame._instance if frame else None, mdesc._instance if mdesc else None))

	def reset_motion(self) -> MotionReturnCode:
		'''Reset the motion of the robot

		:returns: MotionReturnCode indicating the result of the reset operation
		'''
		return MotionReturnCode(int(self._instance.ResetMotion()))

	def restart_motion(self) -> MotionReturnCode:
		'''Restart the motion of the robot

		:returns: MotionReturnCode indicating the result of the restart operation
		'''
		return MotionReturnCode(int(self._instance.RestartMotion()))

	def stop_motion(self) -> MotionReturnCode:
		'''Stop the motion of the robot immediately

		:returns: MotionReturnCode indicating the result of the restart operation
		'''
		return MotionReturnCode(int(self._instance.StopMotion()))

	def set_power(self, power: bool) -> PowerReturnCode:
		'''Set the power state of the robot (controller mut be in remote mode)

		:param power: true to power on the robot, false to power off
		:returns: PowerReturnCode indicating the result of the operation
		'''
		return PowerReturnCode(int(self._instance.SetPower(power)))

	@property
	def ip(self) -> str:
		'''Connected robot IP address or host name'''
		return self._instance.Ip

	@property
	def port(self) -> int:
		'''SOAP TCP port'''
		return self._instance.Port

	@property
	def session_id(self) -> int:
		'''Session ID for the SOAP connection'''
		return self._instance.SessionId

	@property
	def enabled(self) -> bool:
		'''Check if the SOAP client is connected to a robot'''
		return self._instance.Enabled

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SoapClientBase):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
