from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = Options()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://birdbank.pythonanywhere.com/")
signin_button = driver.find_element(By.ID, "signin_button")
signin_button.click()
assert "Login - Internet Banking" == driver.title, "Title is incorrect"
driver.find_element(By.ID, "id_username").send_keys("testuser1")
driver.find_element(By.NAME, "password").send_keys("testpassword")
driver.find_element(By.ID, "signin").click()
assert "My Accounts - Bird Bank" == driver.title, "Title is incorrect"

driver.find_element(By.LINK_TEXT,"LOANS").click()
driver.find_element(By.XPATH,"//h5[text()='Personal Loan']/following-sibling::span").click()

driver.find_element(By.ID,"name").send_keys("Naveen")
driver.find_element(By.ID,"email").send_keys("Naveen@gmail.com")
driver.find_element(By.ID,"mobile").send_keys("48326584622")

ele = driver.find_element(By.ID,"basic")
proof_selection = Select(ele)
proof_selection.select_by_visible_text("Aadhar card")
proof_selection.select_by_visible_text("Pan card")

driver.find_element(By.ID,"myFile").send_keys(r"C:\Users\Naveen S\Pictures\execution_plan.png")

checkbox = driver.find_element(By.XPATH,'//input[@type="checkbox"]')
if not checkbox.is_selected():
    checkbox.click()
