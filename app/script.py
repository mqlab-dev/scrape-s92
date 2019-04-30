from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
from fake_useragent import UserAgent

import params

user_agent = UserAgent()
options = Options()
options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(executable_path=params.driver_path, options=options)
driver.get('https://www.linkedin.com/uas/login?trk=guest_homepage-basic_nav-header-signin')

email = driver.find_element_by_id('username')
email.send_keys(params.linkedin_email)
sleep(0.5)

password = driver.find_element_by_id('password')
password.send_keys(params.linkedin_password)
sleep(0.5)

sign_in_button = driver.find_element_by_xpath('//*[@type="submit"]')
sign_in_button.click()
sleep(5)

# TODO: If not logged in, pause/stop the script.

for sq in params.search_queries[1:]:
    driver.get('https://www.google.com')
    driver.implicitly_wait(10)
    search_query = driver.find_element_by_name('q')

    search_query.send_keys(sq)
    sleep(5)

    search_query.send_keys(Keys.RETURN)
    sleep(3)

    linkedin_url_element = driver.find_elements_by_tag_name('cite')[0]
    linkedin_url = linkedin_url_element.text
    sleep(0.5)

    try:
        driver.get(linkedin_url)
        sleep(3)

        linkedin_btns_toggle = driver.find_element_by_class_name('pv-s-profile-actions__overflow-toggle')
        linkedin_btns_toggle.click()
        sleep(3)

        driver.find_element_by_xpath('//span[text()="Connect"]').click()
        sleep(3)

        driver.find_element_by_xpath('//button[text()="Done"]').click()
        sleep(3)

    except:
        pass

driver.close()
driver.quit()
