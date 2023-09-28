https://www.devbridge.com/articles/top-design-pattern-test-automation-frameworks/

## Design Pattern 
1. Structural pattern - explain how to assemble objects and classes into larger structures while keeping these structures flexible and efficient.
2. Creational pattern -provide various object creation mechanisms, which increase flexibility and reuse of existing code
3. Behaviour pattern -are concerned with algorithms and the assignment of responsibilities between objects.

## Structural pattern
### POM (Page Object Model)
* The pattern abstracts any page information away from the actual tests.

**Benefits**
* Reusability of page components 
* The pattern provides encapsulation and abstraction. Page objects encapsulate web elements, or other class members and provide access to wrapper methods that hide all the logic (i.e., the mechanics used to locate or change data).

**Key point to take care**
* preferably encapsulated web elements
* methods to operate with page object (page actions) and return other page objects by design
* no assertions should be used on page objects

**Sample Design**

## Decorator patterns
I think its PageFactory. And Python doesn't support page factory
Insight --> Implement CacheLoopup in pom also avoid stale reference execption

Note: Farz-So*y-Framework refer for lazy implementation -- similar to pagefactory

![pom](pom.PNG)

## Creational design patterns
### Factory method patterns
* This pattern defines an interface for creating an object but allows subclasses to decide which class to instantiate. Factory methods let a class defer instantiation to subclasses.

**Benefits**
* Having all objects initialization in a single place makes support much easier later (Single Responsibility Principle).
* The pattern is easily extendable without altering existing code (e.g., open/close principle).
* Scalability is easy to handle for tests runs **(e.g., using Selenium Grid/ Docker containers)**.

![factory_method](factory_method.PNG)

**Sample Code**
In that case, the Factory Method pattern can be applied to create instances of the WebDriver interface for different browsers.

Here's an updated example using the Factory Method pattern with the existing WebDriver interface in Selenium:

```java
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.safari.SafariDriver;

public class WebDriverFactory {
    public static WebDriver createWebDriver(String browserType) {
        switch (browserType.toLowerCase()) {
            case "chrome":
                return new ChromeDriver();
            case "firefox":
                return new FirefoxDriver();
            case "safari":
                return new SafariDriver();
            default:
                throw new IllegalArgumentException("Unsupported browser type: " + browserType);
        }
    }
}

public class TestAutomation {
    public static void main(String[] args) {
        // Create a ChromeDriver instance using the factory method
        WebDriver chromeDriver = WebDriverFactory.createWebDriver("chrome");

        // Use the WebDriver instance for test automation
        // ...
    }
}
```

In this updated example, we are utilizing the WebDriver interface provided by Selenium and implementing the factory method to create instances of different WebDriver implementations, such as ChromeDriver, FirefoxDriver, and SafariDriver, based on the specified browser type.

Using the Factory Method pattern in this way allows for flexible creation of WebDriver instances, enabling you to switch between different browsers without directly instantiating the specific driver classes. This promotes code maintainability and extensibility in Selenium automation projects.

### Builder Pattern
The Builder pattern is a creational design pattern that allows for the step-by-step construction of complex objects. It provides a way to construct objects by separating the construction logic from the object's representation, resulting in a more readable and flexible code.

Here's an example of the Builder pattern in Python:

```python
class Product:
    def __init__(self):
        self.name = None
        self.price = None
        self.quantity = None

    def __str__(self):
        return f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}"


class ProductBuilder:
    def __init__(self):
        self.product = Product()

    def set_name(self, name):
        self.product.name = name
        return self

    def set_price(self, price):
        self.product.price = price
        return self

    def set_quantity(self, quantity):
        self.product.quantity = quantity
        return self

    def build(self):
        return self.product


# Usage
builder = ProductBuilder()
product = builder.set_name("Example Product").set_price(10.99).set_quantity(5).build()
print(product)
```
 It promotes a fluent and step-by-step approach to object construction, improving the overall readability and reducing the complexity of object initialization.
 
**Is Fluent POM use Builder pattern**
The Fluent Page Object Model (POM) is an extension or variation of the traditional POM design pattern that incorporates the use of method chaining or a fluent interface for interacting with web elements. While it shares some similarities with the Builder pattern, the Fluent POM is not a strict implementation of the Builder pattern.
While the Fluent POM shares similarities with the Builder pattern in terms of method chaining, it does not involve the creation of complex objects step-by-step like the traditional Builder pattern. Instead, it focuses on providing a more fluent and concise way of interacting with web elements within the Page Object Model.

**Sample Code**
```
class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element("username_input_locator").send_keys(username)
        return self

    def enter_password(self, password):
        self.driver.find_element("password_input_locator").send_keys(password)
        return self

    def click_login_button(self):
        self.driver.find_element("login_button_locator").click()
        return HomePage(self.driver)


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def get_welcome_message(self):
        return self.driver.find_element("welcome_message_locator").text


# Usage
login_page = LoginPage(driver)
welcome_message = login_page.enter_username("user123").enter_password("pass123").click_login_button().get_welcome_message()
print(welcome_message)
```

### Singleton patterns
* There’s only one instance of an object. In most cases, the pattern is used for Logger, Connections, or External Resources. 
* Developers need a global access point to a class instance.

Singleton pattern to ensure that only one instance of the WebDriver is created and shared across the test cases. For example: TestSession.driver where driver is a static  

## Behavioral design patterns
### Strategy patterns
* This pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. Strategy patterns let the algorithm vary independently from the clients that use it.

**Benefits**
* Engineers have various algorithms to complete a task, and that can switch depending on the specific task at the run time. 
* Developers are able to easily add new strategies without altering the code (Open/Close principle).

For Example, My application has feature to create event and events can be create through UI and API(Rest Service). Now, I need to handle both with same interface name. Why I had to create event from API - Because I had to validate the event create from other sources are updated on my calendar. 

Certainly! Here's the same example of creating a calendar event using UI and API strategies, implemented in Java with the Strategy pattern:

1. Define the Strategy Interface:
   ```java
   public interface EventCreationStrategy {
       void createEvent(EventData eventData);
   }
   ```

2. Implement the UI Creation Strategy:
   ```java
   public class UICreationStrategy implements EventCreationStrategy {
       @Override
       public void createEvent(EventData eventData) {
           // Implement the UI-based event creation logic here
           // ...
           System.out.println("Created event using the UI");
       }
   }
   ```

3. Implement the API Creation Strategy:
   ```java
   public class APICreationStrategy implements EventCreationStrategy {
       @Override
       public void createEvent(EventData eventData) {
           // Implement the API-based event creation logic here
           // ...
           System.out.println("Created event using the API");
       }
   }
   ```

4. Create the Context Class:
   ```java
   public class EventCreationContext {
       private EventCreationStrategy creationStrategy;

       public EventCreationContext(EventCreationStrategy creationStrategy) {
           this.creationStrategy = creationStrategy;
       }

       public void createEvent(EventData eventData) {
           creationStrategy.createEvent(eventData);
       }
   }
   ```

5. Usage:
   ```java
   // Create event using the UI strategy
   EventCreationStrategy uiStrategy = new UICreationStrategy();
   EventCreationContext context = new EventCreationContext(uiStrategy);
   EventData eventDataUI = new EventData(); // Event data for UI creation
   context.createEvent(eventDataUI); // Output: Created event using the UI

   // Create event using the API strategy
   EventCreationStrategy apiStrategy = new APICreationStrategy();
   context = new EventCreationContext(apiStrategy);
   EventData eventDataAPI = new EventData(); // Event data for API creation
   context.createEvent(eventDataAPI); // Output: Created event using the API
   ```
