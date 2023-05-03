import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestFrames(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
       
        cls.driver = webdriver.Chrome()

    def test_i_frame(self):

        self.driver.get("https://the-internet.herokuapp.com/frames")


        iframe_link = self.driver.find_element(By.XPATH, "//a[contains(text(),'iFrame')]")
        iframe_link.click()


        iframe = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "mce_0_ifr"))
        )


        self.driver.switch_to.frame(iframe)


        body = self.driver.find_element(By.TAG_NAME, "body")
        body.send_keys("Hello, World!")


        self.driver.switch_to.default_content()


        iframe = self.driver.find_element(By.ID, "mce_0_ifr")
        self.driver.switch_to.frame(iframe)
        iframe_text = self.driver.find_element(By.ID, "tinymce").text
        expected_text = "Hello, World!"
        self.assertEqual(iframe_text, expected_text)

    def test_nested_frames(self):

        self.driver.get("https://the-internet.herokuapp.com/nested_frames")


        self.driver.switch_to.frame("frame-top")


        self.driver.switch_to.frame(0)


        element = self.driver.find_element(By.TAG_NAME, "body")
        text = element.text


        expected_text = "LEFT"
        self.assertEqual(text, expected_text)

    @classmethod
    def tearDownClass(cls):

        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()