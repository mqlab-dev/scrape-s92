import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent

import app.params


class LinkedInTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.options = Options()
        cls.user_agent = UserAgent()
        cls.options.add_argument(
            f'user-agent={cls.user_agent}')
        cls.driver = webdriver.Chrome(executable_path=app.params.driver_path, options=cls.options)

    def test_get_linkedin(self):
        self.driver.get('https://www.linkedin.com/')
        self.assertIn('LinkedIn: Log In or Sign Up', self.driver.title)

    def test_google_search(self):
        self.driver.get('https://www.google.com')
        search_query = self.driver.find_element_by_name('q')
        search_query.send_keys('hello world')
        search_query.send_keys(Keys.RETURN)
        self.assertEqual(self.driver.title, 'hello world - Google Search')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
