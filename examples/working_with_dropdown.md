![](https://github.com/naveens33/selenium_python/blob/master/images/dropdown.gif)

To handle dropdowns using Selenium WebDriver in Python, you can use the Select class from the selenium.webdriver.support.ui module

```
from selenium.webdriver.support.ui import Select 
```

Declare the drop-down element as an instance of the Select class

```
dropdown_element = driver.find_element(By.ID,"dropdown_id")
dropdown = Select(dropdown_element)
```
We created a Select object with the dropdown element, which allows us to select/deselect options using select_by_index, select_by_value, select_by_visible_text, and deselect_all methods.

### Select Methods:

* select_by_index(index) - Select the option at the given index counting

* select_by_value(value) - Select all options that have a value matching the argument

* select_by_visible_text(text) - Select all options that display text matching the argument 

> Refer [transfer_amount.py](transfer_amount.py) file
> Refer [working_with_single_select_dropdown.py](working_with_single_select_dropdown.py) file

## Working with multiselect dropdown

Working with multiselect dropdowns in Selenium involves a few steps. Here's an example of how you can interact with a multiselect dropdown using Selenium in Python:

> Refer [working_with_multi_select_dropdown.py](working_with_multi_select_dropdown.py) file

1. Import the necessary modules:
    ```
        from selenium import webdriver
        from selenium.webdriver.support.select import Select
        driver = webdriver.Chrome()
        driver.get('https://example.com')
    ```
2. Locate the multiselect dropdown element using a unique identifier, such as its ID, class, or XPath:
    ```
        dropdown = Select(driver.find_element_by_id('dropdown-id'))
    ```
3. Select options from the dropdown by value, index, or visible text:
    ```
        # Select options by value
    dropdown.select_by_value('value1')
    dropdown.select_by_value('value2')
    
    # Select options by index (0-based)
    dropdown.select_by_index(0)
    dropdown.select_by_index(1)
    
    # Select options by visible text
    dropdown.select_by_visible_text('Option 1')
    dropdown.select_by_visible_text('Option 2')
    ```
4. Deselect options if needed:
    ```
   # Deselect options by value
    dropdown.deselect_by_value('value1')
    
    # Deselect options by index
    dropdown.deselect_by_index(0)
    
    # Deselect options by visible text
    dropdown.deselect_by_visible_text('Option 1')
    ```
5. Get all available options in the dropdown:
    ```
    all_options = dropdown.options
    for option in all_options:
        print(option.text)
    ```
6. Check if an option is selected:
    ```
    is_selected = dropdown.first_selected_option.is_selected()
    print(is_selected)
   ```
7. Get the selected options:
    ```
    selected_options = dropdown.all_selected_options
    for option in selected_options:
        print(option.text)
   ```
8. Clear all selected options:
    ```
        dropdown.deselect_all()
    ```
9. Check if the dropdown supports multiple selection:
    ```
        is_multiple = dropdown.is_multiple
        print(is_multiple)
    ```

## Q&A:

### How to get all available options

options = select.options
