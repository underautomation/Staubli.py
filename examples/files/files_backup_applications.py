"""
Example: Back up the VAL 3 applications - Staubli Robot

This script copies all the VAL 3 applications of the controller to a folder of the PC:
  1. Connect to a Staubli controller (file client only)
  2. Walk through /usr/usrapp and its sub-folders
  3. Download each file to backup_<date>/<application>/... on the PC

Requirements:
  - A Staubli controller with its FTP server, or the .controller file of a controller emulated by Staubli Robotics Suite.
    The address, the users and the passwords are asked once and saved in examples/robot_config.json
  - The UnderAutomation.Staubli Python package installed

Usage:
  python examples/files/files_backup_applications.py
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot, print_title

import datetime
import posixpath

from underautomation.staubli.files.file_item_type import FileItemType

# ---------------------------------------------------------------------------
# 1. Connect with the file client
# ---------------------------------------------------------------------------
controller = connect_robot(files=True)

backup_folder = os.path.abspath(f"backup_{datetime.datetime.now():%Y%m%d_%H%M%S}")
print_title(f"BACKUP OF /usr/usrapp TO {backup_folder}")

# ---------------------------------------------------------------------------
# 2. and 3. Walk through the folders and download the files
# ---------------------------------------------------------------------------
count = 0
total_size = 0

def backup(remote_folder, local_folder):
    """Download the files of a folder of the controller, then its sub-folders."""
    global count, total_size
    os.makedirs(local_folder, exist_ok=True)

    for item in controller.file.get_listing(remote_folder):
        remote = posixpath.join(remote_folder, item.name)
        local = os.path.join(local_folder, item.name)

        if item.type == FileItemType.Directory:
            backup(remote, local)
        else:
            controller.file.download_file_from_controller(local, remote)
            count += 1
            total_size += item.size
            print(f"  {remote}")

backup("/usr/usrapp", backup_folder)

print(f"\n{count} file(s), {total_size} bytes, in {backup_folder}")

controller.disconnect()
print("Done.")
