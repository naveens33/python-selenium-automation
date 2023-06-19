If we want to perform any automated action on a web page, we need the locators from it to find it.

## Locate Elements Using Selenium Methods  

* Locate Element by Name
```
  element = driver.find_element(By.NAME, "element_name")
```
Example: 
```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://birdbank.pythonanywhere.com/")
login_button = driver.find_element(By.ID,"signin_button")
login_button.click()
# locating element using NAME
# loginpage -> username input field
username = driver.find_element(By.NAME, "username")
username.send_keys("testuser1")
```
* Locate Element by ID
```
  element = driver.find_element(By.ID, "element_id")
```
Example:
```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://birdbank.pythonanywhere.com/")
# locating element using ID
# homepage -> login button
login_button = driver.find_element(By.ID,"signin_button")
login_button.click()
```
* Locate Element by Link Text
```
  element = driver.find_element(By.LINK_TEXT, "element_link_text")
```
Example:
```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://birdbank.pythonanywhere.com/")
login_button = driver.find_element(By.ID,"signin_button")
login_button.click()
# locating element using LINK_TEXT
# loginpage -> forgot password link
forgot_password_link = driver.find_element(By.LINK_TEXT,"Forgot your password?")
forgot_password_link.click()

```
* Locate Element by Partial Link Text
```
  element = driver.find_element(By.PARTIAL_LINK_TEXT, "element_partial_link_text")
```
Example:
```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://birdbank.pythonanywhere.com/")
login_button = driver.find_element(By.ID,"signin_button")
login_button.click()
# locating element using PARTIAL_LINK_TEXT
# loginpage -> forgot password link
forgot_password_link = driver.find_element(By.PARTIAL_LINK_TEXT,"Forgot")
forgot_password_link.click()

```
* Locate Element by XPath
```
  element = find_element_by_xpath("element_xpath")
```
* Locate Element by CSS Selector
```
  element = driver.find_element(By.CSS_SELECTOR, "element_css_selector")
```
* Locate Element by Tagname
```
  element = driver.find_element(By.TAG_NAME, "element_tag_name")
```
Example:
```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://birdbank.pythonanywhere.com/")
login_button = driver.find_element(By.ID,"signin_button")
login_button.click()
# locating element using TAG_NAME
# loginpage -> login button
login_button = driver.find_element(By.TAG_NAME,"button")
login_button.click()
```
* Locate Element by Classname
```
  element = driver.find_element(By.CLASS_NAME,"element_class_name")
```
Example:
```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://birdbank.pythonanywhere.com/")
login_button = driver.find_element(By.ID,"signin_button")
login_button.click()
# locating element using CLASS_NAME
# loginpage -> virtual keyboard
virtual_keyboard = driver.find_element(By.CLASS_NAME,"far.fa-keyboard")
virtual_keyboard.click()
```
## Q&A:

### How to find multiple elements
To find multiple elements using Selenium, you can use find_elements method,

```
  element = driver.find_elements(By,locator)
```