"""
Example: Read Physical IOs - Staubli Robot

This script demonstrates how to read physical I/O signals:
  1. Connect to a Staubli controller via SOAP
  2. Retrieve and display all available physical IOs
  3. Prompt the user to select an IO to read
  4. Display the IO value and state
  5. Loop to allow reading multiple IOs

Requirements:
  - A Staubli controller (or emulator) reachable at the specified IP address
  - The UnderAutomation.Staubli Python package installed

Usage:
  python example_read_ios.py
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
# 2. Retrieve all physical IOs
# ---------------------------------------------------------------------------
print("=" * 70)
print("ALL PHYSICAL IOs")
print("=" * 70)

all_ios = controller.soap.get_all_physical_ios()
print(f"\nFound {len(all_ios)} physical IO(s):\n")

# Display IOs in a table
print(f"  {'#':<4}  {'Name':<30}  {'Type':<10}  {'Description'}")
print(f"  {'-'*4}  {'-'*30}  {'-'*10}  {'-'*30}")

io_names = []
for i, io in enumerate(all_ios):
    io_names.append(io.name)
    desc = io.description if io.description else ""
    type_str = io.type_str if io.type_str else ""
    print(f"  {i:<4}  {io.name:<30}  {type_str:<10}  {desc}")

print()

# ---------------------------------------------------------------------------
# 3. Interactive loop: prompt user to read specific IO
# ---------------------------------------------------------------------------
print("=" * 70)
print("READ IO VALUE")
print("=" * 70)
print("\nEnter the IO name (or number) to read its value.")
print("Type 'quit' or 'q' to exit.\n")

while True:
    user_input = input("IO to read: ").strip()
    
    # Check for exit
    if user_input.lower() in ("quit", "q", "exit"):
        print("Exiting...")
        break
    
    # Determine the IO name
    io_name = None
    
    # Check if user entered a number (index)
    if user_input.isdigit():
        idx = int(user_input)
        if 0 <= idx < len(io_names):
            io_name = io_names[idx]
        else:
            print(f"  Invalid index. Please enter a number between 0 and {len(io_names) - 1}.")
            continue
    else:
        # User entered a name directly
        io_name = user_input
    
    # Read the IO value
    try:
        io_states = controller.soap.read_ios([io_name])
        
        if io_states and len(io_states) > 0:
            state = io_states[0]
            print(f"\n  IO Name   : {io_name}")
            print(f"  Value     : {state.value}")
            print(f"  State     : {state.state}")
            print(f"  Locked    : {state.locked}")
            print(f"  Simulated : {state.simulated}")
            print()
        else:
            print(f"  No state returned for IO '{io_name}'.\n")
    except Exception as e:
        print(f"  Error reading IO '{io_name}': {e}\n")

print("\nDone.")
