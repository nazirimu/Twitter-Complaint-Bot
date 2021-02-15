from selenium import webdriver
import time

# Twitter account set up
TWITTER_USERNAME = "USERNAME NOT INCLUDED. Add your own"
TWITTER_PASSWORD = "Passowrd not included. Add your own"

# PROMISED SPEEDS
PROMISED_DOWN = float(150)
PROMISED_UP = float(10)

# Selenium set up
chrome_driver_path = '/Users/shaznaz/Desktop/Web development/chromedriver'


# Internet speed class

class InternetSpeedTwitterBot:
    def __init__(self, path):
        self.down = 0
        self.up = 0
        self.driver = webdriver.Chrome(executable_path=path)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net")
        time.sleep(2)
        go_button = self.driver.find_element_by_css_selector(".start-button")
        go_button.click()
        time.sleep(100)
        upload = self.driver.find_element_by_css_selector(".upload-speed")
        self.up = float(upload.text)
        print(f'Upload: {upload.text}')
        download = self.driver.find_element_by_css_selector(".download-speed")
        self.down = float(download.text)
        print(f'Download: {download.text}')



    def tweet_at_provider(self):
        # Open the page
        self.driver.get("https://twitter.com/")
        time.sleep(2)

        # Pressing the log in button to open the login page
        sign_in_button = self.driver.find_element_by_link_text("Log in")
        sign_in_button.click()
        time.sleep(2)

        # Entering login info
        username_box = self.driver.find_element_by_css_selector('.r-1awozwy input')
        username_box.send_keys(TWITTER_USERNAME)
        password_box = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        password_box.send_keys(TWITTER_PASSWORD)
        login_button = self.driver.find_element_by_css_selector('.css-18t94o4')
        login_button.click()
        time.sleep(4)

        # Writing the tweet
        tweet_box = self.driver.find_element_by_css_selector(".public-DraftStyleDefault-ltr span")
        tweet_box.send_keys(
            f"Hey Internet Provider, why is my internet speed {self.down} down/ {self.up} up, when I am guaranteed {PROMISED_DOWN} down/ {PROMISED_UP} up?")
        tweet_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()

    


# Using the class
bot = InternetSpeedTwitterBot(chrome_driver_path)

bot.get_internet_speed()

if bot.up < PROMISED_UP or bot.down < PROMISED_DOWN:
    bot.tweet_at_provider()
else:
    print('All good! Nothing to report!')
