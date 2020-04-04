from WebLogin import WebLogin
from dotenv import load_dotenv, unset_key
import os
import base64
from selenium import webdriver

CURRENT_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--incognito')
chrome_options.add_argument('--user-agent=' + CURRENT_USER_AGENT)
chrome_options.add_argument('--ignore-ssl-errors=yes')
chrome_options.add_argument('--ignore-certificate-errors')

chrome_driver = None


def fetch_necessary_data():
    return os.getenv("URL"), {
        'username': os.getenv("USERNAME"),
        'password': base64.b64decode(os.getenv("PASS")).decode("ascii")
    }


def fetch_absence_data():
    return os.getenv("LOG_BOOK_URL"), {
        'clock_in': os.getenv("CLOCK_IN"),
        'clock_out': os.getenv("CLOCK_OUT"),
        'activity_title': os.getenv("ACTIVITY_TITLE"),
        'activity_detail': os.getenv("ACTIVITY_DETAIL")
    }


def prep_chrome_driver():
    global chrome_driver
    chrome_driver = webdriver.Chrome(chrome_options=chrome_options)


if __name__ == '__main__':
    load_dotenv(override=True)
    url, credential = fetch_necessary_data()
    prep_chrome_driver()
    web_login_instance = WebLogin(chrome_driver, url, credential)
    web_login_instance.login()
    url, absence = fetch_absence_data()
    web_login_instance.fill_log_book(url, absence)