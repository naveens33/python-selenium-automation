# List of supported browsers

|Browser|Supported OS|
|-------|---------------|
|Chromium/Chrome|	Windows/macOS/Linux|
|Firefox|	Windows/macOS/Linux	Mozilla|
|Edge|	Windows/macOS/Linux	Microsoft|
|Internet Explorer|	Windows|
|Safari|	macOS|

## Drivers
In Selenium, a driver is a software component that facilitates the communication between the Selenium framework and the browser. It acts as a bridge between the automated test script and the browser.

Selenium supports multiple web browsers, such as Chrome, Firefox, Safari, and Internet Explorer. Each browser requires a specific driver to interact with Selenium. For example, to automate Chrome browser using Selenium, you need to download and install the ChromeDriver.

The driver interacts with the browser through the browser's native support for automation. For example, ChromeDriver uses Chrome's DevTools protocol to interact with the browser. The driver sends commands to the browser and retrieves information from it. The commands can be used to simulate user actions like clicking, typing, and navigating through pages. The driver also retrieves information from the browser such as page source, cookies, and window handles.

### Install browser driver
After Selenium v4.6 the way of installation of driver has been changed,

Selenium has introduced Selenium Manager. So, we don't want to manage any executable driver file rather selenium will take care.

Selenium Manager provides a robust mechanism (inherited from WebDriverManager) to detect the version of the local browser to be controlled with Selenium WebDriver, download the proper driver, and make it available for Selenium WebDriver

## Chrome Options
Chrome options are command-line arguments that can be passed to the Google Chrome browser when it is launched. These options modify the behavior of Chrome and can be used to customize how the browser runs.

Mostly commonly used chrome options are,

1. `--headless`: This option runs Chrome in headless mode, which means that it runs without a graphical user interface (GUI). This can be useful for running tests on servers or other systems that do not have a GUI.
2. `--start-maximized`: This option is used to start the Google Chrome browser with the window fully maximized.
3. `--incognito`: This option starts Chrome in incognito mode, which means that it does not save any browsing history or cookies.
4. `--disable-infobars`: This option disables the yellow information bar that appears at the top of the Chrome window when a site tries to install an extension or use a pop-up window.

## Dec 17, 2022 Browser closes automatically
A while ago, I encountered a new and unusual feature of Selenium. Even when the driver.quit() command is absent, the browser automatically closes after running tests with Python. 

Initially, I tolerated this feature and resorted to adding time delays for a minute. However, I eventually decided to investigate how to manage it properly.

As it turns out, this feature was intentionally added so that the system returns to its previous state after the program ends. But the good news is that you don't have to accept it as is. You can still keep your browser open by providing experimental option called "detach." 

[ChromeOptions - Detach](https://sites.google.com/a/chromium.org/chromedriver/capabilities#:~:text=directory%20for%20examples.-,detach,-boolean)
```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
```
```python
from selenium import webdriver
from selenium.webdriver.edge.options import Options
options = Options()
options.add_experimental_option('detach', True)
driver =  webdriver.Edge(options=options)
```
[click here](stop_chromedriver_kill.py)

