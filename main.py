# ------------------------imports-----------------------
from selenium import webdriver
from internetspeed import InternetSpeedTwitterBot
# ------------------------constants-----------------------


# ------------------------if the page crashes-----------------------
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
# ------------------------driver-----------------------



complaint_bot = InternetSpeedTwitterBot()
complaint_bot.get_internet_speed()
complaint_bot.tweet_at_provider()



