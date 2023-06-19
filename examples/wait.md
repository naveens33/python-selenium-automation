# Wait
Most of the web applications are developed using Ajax and Javascript. When a page is loaded by the browser the elements which we want to interact with may load at different time intervals. Not only it makes this difficult to identify the element but also if the element is not located it will throw an "NoSuchElementException" exception. Using Waits, we can resolve this problem.

In Selenium, "waits" are used to pause the execution of a script for a certain amount of time or until a certain condition is met. This is important in automating web applications as it allows the script to wait for elements to load before interacting with them. There are three types of waits in Selenium:

## Implicit Wait
An implicit wait when used is set to the WebDriver instance and is applied to all the web elements. In implicit wait the webdriver polls the DOM to check the availability of the webElement and waits till the maximum time specified before throwing NoSuchElementException.

```driver.implicitly_wait(10) # seconds```

## Explicit Wait: 
Unlike implicit waits, the explicit waits are applied to each and every webElement. In explicit wait, certain conditions are defined for which the webDriver instance waits before locating webElements or performing actions on them. Some of the most common conditions specified in explicit waits are- elementToBeClickable, presenceOfElementLocated etc.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://birdbank.pythonanywhere.com/")
wait=WebDriverWait(driver,10)
signin =wait.until(EC.visibility_of_element_located((By.ID,"signin_button")))
signin.click()
```
This waits up to 10 seconds before throwing a TimeoutException unless it finds the element to return within 10 seconds. WebDriverWait by default calls the ExpectedCondition every 500 milliseconds until it returns successfully. A successful return is for ExpectedCondition type is Boolean return true or not null return value for all other ExpectedCondition types.
## Fluent Wait
Fluent Wait is a more flexible wait that allows for a custom polling interval and ignore specific type of exception. It waits for a certain condition to be met within a certain time period.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import ElementNotVisibleException


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://birdbank.pythonanywhere.com/")
wait=WebDriverWait(driver,10, poll_frequency=3, ignored_exceptions=[ElementNotVisibleException])
signin =wait.until(EC.visibility_of_element_located((By.ID,"signin_button")))
signin.click()
```

## Expected Conditions
The expected_conditions module contains a set of predefined conditions to use with WebDriverWait.

```from selenium.webdriver.support import expected_conditions as EC```

Listed below are some of the methods.

* title_is
* title_contains
* presence_of_element_located
* visibility_of_element_located
* visibility_of
* presence_of_all_elements_located
* text_to_be_present_in_element
* text_to_be_present_in_element_value
* frame_to_be_available_and_switch_to_it
* invisibility_of_element_located
* element_to_be_clickable
* staleness_of
* element_to_be_selected
* element_located_to_be_selected
* element_selection_state_to_be
* element_located_selection_state_to_be
* alert_is_present

> Refer [purchase_foreign_currency.py](https://github.com/naveens33/selenium_python/blob/master/examples/purchase_foreign_currency.py)

## Q&A

## Difference between Implicit Wait Vs Explicit Wait

Implicit Wait

* Implicit Wait time is applied to all the elements in the script
* In Implicit Wait, we need not specify "ExpectedConditions" on the element to be located
* It is recommended to use when the elements are located with the time frame specified in implicit wait

Explicit Wait
* Explicit Wait time is applied only to those elements which are intended by us
* In Explicit Wait, we need to specify "ExpectedConditions" on the element to be located
* It is recommended to use when the elements are taking long time to load and also for verifying the property of the element like(visibility_of_element_located, element_to_be_clickable,element_to_be_selected)

## Difference between presence_of_element_located and visibility_of_element_located

presence_of_element_located - This method basically tests if the element we are looking for is present somewhere on the page.

visibility_of_element_located - This method looks for display: none. In visibility_of_element_located method element is first checked is present or not using presence_of_element_located method. Then try checking if the element is visible

Note: that presence_of_element_located won't mind even if our element is not visible.