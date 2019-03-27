from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

import params

driver = webdriver.Chrome(params.driver_path)
driver.get('https://www.linkedin.com/')

email = driver.find_element_by_id('login-email')
email.send_keys(params.linkedin_email)
sleep(0.5)

password = driver.find_element_by_id('login-password')
password.send_keys(params.linkedin_password)
sleep(0.5)

sign_in_button = driver.find_element_by_xpath('//*[@type="submit"]')
sign_in_button.click()
sleep(5)

driver.get('https://www.google.com')
sleep(3)

search_query = driver.find_element_by_name('q')
search_query.send_keys(params.search_query)
sleep(0.5)

search_query.send_keys(Keys.RETURN)
sleep(3)

linkedin_urls = driver.find_elements_by_tag_name('cite')
linkedin_urls_clean = [url.text for url in linkedin_urls]
sleep(0.5)

for linkedin_url in linkedin_urls_clean:
    try:
        driver.get(linkedin_url)
        sleep(3)

        linkedin_btns_toggle = driver.find_element_by_class_name('pv-s-profile-actions__overflow-toggle')
        linkedin_btns_toggle.click()
        sleep(3)

        driver.find_element_by_xpath('//span[text()="Connect"]').click()
        sleep(3)

        driver.find_element_by_xpath('//button[text()="Send now"]').click()
        sleep(3)

    except:
        pass


driver.quit()
