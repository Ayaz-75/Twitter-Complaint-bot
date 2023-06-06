import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service



my_email = "your_email"
my_password = "your_password"



twitter_link = "https://twitter.com/"
chrome_driver_path = "D:\Development\chromedriver.exe"


s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
driver.get(twitter_link)


time.sleep(5)
signin_button = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div'
                                              '/div[3]/div[5]/a/div')
signin_button.click()


time.sleep(5)
email = driver.find_element(By.XPATH, '//input[@autocomplete="username"]')
email.send_keys(my_email)
email.send_keys(Keys.ENTER)

time.sleep(5)
password = driver.find_element(By.XPATH, '//input[@autocomplete="current-password"]')
password.send_keys(my_password)
password.send_keys(Keys.ENTER)



time.sleep(5)
click_tweet = driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/header/div/div/div/"
                                            "div[1]/div[3]/a")
click_tweet.click()



def get_quote():
    quote = f"@PTCLOfficial is the worst network like all network providers in Pakistan. Shame on all of you\n" \
            f"@Zongers\n" \
            f"@jazzpk\n" \
            f"@telenorpakistan"
    return quote


time.sleep(5)
tweet_text = driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-block')
tweet_text.send_keys(get_quote())
print(f"Tweet has been written successfully!")


time.sleep(5)
tweet_button = driver.find_element(By.XPATH, "//*[text()='Tweet']")
driver.execute_script("arguments[0].click();", tweet_button)
print(f"{tweet_button.text} has been sent successfully!")
















































