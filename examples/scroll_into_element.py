from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("http://birdbank.pythonanywhere.com/")
element = driver.find_element(By.ID, "source")
driver.execute_script("arguments[0].scrollIntoView(true)",element)