from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


class WebAuto: # class defining
    # Constructor method  initializes a new instance of the WebAuto class
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # Method to launch the web browser, navigate to the specified URL, and maximize
    def boot(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(5)
   #Method to get the title of the current webpage
    def get_title(self):
        return self.driver.title
    #Method to pause the execution for the specified number of seconds for viewing purpose
    def sleep(self, seconds):
        sleep(seconds)
    #Method to locate an input element on the webpage by name and input the provided text
    def inputBox(self, value, key):
        self.driver.find_element(by=By.NAME, value=value).send_keys(key)
        self.sleep(2)
    #Method to locate and click on the login button on the webpage
    def submitBtn(self):
        self.driver.find_element(by=By.NAME, value="login-button").click()
        self.sleep(2)
    #Method to close the web browser and terminate the WebDriver session
    def quit(self):
        self.driver.quit()
    #Method to perform the login action using  username and password and then clicking the login button
    def login(self):
        self.boot()
        self.inputBox("user-name", self.username)
        self.inputBox("password", self.password)
        self.submitBtn()
        return self.driver.current_url  # Return the URL after login
    #Method to save the entire contents of the webpage to a text file
    def save_page_content(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(self.driver.page_source)


# usuage
url = "https://www.saucedemo.com/" #web page url
obj = WebAuto(url, "standard_user", "secret_sauce") #creating a object
redirected_url = obj.login()  # Get the URL after login # through object accesing the login method
print("URL after login:", redirected_url)

# we can get the title of the webpage  and save the page content in text filr
print("Title of the webpage:", obj.get_title()) # through object we are accessing the title
filename = "Webpage_task_11.txt"
obj.save_page_content(filename)
print(f"Webpage content saved to '{filename}'")
# Closing WebDriver session
obj.quit()
