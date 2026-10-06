"""
Example: Send a VAL 3 application - Staubli Robot

This script sends a complete VAL 3 application from the PC to the controller, then loads it:
  1. Connect to a Staubli controller (SOAP and file client)
  2. List the applications in /usr/usrapp on the controller
  3. Ask the local folder of the application (named as the application, with its .pjx file inside)
  4. Stop and unload the applications in memory
  5. Copy the folder to /usr/usrapp/<application>. The previous version on the controller is replaced.
  6. Load the project and, if you want, start it

The VAL 3 applications are in /usr/usrapp on the controller, one sub-folder per application.
The file /usr/usrapp/myApp/myApp.pjx is the project "Disk://myApp/myApp.pjx" of the SOAP methods.

Requirements:
  - A Staubli controller with its FTP server, or the .controller file of a controller emulated by Staubli Robotics Suite.
    The address, the users and the passwords are asked once and saved in examples/robot_config.json
  - The UnderAutomation.Staubli Python package installed
  - The folder of a VAL 3 application on this PC

Usage:
  python examples/files/files_upload_application.py
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot, print_title

from underautomation.staubli.files.file_item_type import FileItemType

# ---------------------------------------------------------------------------
# 1. Connect with the file client
# ---------------------------------------------------------------------------
controller = connect_robot(files=True)

# ---------------------------------------------------------------------------
# 2. Applications on the controller
# ---------------------------------------------------------------------------
print_title("APPLICATIONS ON THE CONTROLLER (/usr/usrapp)")
for item in controller.file.get_listing("/usr/usrapp"):
    if item.type == FileItemType.Directory:
        print(f"  {item.name}")
print()

# ---------------------------------------------------------------------------
# 3. Local folder of the application
# ---------------------------------------------------------------------------
local_folder = input("Local folder of the application (for example C:\\MyApps\\myApp): ").strip().strip('"')
if not os.path.isdir(local_folder):
    print(f"The folder {local_folder} does not exist.")
    sys.exit(1)

name = os.path.basename(os.path.normpath(local_folder))
if not os.path.isfile(os.path.join(local_folder, name + ".pjx")):
    print(f"Warning: {name}.pjx is not in the folder. The project of a VAL 3 application has the name of its folder.")

if input(f"Replace /usr/usrapp/{name} on the controller? [y/N] ").strip().lower() != "y":
    sys.exit(0)

# ---------------------------------------------------------------------------
# 4. Stop and unload: the files of a loaded application cannot always be replaced
# ---------------------------------------------------------------------------
print("\nStopping and unloading the applications...")
controller.soap.stop_and_unload_all()

# ---------------------------------------------------------------------------
# 5. Send the application
# ---------------------------------------------------------------------------
def show_progress(progress):
    if progress >= 0:
        print(f"\r  Upload: {progress:5.1f} %", end="", flush=True)

remote_folder = controller.file.upload_application_to_controller(local_folder, show_progress)
print(f"\n  Sent to {remote_folder}")

# ---------------------------------------------------------------------------
# 6. Load and start
# ---------------------------------------------------------------------------
project = f"Disk://{name}/{name}.pjx"
print(f"\nLoading {project}...")
controller.soap.load_project(project)

if input("Start the application? It can move the arm. [y/N] ").strip().lower() == "y":
    controller.soap.start_application(project)
    print("  Started.")

controller.disconnect()
print("Done.")
