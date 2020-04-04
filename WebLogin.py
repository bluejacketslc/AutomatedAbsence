from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class WebLogin:
    def __init__(self, driver, url, credential):
        self.driver = driver
        self.url = url
        self.credential = credential

    def login(self):
        self.driver.get(self.url)
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.TAG_NAME, "input")))

        self.driver.find_element_by_xpath("//input[@name='username']").send_keys(self.credential['username'])
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys(self.credential['password'])
        self.driver.find_element_by_xpath("//input[@value='Login']").send_keys(Keys.ENTER)

        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='pusher']")))

    def fill_log_book(self, url, absence):
        self.driver.get(url)

        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//button[@class='ui primary large button']")))

        self.driver.find_element_by_xpath("//input[@name='clock-in']").send_keys(absence['clock_in'])
        self.driver.find_element_by_xpath("//input[@name='clock-out']").send_keys(absence['clock_out'])
        self.driver.find_element_by_xpath("//input[@name='activity']").send_keys(absence['activity_title'])
        self.driver.find_element_by_xpath("//textarea[@name='description']").send_keys(absence['activity_detail'])

        self.driver.find_element_by_xpath("//button[@class='ui primary large button']").send_keys(Keys.ENTER)



