from selenium import webdriver

driver = webdriver.Ie()
driver.get("http://birdbank.pythonanywhere.com/")

"""
New issue found on Selenium 4.9,
Exception 'internet explorer is not a valid browser' in IE after upgrading to 4.9.0

selenium.common.exceptions.SeleniumManagerException: Message: internet explorer is not a valid browser.  
Choose one of: ['chrome', 'firefox', 'edge', 'MicrosoftEdge', 'ie']

Refer issue: https://github.com/SeleniumHQ/selenium/issues/11928
"""
