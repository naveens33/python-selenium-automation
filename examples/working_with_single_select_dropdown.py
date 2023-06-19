from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = Options()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://birdbank.pythonanywhere.com/")
source_ele = driver.find_element(By.ID,"source")
source = Select(source_ele)
# source.options -> all the option tag as a webelement
options = source.options
for option in options:
    print(option.text)

# first_selected_option -> get the selected option in the dropdown
option = source.first_selected_option
print(option.text)


