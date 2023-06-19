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

driver.find_element(By.LINK_TEXT, "LOANS").click()
driver.find_element(By.XPATH,'//*[@id="loan_sections_tab"]/div[1]/div/div/span').click()

doc_ele = driver.find_element(By.CSS_SELECTOR,"#basic")
doc =  Select(doc_ele)
doc.select_by_visible_text("License")
doc.select_by_visible_text("Pan card")

options = doc.all_selected_options
for option in options:
    print(option.text)

doc.deselect_by_visible_text("License")

doc.deselect_all()

print(doc.is_multiple)



