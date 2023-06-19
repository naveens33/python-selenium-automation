from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = Options()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("http://birdbank.pythonanywhere.com/")
login_button = driver.find_element(By.ID,"signin_button")
login_button.click()
username = driver.find_element(By.ID, "id_username")
username.send_keys("testuser1")
driver.find_element(By.ID, "id_password").send_keys("testpassword")
driver.find_element(By.ID,"signin").click()

driver.find_element(By.LINK_TEXT,"HELP").click()
driver.find_element(By.ID,"submit").click()

alert = driver.switch_to.alert
print(alert.text)
#alert.dismiss()
alert.accept()