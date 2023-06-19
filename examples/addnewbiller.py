from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("http://127.0.0.1:8000")
login_button = driver.find_element(By.ID, "signin_button")
login_button.click()
username = driver.find_element(By.ID, "id_username")
username.send_keys("testuser1")
driver.find_element(By.ID, "id_password").send_keys("testpassword")
driver.find_element(By.ID, "signin").click()

driver.find_element(By.LINK_TEXT, "PAY BILLS").click()
driver.find_element(By.CSS_SELECTOR, "button#add_payee").click()

"""
Unconditional wait
-----------------------
import time
time.sleep(30)
driver.find_element(By.XPATH, "//div[contains(text(),'Biller Name')]/following-sibling::div/input").send_keys(
    "Emily Johnson")
"""

"""
implicit wait
------------------------
driver.implicitly_wait(30)
driver.find_element(By.XPATH, "//div[contains(text(),'Biller Name')]/following-sibling::div/input").send_keys(
   "Emily Johnson")
"""

"""
explicit wait
------------------------
wait = WebDriverWait(driver, 30)
element = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                       "//div[contains(text(),'Biller Name')]/following-sibling::div/input")))
element.send_keys("Emily Johnson")
"""

wait = WebDriverWait(driver, 30, poll_frequency=5)
element = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                       "//div[contains(text(),'Biller Name')]/following-sibling::div/input")))
element.send_keys("Emily Johnson")
