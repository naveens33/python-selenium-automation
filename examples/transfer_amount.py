from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = Options()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("http://127.0.0.1:8000/")
login_button = driver.find_element(By.ID,"signin_button")
login_button.click()
username = driver.find_element(By.ID, "id_username")
username.send_keys("testuser1")
driver.find_element(By.ID, "id_password").send_keys("testpassword")
driver.find_element(By.ID,"signin").click()

driver.find_element(By.LINK_TEXT,"TRANSFER").click()
driver.find_element(By.ID, "ownacc").click()
driver.find_element(By.ID, "9999000453354527").click()
from_acc_element = driver.find_element(By.ID, "fromaccount")
from_acc_dropdown = Select(from_acc_element)
#from_acc_dropdown.select_by_index(3)
#from_acc_dropdown.select_by_value("530")
from_acc_dropdown.select_by_visible_text("9999000453354530")

to_acc_ele = driver.find_element(By.XPATH, '//*[@id="toaccount"]')
assert to_acc_ele.is_enabled() == False, "Element must be disabled"

driver.find_element(By.ID,"sd").send_keys(6000)
driver.find_element(By.ID,"message").send_keys("Loan Payment")
driver.find_element(By.ID,"confirm_payment").click()

assert driver.find_element(By.ID,"confirmationMessage").text == "Transaction Successful"

