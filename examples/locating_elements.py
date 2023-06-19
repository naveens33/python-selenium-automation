from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://birdbank.pythonanywhere.com/")

# locating element using ID
# homepage -> login button
login_button = driver.find_element(By.ID,"signin_button")
login_button.click()

# locating element using NAME
# loginpage -> username input field
username = driver.find_element(By.NAME, "username")
username.send_keys("testuser1")


# locating element using CLASS_NAME
# loginpage -> virtual keyboard
virtual_keyboard = driver.find_element(By.CLASS_NAME,"far.fa-keyboard")
virtual_keyboard.click()


# locating element using LINK_TEXT
# loginpage -> forgot password link
forgot_password_link = driver.find_element(By.LINK_TEXT,"Forgot your password?")
forgot_password_link.click()

# locating element using PARTIAL_LINK_TEXT
# loginpage -> forgot password link
forgot_password_link = driver.find_element(By.PARTIAL_LINK_TEXT,"Forgot")
forgot_password_link.click()


# locating element using TAG_NAME
# loginpage -> login button
login_button = driver.find_element(By.TAG_NAME,"button")
login_button.click()
