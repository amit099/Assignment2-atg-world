import unittest
from selenium import webdriver

class TestWebsiteLoad(unittest.TestCase):
    # Define a method to test website loading
    def test_load_website(self):
        driver = webdriver.Chrome() # Use any browser driver of your choice.
        driver.get("https://atg.world/")
        driver.quit()

