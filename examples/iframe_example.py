from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

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

driver.find_element(By.LINK_TEXT,"LOANS").click()
driver.find_element(By.XPATH,"//div[@id='loan_sections_tab']/div[1]//span").click()

iframe_ele = driver.find_element(By.TAG_NAME,"iframe")
driver.switch_to.frame(iframe_ele)
print(driver.find_element(By.XPATH,"//*[text()='ctreport-selenium']").text)