## Files of the controller

New file client `controller.file`, and standalone `FileClient`: list, upload, download, create, rename and delete the files and folders of the controller. Errors raise a `FileException`.

- Real controller: the client uses the FTP server of the controller. Set `parameters.file.enable = True`, and the FTP user and password (`default` and `default` by default, port 21).
- Controller emulated by Staubli Robotics Suite: the emulator has no FTP server. Give the path of the `.controller` file of the emulated controller as address: the client reads and writes the files in the folder of this file, which has the same tree as the FTP server of a real controller. The paths are the same.

```python
parameters = ConnectionParameters("192.168.0.254")  # or r"C:\...\MyCell\Controller1\Controller1.controller"
parameters.file.enable = True
parameters.file.user = "default"
parameters.file.password = "default"

controller = StaubliController()
controller.connect(parameters)

for item in controller.file.get_listing("/usr/usrapp"):
    print(item.full_name, item.type, item.size)

controller.file.upload_file_to_controller(r"C:\Data\points.dat", "/usr/usrapp/myApp/points.dat")
content = controller.file.download_bytes_from_controller("/usr/usrapp/myApp/myApp.pjx")
```

The `file.enable` parameter is `False` by default: the connection of existing scripts does not change.

## Send a VAL 3 application

`upload_application_to_controller(local_app_folder)` copies the folder of a VAL 3 application, with its sub-folders, to `/usr/usrapp/<application>` on the controller. When the application exists on the controller, its folder is replaced. The VAL 3 applications are in `/usr/usrapp` (`FileClientBase.USER_APP_FOLDER`), and `/usr/usrapp/myApp/myApp.pjx` is the project `Disk://myApp/myApp.pjx` of the SOAP methods.

```python
controller.soap.stop_and_unload_all()
controller.file.upload_application_to_controller(r"C:\MyApps\myApp")
controller.soap.load_project("Disk://myApp/myApp.pjx")
```

## Connection to the emulator of Staubli Robotics Suite

- The address can be the path of the `.controller` file of a controller emulated by Staubli Robotics Suite. The SDK connects to this computer, or to the computer of a UNC path. A path that is not a `.controller` file raises an `ArgumentException`.
- The default SOAP port is now `0` (automatic). On a real controller, the SDK uses 851, as before. On an emulated controller, it reads the SOAP port in the network configuration of the emulated controller (`usr\configs\network.cfx`), and uses 851 when it is not found. When 851 was used as a fallback and the connection fails, the message of the exception says it.
- `SoapClient.connect` accepts the same addresses and the port 0.

```python
controller = StaubliController()
controller.connect(r"C:\Users\me\Documents\Staubli\SRS\MyCell\Controller1\Controller1.controller")
print(controller.soap.port)  # port of the emulated controller
```
