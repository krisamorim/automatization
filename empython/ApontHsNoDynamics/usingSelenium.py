# from selenium import webdriver
# driver = webdriver.Firefox(executable_path='C:\Program Files\SeleniumMozila\geckodriver.exe')
# driver.get("http://www.python.org")

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
service = webdriver.FirefoxService(executable_path=r'C:\Program Files\SeleniumMozila\geckodriver.exe')
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=service, options=options)
driver.get('https://linxprd.crm2.dynamics.com/main.aspx?pagetype=entitylist&etn=msdyn_workorder&viewid=63e0ccf4-8db5-e711-80f9-e0071b664ec1&viewType=1039&forceUCI=1&appid=0f6e740a-7a48-4536-872f-268ac257e0c7')
