from dotenv import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options



def environment_load(context):
    load_dotenv()
    config = dotenv_values(find_dotenv())
    for key, value in config.items():
        setattr(context, key, value)

def before_all(context):
    environment_load(context)

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    
    context.browser = webdriver.Chrome(options=chrome_options)    
    print("Se está ejecutando la prueba con Selenium")

def after_all(context):
    print("Se ejecuto Correctamente la prueba!")
