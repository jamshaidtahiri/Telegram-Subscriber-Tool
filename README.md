# Telegram Subscriber Tool 🚀

## Introduction
This is a Python-based Telegram Subscriber Tool designed to simplify the process of adding subscribers to a Telegram channel. The tool utilizes the Appium Python Client v2 to interact with the Telegram app on an Android device. With Appium's capabilities, the script automatically starts the Appium server, removing the need for users to manually set it up.

## Prerequisites
Before running the tool, make sure you have the following prerequisites installed on your system:

1. Python: Ensure you have Python installed on your machine. You can download Python from the official website: https://www.python.org/downloads/

2. Appium-Python-Client: Install the Appium Python Client by running the following command:
   ```
   pip install Appium-Python-Client
   ```

3. Appium Server: The Appium server should also be installed on your machine to facilitate the interaction with the Android device. The tool will automatically start the Appium server in the background, so you don't need to set it up manually.

4. Android Device: Connect an Android device to your computer with USB debugging enabled. Additionally, make sure the device has the Telegram app installed.

## Getting Started 🚀
1. Clone the repository or download the provided script onto your machine.

2. Open a terminal or command prompt and navigate to the directory containing the script.

3. Run the following command to start the Telegram Subscriber Tool:
   ```
   python telegram_subscriber_tool.py
   ```

## How it Works 🛠️
1. Upon executing the script, it automatically starts the Appium server in the background, so you don't need to worry about setting it up yourself.

2. A GUI window will pop up, prompting you to enter the name of your Telegram channel.

3. Enter the channel name (without '@') and click "Submit."

4. The script will launch the Telegram app on your connected Android device and search for the specified channel.

5. If the channel is found, it will open the channel and proceed to add subscribers.

6. The script reads a CSV file named "usernames.csv," which should contain a column labeled "username" with the usernames of the subscribers you want to add to the channel.

7. It iterates through the CSV file, searching for users matching the usernames and adding them as subscribers to the channel.

8. After successfully adding all subscribers, the script completes the process.

## Important Notes ❗
- Ensure that your Android device is properly connected, and USB debugging is enabled.

- Make sure the Appium server has sufficient time to start (approximately 10 seconds).

- The CSV file must be present in the same directory as the script, and the usernames should be listed under the "username" column.

## Creating the Executable 📦
I have already created an executable (`.exe`) file for you, so you don't need to do anything. The executable includes all the required dependencies, including the Appium-Python-Client, making it a standalone tool. You can simply run the `telegram_subscriber_tool.exe` file on your Windows machine without any additional setup.

## Conclusion 🎉
The Telegram Subscriber Tool automates the process of adding subscribers to your Telegram channel, making it faster and more convenient. With the integrated Appium server setup, you can now enjoy a hassle-free experience without worrying about any manual configurations. The tool simplifies the subscriber addition process, making it an ideal solution for Telegram channel administrators seeking to expand their audience effortlessly. Happy channel growth! 🚀🎊

If you have any questions or need further assistance, feel free to ask!
