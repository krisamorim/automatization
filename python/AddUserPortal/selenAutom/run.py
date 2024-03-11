import os
root = os.getcwd()
pathComplet = os.path.join(os.getcwd(),'Milium','selenAutom')
os.chdir(root)
print(pathComplet)

file = pathComplet+r'\a.xlsx'
print(file)

# print(os.path.basename('run.py'))
# print(os.path.commonpath('run.py'))
# print(os.path.dirname('run.py'))

##################### FIREFOX v2 ##################### 
# from selenium.webdriver import FirefoxService, FirefoxOptions, Firefox
# # user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0'
# user_agentFFX = 'Mozilla/5.0 (Windows NT 10.0; Win32; x32; rv:109.0) Gecko/20100101 Firefox/117.0' #chando to 32bts to test
# serviceFFX = FirefoxService(executable_path=r'C:\Users\kris.amorim\.anaconda\geckodriver.exe', user_agent=user_agentFFX)
# optionsFFX = FirefoxOptions()
# optionsFFX.set_preference('general.useragent.override', user_agentFFX)
# brownser = Firefox(service=serviceFFX, options=optionsFFX) #start brownser
# brownser.get('https://portal.milium.com.br/index.aspx') #access URL

##################### FIREFOX v1##################### 
#WORKED
# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service
# service = webdriver.FirefoxService(executable_path=r'C:\Users\kris.amorim\.anaconda\geckodriver.exe')
# options = webdriver.FirefoxOptions()
# driver = webdriver.Firefox(service=service, options=options)
# driver.get('https://portal.milium.com.br/index.aspx')

##################### VARIABLES #####################
# C:\Users\kris.amorim\AppData\Local\anaconda3 #Python path
# C:\Program Files (x86)\Google\Chrome Beta\v122-Test #google test
# C:\Program Files\Google\Chrome\Application\chrome.exe #chrome normal
