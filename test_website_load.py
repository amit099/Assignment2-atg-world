from selenium import webdriver
import unittest

class TestWebsiteLoad(unittest.TestCase):
    def test_load_website(self):
        driver = webdriver.Chrome()
        driver.get("https://Q124FREYGBG23%40@hhfebhjgds/")
        self.assertIn("ATG - Access To Global", driver.title)
        driver.quit()
