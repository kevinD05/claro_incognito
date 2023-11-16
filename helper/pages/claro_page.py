from selenium.webdriver.common.by import By

class pageclaro():

    btn_contact_us = (By.XPATH, '//a[@class="button btn-header is-small w-button"]')
    btn_cookies = (By.XPATH, '//button[@id="onetrust-accept-btn-handler"]')
    btn_solutions = (By.XPATH, '//*[@id="w-dropdown-toggle-1"]')
    btn_mpls = (By.XPATH, '//*[@id="w-dropdown-list-1"]/div/div/div/div[2]/div[2]/div/div/div/div[10]/a/div')
    delete = (By.XPATH, '//button[@id="onetrust-accept-btn-handler"]')
    btn_submit =(By.XPATH, '//input[@accesskey="s"]')
    first_name = (By.XPATH, '//*[@id="pardot-form"]/p[1]/label')