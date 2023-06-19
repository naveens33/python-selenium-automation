from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://birdbank.pythonanywhere.com/")
login_button = driver.find_element(By.ID,"signin_button")
login_button.click()
username = driver.find_element(By.ID, "id_username")
username.send_keys("testuser1")
driver.find_element(By.ID, "id_password").send_keys("testpassword")
driver.find_element(By.ID,"signin").click()

driver.find_element(By.LINK_TEXT,"PURCHASE").click()
driver.find_element(By.XPATH,"(//span[text()='Order Now'])[2]").click()

source = driver.find_element(By.ID,"drag1")
target = driver.find_element(By.ID,"droppable")
action = ActionChains(driver)
action.drag_and_drop(source, target).perform()

source = driver.find_element(By.ID,"drag2")
target = driver.find_element(By.ID,"droppable")
action.drag_and_drop(source, target).perform()
