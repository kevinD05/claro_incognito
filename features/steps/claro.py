from behave import step
import os
import time
from helper.pages.claro_page import pageclaro
from selenium.webdriver import ActionChains
from helper.services.actions_basic import Basepage
from selenium.webdriver.common.by import By

@step(u'Ingresamos a la url "claro_url"')
def step_impl(context):
    url = os.getenv('Claro_url')
    context.browser.get(url)
    time.sleep(2)

@step(u'Aceptamos las cookies')
def step_impl(context):
    Basepage.click_button(context, pageclaro.btn_cookies)
    time.sleep(1)

@step(u'Damos click en el boton solutions y ingresamos a MPLS')
def step_impl(context):
    driver = context.browser
    solucion = driver.find_element(By.XPATH, '//*[@id="w-dropdown-toggle-1"]')
    actions = ActionChains(driver)
    actions.move_to_element(solucion).perform()
    time.sleep(1)
    Basepage.click_button(context, pageclaro.btn_mpls)
    time.sleep(2)


@step(u'Rellenaremos el formulario')
def step_impl(context):
    driver = context.browser
    driver.execute_script('window.scrollTo(0, document.documentElement.scrollHeight / 1.3);')
    time.sleep(2)
    driver.switch_to.frame(driver.find_element(By.XPATH, '//iframe[@id="form-usclaro"]'))
    time.sleep(2)
    firs_name = driver.find_element(By.XPATH, '//input[@name="1005782_419038pi_1005782_419038"]')
    firs_name.click()
    firs_name.send_keys('kevin')
    time.sleep(3)
    last_name = driver.find_element(By.XPATH, '//input[@name="1005782_419041pi_1005782_419041"]')
    last_name.click()
    last_name.send_keys('diaz')
    time.sleep(2)
    company_name = driver.find_element(By.XPATH, '//input[@name="1005782_419044pi_1005782_419044"]')
    company_name.click()
    company_name.send_keys('chester enterprise')
    time.sleep(1)
    email = driver.find_element(By.XPATH, '//input[@name="1005782_419047pi_1005782_419047"]')
    email.click()
    email.send_keys('kevin@gmail.com')
    time.sleep(1)
    phone_number = driver.find_element(By.XPATH, '//input[@name="1005782_419050pi_1005782_419050"]')
    phone_number.click()
    phone_number.send_keys('88523793')
    time.sleep(1)
    interested = driver.find_element(By.XPATH, '//select[@name="1005782_419053pi_1005782_419053"]')
    interested.click()
    time.sleep(1)
    business = driver.find_element(By.XPATH, '//option[@value="2541394"]')
    business.click()
    time.sleep(1)


@step(u'daremos click en el boton submit')
def step_impl(context):
    Basepage.click_button(context, pageclaro.btn_submit)
    time.sleep(1)

@step(u'validamos mensaje de error')
def step_impl(context): 
    error_message = context.browser.find_element(By.XPATH, '//p[text()="Invalid CAPTCHA"]')  
    assert "Mensaje de error esperado" in error_message.text, "El mensaje de error coincide con lo esperado"
    time.sleep(2)