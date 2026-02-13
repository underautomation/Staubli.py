"""
Example: Write Physical IOs - Staubli Robot

This script demonstrates how to write physical I/O signals:
  1. Connect to a Staubli controller via SOAP
  2. Retrieve and display all available physical IOs
  3. Prompt the user to select an IO to write
  4. Prompt for the value to write
  5. Write the value and display the result
  6. Loop to allow writing multiple IOs

Requirements:
  - A Staubli controller (or emulator) reachable at the specified IP address
  - The UnderAutomation.Staubli Python package installed

Usage:
  python example_write_ios.py
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
print(f"  {'#':<4}  {'Name':<30}  {'Type':<10}  {'Lockable':<10}  {'Description'}")
print(f"  {'-'*4}  {'-'*30}  {'-'*10}  {'-'*10}  {'-'*30}")

io_names = []
for i, io in enumerate(all_ios):
    io_names.append(io.name)
    desc = io.description if io.description else ""
    type_str = io.type_str if io.type_str else ""
    lockable = "Yes" if io.lockable else "No"
    print(f"  {i:<4}  {io.name:<30}  {type_str:<10}  {lockable:<10}  {desc}")

print()

# ---------------------------------------------------------------------------
# 3. Interactive loop: prompt user to write specific IO
# ---------------------------------------------------------------------------
print("=" * 70)
print("WRITE IO VALUE")
print("=" * 70)
print("\nEnter the IO name (or number) to write a value.")
print("Type 'quit' or 'q' to exit.\n")

while True:
    user_input = input("IO to write: ").strip()
    
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
    
    # Prompt for the value
    value_input = input(f"Value to write to '{io_name}': ").strip()
    
    try:
        value = float(value_input)
    except ValueError:
        print(f"  Invalid value '{value_input}'. Please enter a numeric value.\n")
        continue
    
    # Write the IO value
    try:
        responses = controller.soap.write_ios([io_name], [value])
        
        if responses and len(responses) > 0:
            response = responses[0]
            print(f"\n  IO Name  : {io_name}")
            print(f"  Value    : {value}")
            print(f"  Found    : {response.found}")
            print(f"  Success  : {response.success}")
            
            if response.success:
                print("  --> Write successful!")
            else:
                if not response.found:
                    print("  --> IO not found.")
                else:
                    print("  --> Write failed (check IO permissions or mode).")
            print()
        else:
            print(f"  No response for IO '{io_name}'.\n")
    except Exception as e:
        print(f"  Error writing IO '{io_name}': {e}\n")

print("\nDone.")
