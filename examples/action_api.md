In Selenium, the Action class provides a way to perform complex user interactions with the web page, such as mouse hover, drag and drop, double-click, etc. These actions can be performed using the ActionChains class, which is a part of the Selenium WebDriver API.

## Methods of Action 

* click()
* click_and_hold()
* context_click()
* double_click()
* drag_and_drop(source, target)
* drag_and_drop_by_offset(source, x_offset, y_offset)
* key_down(value), key_up(value)
* move_by_offset(x_offset, y_offset)
* move_to_element(target_element)
* move_to_element_with_offset(target_element, x_offset, y_offset)
* pause(seconds)
* perform()
* release()
* reset_actions()
* send_keys(keys_to_send)
* send_keys_to_element(element, keys_to_send)


> Refer [purchase_digital_gold.py](purchase_digital_gold.py) file