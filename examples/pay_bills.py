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

# driver.find_element(By.XPATH,"//td[text()='TATA Mutual Fund iSIP']/following-sibling::td[last()]").click()

table = driver.find_element(By.XPATH,"//table")
tbody = table.find_element(By.XPATH,"tbody")

for tr in tbody.find_elements(By.XPATH,"tr"):
    for td in tr.find_elements(By.XPATH,"td"):
        if td.text == "TATA Mutual Fund iSIP":
            tr.find_element(By.XPATH, "td[last()]").click()
            break

wait = WebDriverWait(driver, 30)
wait.until(EC.invisibility_of_element_located((By.ID,"spinner")))
driver.find_element(By.ID,"confirm").click()

alert = driver.switch_to.alert
print(alert.text)
alert.accept()