from selenium import webdriver
import unittest

class TestWebsiteLoad(unittest.TestCase):
    def test_load_website(self):
        driver = webdriver.Chrome()
        driver.get("https://123")
        self.assertIn("ATG - Access To Global", driver.title)
        driver.quit()
