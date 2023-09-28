1. `switch_to.frame(frame_reference)`
   - This method allows you to switch the focus of the Selenium WebDriver to a specific iframe on the page.
   - `frame_reference` can be a frame element, index (0-based), or frame name or ID.

2. `switch_to.parent_frame()`
   - Use this method to switch the focus back to the parent frame after interacting with an iframe.
   - It's useful when you are nested within multiple iframes.

3. `switch_to.default_content()`
   - This method switches the focus back to the default content of the page, i.e., outside all iframes.
   - Use it when you want to interact with elements outside of any iframes.

> Refer [iframe_example.py](iframe_example.py) file