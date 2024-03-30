# Android App Automation Script

This script automates the testing process for a specific Android application, handling tasks such as installing the app, launching it, performing actions within the app, and uninstalling it afterwards. It utilizes tools like ADB (Android Debug Bridge), Androguard for APK analysis, and optionally UIAutomator for interacting with UI elements.

## Prerequisites

Before running the script, ensure you have the following installed and set up on your system:

- Python 3.x
- ADB (Android Debug Bridge) - part of the Android SDK Platform-Tools package
- Androguard
- An Android device or emulator connected and visible to ADB (use `adb devices` to check)

## Installation

1. **Install Python dependencies**:

    Open a terminal or command prompt and navigate to the project directory. Then run:

    pip install androguard


2. **Set up ADB**:

    Ensure ADB is installed and your device/emulator is connected. You can download ADB from the Android SDK Platform-Tools package available on the Android developer website.

3. **Prepare your device**:

    - Enable Developer Options on your Android device.
    - Enable USB Debugging within the Developer Options.

## Running the Script

1. **Modify the script**:

    Open the Python script in your favorite text editor or IDE, and modify the `apk_path` variable to point to the location of your APK file on your local system.

2. **Execute the script**:

    Navigate to your project directory in a terminal or command prompt window and run:

    python TaskAndroGuard.py


## Understanding the Output

- The script will print the package name, main activity, and other APK information to the console.
- It will install the APK on the connected device or emulator, launch it, perform specified actions (e.g., clicking the "SKIP" button), extract and save the UI layout, and finally, uninstall the app.
- The UI layout will be saved to a specified location on your local machine.

## Troubleshooting

- Ensure your device or emulator is correctly connected and visible to ADB by running `adb devices`.
- If the script fails to find the device or execute commands, check your ADB and USB Debugging setup.
- For issues related to Androguard or Python, ensure you have the correct versions installed and that your environment is set up correctly.



## Contact

[Maor Shiri] - [0545528704]

https://github.com/maor1614/PythonAndroTask



images of the project -

<img src="https://i.ibb.co/nrjyBqB/Screenshot-9.jpg" width="100" height="100">

