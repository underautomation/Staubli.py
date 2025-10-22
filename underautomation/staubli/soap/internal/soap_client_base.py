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
import clr
import os
clr.AddReference(os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..",  'lib', 'UnderAutomation.Staubli.dll')))
from UnderAutomation.Staubli.Soap.Internal import SoapClientBase as soap_client_base

T = typing.TypeVar('T')
class SoapClientBase:
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = soap_client_base()
		else:
			self._instance = _internal
	def disconnect(self) -> None:
		self._instance.Disconnect()
	def get_robots(self) -> typing.List[Robot]:
		return [Robot(x) for x in self._instance.GetRobots()]
	def get_current_cartesian_joint_position(self, robot: int=0, tool: CartesianPosition=None, frame: CartesianPosition=None) -> CartesianJointPosition:
		return CartesianJointPosition(self._instance.GetCurrentCartesianJointPosition(robot, tool._instance, frame._instance))
	def get_current_joint_position(self, robot: int=0) -> typing.List[float]:
		return self._instance.GetCurrentJointPosition(robot)
	def get_controller_parameters(self) -> typing.List[Parameter]:
		return [Parameter(x) for x in self._instance.GetControllerParameters()]
	def get_val_applications(self) -> typing.List[ValApplication]:
		return [ValApplication(x) for x in self._instance.GetValApplications()]
	def get_joint_range(self, robot: int=0) -> JointRange:
		return JointRange(self._instance.GetJointRange(robot))
	def get_all_physical_ios(self) -> typing.List[PhysicalIo]:
		return [PhysicalIo(x) for x in self._instance.GetAllPhysicalIos()]
	def get_dh_parameters(self, robot: int=0) -> typing.List[DhParameters]:
		return [DhParameters(x) for x in self._instance.GetDhParameters(robot)]
	def get_tasks(self) -> typing.List[ControllerTask]:
		return [ControllerTask(x) for x in self._instance.GetTasks()]
	def read_ios(self, ios: typing.List[str]) -> typing.List[PhysicalIoState]:
		return [PhysicalIoState(x) for x in self._instance.ReadIos(ios)]
	def start_application(self, applicationPath: str) -> None:
		self._instance.StartApplication(applicationPath)
	def stop_and_unload_all(self) -> None:
		self._instance.StopAndUnloadAll()
	def stop_application(self) -> None:
		self._instance.StopApplication()
	def task_kill(self, taskName: str, createdBy: str) -> None:
		self._instance.TaskKill(taskName, createdBy)
	def task_resume(self, taskName: str, createdBy: str) -> None:
		self._instance.TaskResume(taskName, createdBy)
	def task_suspend(self, taskName: str, createdBy: str) -> None:
		self._instance.TaskSuspend(taskName, createdBy)
	def write_ios(self, ios: typing.List[str], values: typing.List[float]) -> typing.List[PhysicalIoWriteResponse]:
		return [PhysicalIoWriteResponse(x) for x in self._instance.WriteIos(ios, values)]
	def load_project(self, projectPath: str) -> None:
		self._instance.LoadProject(projectPath)
	def forward_kinematics(self, robot: int, joints: typing.List[float]) -> IForwardKinematics:
		return IForwardKinematics(self._instance.ForwardKinematics(robot, joints))
	def reverse_kinematics(self, robot: int, joint: typing.List[float], target: Frame, config: Config, jointRange: JointRange) -> IReverseKinematics:
		return IReverseKinematics(self._instance.ReverseKinematics(robot, joint, target._instance, config._instance, jointRange._instance))
	def move_c(self, robot: int, frameB: Frame, frameC: Frame, mdesc: MotionDesc) -> IMoveResult:
		return IMoveResult(self._instance.MoveC(robot, frameB._instance, frameC._instance, mdesc._instance))
	def move_jc(self, robot: int, frame: Frame, mdesc: MotionDesc) -> IMoveResult:
		return IMoveResult(self._instance.MoveJC(robot, frame._instance, mdesc._instance))
	def move_jj(self, robot: int, joints: typing.List[float], mdesc: MotionDesc) -> IMoveResult:
		return IMoveResult(self._instance.MoveJJ(robot, joints, mdesc._instance))
	def move_l(self, robot: int, frame: Frame, mdesc: MotionDesc) -> IMoveResult:
		return IMoveResult(self._instance.MoveL(robot, frame._instance, mdesc._instance))
	def reset_motion(self) -> MotionReturnCode:
		return MotionReturnCode(self._instance.ResetMotion())
	def restart_motion(self) -> MotionReturnCode:
		return MotionReturnCode(self._instance.RestartMotion())
	def stop_motion(self) -> MotionReturnCode:
		return MotionReturnCode(self._instance.StopMotion())
	def set_power(self, power: bool) -> PowerReturnCode:
		return PowerReturnCode(self._instance.SetPower(power))
	@property
	def ip(self) -> str:
		return self._instance.Ip
	@property
	def port(self) -> int:
		return self._instance.Port
	@property
	def session_id(self) -> int:
		return self._instance.SessionId
	@property
	def enabled(self) -> bool:
		return self._instance.Enabled
