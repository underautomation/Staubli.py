"""
Example: Handle Applications - Staubli Robot

This script demonstrates how to manage VAL3 applications and tasks:
  1. Connect to a Staubli controller via SOAP
  2. List available applications (projects)
  3. Ask which project to load
  4. Start the application
  5. Wait for user to press ENTER to suspend the task (pause)
  6. Display task information
  7. Wait for user to press ENTER to resume the task
  8. Wait for user to press ENTER to finally kill the task

Requirements:
  - A Staubli controller (or emulator) reachable at the specified IP address
  - The UnderAutomation.Staubli Python package installed
  - At least one VAL3 application available on the controller

Usage:
  python example_applications.py
"""

import time
from underautomation.staubli.connection_parameters import ConnectionParameters
from underautomation.staubli.staubli_controller import StaubliController

# ---------------------------------------------------------------------------
# Helper function to display tasks
# ---------------------------------------------------------------------------
def display_tasks(controller):
    """Retrieve and display all running tasks."""
    tasks = controller.soap.get_tasks()
    if not tasks:
        print("  No tasks currently running.")
        return tasks
    
    print(f"\n  {'Name':<20}  {'State':<12}  {'Priority':<10}  {'Created By':<20}")
    print(f"  {'-'*20}  {'-'*12}  {'-'*10}  {'-'*20}")
    
    for task in tasks:
        print(f"  {task.name:<20}  {task.state!r:<12}  {task.priority:<10}  {task.created_by:<20}")
    
    return tasks

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
# 2. List available applications (projects)
# ---------------------------------------------------------------------------
print("=" * 70)
print("AVAILABLE APPLICATIONS")
print("=" * 70)


applications = controller.soap.get_val_applications()
print(f"\nFound {len(applications)} application(s):\n")

print(f"  {'#':<4}  {'Name':<30}  {'Loaded':<8}  {'Running':<8}  {'Encrypted'}")
print(f"  {'-'*4}  {'-'*30}  {'-'*8}  {'-'*8}  {'-'*10}")

app_names = []
for i, app in enumerate(applications):
    app_names.append(app.name)
    loaded = "Yes" if app.loaded else "No"
    running = "Yes" if app.is_running else "No"
    encrypted = "Yes" if app.is_crypted else "No"
    print(f"  {i:<4}  {app.name:<30}  {loaded:<8}  {running:<8}  {encrypted}")

print()

if not applications:
    print("No applications found. Exiting.")
    exit(0)

# ---------------------------------------------------------------------------
# 3. Ask which application to manage
# ---------------------------------------------------------------------------
print("=" * 70)
print("SELECT APPLICATION")
print("=" * 70)

while True:
    user_input = input("\nEnter application name or # (or 'quit' to exit): ").strip()
    
    if user_input.lower() in ("quit", "q", "exit"):
        print("Exiting...")
        exit(0)
    
    # Determine the application name
    app_name = None
    selected_app = None
    
    if user_input.isdigit():
        idx = int(user_input)
        if 0 <= idx < len(app_names):
            app_name = app_names[idx]
            selected_app = applications[idx]
        else:
            print(f"  Invalid index. Please enter a number between 0 and {len(app_names) - 1}.")
            continue
    else:
        app_name = user_input
        # Find the matching application object
        for app in applications:
            if app.name.lower() == app_name.lower():
                selected_app = app
                break
    
    break

# ---------------------------------------------------------------------------
# 4. Load and start only if not already running
# ---------------------------------------------------------------------------
if selected_app and selected_app.is_running:
    print(f"\n  Application '{app_name}' is already running. Skipping load & start.")
else:
    # Load the project
    print(f"\nLoading project '{app_name}'...")
    try:
        controller.soap.load_project(app_name)
        print(f"  Project '{app_name}' loaded successfully.")
    except Exception as e:
        print(f"  Error loading project: {e}")
        exit(1)

    # Start the application
    print(f"\nStarting application '{app_name}'...")
    try:
        controller.soap.start_application(app_name)
        print(f"  Application '{app_name}' started successfully.")
    except Exception as e:
        print(f"  Error starting application: {e}")
        exit(1)

    # Give the application a moment to start
    time.sleep(1)

# Display current tasks
print("\n--- Current Tasks ---")
tasks = display_tasks(controller)

# Find our task (the task name is usually the application name)
task_name = None
created_by = None
for task in tasks:
    if task.name.lower() == app_name.lower() or app_name.lower() in task.name.lower():
        task_name = task.name
        created_by = task.created_by
        break

if not task_name and tasks:
    # Use the first task if we can't find a match
    task_name = tasks[0].name
    created_by = tasks[0].created_by

if not task_name:
    print("\n  Could not identify the running task. Exiting.")
    exit(1)

print(f"\n  Selected task: '{task_name}' (created by: '{created_by}')")

# ---------------------------------------------------------------------------
# 6. Wait for user to suspend (pause) the task
# ---------------------------------------------------------------------------
print("\n" + "=" * 70)
print("TASK CONTROL")
print("=" * 70)

input("\nPress ENTER to SUSPEND (pause) the task...")

print(f"\nSuspending task '{task_name}'...")
try:
    controller.soap.task_suspend(task_name, created_by)
    print("  Task suspended.")
except Exception as e:
    print(f"  Error suspending task: {e}")

# Give it a moment
time.sleep(0.5)

# Display task info
print("\n--- Current Tasks (after suspend) ---")
tasks = display_tasks(controller)

# Show detailed task info
for task in tasks:
    if task.name == task_name:
        print(f"\n  Detailed info for task '{task_name}':")
        print(f"    State                  : {task.state!r}")
        print(f"    Priority               : {task.priority}")
        print(f"    Created By             : {task.created_by}")
        print(f"    Runtime Error          : {task.runtime_error}")
        print(f"    Runtime Error Desc     : {task.runtime_error_description}")
        break

# ---------------------------------------------------------------------------
# 7. Wait for user to resume the task
# ---------------------------------------------------------------------------
input("\nPress ENTER to RESUME the task...")

print(f"\nResuming task '{task_name}'...")
try:
    controller.soap.task_resume(task_name, created_by)
    print("  Task resumed.")
except Exception as e:
    print(f"  Error resuming task: {e}")

# Give it a moment
time.sleep(0.5)

# Display task info
print("\n--- Current Tasks (after resume) ---")
display_tasks(controller)

# ---------------------------------------------------------------------------
# 8. Wait for user to kill the task
# ---------------------------------------------------------------------------
input("\nPress ENTER to KILL the task...")

print(f"\nKilling task '{task_name}'...")
try:
    controller.soap.task_kill(task_name, created_by)
    print("  Task killed.")
except Exception as e:
    print(f"  Error killing task: {e}")

# Give it a moment  
time.sleep(0.5)

# Display final task list
print("\n--- Current Tasks (after kill) ---")
display_tasks(controller)

print("\nDone.")
