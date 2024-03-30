from androguard.misc import AnalyzeAPK
import subprocess
import time

# modify the `apk_path` variable to point to the location of your APK file on your local system.
apk_path = "C:\\Users\\maors\\PycharmProjects\\AppiumSandbox\\pythonProject\\Physics Toolbox Sensor Suite_2024.03.03_apkcombo.com.apk"

app, _, _ = AnalyzeAPK(apk_path)

# Get the AndroidManifest.xml as an object
android_ns = '{http://schemas.android.com/apk/res/android}'

manifest = app.get_android_manifest_axml().get_xml_obj()
# Print package name
print("Package name:", app.get_package())

# Print main activity
print("Main activity:", app.get_main_activity())

# List all activities
activities = app.get_activities()
print("Activities:", activities)

# Iterate over all activities
for activity in manifest.findall(".//activity"):
    activity_name = activity.get(f"{android_ns}name")
    print(f"Activity: {activity_name}")

    # For each activity, find intent-filter tags
    for intent_filter in activity.findall('intent-filter'):
        print("  Intent Filter:")

        # Actions
        for action in intent_filter.findall('action'):
            print(f"    Action: {action.get(f'{android_ns}name')}")

        # Categories
        for category in intent_filter.findall('category'):
            print(f"    Category: {category.get(f'{android_ns}name')}")

        # Data
        for data in intent_filter.findall('data'):
            print(
                f"    Data: {data.get(f'{android_ns}scheme')}://{data.get(f'{android_ns}host')}{data.get(f'{android_ns}path')}")

        print("  ----")

# Install the app
subprocess.run(["adb", "install", apk_path], check=True)

# Launch the app
launch_command = f"adb shell am start -n {app.get_package()}/{app.get_main_activity()}"
subprocess.run(launch_command.split(), check=True)

# Command to press the Skip button using its resource-id
skip_button_resource_id = "com.chrystianvieyra.physicstoolboxsuite:id/skip"
click_skip_command = f"adb shell input keyevent KEYCODE_TAB && adb shell input keyevent KEYCODE_ENTER"
# The above command assumes the Skip button can be selected with a Tab key press and activated with the Enter key.
# This might not always work depending on the app's UI layout and how it handles focus navigation.


click_skip_command_uiautomator = (f"adb shell uiautomator runtest AppUIAutomation.jar -c "
                                  f"com.example.tests.UiAutomator#clickById {skip_button_resource_id}")

# Running the command to press the "Skip" button
subprocess.run(["adb", "shell", "input", "keyevent", "KEYCODE_TAB"], check=True)
subprocess.run(["adb", "shell", "input", "keyevent", "KEYCODE_ENTER"], check=True)

# Running the command to press done Button
done_button_resource_id = "com.chrystianvieyra.physicstoolboxsuite:id/done"
click_done_command = f"adb shell input keyevent KEYCODE_TAB && adb shell input keyevent KEYCODE_ENTER"
click_done_command_uiautomator = (f"adb shell uiautomator runtest AppUIAutomation.jar -c "
                                  f"com.example.tests.UiAutomator#clickById {done_button_resource_id}")
subprocess.run(["adb", "shell", "input", "keyevent", "KEYCODE_TAB"], check=True)
subprocess.run(["adb", "shell", "input", "keyevent", "KEYCODE_ENTER"], check=True)

# Extract UI Layout
device_xml_path = "/sdcard/window_dump.xml"

# modify the `local_xml_path` variable to point to the location of your APK file on your local system.
local_xml_path = "C:\\users\\maors\\PycharmProjects\\AppiumSandbox\\pythonProject\\ui_layout.xml"

subprocess.run(["adb", "shell", "uiautomator", "dump", device_xml_path], check=True)
time.sleep(2)  # Give time for the dump to complete
subprocess.run(["adb", "pull", device_xml_path, local_xml_path], check=True)
print(f"UI layout saved to {local_xml_path}")

# Wait for 13 seconds
time.sleep(13)

# Stop the app
subprocess.run(f"adb shell am force-stop {app.get_package()}".split(), check=True)

# Uninstall the app
subprocess.run(["adb", "uninstall", app.get_package()], check=True)

print("Completed automation tasks.")
