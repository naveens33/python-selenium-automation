Selenium WebDriver - WebElement methods

* clear() 
```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://birdbank.pythonanywhere.com/")
login_button = driver.find_element(By.ID,"signin_button")
login_button.click()
username = driver.find_element(By.NAME, "username")
# clear() - clear method is used to clear text in input field
username.clear()
username.send_keys("testuser1")
```
* click()
```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://birdbank.pythonanywhere.com/")
login_button = driver.find_element(By.ID,"signin_button")
# click() -  click method is used to click on any web element
login_button.click()
```
* send_keys()
```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://birdbank.pythonanywhere.com/")
login_button = driver.find_element(By.ID,"signin_button")
login_button.click()
username = driver.find_element(By.NAME, "username")
# send_keys() - send_keys method is used to send text to any field
username.send_keys("testuser1")
```