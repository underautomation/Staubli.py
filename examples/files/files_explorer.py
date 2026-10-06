"""
Example: Files explorer - Staubli Robot

Browse and manage the files of a Staubli controller from the console:
  - real controller: through the FTP server of the controller
  - controller emulated by Staubli Robotics Suite: give its .controller file as address (local path, or
    UNC path when SRS runs on another PC). The emulator has no FTP server: the files are in the folder of this file.
The paths are the same in both cases. The VAL 3 applications are in /usr/usrapp.

Commands:
  ls                    list the current folder
  cd <folder>           open a folder ("..": parent folder, "/": root)
  info <name>           information about a file or a folder
  get <name> [local]    download a file (to the current local folder by default)
  put <local>           upload a local file to the current folder
  mkdir <name>          create a folder
  mv <name> <new name>  rename a file or a folder
  rm <name>             delete a file, or a folder with all its content
  quit

Requirements:
  - A Staubli controller with its FTP server, or the .controller file of a controller emulated by Staubli Robotics Suite.
    The address, the users and the passwords are asked once and saved in examples/robot_config.json
  - The UnderAutomation.Staubli Python package installed

Usage:
  python examples/files/files_explorer.py
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot, print_title

import posixpath
import shlex

from underautomation.staubli.files.file_item_type import FileItemType

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def remote_path(current, name):
    """Path on the controller of a name typed by the user, relative to the current folder."""
    if name.startswith("/"):
        return posixpath.normpath(name)
    return posixpath.normpath(posixpath.join(current, name))

def show_listing(controller, folder):
    """Print the content of a folder of the controller, folders first."""
    items = list(controller.file.get_listing(folder))
    items.sort(key=lambda i: (i.type != FileItemType.Directory, i.name.lower()))
    print(f"\n  {folder}")
    for item in items:
        if item.type == FileItemType.Directory:
            print(f"    [DIR]  {item.name}")
        else:
            print(f"           {item.name:<40} {item.size:>10} bytes")
    print(f"  {len(items)} item(s)\n")

def show_progress(progress):
    """Called during the transfers with the percentage transferred."""
    if progress >= 0:
        print(f"\r  {progress:5.1f} %", end="", flush=True)

# ---------------------------------------------------------------------------
# 1. Connect with the file client
# ---------------------------------------------------------------------------
controller = connect_robot(files=True)

print_title("FILES EXPLORER")
print("Commands: ls, cd, info, get, put, mkdir, mv, rm, quit")

# ---------------------------------------------------------------------------
# 2. Command loop
# ---------------------------------------------------------------------------
current = "/usr/usrapp"
show_listing(controller, current)

while True:
    try:
        line = input(f"{current}> ").strip()
    except (EOFError, KeyboardInterrupt):
        break
    if not line:
        continue

    # posix=False keeps the backslashes of the Windows paths, quotes are removed by hand
    args = [a.strip('"') for a in shlex.split(line, posix=False)]
    command, args = args[0].lower(), args[1:]

    try:
        if command in ("quit", "exit", "q"):
            break

        elif command == "ls":
            show_listing(controller, current)

        elif command == "cd" and len(args) == 1:
            target = remote_path(current, args[0])
            if controller.file.directory_exists(target):
                current = target
                show_listing(controller, current)
            else:
                print(f"  No folder {target}")

        elif command == "info" and len(args) == 1:
            item = controller.file.get_file_info(remote_path(current, args[0]))
            if item is None:
                print("  Not found")
            else:
                print(f"  Full name : {item.full_name}")
                print(f"  Type      : {item.type.name}")
                print(f"  Size      : {item.size} bytes")
                print(f"  Modified  : {item.modified}")

        elif command == "get" and len(args) in (1, 2):
            source = remote_path(current, args[0])
            local = args[1] if len(args) == 2 else os.path.join(os.getcwd(), posixpath.basename(source))
            controller.file.download_file_from_controller(local, source, show_progress)
            print(f"\n  Downloaded to {local}")

        elif command == "put" and len(args) == 1:
            target = remote_path(current, os.path.basename(args[0]))
            controller.file.upload_file_to_controller(args[0], target, False, show_progress)
            print(f"\n  Uploaded to {target}")

        elif command == "mkdir" and len(args) == 1:
            controller.file.create_directory(remote_path(current, args[0]))
            show_listing(controller, current)

        elif command == "mv" and len(args) == 2:
            controller.file.rename(remote_path(current, args[0]), remote_path(current, args[1]))
            show_listing(controller, current)

        elif command == "rm" and len(args) == 1:
            target = remote_path(current, args[0])
            item = controller.file.get_file_info(target)
            if item is None:
                print("  Not found")
            elif input(f"  Delete {target}? [y/N] ").strip().lower() == "y":
                if item.type == FileItemType.Directory:
                    controller.file.delete_directory(target)
                else:
                    controller.file.delete_file(target)
                show_listing(controller, current)

        else:
            print("  Unknown command or wrong arguments")

    except Exception as e:
        # FileException (refused by the controller, file not found...) and local errors
        print(f"\n  Error: {e}")

controller.disconnect()
print("Done.")
