"""
Helper for the Staubli.py examples
- Import path of the package when the examples run from the sources
- Settings of the controller, saved in examples/robot_config.json
- License registration
- Connection
"""
import sys
import json
from pathlib import Path

# ==============================================================================
# Path setup for imports
# ==============================================================================
def setup_path():
    root = Path(__file__).parent.parent
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))

setup_path()

# ==============================================================================
# Configuration file
# ==============================================================================
_config_file = Path(__file__).parent / "robot_config.json"

def _load_config():
    """Load the saved settings."""
    if _config_file.exists():
        try:
            with open(_config_file, "r") as f:
                return json.load(f)
        except Exception:
            pass
    return {}

def _save_config(config):
    """Save the settings."""
    with open(_config_file, "w") as f:
        json.dump(config, f, indent=2)

def _get_setting(key, prompt, default=None, hide_default=False):
    """
    Ask a setting. The saved value, or the default, is proposed: press Enter to keep it.

    Args:
        key: key in the configuration file
        prompt: text shown to the user
        default: value when nothing is saved
        hide_default: show '****' instead of the saved value (passwords)

    Returns:
        str: the value
    """
    config = _load_config()
    saved = config.get(key, default)

    if saved is not None:
        display = "****" if hide_default and saved else saved
        user_input = input(f"{prompt} [{display}]: ").strip()
        value = user_input if user_input else saved
    else:
        value = input(f"{prompt}: ").strip()

    if value != config.get(key):
        config[key] = value
        _save_config(config)

    return value

# ==============================================================================
# Controller settings
# ==============================================================================
def get_robot_ip():
    """
    Address of the controller (IP or host name).
    The emulator of Staubli Robotics Suite usually answers on 127.0.0.1.
    """
    return _get_setting("robot_ip", "Controller IP address or host name", default="127.0.0.1")

def get_soap_user():
    """User of the SOAP server of the controller."""
    return _get_setting("soap_user", "SOAP user", default="default")

def get_soap_password():
    """Password of the SOAP server of the controller."""
    return _get_setting("soap_password", "SOAP password", default="default", hide_default=True)

def get_soap_port():
    """Port of the SOAP server of the controller, 851 by default."""
    raw = _get_setting("soap_port", "SOAP port", default="851")
    try:
        return int(str(raw).strip())
    except ValueError:
        return 851

# ==============================================================================
# License
# ==============================================================================
def setup_license():
    """
    Check the license state.

    - Licensed or in trial: print the license information.
    - Expired or invalid: ask for the licensee and the key, and register them.

    Returns:
        LicenseInfo: the license information
    """
    from underautomation.staubli.staubli_controller import StaubliController
    from underautomation.staubli.license.license_state import LicenseState

    config = _load_config()
    saved_licensee = config.get("licensee", "")
    saved_key = config.get("license_key", "")

    if saved_licensee and saved_key:
        license_info = StaubliController.register_license(saved_licensee, saved_key)
    else:
        license_info = StaubliController().license_info

    if license_info.state in (LicenseState.Licensed, LicenseState.Trial, LicenseState.ExtraTrial):
        print(f"License: {license_info}")
        return license_info

    print("=" * 60)
    print("LICENSE REGISTRATION REQUIRED")
    print("=" * 60)
    print(f"Current license state: {license_info}")
    print()
    print("If you have no license key, request a trial key at:")
    print("  https://underautomation.com/license?sdk=staubli")
    print()

    licensee = input("Licensee (company or name) [empty to skip]: ").strip()
    if not licensee:
        return license_info

    key = input("License key: ").strip()
    if not key:
        return license_info

    license_info = StaubliController.register_license(licensee, key)
    print(f"License: {license_info}")

    if license_info.state in (LicenseState.Licensed, LicenseState.Trial, LicenseState.ExtraTrial):
        config = _load_config()
        config["licensee"] = licensee
        config["license_key"] = key
        _save_config(config)

    return license_info

# ==============================================================================
# Connection
# ==============================================================================
def connect_robot():
    """
    Ask the settings of the controller, check the license and connect.

    Returns:
        StaubliController: a connected controller
    """
    from underautomation.staubli.staubli_controller import StaubliController
    from underautomation.staubli.connection_parameters import ConnectionParameters

    setup_license()

    parameters = ConnectionParameters(get_robot_ip())
    parameters.soap.user = get_soap_user()
    parameters.soap.password = get_soap_password()
    parameters.soap.port = get_soap_port()

    controller = StaubliController()
    controller.connect(parameters)
    print(f"Connected to {parameters.address}.\n")
    return controller

def print_title(title):
    """Print the title of an example."""
    print("=" * 60)
    print(title)
    print("=" * 60)
