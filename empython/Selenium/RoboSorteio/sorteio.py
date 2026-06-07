from selenium import webdriver
from time import sleep
import automatization.python.RoboSorteio.credntials as cred

service = webdriver.ChromeService()
options = webdriver.ChromeOptions()
brownser = webdriver.Chrome(service=service, options=options)
options.binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
options.add_argument('--enable-chrome-browser-cloud-management')

brownser.get('http://www.instagram.com.br')
sleep(10)
brownser.find_element('xpath', '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(cred.user)
brownser.find_element('name', 'password').send_keys(cred.xxx)
sleep(10)