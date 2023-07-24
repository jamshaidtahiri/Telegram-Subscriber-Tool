# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

import csv
import tkinter as tk
import subprocess
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from contextlib import contextmanager

# Function to start the Appium server
def start_appium_server():
    appium_cmd = "appium"
    subprocess.Popen(appium_cmd, shell=True)
    time.sleep(10)  # Give some time for the server to start
start_appium_server()

# Appium capabilities for the device
appium_capabilities = {
    "platformName": "Android",
    "appium:platformVersion": "13",
    "appium:automationName": "UiAutomator2",
    "appium:deviceName": "CPH2219",
    "appium:noReset": True,
    "appium:appPackage": "org.telegram.messenger",  # Package name of the Telegram app
    "appium:appActivity": "org.telegram.ui.LaunchActivity",  # Main activity of the Telegram app
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True,
}

@contextmanager
def appium_driver_context():
    driver = webdriver.Remote("http://127.0.0.1:4723", appium_capabilities)
    yield driver
    driver.quit()



# Function to find the element using explicit wait
def find_element(driver, locator_type, locator_value):
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located((locator_type, locator_value)))
    return element

def find_exact_match_channel_element(elements, username):
    for element in elements:
        text = element.text
        # Split the text by commas
        parts = text.split(',')
        # Check if the second part (index 1) is exactly equal to the current username
        if len(parts) >= 2 and parts[1].strip() == username:
            # If it matches, print the text and return the element
            print(text)
            return element
    return None
def find_exact_match_username_element(elements, username):
    for element in elements:
        text = element.text.lower()
        # Split the text by commas
        print(text)
        # Check if the second part (index 1) is exactly equal to the current username
        if text.strip() == username.strip():
            # If it matches, print the text and return the element
            print(text)
            return element
    return None

def click_element(element):
        if element:
            element.click()

# Global variable to store the channel name
# channel_name_var = tk.StringVar()

# Create a simple GUI to get the channel name
def get_channel_name():
    root = tk.Tk()
    root.title("Enter Channel Name")

    # Global variable to store the channel name
    channel_name_var = tk.StringVar()
    def on_submit():
        channel_name_var.set(entry.get().strip())
        root.destroy()

    
    label = tk.Label(root, text="Enter the channel name:")
    label.pack()
    entry = tk.Entry(root)
    entry.pack()
    submit_btn = tk.Button(root, text="Submit", command=on_submit)
    submit_btn.pack()
    root.mainloop()
    return channel_name_var.get()

    

# Perform some W3C actions
with appium_driver_context() as driver:

    el4 = find_element(driver, AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc=\"Search\"]/android.widget.ImageView")

    el4.click()
    # el5 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText")
    el5 = find_element(driver, AppiumBy.CLASS_NAME, "android.widget.EditText")

    # Call the get_channel_name function to start the GUI and get the channel name
    channelname = "@"+get_channel_name()
    # channelname = "@mjttest"
    el5.send_keys(channelname)

    # Find a specific element with an exact match for "@mjttest"

    el6 = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((AppiumBy.XPATH, "//android.view.ViewGroup[contains(@class, 'android.view.ViewGroup') ]")))
    # el6 = driver.find_elements(by=AppiumBy.XPATH, value="//android.view.ViewGroup[contains(@class, 'android.view.ViewGroup') ]")
    # el6 = find_element(driver, AppiumBy.XPATH, "//android.view.ViewGroup[contains(@class, 'android.view.ViewGroup') ]")\

    exact_match_element = find_exact_match_channel_element(el6, channelname)
    click_element(exact_match_element)

    # el7 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.FrameLayout[@content-desc]")
    el7 = find_element(driver, AppiumBy.XPATH, "//android.widget.FrameLayout[@content-desc]")

    el7.click()
    # el8 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[4]/android.widget.TextView[2]")

    el8 = find_element(driver, AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[4]/android.widget.TextView[2]")

    el8.click()
    # el9 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout[2]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.TextView")
    el9 = find_element(driver, AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout[2]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.TextView")

    el9.click()
    # el10 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText")

    el10 = find_element(driver, AppiumBy.CLASS_NAME, "android.widget.EditText")

    with open('usernames.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            username = row["username"].strip().lower()
            print(username) 
            if username:
                el10.send_keys(username)
                el11 = driver.find_elements(by=AppiumBy.XPATH, value="//android.widget.FrameLayout//android.widget.TextView[2]")
                exact_match_element = find_exact_match_username_element(el11, username.lower())
                click_element(exact_match_element)

    # el12 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Next")
    el12 = find_element(driver, AppiumBy.ACCESSIBILITY_ID, "Next")
    el12.click()
    
    # el13 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.TextView[2]")
    el13 = find_element(driver, AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.TextView[2]")
    el13.click()